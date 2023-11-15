'''
    작성일 : 2023년 11월 15일
    작성자 : 컴퓨터공학부 201995004 강명일
    설명 : LAB 9-2 : 트위터 메시지 처리의 단위 추출
        띄어쓰기로 문자열을 분리하고, 단어의 개수를 찾아라
'''

text = "There's a reason some people are working to make \
    it harder to vote, especially for people of color. \
    It's because when we show up, things change."

# 띄어쓰기로 문자열을 분리하고, 단어의 개수를 찾아라
# 단어의 개수는 len(리스트 항목 개수를 찾는 함수)으로 찾기
# count로는 찾는 기준이 없음
text2 = text.split()
print(text2)
print('word count : ', len(text2))

# 도전문제 9-1
# 회사 이름은 **로 표시
# KT, Samsung, LG, SKT
text = '[ARTICLE] 200820 BLACKPINK Jennie is regarded to have great effect on KT Mystic \
    Red as it was chosen by 50% of those who prebooked for the Samsung Galaxy Note 20 ( LG \
    U+ Mystic Pink 30%, SKT Mystic Blue not disclosed) '
# 모든 문자를 소문자로 변환
low = text.lower()

# 소문자로 바뀐 단어들을 공백으로 구분한다.
# 구분된 단어를 검사한다. => 단어가 kt 또는 samsung 또는 lg 또는 skt인가?
# 검사하는 단어가 회사명이면 **으로 바꾼다.
# 아니면 그 단어는 그대로 사용한다.
a = low.split()
text = ''
for x in a:
    if x == 'skt' or x == 'kt' or x == 'samsung' or x == 'lg':
        text += x.replace(x,'** ')
    else:
        text += x + ' '
print(text)