import logging

from .work_item import WorkItem
from .priority_queue import PriorityQueue


_logger = logging.getLogger(__name__)


class PriorityQueueAPI:
    """
    API for interacting with the PriorityQueue.

    Attributes:
        priority_queue (PriorityQueue): Instance of the PriorityQueue class.

    """

    def __init__(self):
        _logger.debug("Initialize PriorityQueueAPI.")

        self.priority_queue = PriorityQueue()

    def add_item(self, work_item_data):
        """
        Adds a work item to the priority queue.

        Args:
            work_item_data (Dict): Dictionary representing the work item.

        """
        _logger.debug(f"Add item : {work_item_data}.")

        if WorkItem.is_valid(work_item_data):
            work_item = WorkItem.from_dict(work_item_data)
            self.priority_queue.add_item(work_item)

    def pop_item(self):
        """
        Pops the highest priority command from the priority queue.

        Returns:
            Union[str, None]: The highest priority command (str) or None if the priority queue is empty.

        """
        _logger.debug(f"Pop item.")

        return self.priority_queue.pop_item()

    def current_state(self):
        """
        Returns the current state of the priority queue.

        Returns:
            List: List representing the current state of the priority queue.

        """
        _logger.debug("Current state.")

        return self.priority_queue.current_state()
