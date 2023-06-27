import heapq
import logging

from .work_item import WorkItem


_logger = logging.getLogger(__name__)


class PriorityQueue:
    """
    Simple priority queue implementation.

    By using heapq.heappush and heapq.heappop functions, the items are maintained in a heap-based data structure
    internally.
    The heapq.heappop function ensures that the item with the highest priority is efficiently extracted from the heap.
    The underlying implementation of heapq takes care of maintaining the heap property and ensures that the operations
    are performed with logarithmic complexity.

    Attributes:
        _queue (List): List to store the work items in priority order, according to the heap data structure.

    """
    def __init__(self):
        _logger.debug("Initialize PriorityQueue.")

        self._queue = list()

    def __bool__(self):
        """Checks if the priority queue is non-empty.

        Returns:
            bool: True if the priority queue is not empty, False otherwise.

        """
        return len(self._queue) > 0

    def add_item(self, work_item: WorkItem):
        """
        Adds a WorkItem to the priority queue.

        The negative sign before work_item.priority ensures that higher priority items are placed at the front of the
        list. Second value in the tuple is the uid_counter, meaning that if two items have the same priority, the one
        with the highest counter will be added after, in other terms, the most recent one will have priority.

        Args:
            work_item (WorkItem): The work item to be added.

        """
        _logger.debug(f"Add item : {work_item}.")

        heapq.heappush(self._queue, (-work_item.priority, work_item.uid_counter, work_item.command))  # O(log(n))

    def pop_item(self):
        """
        Pop the highest priority command from the priority queue.

        Returns:
            Union[str, None]: The highest priority command or None if the priority queue is empty.

        """
        _logger.debug("Pop item.")

        if self:
            _, _, command = heapq.heappop(self._queue)
            return command

        return None

    def current_state(self):
        """
        Returns the current state of the priority queue.

        Returns:
            List: List representing the current state of the priority queue.

        """
        _logger.debug("Current state.")

        return sorted(self._queue)
