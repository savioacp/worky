from queue import Queue
from typing import Any, Callable, Union

from loguru import logger

from worky.worker.work_unit import Break
from worky.worker import WorkerThread

WorkerFunction = Callable[[Any], Any]


class WorkQueue():

    def __init__(self) -> None:
        self._queue = Queue()
        self._workers: list[WorkerThread] = []

    @property
    def queue(self) -> Queue:
        return self._queue

    def enqueue(self, unit):
        self.queue.put(unit)
        return self

    def worker(self, worker: Union[WorkerThread], count: int = 1):
        for _ in range(count):
            self._workers.append(worker(self.queue))
        return self

    def start(self):
        for worker in self._workers:
            worker.start()
        return self

    def block(self):
        for _ in self._workers:
            self.enqueue(Break)
        logger.debug(f'Waiting for {self.queue.unfinished_tasks} unfinished tasks.')
        self.queue.join()
        return self