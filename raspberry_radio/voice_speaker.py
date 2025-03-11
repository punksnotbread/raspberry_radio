import logging
import os
from pathlib import Path

from gtts import gTTS

_logger = logging.getLogger(__name__)

ROOT_DIR = Path(__file__).parent.parent
MP3S_DIR = ROOT_DIR / "mp3s"


class ESpeaker:
    def __init__(self):
        self.speaker = gTTS

    def save_words(self, words: str) -> dict:
        # Write words TTS to file if they don't exist.
        writepath = words
        if not writepath.endswith(".mp3"):
            writepath = f"{words}.mp3"
        saved_file = False
        absolute_writepath = MP3S_DIR / writepath
        if not os.path.exists(absolute_writepath):
            tts = self.speaker(words)
            tts.save(str(absolute_writepath))
            saved_file = True
        return {"path": absolute_writepath, "file_was_saved": saved_file}
