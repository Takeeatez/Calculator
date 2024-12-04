# calculator.py

# 계산기 클래스: 덧셈, 뺄셈, 곱셈, 나눗셈 기능을 제공합니다.
class Calculator:
    def __init__(self):
        # 계산기 초기화
        print("Calculator initialized")

    def calculate(self, operation, a, b):
        """
        주어진 연산(operation)에 따라 계산을 수행합니다.
        :param operation: 수행할 연산 (add, subtract, multiply, divide)
        :param a: 첫 번째 숫자
        :param b: 두 번째 숫자
        :return: 연산 결과
        """
        if operation == "add":
            return self.add(a, b)
        elif operation == "subtract":
            return self.subtract(a, b)
        elif operation == "multiply":
            return self.multiply(a, b)
        elif operation == "divide":
            return self.divide(a, b)
        else:
            raise ValueError("알 수 없는 연산입니다.")

    def add(self, a, b):
        """
        두 숫자의 합을 반환합니다.
        :param a: 첫 번째 숫자
        :param b: 두 번째 숫자
        :return: 합
        """
        return a + b

    def subtract(self, a, b):
        """
        두 숫자의 차를 반환합니다.
        :param a: 첫 번째 숫자
        :param b: 두 번째 숫자
        :return: 차
        """
        return a - b

    def multiply(self, a, b):
        """
        두 숫자의 곱을 반환합니다.
        :param a: 첫 번째 숫자
        :param b: 두 번째 숫자
        :return: 곱
        """
        return a * b

    def divide(self, a, b):
        """
        두 숫자의 나눗셈 결과를 반환합니다.
        0으로 나눌 경우 예외를 발생시킵니다.
        :param a: 첫 번째 숫자
        :param b: 두 번째 숫자
        :return: 나눗셈 결과
        """
        if b != 0:
            return a / b
        else:
            raise ValueError("0으로 나눌 수 없습니다.")
