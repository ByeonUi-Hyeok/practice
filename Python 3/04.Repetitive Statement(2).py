# 21.05.31 while
import random

while True :                                                    # While이 참일동안 반복, While은 참.(무한반복)
    Filename_Number = random.randint( 1, 5 )                    # 1~5까지 수중 랜덤 숫자를 추출한다.
    print( '추출된 숫자: %d' % Filename_Number )                 # 추출한 숫자를 출력한다.
    if Filename_Number == 5 :                                   # 추출된 숫자가 5와 같으면
        break                                                   # 종료한다.

'''
1 ~ 5 까지 랜덤 수를 추출해서 ( 보통 파이썬의 범위열에서 뒤에숫자는 제외하지만 randint는 뒤에수를 포함함.)
5라는 숫자가 나올때까지 반복하는 코드
'''


