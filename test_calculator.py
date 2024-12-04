# test_calculator.py

# Calculator 클래스 가져오기
from calculator import Calculator

# Calculator 기능 테스트 함수
def test_operations():
    calc = Calculator()
    # 덧셈 테스트
    assert calc.calculate("add", 10, 5) == 15, "덧셈 테스트 실패"
    # 뺄셈 테스트
    assert calc.calculate("subtract", 10, 5) == 5, "뺄셈 테스트 실패"
    # 곱셈 테스트
    assert calc.calculate("multiply", 10, 5) == 50, "곱셈 테스트 실패"
    # 나눗셈 테스트
    assert calc.calculate("divide", 10, 5) == 2, "나눗셈 테스트 실패"
    print("모든 테스트가 성공적으로 통과되었습니다!")

# 메인 실행
if __name__ == "__main__":
    test_operations()
