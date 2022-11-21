class Equipment:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


class Composite:
    def __init__(self, name: str):
        self.name = name
        self.items = []

    def add(self, equipment: Equipment):
        self.items.append(equipment)
        return self

    @property
    def price(self):
        return sum([x.price for x in self.items])

    @price.setter
    def price(self, value):
        self.price = value


if __name__ == '__main__':
    computer = Composite("PC")
    processor = Equipment("Processor", 1000)
    hard_drive = Equipment("Hard drive", 250)
    memory = Composite("Memory")
    rom = Equipment("Read only memory", 100)
    ram = Equipment("Random access memory", 75)

    mem = memory.add(rom).add(ram)
    pc = computer.add(processor).add(hard_drive).add(memory)

    print(pc.price)
