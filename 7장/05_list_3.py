'''
    작성일 : 2023년 10월 18일
    작성자 : 컴퓨터공학부 201995004 강명일
    설명 : 리스트의 객체 생성과 참조
'''

fruits1 = ['딸기', '수박', '바나나']

# 실제 값을 복사하는 것이라 아니라 리스트의 저장 위치가 복사된다.
fruits2 = fruits1

print("fruits 1 : ", fruits1)
print("fruits 2 : ", fruits2)

fruits2[1] = '망고' #fruits2의 [1]번지 과일을 '망고'로 바꾸면..
print("fruits 1 : ", fruits1) # 모두 1번지 내용이 망고로 바뀐다.
print("fruits 2 : ", fruits2) # 주소를 참조하기 때문(같은 주소)

# 주소 확인 > 메모리 위치 정보 알아보기 id() 함수
print("fruits 1의 id : ", id(fruits1))
print("fruits 2의 id : ", id(fruits2)) # 두 리스트의 id정보가 같다

'''
    리스트 내용 복제하기 list() 함수
'''

fruits2 = list(fruits1)
print(":: 내용 복제 후 ::")
print("fruits 1 :", fruits1)
print("fruits 2 :", fruits2)

print("fruits 1의 id : ", id(fruits1))
print("fruits 2의 id : ", id(fruits2))

# 내용 복제 2
fruits3 = fruits1[:]
print(":: 내용 복제 후 2 ::")
print("fruits 1 :", fruits1)
print("fruits 3 :", fruits3)

print("fruits 1의 id : ", id(fruits1)) # id 정보가 다르다
print("fruits 3의 id : ", id(fruits3))

fruits3[0] = '수박'
print(":: fruits 3의 0번지에 수박을 넣으면 ::")
print("fruits 1 :", fruits1)
print("fruits 3 :", fruits3)
