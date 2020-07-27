import src.exceptions.exceptions as exceptions
import sys


class Calculator:
    def add(self, a, b):
        a = self._check_numeric(a)
        b = self._check_numeric(b)
        print("in add")
        return a + b

    def subtract(self, a, b):
        a = self._check_numeric(a)
        b = self._check_numeric(b)
        return a - b

    def multiply(self, a, b):
        a = self._check_numeric(a)
        b = self._check_numeric(b)
        return a * b

    def divide(self, a, b):
        a = self._check_numeric(a)
        b = self._check_numeric(b)
        if b == 0:
            raise exceptions.CalculatorException(
                "The denominator cannot be 0 for division"
            )
        else:
            return a / b

    def _check_numeric(self, a):
        try:
            a = float(a)
            return a
        except ValueError:
            raise exceptions.CalculatorException(
                f"The supplied argument {a} is not numeric")


def main():
    c = Calculator()

    operations = [c.add, c.subtract, c.multiply, c.divide]

    for index, operation in enumerate(operations, start=1):
        print(f"{index}. {operation.__name__}")
    print("Enter q or Q for quit")

    choice = None
    while True:
        choice = input("Enter your choice: ")
        if choice not in ('1', '2', '3', '4', 'q', 'Q'):
            print("You must choose one of these choices: 1, 2, 3, 4, q or Q")
            continue
        else:
            if choice == 'q' or choice == 'Q':
                print("Good Bye")
                sys.exit()
            else:
                a = input("Enter a: ")
                b = input("Enter b: ")
                try:
                    result = operations[int(choice) - 1](a, b)
                    print(f"Result: {result}")
                except exceptions.CalculatorException:
                    print("Please enter numeric arguments.")
                    print("For division, the denominator cannot be 0")
                    continue


if __name__ == '__main__':
    main()
