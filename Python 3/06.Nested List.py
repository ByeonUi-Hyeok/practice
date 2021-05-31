# 1. [ggoreb]신림동/둔산동 출력하기

filename_ex = [
 'ggoreb',
 20,
 ['서울', '관악구', '신림동'],
 ['대전', '서구', '둔산동']
]

print('[%s]%s/%s' % (filename_ex[0], filename_ex[2][2], filename_ex[-1][-1])) #[][] 리스트 속의 리스트 인덱스


# 2. 리스트 정렬하기

filename_sortlist = ['p', 'y', 't', 'h', 'o', 'n']

filename_sortlist.sort()               # 정렬함수 (sort) 아스키코드의 지정된 알파벳의 숫자순으로 정렬함
print(filename_sortlist)

filename_sortlist.sort(reverse=True)   # reverse =True 는 역순
print(filename_sortlist)