import threading

from raspberry_radio.logger import init_logger
from raspberry_radio.player import VLCPlayer
from raspberry_radio.radio import Radio
from raspberry_radio.voice_speaker import ESpeaker
from raspberry_radio.webserver import Webserver
from raspberry_radio.worker import RadioQueueWorker

_logger = init_logger(__name__)


def main():
    speaker = ESpeaker()
    player = VLCPlayer(speaker)
    radio = Radio(player)

    button_thread = threading.Thread(name="Button", target=radio.run)
    button_thread.start()
    _logger.info("Started button listener.")

    webserver = Webserver()
    webserver_thread = threading.Thread(name="Webserver", target=webserver.run)
    webserver_thread.start()
    _logger.info("Started webserver.")

    worker = RadioQueueWorker()
    consumer_thread = threading.Thread(
        name="Consumer", target=worker.consume_queue, args=(radio.play_option,)
    )
    consumer_thread.start()
    _logger.info("Started radio queue worker.")


if __name__ == "__main__":
    main()
