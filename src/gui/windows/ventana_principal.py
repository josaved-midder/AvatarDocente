# src/gui/windows/ventana_principal.py
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from ._ui_main import Ui_ventanaPrincipal   # <-- usa la clase que generó pyuic5

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ventanaPrincipal()
        self.ui.setupUi(self)   # monta los widgets del .ui en este QMainWindow

        self.tts_thread = None
        self._conectar_signales()

        # Mensaje inicial (si tienes chatView)
        if hasattr(self.ui, "chatView"):
            self.ui.chatView.append("<b>Conecta-T:</b> Bienvenido. Escribe tu mensaje y pulsa Enviar.")

    def _conectar_signales(self):
        if hasattr(self.ui, "btnEnviar"):
            self.ui.btnEnviar.clicked.connect(self.on_enviar_clicked)
        if hasattr(self.ui, "btnHablar"):
            self.ui.btnHablar.clicked.connect(self.on_hablar_clicked)

    def on_enviar_clicked(self):
        # Toma el texto de entrada, lo agrega al chat y responde con reglas simples
        text = ""
        if hasattr(self.ui, "txtEntrada"):
            text = self.ui.txtEntrada.toPlainText().strip()
            self.ui.txtEntrada.clear()

        if not text:
            QMessageBox.information(self, "Mensaje vacío", "Escribe algo antes de enviar.")
            return

        if hasattr(self.ui, "chatView"):
            self.ui.chatView.append(f"<b>Tú:</b> {text}")
            resp = self._responder(text)
            self.ui.chatView.append(f"<b>Conecta-T:</b> {resp}")

            # Leer por voz si el checkbox existe y está marcado
            if hasattr(self.ui, "chkLeer") and self.ui.chkLeer.isChecked():
                self._hablar(resp)

    def _responder(self, user_text: str) -> str:
        t = (user_text or "").lower()
        if "hola" in t:
            return "¡Hola! Soy Conecta-T. ¿En qué te apoyo hoy?"
        if "domótica" in t or "iot" in t or "sensor" in t or "actuador" in t:
            return "La domótica automatiza el hogar con sensores, controladores y actuadores."
        if "php" in t or "poo" in t or "programación orientada a objetos" in t:
            return "En PHP POO usamos clases, propiedades y métodos. ¿Empezamos con una clase Player?"
        if "tecnología" in t or "proyecto" in t:
            return "La tecnología resuelve problemas del entorno. Podemos planear un mini-proyecto guiado."
        return "Gracias por tu mensaje. Puedo ayudarte con domótica, PHP POO, y planeación de clases."

    def on_hablar_clicked(self):
        # Lee el último mensaje del bot si existe
        texto = ""
        if hasattr(self.ui, "chatView"):
            # opcional: podrías guardar el último mensaje en una variable; aquí simplificamos
            texto = "Hola, soy Conecta-T."  # fallback
        self._hablar(texto)

    def _hablar(self, texto: str):
        try:
            from ...services.tts_service import TTSWorker  # import diferido/seguro
        except Exception:
            # Si no tienes aún tts_service.py o pyttsx3, no se cae la app.
            if hasattr(self.ui, "chatView"):
                self.ui.chatView.append("<i>(TTS no disponible: instala pyttsx3 y crea services/tts_service.py)</i>")
            return

        self.tts_thread = TTSWorker(texto, rate=180, voice_id=None)
        # Si quieres, puedes conectar señales started/finished para actualizar un lblEstado
        self.tts_thread.start()
