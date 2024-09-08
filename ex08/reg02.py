from re import match

# 패턴과 일치
jumin = '123456-3234567'
result = match('[0-9]{6}-[1-4][0-9]{6}', jumin)
# print(result)
# if result:
#     print('주민번호 형식일치')
# else:
#     print('주민번호 패턴 불일치')

# 문자열 치환
from re import sub
str3 = 'test^홍길동 abc 대한*민국 1234$tbc'

# 특수문자 제거
text1 = sub('[\^*$]+', '', str3)
print(str3)
print(text1)

text2 = sub('[0-9]', '', text1)
print(text2)

from re import split, compile

# 텍스트 자료
multi_line="""\
http://www.naver.com
http://www.daum.net
www.google.com\
"""
print("---------------------")
print(multi_line)

# 구분자를 이용하여 문자열 분리
web_site = split("\n", multi_line) # '\n'줄바뀜 기준으로 분리하여 리스트 저장
print(web_site)

#패턴 객체 만들기
pat = compile("http://")

sel_site = [ site for site in web_site if match(pat, site)]
print(sel_site)


