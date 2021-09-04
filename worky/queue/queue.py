from queue import Queue
from typing import Any, Callable, Iterator
import threading

WorksGenerator = Iterator[Any]
WorkerFunction = Callable[[WorksGenerator], Any]


class WorkQueue():

    def __init__(self, worker: WorkerFunction, worker_count: int) -> None:
        self._queue = Queue()
        self._worker = worker
        self._worker_threads = [threading.Thread(target=self._worker) for _ in range(worker_count)]

        # Create worker threads

    def get_works(self) -> Iterator(Any):
        raise NotImplementedError()
