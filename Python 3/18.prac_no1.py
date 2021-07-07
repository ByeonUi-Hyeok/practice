items = {'사과':12,'배':9,'귤':20}

item = input("과일명을 입력하세요 >>> ")
count = input("과일의 갯수를 입력하세요 >>> ")
if count.isdigit():
    count = int(count)
    if items[item] :
        box = count // items[item]
        remainder = count % items[item]
        print('{}박스 {}개 입니다.'.format(box,remainder))
    else:
        print("해당 품목이 없습니다.")
else:
    print("숫자로 입력하세요")