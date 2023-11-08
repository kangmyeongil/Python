'''
    작성일 : 2023년 11월 8일
    작성자 : 컴퓨터공학부 201995004 강명일
    설명 : 심화문제 8-6
    
    1. 학번,이름,전화번호의 3쌍을 요소를 가지는
    student_tuple라는 튜플이 존재한다.

    2. 이 튜플을 수정하여 {학번: [이름, 전화번호]}의 쌍으로 이루어진 딕셔너리를 만들어 출력

    3. 이 정보를 이용하여 학생의 학번을 입력받아 이름과 전화번호를 출력하는 학사정보 프로그램을 작성
'''

student_tuple = (('211101', '강이안', '010-123-1111'), ('211102', '박동민', '010-123-2222'), ('211103', '김수정', '010-123-3333'))
student_dict={}
# 딕셔너리에 내용 추가
for studno, name, phone in student_tuple:
    student_dict[studno] = [name, phone];

# 내용 출력
for key, value in student_dict.items():
    print(key, " : ", value[0])

studno = input("학번을 입력하시오 : ")
if studno in student_dict.keys():
    print(f"{studno} 학생은 {student_dict[studno][0]}이며, 전화번호는 {student_dict[studno][1]}입니다.")