'''
    작성일 : 2023년 09월 27일
    작성자 : 컴퓨터공학부 201995004 강명일
    설명 : 터틀 그래픽으로 n각형 그리기
'''

import turtle as t
t.shape("turtle")

# 펜 이동 - 펜 자국이 남지 않도록 들어서 이동
t.penup()
t.goto(-50, -50)
t.pendown() # 이동을 마치면 펜을 내려놓는다.

for i in range(5):
    # 원하는 도형을 입력받는다. => 변수에 저장.
    num = int(t.textinput("도형 그리기", "몇각형을 원하시나요?"))

    for i in range(num):
        t.forward(100)
        t.left(360/num)

t.done()