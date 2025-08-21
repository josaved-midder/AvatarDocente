import sys
from PyQt5.QtWidgets import QApplication
from gui.windows.ventana_principal import VentanaPrincipal

def main():
    app = QApplication(sys.argv)
    w = VentanaPrincipal()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
