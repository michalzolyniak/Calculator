class Calculator:
    """
        Performing mathematical operations:
        addition, multiplication, subtraction, division between two numbers
    """

    def add(self, a, b):
        """
        :param float a: number
        :param float b: number
        :return: float result: result of adding two numbers
        """
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def mul(self, a, b):
        """
        :param float a: number
        :param float b: number
        :return: float result: result of multiplication two numbers
        """
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        # self.history.append(f"")
        return result

    def sub(self, a, b):
        """
        :param float a: number
        :param float b: number
        :return: float result: result of subtraction two numbers
        """
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def div(self, a, b):
        """
        :param float a: number
        :param float b: number
        :return: float result: result of division two numbers
        """
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result


class LoggingCalculator(Calculator):
    """
        Performing mathematical operations with a history of earlier operations.
    """

    def __init__(self):
        self.history = []
        super().__init__()


if __name__ == '__main__':
    calc = LoggingCalculator()
    print(calc.add(2, 3))
    print(calc.mul(3, 3))
    print(calc.sub(7, 4))
    print(calc.div(5, 2))
    print(calc.history)
