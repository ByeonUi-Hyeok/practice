# 21.06.06
# 문자열 처리 / 입력받은 문자열 숫자, 문자, 특수문자 구분하기
# 예외처리문 / 정규식표현 쓰기
# 숫자 10처리하지 못함
filename_ap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
filename_result = []
filename_input = input()
filename_nb = '0123456789'
filename_ast = '*#'

for i in filename_input:
    for j in range(10):
        if i == str(j) :
            #if i == '1':
            filename_result.append(int(i))
            break
        elif i in filename_ap :
            filename_result.append(i)
            break
        elif i in filename_ast :
            filename_result.append(i)
            break
print(filename_result)