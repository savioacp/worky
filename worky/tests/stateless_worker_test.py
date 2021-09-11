from worky import WorkQueue, StatelessWorker, WorkUnit
import unittest
from loguru import logger


class StatelessWorkerTest(unittest.TestCase):
    def test_single_stateless_worker(self):
        wq = WorkQueue()
        wq.enqueue(
            WorkUnit({
                'test': 'dict'
            })
        ).enqueue(
            WorkUnit(1337)
        ).enqueue(
            WorkUnit(True)
        ).enqueue(
            WorkUnit('test string')
        )

        def do_work(unit: WorkUnit):
            logger.info(f'Working on {type(unit.data).__name__} - {unit.data}')

        wq.worker(StatelessWorker, args=(do_work,))

        wq.start()

        wq.block()
