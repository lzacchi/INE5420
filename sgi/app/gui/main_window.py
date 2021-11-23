from datetime import datetime
from typing import Any
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QFileDialog, QMainWindow
from gui.new_wireframe_window import NewWireframeWindow
from gui.transformation_widow import TransformationWindow
from utils.coordinates import Coordinates
from utils.viewport_transformation import x_viewport, y_viewport
from utils.wireframe_structure import WireframeStructure
from utils.math_utils import normalize_window
from utils.wavefront_obj import ObjReader


# Constants
X_MIN = 0
Y_MIN = 0
X_MAX = 550
Y_MAX = 380
SCALE_STEP = 0.1
PAN_STEP = 10
ROTATION_STEP = 0.1

class MainWindow(QMainWindow):
    def __init__(self, parent:QMainWindow = None) -> None:
        super().__init__(parent)

        self.display_file: list = []
        self.window_normalization: list = []
        self.window_denormalization: list = []
        
        self.total_wireframes = 0
        self.scale_accumulator = 0.0
        self.rotation_accumulator = 0.0
        self.x_shift_accumulator = 0.0
        self.y_shift_accumulator = 0.0
        self.pan_step = PAN_STEP
        
        self.new_wireframe = NewWireframeWindow(self)
        self.transformation_window = TransformationWindow(self)
        
        self.window_coordinates = Coordinates(-X_MAX/2, -Y_MAX/2, X_MAX/2, Y_MAX/2, ROTATION_STEP)
        self.viewport_coordinates = Coordinates(X_MIN, Y_MIN, X_MAX, Y_MAX, SCALE_STEP)

        self.normalization_matrix()
        self.denormalization_matrix()
        self.setupUi(self)


    # --- Ui stuff ---

    def setupUi(self, MainWindow:QMainWindow) -> None:
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        # Qt initialization
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.label.setObjectName("label")
        self.display_file_list = QtWidgets.QListWidget(self.centralwidget)
        self.display_file_list.setGeometry(QtCore.QRect(10, 30, 131, 198))
        self.display_file_list.setObjectName("display_file_list")
        self.new_btn = QtWidgets.QPushButton(self.centralwidget)
        self.new_btn.setGeometry(QtCore.QRect(150, 30, 71, 31))
        self.new_btn.setObjectName("new_btn")
        self.delete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_btn.setGeometry(QtCore.QRect(150, 70, 71, 31))
        self.delete_btn.setObjectName("delete_btn")
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setGeometry(QtCore.QRect(150, 110, 71, 31))
        self.clear_btn.setObjectName("clear_btn")
        self.reset_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reset_btn.setGeometry(QtCore.QRect(150, 150, 71, 31))
        self.reset_btn.setObjectName("reset_btn")

        self.redraw_btn = QtWidgets.QPushButton(self.centralwidget)
        self.redraw_btn.setGeometry(QtCore.QRect(150, 190, 71, 31))
        self.redraw_btn.setObjectName("redraw_btn")

        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(10, 230, 61, 31))
        self.save_btn.setObjectName("save_btn")
        self.load_btn = QtWidgets.QPushButton(self.centralwidget)
        self.load_btn.setGeometry(QtCore.QRect(80, 230, 61, 31))
        self.load_btn.setObjectName("load_btn")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 270, 211, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 280, 71, 21))
        self.label_2.setObjectName("label_2")
        self.nav_up_btn = QtWidgets.QPushButton(self.centralwidget)
        self.nav_up_btn.setGeometry(QtCore.QRect(90, 330, 31, 26))
        self.nav_up_btn.setObjectName("nav_up_btn")
        self.nav_right_btn = QtWidgets.QPushButton(self.centralwidget)
        self.nav_right_btn.setGeometry(QtCore.QRect(120, 350, 31, 26))
        self.nav_right_btn.setObjectName("nav_right_btn")
        self.nav_down_btn = QtWidgets.QPushButton(self.centralwidget)
        self.nav_down_btn.setGeometry(QtCore.QRect(90, 370, 31, 26))
        self.nav_down_btn.setObjectName("nav_down_btn")
        self.nav_left_btn = QtWidgets.QPushButton(self.centralwidget)
        self.nav_left_btn.setGeometry(QtCore.QRect(60, 350, 31, 26))
        self.nav_left_btn.setObjectName("nav_left_btn")
        self.nav_zoom_in_btn = QtWidgets.QPushButton(self.centralwidget)
        self.nav_zoom_in_btn.setGeometry(QtCore.QRect(130, 310, 31, 26))
        self.nav_zoom_in_btn.setObjectName("nav_zoom_in_btn")
        self.nav_zoom_out_btn = QtWidgets.QPushButton(self.centralwidget)
        self.nav_zoom_out_btn.setGeometry(QtCore.QRect(50, 310, 31, 26))
        self.nav_zoom_out_btn.setObjectName("nav_zoom_out_btn")

        self.viewport_frame = QtWidgets.QLabel(self.centralwidget)
        self.viewport_frame.setGeometry(QtCore.QRect(240, 40, 550, 380))
        self.viewport_frame.setText("")
        self.viewport_frame.setObjectName("viewport_frame")

        self.transform_btn = QtWidgets.QPushButton(self.centralwidget)
        self.transform_btn.setGeometry(QtCore.QRect(150, 230, 71, 31))
        self.transform_btn.setObjectName("transform_btn")

        viewport_area = QtGui.QPixmap(551,381)
        viewport_area.fill(QtGui.QColor("black"))

        self.viewport_frame.setPixmap(viewport_area)

        self.painter = QtGui.QPainter(self.viewport_frame.pixmap())

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(220, 30, 20, 541))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 10, 71, 21))
        self.label_3.setObjectName("label_3")
        self.log_browser = QtWidgets.QTextBrowser(self.centralwidget)
        self.log_browser.setGeometry(QtCore.QRect(240, 430, 551, 141))
        self.log_browser.setObjectName("log_browser")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 400, 211, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.label_rotation = QtWidgets.QLabel(self.centralwidget)
        self.label_rotation.setGeometry(QtCore.QRect(10, 410, 71, 21))
        self.label_rotation.setObjectName("label_rotation")
        self.rotation_x_btn = QtWidgets.QPushButton(self.centralwidget)
        self.rotation_x_btn.setGeometry(QtCore.QRect(30, 480, 41, 31))
        # self.rotation_x_btn.setObjectName("rotation_x_btn")
        # self.rotation_y_btn = QtWidgets.QPushButton(self.centralwidget)
        # self.rotation_y_btn.setGeometry(QtCore.QRect(80, 480, 41, 31))
        # self.rotation_y_btn.setObjectName("rotation_y_btn")
        # self.rotation_z_btn = QtWidgets.QPushButton(self.centralwidget)
        # self.rotation_z_btn.setGeometry(QtCore.QRect(130, 480, 41, 31))
        # self.rotation_z_btn.setObjectName("rotation_z_btn")
        self.label_rotation_val = QtWidgets.QLabel(self.centralwidget)
        self.label_rotation_val.setGeometry(QtCore.QRect(20, 450, 101, 21))
        self.label_rotation_val.setObjectName("label_rotation_val")
        self.rotation_val_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.rotation_val_textEdit.setGeometry(QtCore.QRect(120, 440, 91, 31))
        self.rotation_val_textEdit.setObjectName("rodation_val_textEdit")

        self.clear_log_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_log_btn.setGeometry(QtCore.QRect(750, 550, 41, 21))
        self.clear_log_btn.setObjectName("clear_log_btn")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.connect_signals()


    def retranslateUi(self, MainWindow:Any) -> None:
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "INE5420 SGI"))
        self.label.setText(_translate("MainWindow", "Display File"))
        self.new_btn.setText(_translate("MainWindow", "New"))
        self.delete_btn.setText(_translate("MainWindow", "Delete"))
        self.clear_btn.setText(_translate("MainWindow", "Clear"))
        self.reset_btn.setText(_translate("MainWindow", "Reset"))
        self.redraw_btn.setText(_translate("MainWindow", "Redraw"))

        self.save_btn.setText(_translate("MainWindow", "Save"))
        self.load_btn.setText(_translate("MainWindow", "Load"))

        self.label_2.setText(_translate("MainWindow", "Navigation"))
        self.nav_up_btn.setText(_translate("MainWindow", "▲"))
        self.nav_right_btn.setText(_translate("MainWindow", "▶"))
        self.nav_down_btn.setText(_translate("MainWindow", "▼"))
        self.nav_left_btn.setText(_translate("MainWindow", "◀"))
        self.nav_zoom_in_btn.setText(_translate("MainWindow", "➕"))
        self.nav_zoom_out_btn.setText(_translate("MainWindow", "➖"))
        self.label_3.setText(_translate("MainWindow", "Viewport"))

        self.label_rotation.setText(_translate("MainWindow", "Rotation"))
        self.rotation_x_btn.setText(_translate("MainWindow", "X"))
        # self.rotation_y_btn.setText(_translate("MainWindow", "Y"))
        # self.rotation_z_btn.setText(_translate("MainWindow", "Z"))
        self.label_rotation_val.setText(_translate("MainWindow", "Value (Degrees):"))

        self.clear_log_btn.setText(_translate("MainWindow", "Clear"))
        self.transform_btn.setText(_translate("MainWindow", "Transform"))

    # --- Utils ---

    def console_log(self, message: str) -> None:
        self.log_browser.append(f"[{datetime.now().strftime('%H:%M:%S')}]: " + message)

    def select_current_object(self) -> WireframeStructure:
        current_row = self.display_file_list.currentRow()
        return self.display_file[current_row]

    # --- Viewport/canvas drawing ---

    def open_new_wireframe_window(self) -> None:
        self.new_wireframe.open_new()


    def open_transformation_window(self) -> None:
        current_object = self.select_current_object()
        if current_object is None:
            self.console_log("Can't transform without selecting a wireframe!")
            return
        self.transformation_window.open_new(current_object)


    def delete_wireframe(self) -> None:
        try:
            self.display_file.pop()
        except IndexError:
            self.console_log("There are no wireframe structures to delete.")

        self.console_log(f"Deleting structure: {self.display_file_list.currentRow()}")
        self.display_file_list.takeItem(self.display_file_list.currentRow())


    def clear_viewport(self) -> None:
        self.viewport_frame.pixmap().fill(QtGui.QColor("black"))
        self.viewport_frame.update()

    
    def normalization_matrix(self) -> None:
        window_width = self.window_coordinates.max_x - self.window_coordinates.min_x
        window_height = self.window_coordinates.max_y - self.window_coordinates.min_y
        self.window_normalization = normalize_window(self.x_shift_accumulator, self.y_shift_accumulator, window_width, window_height, self.rotation_accumulator)

    def denormalization_matrix(self) -> None:
        window_width = self.window_coordinates.max_x - self.window_coordinates.min_x
        window_height = self.window_coordinates.max_y - self.window_coordinates.min_y
        self.window_denormalization = normalize_window(-self.x_shift_accumulator, -self.y_shift_accumulator, 4/window_width, 4/window_height, -self.rotation_accumulator)


    def draw_wireframe(self, wireframe: WireframeStructure, refresh:bool = False) -> None:
        if not refresh:
            self.console_log(f"Drawing {wireframe.struct_name}: {[point for point in wireframe.coordinates]}")

        for point in range(wireframe.vertices):
            x1, y1 = wireframe.transformed_coordinates[point]

            # viewport transformation
            x1_vp = x_viewport(x1, self.window_coordinates.min_x, self.window_coordinates.max_x, self.viewport_coordinates.min_x, self.viewport_coordinates.max_x)
            y1_vp = y_viewport(y1, self.window_coordinates.min_y, self.window_coordinates.max_y, self.viewport_coordinates.min_y, self.viewport_coordinates.max_y)

            x2, y2 = wireframe.transformed_coordinates[(point + 1) % wireframe.vertices]

            x2_vp = x_viewport(x2, self.window_coordinates.min_x, self.window_coordinates.max_x, self.viewport_coordinates.min_x, self.viewport_coordinates.max_x)
            y2_vp = y_viewport(y2, self.window_coordinates.min_y, self.window_coordinates.max_y, self.viewport_coordinates.min_y, self.viewport_coordinates.max_y)

            p1 = (x1_vp, y1_vp)
            p2 = (x2_vp, y2_vp)

            self.draw_line_segment((p1, p2) , wireframe.color)


    def draw_line_segment(self, points: tuple, wireframe_color:Any) -> None:
        p1, p2 = points
        p1x, p1y = p1
        p2x, p2y = p2
        self.painter.setPen(QColor(wireframe_color))
        self.painter.drawLine(p1x, p1y, p2x, p2y)
        self.viewport_frame.update()


    def reset_viewport(self) -> None:
        self.scale_accumulator = 0.0
        self.rotation_accumulator = 0.0
        self.x_shift_accumulator = 0.0
        self.y_shift_accumulator = 0.0
        self.window_coordinates.min_x = -X_MAX/2
        self.window_coordinates.min_y = -Y_MAX/2
        self.window_coordinates.max_x = X_MAX
        self.window_coordinates.max_y = Y_MAX

        self.refresh_viewport()
        self.console_log("Reset!")

    def refresh_viewport(self) -> None:
        self.clear_viewport()
        self.normalization_matrix()
        window_width = self.window_coordinates.max_x - self.window_coordinates.min_x
        window_height = self.window_coordinates.max_y - self.window_coordinates.min_y
        for w in self.display_file:
            w.normalized_values = self.window_coordinates
            w.window_width = window_width
            w.window_height = window_height
            w.window_normalization = self.window_normalization
            self.draw_wireframe(w, True)

    # --- Obj handling ---

    def load_obj(self) -> None:
        filename = QFileDialog.getOpenFileName(self, "Open wavefront obj file", "./resources/obj", "Obj files (*.obj)")[0]
        self.console_log(f"Loading file: {filename}")
        objreader = ObjReader(filename, self.total_wireframes, self.window_coordinates, self.transformation_window)
        new_wf = objreader.wireframes
        for w in new_wf:
            self.display_file.append(w)
            self.draw_wireframe(w)
            self.display_file_list.insertItem(self.total_wireframes, w.name)
            self.total_wireframes+=1
            self.console_log(f"Loaded wireframe: {w.name}")

    
    def save_obj(self) -> None:
        pass

    # --- Navigation/transformation

    def navigation(self, _up:bool = False, _left:bool = False, _down:bool = False, _right:bool = False) -> None:
        if _up:
            self.y_shift_accumulator -= self.pan_step
        if _left:
            self.x_shift_accumulator += self.pan_step
        if _down:
            self.y_shift_accumulator += self.pan_step
        if _right:
            self.x_shift_accumulator -= self.pan_step

        self.refresh_viewport()


    def scale_canvas(self, step: float) -> None:
        self.scale_accumulator += step
        scale_factor = 1 + self.scale_accumulator
        self.window_coordinates.max_x = X_MAX * scale_factor
        self.window_coordinates.max_y = Y_MAX * scale_factor


    def zoom(self, _in:bool = False, _out:bool = False) -> None:
        if _in:
            self.scale_canvas(-SCALE_STEP)

        if _out:
            self.scale_canvas(SCALE_STEP)
        self.refresh_viewport()

    def rotation(self) -> None:
        self.aux_rotation()

    def aux_rotation(self) -> None:
        rotation_amount = self.rotation_val_textEdit.toPlainText()
        self.rotation_accumulator = 0.0 if rotation_amount == '' else float(rotation_amount)
        
        for w in self.display_file:
            w.window_view_up = self.rotation_accumulator
        self.console_log(f"Rotating window by {self.rotation_accumulator}º on the x axis.")
        self.refresh_viewport()

    # --- Buttons ---

    def connect_signals(self) -> None:
        # New windows
        self.new_btn.clicked.connect(self.open_new_wireframe_window)
        self.transform_btn.clicked.connect(self.open_transformation_window)

        # Display File/ Viewport Buttons
        self.redraw_btn.clicked.connect(self.refresh_viewport)
        self.clear_btn.clicked.connect(self.clear_viewport)
        self.delete_btn.clicked.connect(self.delete_wireframe)
        self.reset_btn.clicked.connect(self.reset_viewport)

        self.load_btn.clicked.connect(self.load_obj)
        self.save_btn.clicked.connect(self.save_obj)

        # Extra buttons
        self.clear_log_btn.clicked.connect(self.log_browser.clear)

        # Navigation buttons
        self.nav_zoom_in_btn.clicked.connect(lambda: self.zoom(_in=True))
        self.nav_zoom_out_btn.clicked.connect(lambda: self.zoom(_out=True))

        self.nav_up_btn.clicked.connect(lambda: self.navigation(_up=True))
        self.nav_left_btn.clicked.connect(lambda: self.navigation(_left=True))
        self.nav_down_btn.clicked.connect(lambda: self.navigation(_down=True))
        self.redraw_btn.clicked.connect(self.refresh_viewport)
        self.nav_right_btn.clicked.connect(lambda: self.navigation(_right=True))

        self.rotation_x_btn.clicked.connect(self.rotation)
