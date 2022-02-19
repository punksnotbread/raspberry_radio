import queue

QUEUE = queue.Queue()


class RadioQueueWorker:
    def __init__(self):
        self.queue = QUEUE

    def consume_queue(self, func):
        while True:
            print("Waiting on queue with size ", self.queue.qsize())
            item = self.queue.get()
            print("Consuming: ", item)
            func(item)
            self.queue.task_done()
