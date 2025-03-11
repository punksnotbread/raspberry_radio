from signal import pause

from gpiozero import Button

import logger
from library import RADIOS
from player import Player
from worker import QUEUE, RadioQueueWorker

_logger = logger.init_logger(__name__)
_logger.debug("Initialised radio button listener.")


class Radio(Player, RadioQueueWorker):
    def __init__(self, player):
        self.enabled = False
        self.hold_time = 0  # TODO: make configurable.
        self.gpio_pin = 14  # TODO: make configurable.
        try:
            self.button = Button(self.gpio_pin, hold_time=self.hold_time)
        except Exception:
            _logger.exception("Could not load button.")
            self.button = None
        self.wait_time = 2
        self.player = player

    def _get_option(self, num: int) -> str:
        return list(RADIOS.keys())[(num - 1) % len(RADIOS.keys())]

    def _run_command(self, option: str) -> None:
        radio = RADIOS.get(option, None)
        if radio and option.lower() != "off":
            self.player.play_file(option)
            self.player.play_url(radio["url"])
        else:
            _logger.warning(f"Could not find `{option}`, turning off.")
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
        if self.button:
            self.button_listener()
