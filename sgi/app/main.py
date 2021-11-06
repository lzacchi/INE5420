import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from main_window import MainWindow


def app() -> None:
    app = QApplication(sys.argv)
    ex = MainWindow()
    w = QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    app()
