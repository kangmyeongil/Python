'''
    작성일 : 2023년 11월 1일
    작성자 : 컴퓨터공학부 201995004 강명일
    설명 : lab 7-6 도시의 이름과 인구를 튜플로 묶어보자.
'''
# 다음과 같은 리스트가 생성되어 있다.
city_info =[('서울', 9765), ('부산', 3441), ('인천', 2954), ('광주', 1501), ('대전', 1531)]

# 최대값 저장위한 변수
max_pop = city_info[0][1] # 첫 번째 항목이 기준.
# 최소값 저장위한 변수
min_pop = city_info[0][1]
# 전체 인구수 저장위한 변수
total_pop = 0

# 인구수가 가장 많은 도시 출력위한 변수
max_city = city_info[0][0] # 첫 번째 항목이 기준.
# 인구수가 가장 적은 도시 출력위한 변수
min_city = city_info[0][0]

# city_info 리스트에서 반복문 시작
for city, population in city_info:
    total_pop += population
    # 현재 인구수가 여태까지 저장되어있는 max_pop(최대값)보다 크다면
    if population > max_pop :
        # 지금 도시를 최대인구 도시로 재설정하고 인구수를 재설정한다.
        max_pop = population
        max_city = city
    # 현재 인구수가 여태까지 저장되어있는 min_pop(최소값)보다 작다면
    if population < min_pop:
        # 지금 도시를 최소인구 도시로 재설정하고 인구수를 재설정한다.
        min_pop = population
        min_city = city


print(f"최대인구 : {max_city}, 인구 : {max_pop} 천명")
print(f"최소인구 : {min_city}, 인구 : {min_pop} 천명")
# 평균 인구는 모든 도시의 전체 인구수 / 모든 도시 수
print(f"리스트 도시 평균 인구 : {total_pop / len(city_info)} 천명")