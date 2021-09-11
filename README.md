# Worky

Simple work parallel queues for Python.

This was initially written to be used with RabbitMQ, but on the future I want it to be used everwhere :)

## Quick introduction
The idea is to have 
- A queue that can easily be used to add work and workers;
- Modular workers that can be plugged into any queue;
- Cute code.

This is in very early stage of development and don't even think of using it in production now.

## Code example
##### Chaining actions
```python
from worky import WorkQueue, StatelessWorker, WorkUnit

(
    WorkQueue()
    .enqueue(WorkUnit('unit one'))
    .enqueue(WorkUnit('unit two'))
    .enqueue(WorkUnit('unit three'))
    .enqueue(WorkUnit('unit four'))
    .worker(StatelessWorker, args=(lambda u: print(u.data),))
    .start()
    .enqueue(WorkUnit('unit five after start'))
    .block()
)
```

##### Not chaining actions
```python
from worky import WorkQueue, StatelessWorker, WorkUnit


wq = WorkQueue()

wq.enqueue(WorkUnit('unit one'))

wq.enqueue(WorkUnit('unit two'))

wq.enqueue(WorkUnit('unit three'))

wq.enqueue(WorkUnit('unit four'))

wq.worker(StatelessWorker, args=(lambda u: print(u.data),))
wq.start()

wq.enqueue(WorkUnit('unit five after start'))

wq.block()
```

In either way, the output will be the same:
```
unit one
unit two
unit three
unit four
unit five after start
```
