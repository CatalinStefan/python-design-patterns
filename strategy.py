class Printer:
    def __init__(self, format_strategy):
        self.format_strategy = format_strategy

    def print_string(self, message: str):
        print(self.format_strategy(message))


def lowercase_formatter(msg):
    return msg.lower()


def uppercase_formatter(msg):
    return msg.upper()


if __name__ == '__main__':
    input_string = "LOREM ipsum DOLOR sit amet"

    low_printer = Printer(lowercase_formatter)
    low_printer.print_string(input_string)

    up_printer = Printer(uppercase_formatter)
    up_printer.print_string(input_string)