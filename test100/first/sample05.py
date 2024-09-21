# 형식있는 출력 => 1,000 12.34  => .format()
print("원주율=", 3.141592)

# 숫자형식 : %d(정수), %f(실수) %o(8진형), %x(16진형),
# 문자형식: %s(문자열), %c(단일문자)
print("원주율=", format(3.141592, "8.3f"))
print("금액=", format(10000, "10d"))
print("금액=", format(100, "10d"))
print("금액=", format(1, "10d"))
print("금액=", format(100000, "3,d"))

name1 = "동순이"
age1 = 14
price1 = 125.456
print("이름: %s, 나이: %d세, data=%.2f" %(name1, age1, price1))

#외부상수 출력: print("{형식}".format(값))
print("==== '{}'.format() ===")

print("숫자1={}, 숫자2={}, 숫자3={}".format(10,20,30.5))
print("숫자형식: [{:5d}]".format(52))
print("숫자형식: [{:05d}]".format(52))
print("숫자1={2}, 숫자2={0}, 숫자3={1}".format(10,20,30.5))

a = 10
b = 20
print("{}+{}={}".format(a,b,(a+b)))

name2 = "김길동"
age2 = 11

str1 = f"당신의 이름은 {name2}, 나이는 {age2}세 입니다."
print(str1)

print("------------")


# 함수(메서드): 특정기능을 수행하는 단위 프로그램
# print()
# value 인수
age = 10
name = "홍길동"
score = 89.456

print(age)
print("나이:",age, "이름:",name, "점수:",score)
print("010","1234","1234", sep="\n")
print("동길이", "동순이","김길동",end=",")

print(100/3) 




