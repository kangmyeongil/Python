'''
    작성일 : 2023년 09월 27일
    작성자 : 컴퓨터공학부 201995004 강명일
    설명 : 터틀 그래픽으로 여러 개의 원을 그려보자
'''

import turtle as t
# 원 하나 그리기
# t.circle(100)

for count in range(10) :
    t.circle(100)
    t.left(360 / 10)
t.mainloop() # 종료. t.done() 과 같음