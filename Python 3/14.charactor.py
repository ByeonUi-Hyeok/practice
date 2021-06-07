# 21.06.07
# 예외처리문 / 정규식표현 쓰기
filename_ap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
filename_result = []
filename_input = input()
filename_nb = '0123456789'
filename_ast = '*#'

for i in range(len(filename_input)):
    if filename_input[i] == '0' :
        if i - 1 == -1 :
            pass
        elif i - 1 != -1:
            if filename_input[i-1] == '1':
                continue


    for j in range(10):
        if filename_input[i] == str(j) :
            if filename_input[i] == '1' and filename_input[i+1] == '0' :
                filename_result.append(int(filename_input[i:i+2]))
                break
            filename_result.append(int(filename_input[i]))
            break
        elif filename_input[i] in filename_ap :
            filename_result.append(filename_input[i])
            break
        elif filename_input[i] in filename_ast :
            filename_result.append(filename_input[i])
            break
print(filename_result)

# 숫자 10처리 가능