'''
    작성일 : 2023년 09월 27일
    작성자 : 컴퓨터공학부 201995004 강명일
    설명 : range() 함수
'''
for i in range(3):
    print(i, end='. ') # end = ' ' 로 지정하면 줄바꿈하지 않는다.
    print("안녕하세요.")
    print("   강명일입니다.")

# range(시작값, 숫자 앞까지, 증가값(감소값))
# C언어 for(초기값; 조건식; 증감식)
for i in range(1, 6): # range(1, 6, 1) 1은 default값.
    print(i, end=' ')

print() # 빈줄 출력

# 10~1까지 출력
for i in range(10, 0, -1):
    print(i, end=' ')