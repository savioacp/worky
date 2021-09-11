from abc import ABC, abstractmethod
from queue import Queue
import threading
from worky.worker.work_unit import Break, WorkUnit


class WorkerThread(threading.Thread, ABC):
    """
    Defines abstract, base class for worker threads.

    Every thread should have 
    - a setup function, that will execute when the worker is created;
    - a work function, that will execute every time a unit of
    work arrives;
    - a cleanup function, that will execute when there aren't
    any more units of work, or if work fails.  
    """

    def __init__(self, queue: Queue):
        super().__init__()
        self.queue = queue
        self.done = False

    @abstractmethod
    def setup(self):
        """
        Happens before the worker starts working.
        """
        pass

    @abstractmethod
    def work(self, unit: WorkUnit):
        """
        Do the work.

        Parameters
        ---
        - unit - The unit of work.
        """
        pass

    @abstractmethod
    def cleanup(self):
        """
        Happens before the worker stops working.
        """
        pass

    def run(self) -> None:
        self.setup()

        try:
            while True:
                unit = self.queue.get()
                if unit is Break:
                    self.queue.task_done()
                    break
                else:
                    self.work(unit)
                
                self.queue.task_done()
        finally:
            self.cleanup()

    def stop(self):
        self.done = True
