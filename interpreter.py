class AbstractExpression:
    @staticmethod
    def interpret():
        pass


# Terminal expression
class Number(AbstractExpression):
    def __init__(self, value):
        self.value = float(value)

    def interpret(self):
        return self.value


# Non-terminal expression
class AlgebraExpression(AbstractExpression):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(AlgebraExpression):
    def interpret(self):
        return self.left.interpret() + self.right.interpret()


class Subtract(AlgebraExpression):
    def interpret(self):
        return self.left.interpret() - self.right.interpret()


class Multiply(AlgebraExpression):
    def interpret(self):
        return self.left.interpret() * self.right.interpret()


class Divide(AlgebraExpression):
    def interpret(self):
        return self.left.interpret() / self.right.interpret()


if __name__ == '__main__':
    target = "3 + 5 - 2 * 7 / 5 + 11"

    tokens = target.split(" ")
    expressions = []

    for i in range(len(tokens)):
        if i == 0:
            expressions.append(Number(tokens[i]))
        elif tokens[i] == "+":
            expressions.append(Add(expressions.pop(), Number(tokens[i+1])))
        elif tokens[i] == "-":
            expressions.append(Subtract(expressions.pop(), Number(tokens[i + 1])))
        elif tokens[i] == "*":
            expressions.append(Multiply(expressions.pop(), Number(tokens[i + 1])))
        elif tokens[i] == "/":
            expressions.append(Divide(expressions.pop(), Number(tokens[i + 1])))

    result = expressions.pop().interpret()
    print(result)
