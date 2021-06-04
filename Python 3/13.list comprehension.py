'''
1. 표준 입력 정수 2개
2. 첫번째 정수부터 두번째 정수까지 지수로 하는 2의 거듭제곱 리스트 출력
3. 결과물 타입은 List
4. List의 두 번째 요소와 뒤에서 두 번째 요소 삭제
'''

#1. 일반 반복문
filename_inputa, filename_inputb = map( int, input().split(' ') )
filename_result = list()
for i in range ( filename_inputa, filename_inputb + 1 ) :
    filename_result.append( 2**i )
filename_result.pop( 1 )
filename_result.pop( -2 )
print(filename_result)

#2. 리스트 내포