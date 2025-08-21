import sys
from PyQt5.QtWidgets import QApplication
from .gui.windows.ventanaPrincipal import Ui_ventanaPrincipal


def main():
    app = QApplication(sys.argv)
    w = Ui_ventanaPrincipal()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
