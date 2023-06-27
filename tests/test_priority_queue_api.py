import unittest
from src.priority_queue_api import PriorityQueueAPI
from src.work_item import WorkItem


class PriorityQueueAPITest(unittest.TestCase):
    def setUp(self):
        self.api = PriorityQueueAPI()

        example_data = [
            {'command': 'task1', 'priority': 3},
            {'command': 'task2', 'priority': 2},
            {'command': 'task3', 'priority': 3},
            {'command': 'task4', 'priority': 1},
            {'command': 'task5', 'priority': 8},
            {'command': 'task6', 'priority': 2},
        ]

        # Add example items to the priority queue
        for item in example_data:
            self.api.add_item(item)

    def tearDown(self):
        self.api = None
        WorkItem.uid_counter = 0

    def test_add_item(self):
        """Assert that the items are added and have the correct priority and command."""

        self.api.add_item({'priority': 8, 'command': "task7"})
        current_state = self.api.current_state()

        self.assertEqual(len(current_state), 7)
        self.assertIn((-8, 6, "task7"), current_state)

        self.api.add_item({'priority': 1, 'command': "task8 extended command"})
        current_state = self.api.current_state()

        self.assertEqual(len(current_state), 8)
        self.assertIn((-1, 7, "task8 extended command"), current_state)

    def test_get_current_state(self):
        current_state = self.api.current_state()

        expected_state = [
            (-8, 4, 'task5'),
            (-3, 0, 'task1'),
            (-3, 2, 'task3'),
            (-2, 1, 'task2'),
            (-2, 5, 'task6'),
            (-1, 3, 'task4')
        ]
        self.assertEqual(current_state, expected_state)

    def test_pop_item(self):
        next_item = self.api.pop_item()

        self.assertEqual(next_item, 'task5')  # Assert that task5 has the highest priority

        # Pop all items
        self.api.pop_item()
        self.api.pop_item()
        self.api.pop_item()
        self.api.pop_item()
        self.api.pop_item()

        self.assertIsNone(self.api.pop_item())  # After processing all items, the next item should be None


if __name__ == '__main__':
    unittest.main()
