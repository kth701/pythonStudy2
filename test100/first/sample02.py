# 연산자 
# 산술(+,-,*,/,%(나머지),//(몫),**), 관계(>,>=,<,<=,  !=,==)
# 논리(and, or, not), 대입=> =, (a,b), *

print(10+20, 10-20,10*20)
print(10/3, 10%3, 10//3, 10**2)
# 관계연산자 결과 : boolean값 => True, False
print(5>2, 5<2, 5==2, 5!=2)

# and : 모든 bool결과 값이 True일 경우만 True결과 나옴
print(5>2 and 5>3 and 5>4) # True
print(5>2 and 5>3 and 5<4) # False
# or : 모든 bool결과 값이 False 경우만 False결과 나옴
print(5<2 or 5<3 or 5<4)   # False
print(5<2 or 5<3 or 5>4)  # True
print(5>3, not(5>3)) # not 부정, True->False, False->True

#대입 연산자
num1 =  10 # 대입문, 할당문
print("num1=",num1)

num1 += 10 # num1에 10을 더하기
print("num1=",num1)

num1 = num1 + 10 # num1 += 10 와 동일
print("num1=",num1)
num1/=3 # +=, -=, *=,/=, %=, ...
print("num1=",num1)



