# 21.05.31 while

while True :
    print ( '=' * 20 )              # = 문자열 20번 출력
    print ( '1. 입력' )
    print ( '2. 출력' )
    print ( '3. 종료' )
    print ( '=' * 20 )              # = 문자열 20번 출력

    filename_output = input('메뉴를 선택하세요 : ')              # 숫자(문자열)를 입력받음
    if filename_output == '3': break                            # 3을 입력받으면 종료됨

print('종료되었습니다.')