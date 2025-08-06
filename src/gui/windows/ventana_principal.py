from PyQt5.QtWidgets import QMainWindow
from .ventana_principal import Ui_MainWindow  # nombre generado por pyuic5
import gui.resources.recursos_rc  # importa los recursos

class VentanaPrincipal(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._conectar_signales()

    def _conectar_signales(self):
        self.boton.clicked.connect(self.manejar_click)

    def manejar_click(self):
        print("¡Botón presionado!")
