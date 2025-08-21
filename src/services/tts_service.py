# src/services/tts_service.py
from PyQt5.QtCore import QThread, pyqtSignal
import pyttsx3

class TTSWorker(QThread):
    startedSpeaking = pyqtSignal()
    finishedSpeaking = pyqtSignal()
    error = pyqtSignal(str)

    def __init__(self, text: str, rate: int = 180, voice_id: str | None = None):
        super().__init__()
        self.text = text.strip() or "Hola, soy Conecta-T, tu avatar docente."
        self.rate = rate
        self.voice_id = voice_id

    def run(self):
        try:
            engine = pyttsx3.init()
            engine.setProperty("rate", self.rate)
            if self.voice_id:
                engine.setProperty("voice", self.voice_id)
            self.startedSpeaking.emit()
            engine.say(self.text)
            engine.runAndWait()
            self.finishedSpeaking.emit()
        except Exception as e:
            self.error.emit(str(e))
