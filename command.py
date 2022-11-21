from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, command_id: int):
        self.command_id = command_id

    @abstractmethod
    def execute(self):
        pass


class OrderAddCommand(Command):
    def execute(self):
        print(f"Adding order with id {self.command_id}")


class OrderPayCommand(Command):
    def execute(self):
        print(f"Paying for order with id {self.command_id}")


class CommandProcessor:
    queue = []

    def add_to_queue(self, command: Command):
        self.queue.append(command)

    def process_commands(self):
        [item.execute() for item in self.queue]
        self.queue = []


if __name__ == '__main__':
    processor = CommandProcessor()
    processor.add_to_queue(OrderAddCommand(1))
    processor.add_to_queue(OrderAddCommand(2))
    processor.add_to_queue(OrderPayCommand(1))
    processor.add_to_queue(OrderPayCommand(2))

    processor.process_commands()
