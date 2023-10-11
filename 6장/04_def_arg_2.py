'''
    작성일 : 2023년 10월 11일
    작성자 : 컴퓨터공학부 201995004 강명일
    설명 : 여러 개의 값을 넘겨주고 여러 개의 값을 돌려받기.

    두 수를 전달하여 사칙연산의 결과값을 돌려주는 함수.

    [알고리즘]
    (함수)
        3. 전달받은 값을 매개변수에 저장한다.
        4. 두 수를 가지고 사칙연산을 수행한다.
        5. 사칙연산의 결과 5개를 호출한 곳으로 돌려준다.

    (메인)
        1. 두 수를 입력받는다.
        2. 두 수를 가지고 함수를 호출한다.
        6. 돌려받은 값을 출력한다.
'''

def cals(num1,num2) :
    sum = num1+num2
    minus = num1-num2
    mul = num1*num2
    div = num1/num2
    rest = num1%num2
    return sum, minus, mul, round(div,2), rest # 돌려주는 결과는 5개

n1=int(input("첫 번째 수 입력 : "))
n2=int(input("두 번째 수 입력 : "))
sum, minus, mul, div, rest = cals(n1, n2)
print(f"{n1} + {n2} = {sum}")
print(f"{n1} - {n2} = {minus}")
print(f"{n1} * {n2} = {mul}")
print(f"{n1} / {n2} = {div}")
print(f"{n1} % {n2} = {rest}")