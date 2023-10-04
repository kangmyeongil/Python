'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 201995004 강명일
    설명 : 반복을 제어하는 break, continue
            교재 137 페이지
            
    Test word = programming
'''

word = input("단어를 입력하세요 : ")

print(":: break1 ::")
for i in word :
    if i == 'a' or i == 'e' or i == 'i'or i == 'o' or i == 'u' : # 모음 만나면 반복중지
        break # 포함된 반복이 종료
    else :
        print(i, end='') # o 에서 break 되어서 pr 까지 출력이 될것이다.

print()

print(":: break2 ::")
for i in word :
    if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] : # if문에서도 사용할 수 있는 in
        break # 포함된 반복이 종료 (반복을 빠져나간다)
    else :
        print(i, end='')
print()

print(":: continue ::")
for i in word :
    if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] : # if문에서도 사용할 수 있는 in
        continue # 반복의 처음으로 돌아간다. 아래 문장을 만날 수 없다.
    print(i, end='') # 모음 부분을 모두 지우고 prgrmmng 이 나올 것이다.