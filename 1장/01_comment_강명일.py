'''
    작성일 : 2023년 09월 13일
    작성자 : 컴퓨터공학부 201995004 강명일
    설명 : 주석과 출력 함수 사용하기.
'''

# 학과 학번 이름을 저장하시오.
major = "컴퓨터공"
id=201995004
name="강명일"

# 출력 1/2
print("학과 : ",major)
print("학번 :  {}" .format(id))

# 안녕하세요. 저는 00학과 00학번 000입니다.
print("안녕하세요. 저는", major, "학과", id, "학번", name, "입니다.")
# print("안녕하세요. 저는 {} 학과 {} 학번 {} 입니다." .format(major, id, name))

# 파이썬을 10개 출력하시오. (반복문 사용 안함)

print("파이썬")
print("파이썬")
print("파이썬")
print("파이썬")
print("파이썬")
print("파이썬")
print("파이썬")
print("파이썬")
print("파이썬")
print("파이썬")

print("파이썬 " * 256)

num1 = '10'
num2 = '20'

print(num1+num2)
