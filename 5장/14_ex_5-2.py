'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 201995004 강명일
    설명 : 두 수를 입력 받아
           1. 두 수 사이의 합계 출력하기
           2. 두 수 사이의 짝수의 합계 출력하기

           심화문제 5.2, 141쪽
           for 또는 while
'''
# 수 입력하기
num1 = int(input("수 1번 입력 : "))
num2 = int(input("수 2번 입력 : "))
# num1의 수가 클 때도 num2의 수가 클 때도 계산 되도록 하기위해 다른 변수 설정
num3 = 0
# 두 수 사이의 합계
sum=0
# 두 수 사이의 짝수의 합계
evensum=0
# num1이 num2보다 크다면 num1과 num2의 값을 서로 바꿔서 아래의 반복문을 실행하도록 설정
if(num1 > num2) :
    num3 = num1
    num1 = num2
    num2 = num3
# num1이 num2보다 작을 때에 num1을 계속 증가시키며 사이의 합의 값과 짝수의 합을 구한다
while num1 <= num2 :
    sum=sum+num1
    if(num1%2 == 0):
        evensum=evensum+num1
    num1 += 1

# 계산한 결과 출력
print(f"두 수 사이의 합계 = {sum}, 두 수 사이의 짝수의 합계 = {evensum}")