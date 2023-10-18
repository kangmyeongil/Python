'''
    작성일 : 2023년 10월 18일
    작성자 : 컴퓨터공학부 201995004 강명일
    설명 : 도시의 인구 자료에 대한 슬라이싱하기.
'''

# 다음과 같은 리스트가 생성되어 있다.
population = ["Seoul", 9765, "Busan", 3441, "Incheon", 2954]

# 2번째 요소 출력
print("서울 인구 : ", population[1])
# 마지막 요소 출력
print("인천 인구 : ", population[-1])
# step을 이용하여 2단위로 슬라이싱하여 출력
print("도시 리스트 : ", population[::2])
# step과 sum을 이용하여 1번째 요소부터 2단위로 슬라이싱한 후 나온 값들을 합한다
print("인구의 합 : ", sum(population[1::2]))