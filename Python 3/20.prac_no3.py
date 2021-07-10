res = 0
a= 100

for i in range(1, 3):
    res = a >> i
    #print(f' 중간값 {res}')
    res = res + 1
    #print(f' 중간값+1 {res}')

#print(f' 최종값 {res}')
print(res)


# 정처기 비트이동문제