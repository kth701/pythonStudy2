# 제어문(if문, while, for, ....)
# Boolean자료형 : True, False 

# 관계(비교)연산자 결과 : 'bool' type
# >, >=, <, <=, !=, ==
print(5>2, 5<3, type(5==3) ) 

num = 25
print( 10 < num < 30)
# and, or , not 
# => 2개이상 조건의 결과값으로 판별

addr = "부산"
age = 31
gender = '여'

# and : 조건의 결과가 모두가 True => True결과값을 갖는 형태
# 이고, 이면서, 중에서
print("---- and(&&) ")
print( addr=='부산' and age==31 and gender=='여')
print( addr=='부산' and age==31 and gender=='남')
# or : 조건의 결과가 모두가 False => False결과값을 갖는 형태
# 이거나, 또는
print("---- or(||)")
print( addr=='부산' or age==35 or gender=='남')
print( addr=='서울' or age==35 or gender=='남')
print("---- not => !")
# not(5>2) => 5<=3
print(5>2, not(5>2))

