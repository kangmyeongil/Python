'''
    작성일 : 2023년 09월 20일
    작성자 : 컴퓨터공학부 201995004 강명일
    설명 : 선택문 if~else
           random을 이용한 가위바위보 게임.
           random 함수로 생성된 정수를 가지고 게임을 진행합니다.

           0 = 가위
           1 = 바위
           2 = 보

           두 명의 플레이어의 이름을 입력받아 가위바위보 게임을 진행합니다.
'''
import random # random 함수 가져오기.(포함 시키기)

print("가위바위보 게임 시작")
p1 = input("Player 1의 이름을 입력하세요. ")
p2 = input("Player 2의 이름을 입력하세요. ")

game = random.randrange(3) # 랜덤으로 0, 1, 2 생성하여 변수에 저장.
game2 = random.randrange(3)

print(p1, " : ", end='')
if game == 0 :
    print("가위")
if game == 1 :
    print("바위")
if game == 2 :
    print("보")    

print(p2, " : ", end='')
if game2 == 0 :
    print("가위")
if game2 == 1 :
    print("바위")
if game2 == 2 :
    print("보")    


if game == 0 :
    if game2 == 0 :
        print("비겼습니다")
    if game2 == 1 :
        print(f"{p2}이 이겼습니다")
    if game2 == 2 :
        print(f"{p1}이 이겼습니다")
elif game == 1 :
    if game2 == 0 :
        print(f"{p1}이 이겼습니다")
    if game2 == 1 :
        print("비겼습니다")
    if game2 == 2 :
        print(f"{p2}이 이겼습니다")
elif game == 2 :
    if game2 == 0 :
        print(f"{p2}이 이겼습니다")
    if game2 == 1 :
        print(f"{p1}이 이겼습니다")
    if game2 == 2 :
        print("비겼습니다")