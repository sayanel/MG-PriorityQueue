import logging

from src.priority_queue_cli import PriorityQueueCLI

_logger = logging.getLogger(__name__)
_logger.setLevel(logging.DEBUG)


if __name__ == '__main__':
    _logger.info("Start Priority Queue Command Line Interface.")

    cli = PriorityQueueCLI()
    cli.run()
