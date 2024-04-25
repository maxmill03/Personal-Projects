from ui import DoctorUI
from PyQt5 import QtWidgets
import sys


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = DoctorUI()
    ui.setup_ui(ui)
    ui.show()
    sys.exit(app.exec())


main()
