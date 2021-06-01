# 21.06.01
# if(1)

# 표준입력으로 국어, 영어, 수학, 과학 점수 입력
# 4과목 평균 80 이상일 시 합격 그 미만 불합격
# 0 ~ 100 점만 존재 그 이외의 점수시 잘못된 점수 출력
# 잘못된 점수 출력시 합격 불합격 출력X

filename_inputdata = input().split(' ')                                               # 공백을 기준으로 입력 받음

filename_Kor = int(filename_inputdata[0])                                             # 문자열 리스트로 입력받기 때문에 정수형으로 형 변환
filename_Eng = int(filename_inputdata[1])
filename_Mat = int(filename_inputdata[2])
filename_Sie = int(filename_inputdata[3])
filename_avg = (filename_Kor + filename_Eng + filename_Mat + filename_Sie) / 4        # 평균점수 산출
#print(filename_inputdata, filename_Kor, filename_Eng, filename_Mat, filename_Sie)    # 입력 확인용 출력함수


if filename_Kor > 100 or filename_Eng > 100 or filename_Mat > 100 or filename_Sie > 100 :
    print ('잘못된 점수')                                                              # 입력된 점수가 100점을 초과한다면 잘못된점수 출력
else :
    if filename_avg >= 80 :                                                          # 그렇지않고 
        print('합격')                                                                 # 모든 입력의 평균이 80이 넘으면 합격
    else :
        print('불합격')                                                                # 아니면 불합격