'''
    작성일 : 2023년 11월 8일
    작성자 : 컴퓨터공학부 201995004 강명일
    설명 : 심화문제 8-3
    
    1. 학번,이름,전화번호의 3쌍을 요소를 가지는
    student_tuple라는 튜플이 존재한다.

    2. 이 튜플을 수정하여 {학번: [이름, 전화번호]}의 쌍으로 이루어진 딕셔너리를 만들어 출력

    3. 이 정보를 이용하여 학생의 학번을 입력받아 이름과 전화번호를 출력하는 학사정보 프로그램을 작성

    4. student_tuple의 마지막 항목으로 학점을 추가한다.
     이 정보를 바탕으로 딕셔너리를 만들어 출력.

    5. 학생의 학점 평균을 출력하시오.
'''
student_tuple = (('211101', '조성훈', '010-1234-4500'), ('211102', '김은지', '010-2230-6540'), ('211103', '윤소정', '010-3232-7788'))
student_dict={}
# 딕셔너리에 내용 추가
for studno, name, phone in student_tuple:
    student_dict[studno] = [name, phone];

# 내용 출력
for key, value in student_dict.items():
    print(key, " : ", value)

# 학번 입력받아 이름과 연락처 출력
studno = input("학번을 입력하시오 : ") # int로 입력받으면안됨!!!
if studno in student_dict.keys():
    print("이름 : ", student_dict[studno][0])
    print("연락처 : ", student_dict[studno][1])

# 학점 정보 추가
student_dict['211101'].append(4.5)
student_dict['211102'].append(3.8)
student_dict['211103'].append(3.0)

for key, value in student_dict.items():
    print(key, " : ", value)

# 학점의 평균 출력
sum = 0
for i in student_dict.keys():
    sum += student_dict[i][2]
'''
for key, value in student_dict.items():
    sum += value[2]
 위와 같은 합계가 된다
'''
avg = sum / len(student_dict.keys())
print(f"평균은 {avg:.2f}")
