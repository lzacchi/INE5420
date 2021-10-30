from PyQt5 import QtWidgets, QtGui, QtCore


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.resize(500,500)
        self.build()

    def build(self) -> None:
        self.setWindowTitle('INE5420 SGI')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
