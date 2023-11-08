'''
    작성일 : 2023년 11월 8일
    작성자 : 컴퓨터공학부 201995004 강명일
    설명 : 집합 set()
'''

# 빈 집합 생성
number = set()

# 숫자 3개로 이루어진 집합
number1 = {2,1,3} # 키와 밸류값 없이 숫자만 있으면 집합이다.
print("집합 : ", number1) # 자동 정렬

# 리스트로부터 집합 생성
number2 = set([1,2,3,1,2])
print("집합 : ", number2) # 중복을 허용하지 않는다

text1 = set("asdfasdf")
print("text1 = ", text1) # 각 문자가 하나의 요소가 되어 생성, 중복허용 x

numbers = {2,4,5,1,2}
if 1 in numbers: # numbers 안에 1이 존재한다면
    print("집합에 1이 있습니다.")

# 집합은 순서가 없어 index로 접근 불가능. 반복문으로 접근하여 출력 가능
numbers = {1, 5, 4, 7, 3, 2, 3, 7, 8}
for num in numbers :
    print(num, end=" ")
print()

# 정렬 후 출력하기
for num in sorted(text1):
    print(num, end=" ")
print()

# 추가하기
numbers.add(100)
print(numbers)
for num in sorted(numbers) :
    print(num, end=" ")
print()

numbers.remove(100)
print(numbers)