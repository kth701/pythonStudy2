# 1. 처리조건
# 수량변수: su = 5
# 단가변수: dan = 800
# 금액계산 = 수량x단가

# 입력
su = int(input("수량:")) #키보드 문자열 => 형변환(int)
dan = int(input("단가:"))

#계산
result = dan*su

#출력
# print(su, dan, result)
print("수량: {}개 \n단가: {}원 \n금액: {}원".format(su,dan,result))
# id(변수) => 변수 주소값
print(su, id(su))


