import logger
import os

from gtts import gTTS

_logger = logger.init_logger(__name__)


class ESpeaker:
    def __init__(self):
        self.speaker = gTTS

    def save_words(self, words: str) -> dict:
        # Write words TTS to file if they don't exist.
        writepath = words
        if not writepath.endswith(".mp3"):
            writepath = f"{words}.mp3"
        saved_file = False
        if not os.path.exists(writepath):
            tts = self.speaker(words)
            tts.save(writepath)
            saved_file = True
        return {"path": writepath, "file_was_saved": saved_file}
