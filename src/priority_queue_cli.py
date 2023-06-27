import argparse

from src.priority_queue_api import PriorityQueueAPI


class PriorityQueueCLI:
    """
        Command-line interface (CLI) for interacting with the Priority Queue.

        Attributes:
            api (PriorityQueueAPI): Instance of the PriorityQueueAPI class.
            parser (argparse.ArgumentParser): Argument parser for the CLI commands.

    """

    def __init__(self):
        self.api = PriorityQueueAPI()

        self.parser = argparse.ArgumentParser(description='Priority Queue CLI')
        subparsers = self.parser.add_subparsers(dest='action', help='Available actions')

        # Add work item
        add_parser = subparsers.add_parser('add', help='Add a new item to the Priority Queue')
        add_parser.add_argument('priority', type=int, help='Priority of the item (0-10)')
        add_parser.add_argument('command', nargs='+', help='Command to be executed')

        # Process next command
        subparsers.add_parser('pop', help='Process the next item from the Priority Queue')

        # Display the current state of the Queue
        subparsers.add_parser('display', help='Display the current state of the Priority Queue')

    def process_command(self, args):
        """Processes the command specified by the user."""

        if args.action == 'add':
            command = args.command = ' '.join(args.command)
            self.api.add_item(
                {
                    'priority': args.priority,
                    'command': command
                }
            )
            print('Item added successfully!')

        elif args.action == 'pop':
            next_command = self.api.pop_item()
            if next_command:
                print('Next command:', next_command)
            else:
                print('No items in the queue.')

        elif args.action == 'display':
            current_state = self.api.current_state()
            print(f"Display current state : {current_state}")

    def run(self):
        """Runs the Priority Queue CLI."""

        print('Welcome to the Priority Queue CLI!')
        print('Use the following commands:')
        print('  - add <priority> <command>: Add a new item to the priority queue')
        print('  - pop: Process the next item from the priority queue')
        print('  - display: Display the current state of the priority queue')
        print('  - quit: Exit the program')

        while True:
            try:
                user_input = input('>> ')
                if user_input == 'quit':
                    break

                args = self.parser.parse_args(user_input.split())
                self.process_command(args)

            except ValueError as e:
                print('Error:', e)

            except SystemExit:
                print("Invalid command or choice.")
