import threading
import unittest
from worky.work_queue import WorkQueue
from worky.worker import WorkerThread
from loguru import logger


class BasicUnit():
    def __init__(self, name):
        self.name = name


class LoggerWorker(WorkerThread):
    def setup(self):
        logger.info(f'[{threading.current_thread().name}] Setup called!')

    def work(self, item):
        logger.info(f'[{threading.current_thread().name}] Working on {item.name}')

    def cleanup(self):
        logger.info(f'[{threading.current_thread().name}] Cleanup called!')


class TestWorky(unittest.TestCase):
    def test_queue(self):

        (
            WorkQueue()
            .enqueue(BasicUnit('unit one'))
            .enqueue(BasicUnit('unit two'))
            .enqueue(BasicUnit('unit three'))
            .enqueue(BasicUnit('unit four'))
            .worker(LoggerWorker)
            .start()
            .enqueue(BasicUnit('unit five after start'))
            .block()
        )
