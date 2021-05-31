# 21.05.31 Set
'''
Set은 중복 데이터를 허용하지 않고, 순서가 없음
중복 자료를 제거하기 위한 필터 역할로도 사용

'''



# 1. 두 개의 집합에서 공통 요소만 출력하기 (교집합)

filename_num1 = {6, 12, 17, 21, 34, 37}
filename_num2 = {6, 12, 19, 24, 34, 41}

filename_union = filename_num1 & filename_num2                               # 교집합 = 변수1 & 변수2
filename_union2 = filename_num1.intersection (filename_num2)                 # 교집합 = 변수1.intersection ( 변수2 )
print( filename_union )
print( filename_union2 )

# 2. Set을 활용하여 List 요소의 중복 데이터 제거하기

filename_exlist = [9, 7, 11, 26, 15, 9, 15, 26]
filename_deduplication = set( filename_exlist )                              # set내에 중복데이터 존재 할 수 없기에 set으로 만들면 중복제거
print( filename_deduplication )
filename_deduplication = list( filename_deduplication )                      # set을 원래의 데이터 list로 변경
print( filename_deduplication )
