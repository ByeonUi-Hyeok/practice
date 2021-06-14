# 21.06.10
# Regular Expression
# 전화번호 **** 처리

import re
text = '791111-1234567'
regex = '\d{6}-[1-4]{1}\d{6}'
pattern = re.compile(regex)
res = pattern.match(text)
print(res)


text = '123-12-123456'
regex = '[1]{1}\d{2}-[1]{1}\d{1}-\d{6}'
pattern = re.compile(regex)
res = pattern.match(text)
print(res)

text1 = '변의혁'
text2 = 'Byeon Ui-Hyeok'

print(f'안녕하세요 {text1}, 영문이름은 {text2}입니다.' )