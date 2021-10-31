from PyQt5 import QtGui, QtCore, QtWidgets

_DEBUG = True
class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None) -> None:
        """Initializes Main Window, setting initial size and title"""
        super().__init__(parent)
        self.resize(500,500)
        self.setWindowTitle('INE5420 SGI')
        self.build()

    def build(self) -> None:
        """Builds Main window, with menus, buttons and views"""
        self.close_btn = QtWidgets.QPushButton(self)
        self.close_btn.setObjectName('close_btn')
        menu_layout = QtWidgets.QVBoxLayout()
        menu_layout.addWidget(self.close_btn)
        self.setLayout(menu_layout)

        if _DEBUG:
            print(self.children())
