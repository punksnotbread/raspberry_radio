import threading

import logger
from player import VLCPlayer
from radio import Radio
from voice_speaker import ESpeaker
from webserver import Webserver
from worker import RadioQueueWorker

_logger = logger.init_logger(__name__)


def main():
    speaker = ESpeaker()
    player = VLCPlayer(speaker)
    radio = Radio(player)
    button_thread = threading.Thread(name="Button", target=radio.run)
    button_thread.start()

    webserver = Webserver()
    webserver_thread = threading.Thread(name="Webserver", target=webserver.run)
    webserver_thread.start()

    worker = RadioQueueWorker()
    consumer_thread = threading.Thread(
        name="Consumer", target=worker.consume_queue, args=(radio.play_option,)
    )
    consumer_thread.start()


if __name__ == "__main__":
    main()
