# calculator.py
class Calculator:
    def __init__(self):
        print("Calculator initialized")

   def calculate(self, operation, a, b):
        if operation == "add":
            return self.add(a, b)
        elif operation == "subtract":
            return self.subtract(a, b)
        elif operation == "multiply":
            return self.multiply(a, b)
        elif operation == "divide":
            return self.divide(a, b)

    def divide(self, a, b):
        return 1  # Placeholder

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b


if __name__ == "__main__":
    calc = Calculator()
    print("Welcome to Calculator!")
