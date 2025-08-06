# src/main.py  (solo las 4 primeras líneas)
from __future__ import annotations
# ✅ Importa la clase que contiene tu lógica, NO el archivo _ui
from .gui.windows.ventana_principal import VentanaPrincipal

# … resto del código sin cambios …


def main():
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
