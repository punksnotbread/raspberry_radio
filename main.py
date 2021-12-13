import logging

from player import VLCPlayer
from radio import Radio
from voice_speaker import ESpeaker

logging.basicConfig(format="%(asctime)s %(name)s  %(levelname)s  %(message)s")
_logger = logging.getLogger("main")
_logger.level = logging.DEBUG


def main():
    speaker = ESpeaker()
    player = VLCPlayer(speaker)
    radio = Radio(player)
    radio.run()


if __name__ == "__main__":
    main()
