from typing import Any
from PyQt5 import QtCore, QtGui, QtWidgets
from utils.wireframe_structure import WireframeStructure



class NewWireframeWindow(QtWidgets.QDialog):
    def __init__(self, parent:Any = None) -> None:
        super().__init__()
        self.wireframe_idx = 0
        self.main_window = parent  # Exchange information with Main Window
        self.display_file = self.main_window.display_file
        self.points: list[tuple] = []
        self.setupUi(self)


    def setupUi(self, NewWireframeWindow:Any) -> None:
        NewWireframeWindow.setObjectName("new_wireframe_window")
        NewWireframeWindow.resize(333, 298)
        self.new_form_label = QtWidgets.QLabel(NewWireframeWindow)
        self.new_form_label.setGeometry(QtCore.QRect(20, 20, 111, 18))
        self.new_form_label.setObjectName("new_form_label")
        self.new_form_x_label = QtWidgets.QLabel(NewWireframeWindow)
        self.new_form_x_label.setGeometry(QtCore.QRect(30, 60, 58, 18))
        self.new_form_x_label.setObjectName("new_form_x_label")
        self.new_form_x_text = QtWidgets.QTextEdit(NewWireframeWindow)
        self.new_form_x_text.setGeometry(QtCore.QRect(50, 50, 51, 31))
        self.new_form_x_text.setObjectName("new_form_x_text")
        self.new_form_y_text = QtWidgets.QTextEdit(NewWireframeWindow)
        self.new_form_y_text.setGeometry(QtCore.QRect(50, 100, 51, 31))
        self.new_form_y_text.setObjectName("new_form_y_text")
        self.new_form_y_label = QtWidgets.QLabel(NewWireframeWindow)
        self.new_form_y_label.setGeometry(QtCore.QRect(30, 110, 58, 18))
        self.new_form_y_label.setObjectName("new_form_y_label")
        self.new_form_add_btn = QtWidgets.QPushButton(NewWireframeWindow)
        self.new_form_add_btn.setGeometry(QtCore.QRect(30, 260, 80, 26))
        self.new_form_add_btn.setObjectName("new_form_add_btn")
        self.new_form_points_list_widget = QtWidgets.QListWidget(NewWireframeWindow)
        self.new_form_points_list_widget.setGeometry(QtCore.QRect(150, 40, 171, 211))
        self.new_form_points_list_widget.setObjectName("new_form_points_list_widget")
        self.new_form_points_list_label = QtWidgets.QLabel(NewWireframeWindow)
        self.new_form_points_list_label.setGeometry(QtCore.QRect(160, 20, 81, 18))
        self.new_form_points_list_label.setObjectName("new_form_points_list_label")
        self.line = QtWidgets.QFrame(NewWireframeWindow)
        self.line.setGeometry(QtCore.QRect(120, 20, 20, 271))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.new_form_draw_btn = QtWidgets.QPushButton(NewWireframeWindow)
        self.new_form_draw_btn.setGeometry(QtCore.QRect(240, 260, 80, 26))
        self.new_form_draw_btn.setObjectName("new_form_draw_btn")
        # self.new_form_z_label = QtWidgets.QLabel(NewWireframeWindow)
        # self.new_form_z_label.setGeometry(QtCore.QRect(30, 160, 58, 18))
        # self.new_form_z_label.setObjectName("new_form_z_label")
        # self.new_form_z_text = QtWidgets.QTextEdit(NewWireframeWindow)
        # self.new_form_z_text.setGeometry(QtCore.QRect(50, 150, 51, 31))
        # self.new_form_z_text.setObjectName("new_form_z_text")
        self.new_form_delete_btn = QtWidgets.QPushButton(NewWireframeWindow)
        self.new_form_delete_btn.setGeometry(QtCore.QRect(160, 260, 61, 26))
        self.new_form_delete_btn.setObjectName("new_form_delete_btn")


        self.retranslateUi(NewWireframeWindow)
        QtCore.QMetaObject.connectSlotsByName(NewWireframeWindow)

        self.button_actions()


    def retranslateUi(self, NewWireframeWindow: Any) -> None:
        _translate = QtCore.QCoreApplication.translate
        NewWireframeWindow.setWindowTitle(_translate("NewWireframeWindow", "New Wireframe Structure"))
        self.new_form_label.setText(_translate("NewWireframeWindow", "New Point:"))
        self.new_form_x_label.setText(_translate("NewWireframeWindow", "X:"))
        self.new_form_y_label.setText(_translate("NewWireframeWindow", "Y:"))
        self.new_form_add_btn.setText(_translate("NewWireframeWindow", "Add Point"))
        self.new_form_points_list_label.setText(_translate("NewWireframeWindow", "Your points:"))
        self.new_form_draw_btn.setText(_translate("NewWireframeWindow", "Draw"))
        # self.new_form_z_label.setText(_translate("NewWireframeWindow", "Z:"))
        self.new_form_delete_btn.setText(_translate("NewWireframeWindow", "Delete"))


    def console_log(self, message: str) -> None:
        self.main_window.console_log(message)


    def open_new(self) -> None:
        self.points = []
        self.show()


    def add_point(self) -> None:
        text_x = self.new_form_x_text.toPlainText()
        text_y = self.new_form_y_text.toPlainText()
        x = float(0 if text_x == "" else text_x)
        y = float(0 if text_y == "" else text_y)

        self.points.append((x, y))

        self.new_form_x_text.clear()
        self.new_form_y_text.clear()



        point_idx = len(self.points)
        point_to_str = f"Point {point_idx}: ({x}, {y})"

        self.new_form_points_list_widget.insertItem(point_idx, point_to_str)


    def delete_point(self) -> None:
        self.new_form_points_list_widget.takeItem(self.new_form_points_list_widget.currentRow())

        try:
            self.points.pop()
        except IndexError:
            self.console_log("Error trying to delete Point: There are no points to delete.")


    def draw_structure(self) -> None:
        """
        Creates a 'WireframeStructure' object and, adds it
        to the Main Window's display file and draws the structure


        After it's done, all the fields and structures in this window are reset
        """

        structure_id = self.wireframe_idx
        wireframe = WireframeStructure(self.points, structure_id)



        self.display_file.append(wireframe)
        self.main_window.display_file_list.insertItem(structure_id, wireframe.name)
        self.wireframe_idx += 1

        self.console_log(f"Wireframe added: {wireframe.name}")

        self.main_window.draw_wireframe(wireframe)

        self.points = []
        self.new_form_points_list_widget.clear()
        # self.new_form_x_text.clear()
        # self.new_form_y_text.clear()

        self.close()

    def button_actions(self) -> None:
        self.new_form_add_btn.clicked.connect(self.add_point)
        self.new_form_delete_btn.clicked.connect(self.delete_point)
        self.new_form_draw_btn.clicked.connect(self.draw_structure)
