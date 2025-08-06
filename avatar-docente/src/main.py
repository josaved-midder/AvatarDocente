
"""Punto de entrada provisional"""
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout

def main() -> None:
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("Avatar Docente – MVP")
    layout = QVBoxLayout(w)
    layout.addWidget(QLabel("¡Hola, mundo!"))
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
