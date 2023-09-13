'''
    작성일 : 2023년 09월 13일
    작성자 : 컴퓨터공학부 201995004 강명일
    설명 : 90페이지 문제 3.9
          평균 시속과 이동시간을 입력받아
          이동 시간은 시, 분, 초 단위로 출력하고,
          이동한 거리를 계산하여 출력하시오.
'''

speed = float(input("평균 시속(km/h)을 입력하세요 : "))
hour = float(input("이동 시간(h)을 입력하세요 : "))
h = int(hour)
m = int((hour - float(h)) * 60)
m2= (hour - float(h)) * 60
s = int((m2 - m) * 60)

print("평균 시속 : ", speed, "km/h")
print("이동 시간 : {} 시간 {} 분 {} 초" .format(h, m, s))
print("이동 거리 : " , speed * hour, "km/h")