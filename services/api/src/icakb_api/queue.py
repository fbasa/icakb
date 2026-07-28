"""Local queue abstractions for future ingestion work."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from typing import Protocol


class QueuePort[TMessage](Protocol):
    """Minimal queue port used by the service layer."""

    def enqueue(self, message: TMessage) -> None:
        """Add a message to the queue."""

    def dequeue(self) -> TMessage | None:
        """Remove the next message from the queue, if present."""


@dataclass(slots=True)
class InMemoryQueue[TMessage]:
    """FIFO queue implementation for local development and tests."""

    _messages: deque[TMessage] = field(default_factory=deque)

    def enqueue(self, message: TMessage) -> None:
        """Add a message to the tail of the queue."""

        self._messages.append(message)

    def dequeue(self) -> TMessage | None:
        """Remove the message at the head of the queue."""

        if not self._messages:
            return None
        return self._messages.popleft()
