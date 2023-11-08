'''
    작성일 : 2023년 11월 8일
    작성자 : 컴퓨터공학부 201995004 강명일
    설명 : lab 8-3 파티 동시 참석자 알아내기
'''
partyA = set(["Park", "Kim","Lee"])
partyB = set(["Park", "Choi"])

# 모두 참석한 사람
print("모두 참석한 사람은 ",partyA.intersection(partyB))

# 파티 A,B에 참석한 사람을 중복되지 않도록
print("파티 A,B에 참석한 사람들 ", partyA.union(partyB))

# 파티 A, 파티 B중 한군데만 참석
print("파티 A,B에 중복없이 참석한 사람", partyA.symmetric_difference(partyB))

# 파티 A에만 참석한 사람
print("파티 A에만 참석", partyA.difference(partyB))