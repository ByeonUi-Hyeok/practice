# 21.06.01
# if(2)

# 표준입력으로 국어, 영어, 수학, 과학 점수 입력
# 4과목 평균 80 이상일 시 합격 그 미만 불합격
# 0 ~ 100 점만 존재 그 이외의 점수시 잘못된 점수 출력
# 잘못된 점수 출력시 합격 불합격 출력X

filename_inputdata = input().split(' ')                                 # 자료 입력
filename_sum       = 0
for i in  range(4):                                                      # 0,1,2,3 을  i변수에 순서대로 입력한다
    #print('입력데이터',i,'번째는',filename_inputdata[i])                 # i 변수에 삽입된 숫자 확인용 프린트
    if int(filename_inputdata[i]) > 100 :                                # 문자열로 입력받은 입력데이터를 정수형으로 바꾸고 0번인덱스부터 100과 비교              
        print(' 잘못된 점수 ')                                            # 100 초과시 출력
        filename_Dummy = 1                                               # 불합격 출력하지 않게하기위할 쓰레기값...
        break
    else : 
        filename_sum = filename_sum + int(filename_inputdata[i]) 
        # print( filename_sum / 4 )                                      # 입력데이터 평균을 보기위한 함수
        if i >= 3 :
            if filename_sum / 4 >= 80:
                print ('합격')
                break
            else :
                print ('불합격')