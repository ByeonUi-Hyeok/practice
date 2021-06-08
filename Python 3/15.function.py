# 21.06.07
# 배열 array의 i부터 j까지 k번째 있는 수 구하기

from _typeshed import SupportsLessThan


def funcname_solution(filename_array, filename_commands):
    filename_answer =[]
    for b in filename_commands:
        i = b[0]
        j = b[1]
        k = b[2]
        if i == j :
            filename_l = filename_array[i-1]
            filename_answer.append(filename_l)
            continue
        elif i != j :
            filename_l = filename_array[i-1:j]
            filename_l.sort()
            filename_answer.append(filename_l[k-1])
    return filename_answer


arr  = [1,2,3,4,5,6,7,8,9,10]
comm = [[1,1,1],[1,5,3],[2,8,3]] 
print( funcname_solution(arr, comm) )
