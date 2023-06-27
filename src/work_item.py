import dataclasses
from typing import Dict, Union


@dataclasses.dataclass()
class WorkItem:
    """Represents a work item with priority, command, and a unique identifier (uid_counter)."""
    uid_counter: int = dataclasses.field(init=False, default=0)
    priority: int
    command: str

    def __post_init__(self):
        """Initializes the unique identifier (uid_counter) of the WorkItem.

        """
        self.uid_counter = WorkItem.uid_counter
        WorkItem.uid_counter += 1

    def __str__(self) -> str:
        return f"WorkItem(uid_counter={self.uid_counter}, priority={self.priority}, command='{self.command}')"

    @classmethod
    def from_dict(cls, d: Dict) -> 'WorkItem':
        """Creates a WorkItem object from a dictionary.

        Args:
            d (Dict): Dictionary containing the WorkItem attributes.

        Returns:
            WorkItem: Created WorkItem object.

        """
        return cls(**d)

    def to_dict(self) -> Dict:
        """Converts the WorkItem object to a dictionary.

        Returns:
            Dict: Dictionary representation of the WorkItem object.

        """
        return dataclasses.asdict(self)

    @staticmethod
    def is_valid(item: Dict) -> Union[bool, ValueError]:
        """Checks if the given dictionary represents a valid WorkItem.

        Args:
            item (Dict): Dictionary representing a WorkItem.

        Returns:
            Union[bool, ValueError]: True if the WorkItem is valid, otherwise raises a ValueError.

        Raises:
            ValueError: If the work item data is invalid.

        """
        if not isinstance(item.get('priority'), int) or not 0 <= item['priority'] <= 10:
            raise ValueError("Priority must be an integer between 0 and 10.")
        if not isinstance(item.get('command'), str) or not item.get('command'):
            raise ValueError("Command must be a string and can't be empty.")

        return True
