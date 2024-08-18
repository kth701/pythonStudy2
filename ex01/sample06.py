# string
string = "PYTHON"
print(string)
print(string[0]) # 특정위치(인덱스번호)에 있는 값 추출
print(string[3])
print(string[-1])
print(string[-3])

print("홍길동"+"hongil") # 문자형을 + : 문자연결(병합)
#print("hong"+10) # error 타입
print("abc"*3) # 문자열을 반복처리

# 슬라이싱(slicing) : 범위
# 문자열[시작인덱스번호:끝인덱스번호:증감숫자]
online = "this is one line string"
print("문자열 길이len():", len(online))
print(online)
print("------------------------------")
print(online[0:4]) # 마지막번호-1
print(online[:4])
print(online[4:])
print(online[4:7])
print(online[:]) # 전체
print(online[::2]) #2의 배수 index번호
print(online[-6:-1])
print(online[::-1]) # 역순

# 문자열 처리 함수
online2 = "this is one line string"
# 특정 글자수
print('t글자수:', online2.count('t'))
print(online2.startswith('this'))
print(online2.endswith('that'))
print(online2.replace('this','that')) # 문자열 교체
print(online2.replace(' ','')) # 특정문자열(공백) 삭제
print(online2.replace('t','')) 

temp_str = online2.split(' ') # 문자열 분리 -> List구조로 저장
print(temp_str)
print(temp_str[0],temp_str[2])

names = """\
홍길동
홍길순
동길이
동길이홍\
"""
print(names)
list_names = names.split('\n')
print(list_names)
print(list_names[0])
# 문자열 결합 : 단어 -> 문장
names2 = ','.join(list_names)
print(names2)

print(online2.upper())
print(online2.lower())

# 공백제거
space_str = "     abcde     "
print(len(space_str)  )
print( len(space_str.strip())  ) # 양쪽 공백 제거
print( len(space_str.lstrip())  )
print( len(space_str.rstrip())  )

print("abc1234".isalnum()) # 알파벳 또는 숫자 구성되었는 판별
print("abc_1234".isalnum())
print("23.4".isalnum())
print("23".isdigit()) # 숫자
print("abc".islower(), "ABC".isupper())
# 문자열 검색
print("abcdef".index('f')) # 특정 문자의 위치
print("abcdef".find('c'))
print("abcdef".find('g')) # 특정문자 검색 없을 경우 -1반환

#문자열 내부에 어떤 문자열이 있는지 확인
print("Hello" in "Hello World !!!!")
print("python" in "JAVA TEST")


