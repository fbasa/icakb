from __future__ import annotations

from icakb_api.queue import InMemoryQueue


def test_in_memory_queue_preserves_fifo_order() -> None:
    queue = InMemoryQueue[str]()

    queue.enqueue("first")
    queue.enqueue("second")

    assert queue.dequeue() == "first"
    assert queue.dequeue() == "second"
    assert queue.dequeue() is None
