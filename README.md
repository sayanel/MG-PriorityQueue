# MG-PriorityQueue

The PriorityQueue is a simple priority queue implementation that allows you to add work items with different priorities and process them based on their priority order.

Overall, the code architecture promotes separation of concerns and encapsulation. The WorkItem class handles the representation and validation of work items, while the PriorityQueue class manages the priority queue operations. The PriorityQueueAPI class serves as a high-level interface for interacting with the priority queue, abstracting away the internal implementation details. This architecture allows for flexibility and maintainability, as it isolates different responsibilities and promotes modular code.

## Features

    Add work items with a priority and command.
    Process the highest-priority work item.
    Display the current state of the priority queue.

## Installation and Usage

The PriorityQueue CLI provides a command-line interface to interact with the priority queue. Follow the steps below to use the CLI:

1. Clone the repository:

```bash
git clone https://github.com/sayanel/MG-PriorityQueue.git
```

2. Navigate to the project directory:

```bash
cd MG-PriorityQueue
```

3. Run the CLI using the following command:

```bash
python __main__.py
```

1. The CLI will display the available commands and instructions on how to use them.

2. Use the following commands:
   - add <priority> <command>: Add a new item to the priority queue. Replace <priority> with an integer between 0 and 10 representing the priority of the item, and <command> with the command to be executed.
   - pop: Process the next item from the priority queue.
   - display: Display the current state of the priority queue.
   - quit: Exit the program.

## Running Tests

The PriorityQueue project includes unit tests to ensure the correctness of its functionality. To run the tests, follow these steps:
1. Open a terminal and navigate to the project directory.
2. Run the tests using the following command:

```bash
python -m unittest discover tests
```


## What's next
- Add a persistence layer to save and retrieve the state of the queue.
- Allow user to search, modify or delete work items.
- Think about concurrency.
- Add tests for our PriorityQueue and WorkItem models.
- Add a setup.py or package.py.
