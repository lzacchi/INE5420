from typing import Any
from PyQt5 import QtCore, QtGui, QtWidgets
from new_wireframe_window import NewWireframeWindow

class MainWindow(object):

    def setupUi(self, MainWindow:Any) -> None:
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.display_file: list = []
        self.partnerDialog = NewWireframeWindow(self)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.label.setObjectName("label")
        self.display_file_list = QtWidgets.QListWidget(self.centralwidget)
        self.display_file_list.setGeometry(QtCore.QRect(10, 30, 131, 191))
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
        self.refresh_btn = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_btn.setGeometry(QtCore.QRect(150, 150, 71, 31))
        self.refresh_btn.setObjectName("refresh_btn")
        self.transform_btn = QtWidgets.QPushButton(self.centralwidget)
        self.transform_btn.setGeometry(QtCore.QRect(150, 190, 71, 31))
        self.transform_btn.setObjectName("transform_btn")
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
        self.nav_zoom_in_btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.nav_zoom_in_btn_2.setGeometry(QtCore.QRect(130, 310, 31, 26))
        self.nav_zoom_in_btn_2.setObjectName("nav_zoom_in_btn_2")
        self.nav_zoom_out_btn = QtWidgets.QPushButton(self.centralwidget)
        self.nav_zoom_out_btn.setGeometry(QtCore.QRect(50, 310, 31, 26))
        self.nav_zoom_out_btn.setObjectName("nav_zoom_out_btn")
        self.viewport_frame = QtWidgets.QFrame(self.centralwidget)
        self.viewport_frame.setGeometry(QtCore.QRect(250, 30, 541, 391))
        self.viewport_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.viewport_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.viewport_frame.setObjectName("viewport_frame")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(220, 30, 20, 541))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 10, 71, 21))
        self.label_3.setObjectName("label_3")
        self.log_browser = QtWidgets.QTextBrowser(self.centralwidget)
        self.log_browser.setGeometry(QtCore.QRect(250, 430, 541, 141))
        self.log_browser.setObjectName("log_browser")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 400, 211, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        # self.label_rotation = QtWidgets.QLabel(self.centralwidget)
        # self.label_rotation.setGeometry(QtCore.QRect(10, 410, 71, 21))
        # self.label_rotation.setObjectName("label_rotation")
        # self.rotation_x_btn = QtWidgets.QPushButton(self.centralwidget)
        # self.rotation_x_btn.setGeometry(QtCore.QRect(30, 480, 41, 31))
        # self.rotation_x_btn.setObjectName("rotation_x_btn")
        # self.rotation_y_btn = QtWidgets.QPushButton(self.centralwidget)
        # self.rotation_y_btn.setGeometry(QtCore.QRect(80, 480, 41, 31))
        # self.rotation_y_btn.setObjectName("rotation_y_btn")
        # self.rotation_z_btn = QtWidgets.QPushButton(self.centralwidget)
        # self.rotation_z_btn.setGeometry(QtCore.QRect(130, 480, 41, 31))
        # self.rotation_z_btn.setObjectName("rotation_z_btn")
        # self.label_rotation_val = QtWidgets.QLabel(self.centralwidget)
        # self.label_rotation_val.setGeometry(QtCore.QRect(20, 450, 101, 21))
        # self.label_rotation_val.setObjectName("label_rotation_val")
        # self.rodation_val_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        # self.rodation_val_textEdit.setGeometry(QtCore.QRect(120, 440, 91, 31))
        # self.rodation_val_textEdit.setObjectName("rodation_val_textEdit")
        self.clear_log_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_log_btn.setGeometry(QtCore.QRect(750, 550, 41, 21))
        self.clear_log_btn.setObjectName("clear_log_btn")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.button_actions()


    def retranslateUi(self, MainWindow:Any) -> None:
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "INE5420 SGI"))
        self.label.setText(_translate("MainWindow", "Display File"))
        self.new_btn.setText(_translate("MainWindow", "New"))
        self.delete_btn.setText(_translate("MainWindow", "Delete"))
        self.clear_btn.setText(_translate("MainWindow", "Clear"))
        self.refresh_btn.setText(_translate("MainWindow", "Refresh"))
        self.transform_btn.setText(_translate("MainWindow", "Transform"))
        self.save_btn.setText(_translate("MainWindow", "Save"))
        self.load_btn.setText(_translate("MainWindow", "Load"))
        self.label_2.setText(_translate("MainWindow", "Navigation"))
        self.nav_up_btn.setText(_translate("MainWindow", "▲"))
        self.nav_right_btn.setText(_translate("MainWindow", "▶"))
        self.nav_down_btn.setText(_translate("MainWindow", "▼"))
        self.nav_left_btn.setText(_translate("MainWindow", "◀"))
        self.nav_zoom_in_btn_2.setText(_translate("MainWindow", "➕"))
        self.nav_zoom_out_btn.setText(_translate("MainWindow", "➖"))
        self.label_3.setText(_translate("MainWindow", "Viewport"))
        # self.label_rotation.setText(_translate("MainWindow", "Rotation"))
        # self.rotation_x_btn.setText(_translate("MainWindow", "X"))
        # self.rotation_y_btn.setText(_translate("MainWindow", "Y"))
        # self.rotation_z_btn.setText(_translate("MainWindow", "Z"))
        # self.label_rotation_val.setText(_translate("MainWindow", "Value (Degrees):"))
        self.clear_log_btn.setText(_translate("MainWindow", "Clear"))


    def console_log(self, message: str) -> None:
        self.log_browser.append(message)


    def new_wireframe_window(self) -> None:
        self.partnerDialog.open_new()

    def delete_wireframe(self) -> None:
        self.display_file_list.takeItem(self.display_file_list.currentRow())

        try:
            self.display_file.pop()
        except IndexError:
            self.console_log("Error trying to delete")

    def clear_display_file(self) -> None:
        self.display_file_list.clear()
        self.console_log("Display File cleared!")

    def refresh_viewport(self) -> None:
        pass

    def navigation(self) -> None:
        pass


    def button_actions(self) -> None:
        self.new_btn.clicked.connect(self.new_wireframe_window)
        self.clear_btn.clicked.connect(self.clear_display_file)
        self.delete_btn.clicked.connect(self.delete_wireframe)

        self.clear_log_btn.clicked.connect(self.log_browser.clear)
