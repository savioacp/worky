from typing import Callable
from worky.worker import WorkerThread


class StatelessWorker(WorkerThread):
    """
    A `WorkerThread` that has the given function as work.
    """

    def __init__(self, func: Callable):
        super().__init__()
        self.func = func

    def setup(self):
        pass

    def work(self, unit):
        return self.func(unit)

    def cleanup(self):
        pass
    