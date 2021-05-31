# 21.05.31
# control statement

# 1. 주어진 숫자가 홀수인지 짝수인지 확인할 수 있는 조건문 작성

filename_exnum = 122
if filename_exnum % 2 == 0 :
    print( '짝수' )
else : 
    print( '홀수' )

''' 2. Dictionary로 구성된 이수 과목 데이터 중 '자료구조'가 있는지 확인하여
       '자료구조'의 점수가 60점 이상이면 '이수 완료'를 출력하고 조건이 맞지 않으면
       '재수강'을 출력하는 코드 작성 '''

filename_subject = {'자료구조' : 80, '알고리즘' : 60, '네트워크' : 90}
if filename_subject[ '자료구조' ] >= 60 : 
    print( '이수완료' )
else :
    print( '재수강' )


# 3. 1부터 1000 까지의 정수 합 구하기
filename_num = 1
filename_total = 0
while True :
    filename_total += filename_num
    filename_num += 1
    if filename_num == 1001 : 
        break
print(filename_total)

# 3. 1부터 1000 까지의 정수 합 구하기 (2)
filename_num2 = 1
filename_total2 = 0
while filename_num2 <= 1000:
    filename_total2 = filename_total2 + filename_num2
    filename_num2 = filename_num2 + 1
print(filename_total2)