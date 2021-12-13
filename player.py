import logging
import time

import vlc

from voice_speaker import ESpeaker

logging.basicConfig(format="%(asctime)s %(name)s  %(levelname)s  %(message)s")
_logger = logging.getLogger("player")
_logger.level = logging.DEBUG


class Player:
    def __init__(self):
        pass

    def stop(self) -> None:
        return NotImplementedError

    def play_file(self, filepath: str) -> None:
        return NotImplementedError

    def play_url(self, url: str) -> None:
        return NotImplementedError


class VLCPlayer(Player):
    def __init__(self, speaker: ESpeaker = None):
        self.player = vlc.MediaPlayer()  # Main radio player.
        self.word_player = vlc.MediaPlayer()  # Used to say station names.
        self.speaker = speaker

    def stop(self) -> None:
        self.player.stop()

    def play_file(self, filepath: str) -> None:
        self.player.stop()
        if not filepath:
            return

        if self.speaker:
            filepath = self.speaker.save_words(filepath)
            file_was_saved = filepath["file_was_saved"]
            filepath = filepath["path"]
            if file_was_saved:
                _logger.debug(f"{filepath} has not been yet saved, waiting..")
                time.sleep(2)

        media = vlc.Media(filepath)
        _logger.debug(f"Setting media {media} to `{filepath}`.")

        # TODO: This should be somehow fixed and we should use the same VLC instance
        #  for both - radio stream and title speak.
        self.word_player.set_media(media)

        self.word_player.play()

    def play_url(self, url: str) -> None:
        self.player.stop()
        if not url:
            return

        self.player.set_mrl(url)
        self.player.play()
