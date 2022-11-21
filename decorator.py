from abc import ABC, abstractmethod


class CoffeeMachine(ABC):
    @abstractmethod
    def make_small_coffee(self):
        pass

    @abstractmethod
    def make_large_coffee(self):
        pass


class BasicCoffeeMachine(CoffeeMachine):
    def make_small_coffee(self):
        print("Basic coffee machine: Making small coffee")

    def make_large_coffee(self):
        print("Basic coffee machine: Making large coffee")


class EnhancedCoffeeMachine(CoffeeMachine):
    def __init__(self, basic_machine: BasicCoffeeMachine):
        self.basic_machine = basic_machine

    def make_small_coffee(self):
        self.basic_machine.make_small_coffee()

    def make_large_coffee(self):
        print("Enhanced coffee machine: Making large coffee")

    def make_milk_coffee(self):
        print("Enhanced coffee machine: Making milk coffee")
        self.basic_machine.make_small_coffee()
        print("Enhanced coffee machine: adding milk")


if __name__ == '__main__':
    basic_machine = BasicCoffeeMachine()
    enhanced_machine = EnhancedCoffeeMachine(basic_machine)

    enhanced_machine.make_small_coffee()
    print()
    enhanced_machine.make_large_coffee()
    print()
    enhanced_machine.make_milk_coffee()