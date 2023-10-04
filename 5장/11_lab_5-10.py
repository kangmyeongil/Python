'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 201995004 강명일
    설명 : 사용자가 입력하는 숫자의 합
           교재 133 페이지
    문제 분석 : y가 입력되면 계속 반복한다.
                y가 아니면 종료한다.
                입력 받은 수의 합계를 계속 계산한다.
    필요한 변수 : sum = 0, answer = "y", num(입력받아 저장) 
'''

# 1. 합계 계산 위한 초기값
sum = 0
# 2. 첫 루프 실행 위해서 값 설정
answer = 'yes'
# 3. 숫자를 입력받은 후 계속 더할것인지 물으면서 합계를 계산해주고
#    answer가 yes인 동안에 합계가 출력되도록 한다.
'''
while answer == "yes" :
    num = int(input("숫자를 입력하시오: "))
    answer = input("계속?(yes/no): ")
    sum = sum + num
       
print("합계는 :", sum)
'''
# 4. break 이용하기
while answer == 'yes' :
    num = int(input("숫자를 입력하시오: "))
    answer = input("계속?(yes/no): ")
    sum = sum + num
    if (answer =="no") :
        break
print("합계는 :", sum)
