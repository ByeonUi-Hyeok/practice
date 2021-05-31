# 21.05.31
''' 1. '부산'에 해당하는 value 출력
    2. '천안' key가 존재하는지 확인
    3. key 리스트 생성
    4. value 리스트 생성 '''

filename_areacode = {
 '서울':'02', '대전':'042', '부산':'051',
 '광주':'062', '제주':'064'
}

# 1.
print( filename_areacode ['부산'] )                      # 딕셔너리변수['키값'] = value 값 출력
# 2.
print( '천안' in filename_areacode )                     # A in B = B안에 A가 있는지 조회 결과값 (True, False)
filename_chk = filename_areacode.get( '천안' )           # get함수는 key값을 이용해 value값을 조회하는것. 없는 key를 넣으면 None 출력
print( filename_chk )
# 3.
dict_keylist = list( filename_areacode.keys() )          # keys함수는 Dict내의 키값들을 조회할 수 있다. 출력 dict_keys('키값들')
print( dict_keylist )                                    # 결과값이 list가 아니기 때문에 list()함수 안에 넣어 리스트를 만듦.
#4.
dct_valuelist = list( filename_areacode.values() )       # valuue함수는 Dict 내의 밸류값을 조회할 수 있다. 이외에 keys함수와 동일
print( dct_valuelist )