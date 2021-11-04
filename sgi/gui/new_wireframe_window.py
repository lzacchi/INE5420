from typing import Any
from PyQt5 import QtCore, QtGui, QtWidgets
from utils.wireframe_structure import WireframeStructure



class NewWireframeWindow(QtWidgets.QDialog):
    def __init__(self, parent:Any = None) -> None:
        super().__init__()
        self.point_idx = 0
        self.partnerDialog = parent  # Exchange information with Main Window
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


    def open_new(self) -> None:
        self.points = []
        self.show()


    def add_point(self) -> None:
        x = float(self.new_form_x_text.toPlainText())
        y = float(self.new_form_y_text.toPlainText())

        self.new_form_x_label.clear()
        self.new_form_y_label.clear()

        self.points.append((x, y))


        point_idx = len(self.points) - 1
        point_to_str = f"Point {point_idx}: ({x}, {y})"

        self.new_form_points_list_widget.insertItem(point_idx, point_to_str)

        # self.partnerDialog.console_log("Add Point")


    def delete_point(self) -> None:
        self.new_form_points_list_widget.takeItem(self.new_form_points_list_widget.currentRow())
        self.points.pop()


    def draw_structure(self) -> None:
        self.partnerDialog.console_log("Draw")


    def button_actions(self) -> None:
        self.new_form_add_btn.clicked.connect(self.add_point)
        self.new_form_delete_btn.clicked.connect(self.delete_point)
        self.new_form_draw_btn.clicked.connect(self.draw_structure)
