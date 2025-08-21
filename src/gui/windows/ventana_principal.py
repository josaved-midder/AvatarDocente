from PyQt5.QtWidgets import QMainWindow
from ...services.tts_service import TTSWorker
from ._ui_main import Ui_MainWindow

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.tts_thread = None
        self._conectar_signales()
        self._set_estado("Listo")

    def _conectar_signales(self):
        self.ui.btnHablar.clicked.connect(self.on_hablar_clicked)

    def _set_estado(self, texto: str):
        self.ui.lblEstado.setText(texto)

    def on_hablar_clicked(self):
        texto = self.ui.txtSalida.toPlainText()
        self.ui.btnHablar.setEnabled(False)
        self.tts_thread = TTSWorker(texto, rate=180, voice_id=None)  # voice_id opcional

        self.tts_thread.startedSpeaking.connect(lambda: self._set_estado("Hablando..."))
        self.tts_thread.finishedSpeaking.connect(self._fin_tts_ok)
        self.tts_thread.error.connect(self._fin_tts_error)

        self.tts_thread.start()

    def _fin_tts_ok(self):
        self._set_estado("Listo")
        self.ui.btnHablar.setEnabled(True)
        self.tts_thread = None

    def _fin_tts_error(self, msg: str):
        self._set_estado(f"Error: {msg}")
        self.ui.btnHablar.setEnabled(True)
        self.tts_thread = None
