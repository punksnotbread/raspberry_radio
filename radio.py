import logging
from signal import pause

from gpiozero import Button

from library import OPTIONS, RADIOS
from player import Player
from worker import RadioQueueWorker, QUEUE

logging.basicConfig(format="%(asctime)s %(name)s  %(levelname)s  %(message)s")
_logger = logging.getLogger("radio_button")
_logger.level = logging.DEBUG
_logger.debug("Initialised radio button listener.")


class Radio(Player, RadioQueueWorker):
    def __init__(self, player):
        self.enabled = False
        self.hold_time = 0
        self.gpio_pin = 14
        self.button = Button(self.gpio_pin, hold_time=self.hold_time)
        self.wait_time = 2
        self.player = player

    def _get_option(self, num: int) -> str:
        return OPTIONS[(num - 1) % len(OPTIONS)]

    def _run_command(self, option: str) -> None:
        radio = RADIOS.get(option.lower(), None)
        if radio:
            self.player.play_file(radio["name"])
            self.player.play_url(radio["url"])
        else:
            self.player.play_file("off")
            self.player.stop()

    def play_option(self, option: str) -> None:
        self._run_command(option)

    def _listen_button(self):
        press_count = 0
        while True:
            pressed = self.button.wait_for_press(timeout=self.wait_time)
            self.button.wait_for_release()
            if pressed:
                press_count += 1
                _logger.debug(
                    f"Registered a button press, current count is {press_count}"
                )
                option = self._get_option(press_count)
                QUEUE.put(option)
                # self._run_command(option)

    def button_listener(self):
        self._listen_button()
        pause()

    def run(self):
        self.button_listener()
