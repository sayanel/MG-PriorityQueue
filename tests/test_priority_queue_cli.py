import unittest
from io import StringIO
from unittest.mock import patch

from src.priority_queue_cli import PriorityQueueCLI


WELCOME_MESSAGE = """Welcome to the Priority Queue CLI!
Use the following commands:
  - add <priority> <command>: Add a new item to the priority queue
  - pop: Process the next item from the priority queue
  - display: Display the current state of the priority queue
  - quit: Exit the program
"""


class TestPriorityQueueCLI(unittest.TestCase):
    def setUp(self):
        self.cli = PriorityQueueCLI()

    def test_add_item(self):
        with patch('builtins.input', side_effect=['add 5 task to execute a/path var="a_var"', 'quit']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                self.cli.run()
                output = fake_output.getvalue().strip()

                self.assertEqual(output, WELCOME_MESSAGE + 'Item added successfully!')

    def test_pop_item(self):
        with patch('builtins.input', side_effect=['add 1 task1', 'add 3 task3', 'add 2 task2', 'pop', 'pop', 'pop', 'quit']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                self.cli.run()
                output = fake_output.getvalue().strip()

                expected_output = WELCOME_MESSAGE \
                                  + 3 * "Item added successfully!\n" \
                                  + "Next command: task3\nNext command: task2\nNext command: task1"

                self.assertEqual(output, expected_output)

    def test_pop_item_with_empty_queue(self):
        with patch('builtins.input', side_effect=['pop', 'quit']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                self.cli.run()
                output = fake_output.getvalue().strip()

                self.assertEqual(output, WELCOME_MESSAGE + 'No items in the queue.')

    def test_display_current_state(self):
        with patch('builtins.input', side_effect=['display', 'quit']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                self.cli.run()
                output = fake_output.getvalue().strip()

                self.assertEqual(output, WELCOME_MESSAGE + 'Display current state : []')

    def test_invalid_command(self):
        with patch('builtins.input', side_effect=['invalid', 'quit']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                self.cli.run()
                output = fake_output.getvalue().strip()

                self.assertEqual(output, WELCOME_MESSAGE + 'Invalid command or choice.')

    def test_value_error(self):
        with patch('builtins.input', side_effect=['add 5', 'quit']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                self.cli.run()
                output = fake_output.getvalue().strip()

                self.assertEqual(output, WELCOME_MESSAGE + 'Invalid command or choice.')


if __name__ == '__main__':
    unittest.main()
