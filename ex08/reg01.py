# 정규식 표현
import re   # 모듈 추가 - 전체 추가
from re import findall # 모듈 추가 - 특정 이름만 추가

# 문자열 찾기
str1 = '1234 abc홍길동 ABC_555_6 PythonStudy 이시도시'

# 숫자 찾기
print( findall('1234',str1)) # '1234' 검색
print( findall('[0-9]', str1)) # 0~9사이 숫자 1개
print( findall('[0-9]{3}', str1)) # 숫자구성 3자리
print( findall('[0-9]{3,}', str1)) # 숫자구성 3자리이상
print( findall('\\d{3,}', str1))

# 문자열 찾기
print(  re.findall('[가-힣]{3,}', str1)  ) #한글 3자이상
print(  re.findall('[a-z]{3}', str1)  )
print(  re.findall('[a-zA-Z]{3,}', str1)  )

# 특정 위치의 문자열 찾기
str2 = 'test1abcABC 123mbc 45test'
print( findall('^test',str2) )
print( findall('st$',str2) )

print( findall('.bc',str2) ) # 임의의 한 문자가 x앞 뒤에 오는 패턴
print( findall('t.',str2) )

str3 = 'test^홍길동 abc 대한*민국 1234$tbc'
words = findall('\\w{3,}', str3) # [0-9a-zA-Z_]
print(words)



