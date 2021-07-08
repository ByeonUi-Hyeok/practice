coffee = {'아메리카노':2500,'카푸치노':3500,'카페라떼':3000,'레몬레이드':2000}

for c in sorted(coffee.items(),key=lambda x:x[1],reverse=True):
    print(c[0],end=' ')
print()

order = input('메뉴명 >>> ')

print(coffee.get(order))
