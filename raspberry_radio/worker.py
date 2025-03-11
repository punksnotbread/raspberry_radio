import logging
import queue

_logger = logging.getLogger(__name__)
QUEUE: queue.Queue = queue.Queue()


class RadioQueueWorker:
    def __init__(self):
        self.queue = QUEUE

    def consume_queue(self, func):
        while True:
            _logger.debug(f"Waiting on queue with size {self.queue.qsize()}")
            item = self.queue.get()
            _logger.debug(f"Consuming: {item}")
            func(item)
            self.queue.task_done()
