# Popup for the transformation window


from PyQt5 import QtCore, QtGui, QtWidgets
from typing import Any

from utils.math_utils import Matrix


class TransformationWindow(QtWidgets.QMainWindow):
    def __init__(self, parent:Any = None) -> None:
        super().__init__()
        self.main_window = parent
        self.transformations: list[int] = []
        self.center_point = False

        self.setupUi(self)

        self.radio_btns = QtWidgets.QButtonGroup()
        self.radio_btns.addButton(self.center_radio_btn)
        self.radio_btns.addButton(self.origin_radio_btn)
        self.radio_btns.addButton(self.point_radio_btn)
        self.rotation_x_input.setDisabled(True)
        self.rotation_y_input.setDisabled(True)

        self.connect_signals()

        self.button_actions()

    def setupUi(self, TransformationWindow:Any) -> None:
        # Generated code:
        TransformationWindow.setObjectName("TransformationWindow")
        TransformationWindow.resize(443, 529)
        self.centralwidget = QtWidgets.QWidget(TransformationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.transform_list_label = QtWidgets.QLabel(self.centralwidget)
        self.transform_list_label.setGeometry(QtCore.QRect(0, 0, 101, 21))
        self.transform_list_label.setObjectName("transform_list_label")
        self.rotation_label = QtWidgets.QLabel(self.centralwidget)
        self.rotation_label.setGeometry(QtCore.QRect(230, 10, 58, 18))
        self.rotation_label.setObjectName("rotation_label")
        self.translation_label = QtWidgets.QLabel(self.centralwidget)
        self.translation_label.setGeometry(QtCore.QRect(230, 180, 81, 18))
        self.translation_label.setObjectName("translation_label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(230, 160, 221, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.rotation_x_label = QtWidgets.QLabel(self.centralwidget)
        self.rotation_x_label.setGeometry(QtCore.QRect(240, 90, 21, 18))
        self.rotation_x_label.setObjectName("rotation_x_label")
        self.rotation_y_label = QtWidgets.QLabel(self.centralwidget)
        self.rotation_y_label.setGeometry(QtCore.QRect(240, 130, 21, 18))
        self.rotation_y_label.setObjectName("rotation_y_label")
        self.rotate_btn = QtWidgets.QPushButton(self.centralwidget)
        self.rotate_btn.setGeometry(QtCore.QRect(360, 130, 71, 31))
        self.rotate_btn.setObjectName("rotate_btn")
        self.rotation_x_input = QtWidgets.QTextEdit(self.centralwidget)
        self.rotation_x_input.setGeometry(QtCore.QRect(260, 80, 61, 31))
        self.rotation_x_input.setObjectName("rotation_x_input")
        self.rotation_y_input = QtWidgets.QTextEdit(self.centralwidget)
        self.rotation_y_input.setGeometry(QtCore.QRect(260, 120, 61, 31))
        self.rotation_y_input.setObjectName("rotation_y_input")
        self.translation_y_input = QtWidgets.QTextEdit(self.centralwidget)
        self.translation_y_input.setGeometry(QtCore.QRect(260, 270, 61, 31))
        self.translation_y_input.setObjectName("translation_y_input")
        self.translate_btn = QtWidgets.QPushButton(self.centralwidget)
        self.translate_btn.setGeometry(QtCore.QRect(360, 300, 71, 31))
        self.translate_btn.setObjectName("translate_btn")
        self.translation_x_label = QtWidgets.QLabel(self.centralwidget)
        self.translation_x_label.setGeometry(QtCore.QRect(240, 220, 21, 18))
        self.translation_x_label.setObjectName("translation_x_label")
        self.translation_y_label = QtWidgets.QLabel(self.centralwidget)
        self.translation_y_label.setGeometry(QtCore.QRect(240, 280, 21, 18))
        self.translation_y_label.setObjectName("translation_y_label")
        self.translation_x_input = QtWidgets.QTextEdit(self.centralwidget)
        self.translation_x_input.setGeometry(QtCore.QRect(260, 210, 61, 31))
        self.translation_x_input.setObjectName("translation_x_input")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(230, 330, 221, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.scaling_label = QtWidgets.QLabel(self.centralwidget)
        self.scaling_label.setGeometry(QtCore.QRect(240, 350, 58, 18))
        self.scaling_label.setObjectName("scaling_label")
        self.scaling_x_input = QtWidgets.QTextEdit(self.centralwidget)
        self.scaling_x_input.setGeometry(QtCore.QRect(270, 380, 61, 31))
        self.scaling_x_input.setObjectName("scaling_x_input")
        self.scaling_x_label = QtWidgets.QLabel(self.centralwidget)
        self.scaling_x_label.setGeometry(QtCore.QRect(250, 390, 21, 18))
        self.scaling_x_label.setObjectName("scaling_x_label")
        self.scaling_y_label = QtWidgets.QLabel(self.centralwidget)
        self.scaling_y_label.setGeometry(QtCore.QRect(250, 450, 21, 18))
        self.scaling_y_label.setObjectName("scaling_y_label")
        self.scaling_y_input = QtWidgets.QTextEdit(self.centralwidget)
        self.scaling_y_input.setGeometry(QtCore.QRect(270, 440, 61, 31))
        self.scaling_y_input.setObjectName("scaling_y_input")
        self.scale_btn = QtWidgets.QPushButton(self.centralwidget)
        self.scale_btn.setGeometry(QtCore.QRect(360, 465, 71, 31))
        self.scale_btn.setObjectName("scale_btn")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(210, 10, 20, 491))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.transform_list = QtWidgets.QListView(self.centralwidget)
        self.transform_list.setGeometry(QtCore.QRect(10, 20, 201, 441))
        self.transform_list.setObjectName("transform_list")
        self.transform_clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.transform_clear_btn.setGeometry(QtCore.QRect(20, 470, 51, 26))
        self.transform_clear_btn.setObjectName("transform_clear_btn")
        self.transform_btn = QtWidgets.QPushButton(self.centralwidget)
        self.transform_btn.setGeometry(QtCore.QRect(110, 470, 91, 26))
        self.transform_btn.setObjectName("transform_btn")
        self.center_radio_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.center_radio_btn.setGeometry(QtCore.QRect(330, 40, 102, 24))
        self.center_radio_btn.setObjectName("center_radio_btn")
        self.origin_radio_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.origin_radio_btn.setGeometry(QtCore.QRect(330, 60, 102, 24))
        self.origin_radio_btn.setObjectName("origin_radio_btn")
        self.point_radio_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.point_radio_btn.setGeometry(QtCore.QRect(330, 80, 102, 24))
        self.point_radio_btn.setObjectName("point_radio_btn")
        self.rotation_theta_label = QtWidgets.QLabel(self.centralwidget)
        self.rotation_theta_label.setGeometry(QtCore.QRect(240, 50, 16, 18))
        self.rotation_theta_label.setObjectName("rotation_theta_label")
        self.rotation_theta_input = QtWidgets.QTextEdit(self.centralwidget)
        self.rotation_theta_input.setGeometry(QtCore.QRect(260, 40, 61, 31))
        self.rotation_theta_input.setObjectName("rotation_theta_input")
        TransformationWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(TransformationWindow)
        self.statusbar.setObjectName("statusbar")
        TransformationWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TransformationWindow)
        QtCore.QMetaObject.connectSlotsByName(TransformationWindow)

    def retranslateUi(self, TransformationWindow:Any) -> None:
        _translate = QtCore.QCoreApplication.translate
        TransformationWindow.setWindowTitle(_translate("TransformationWindow", "MainWindow"))
        self.transform_list_label.setText(_translate("TransformationWindow", "Transformations"))
        self.rotation_label.setText(_translate("TransformationWindow", "Rotation"))
        self.translation_label.setText(_translate("TransformationWindow", "Translation"))
        self.rotation_x_label.setText(_translate("TransformationWindow", "X:"))
        self.rotation_y_label.setText(_translate("TransformationWindow", "Y:"))
        self.rotate_btn.setText(_translate("TransformationWindow", "Rotate"))
        self.translate_btn.setText(_translate("TransformationWindow", "Translate"))
        self.translation_x_label.setText(_translate("TransformationWindow", "X:"))
        self.translation_y_label.setText(_translate("TransformationWindow", "Y:"))
        self.scaling_label.setText(_translate("TransformationWindow", "Scaling"))
        self.scaling_x_label.setText(_translate("TransformationWindow", "X:"))
        self.scaling_y_label.setText(_translate("TransformationWindow", "Y:"))
        self.scale_btn.setText(_translate("TransformationWindow", "Scale"))
        self.transform_clear_btn.setText(_translate("TransformationWindow", "Clear"))
        self.transform_btn.setText(_translate("TransformationWindow", "Transform"))
        self.center_radio_btn.setText(_translate("TransformationWindow", "Object Center"))
        self.origin_radio_btn.setText(_translate("TransformationWindow", "Origin"))
        self.point_radio_btn.setText(_translate("TransformationWindow", "Specific Point"))
        self.rotation_theta_label.setText(_translate("TransformationWindow", "θ: "))


    def open_new(self, obj:Any) -> None:
        self.selected_object = obj
        self.show()


    def console_log(self, message: str) -> None:
        self.main_window.console_log(message)


    def connect_signals(self) -> None:
        self.radio_btns.buttonClicked.connect(self.toggled_rotation_type)


    def toggled_rotation_type(self, button: QtWidgets.QAbstractButton) -> None:
        if self.point_radio_btn.isChecked():
            self.rotation_x_input.setDisabled(False)
            self.rotation_y_input.setDisabled(False)
            self.center_point = True
        elif self.center_radio_btn.isChecked() or self.origin_radio_btn.isChecked():
            self.rotation_x_input.setDisabled(True)
            self.rotation_y_input.setDisabled(True)


    def add_transformation(self, _rotate:bool = False, _translate:bool = False, _scale:bool = False) -> None:
        self.console_log(f"Selected Object = {self.selected_object}")
        if _rotate:
            theta_angle = self.rotation_theta_input.toPlainText()
            x_value = self.selected_object.coordinates[0]
            y_value = self.selected_object.coordinates[1]
            if self.center_point:
                x_value = self.rotation_x_input.toPlainText()
                y_value = self.rotation_y_input.toPlainText()

            rotation_matrix = Matrix(angle=float(0 if theta_angle == '' else theta_angle))
            rotation_matrix.rotation()
            self.console_log(f"Rotation Matrix = {rotation_matrix}")
            self.console_log(f"x: {x_value}")
            self.console_log(f"y: {y_value}")


        if _translate:
            x_value = self.translation_x_input.toPlainText()
            y_value = self.translation_y_input.toPlainText()
            translation_matrix = Matrix(Dx=float(x_value), Dy=float(y_value))
            translation_matrix.translation()
        if _scale:
            x_value = self.scaling_x_input.toPlainText()
            y_value = self.scaling_y_input.toPlainText()
            scaling_matrix = Matrix(Sx=float(x_value), Sy=float(y_value))
            scaling_matrix.scaling()

    def button_actions(self) -> None:
        self.rotate_btn.clicked.connect(lambda: self.add_transformation(_rotate=True))
