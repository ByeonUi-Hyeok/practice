<<<<<<< HEAD
res = 0
a= 100

for i in range(1, 3):
    res = a >> i
    #print(f' 중간값 {res}')
    res = res + 1
    #print(f' 중간값+1 {res}')

#print(f' 최종값 {res}')
print(res)


# 정처기 비트이동문제 구현
=======
coffee = {'아메리카노':2500,'카푸치노':3500,'카페라떼':3000,'레몬레이드':2000}

for c in sorted(coffee.items(),key=lambda x:x[1],reverse=True):
    print(c[0],end=' ')
print()

order = input('메뉴명 >>> ')

print(coffee.get(order))
>>>>>>> 834029442b01bbbb2016cb0a60c9a942f1ad6919
