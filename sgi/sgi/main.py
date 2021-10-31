import sys
from PyQt5.QtWidgets import QApplication

from main_window import MainWindow

import main_window

def app() -> None:
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    app()
