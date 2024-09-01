# 사용자 정의 함수 : 
# 선언 : def 함수이름(매개변수,...) => 함수이름 구분자역할, 저장소역할
# 호출 : 함수이름(인자,...)

# 어떤 기능을 수행 할 내용을 작성
def my_fun01():
    for i in range(3):
        print("hello")
    print("인자없고, 반환값 없는 함수 형식")

#함수호출(실행)
my_fun01() 

x = 100
# 기능을 수행할 전달할 값이 있는 함수 선언
def my_fun02(x,y):
    print("전달받은 데이터는 {},{}입니다.".format(x,y))
    print( x+y)

my_fun02(10,20)
my_fun02(10.2,20.9)
my_fun02(1,2)

# 기능을 수행할 때 전달값 있고, 반환값이 있는 함수
def my_fun03(x,y):
    add = x+y
    return add  # 반환값

rs1 = my_fun03(100,200)
print("{}+{}={}".format(100,200, rs1))

print( my_fun03(1.5,200.4))

# 가변인자 매개변수 : *매개변수, **매개변수
# *매개변수=> tuple 자료형, **매개변수 => dict자료형
# 가변인자가 있는 함수 작성, 가변인자는 맨마지막에 작성

# tuple가변인자 함수
def my_fun04(x,*value): # 가변인자매개변수 타입 => tuple
    print(x, value)

    add = sum(value)+x
    return add

rs1 = my_fun04(10,1,2,3,4,5)
rs2 = my_fun04(10,1,2)
print(rs1, rs2)

# 반환값이 여러개인 함수 형식
def my_fun05(x,y):
    return (x+y), (x-y), (x*y), (x/y)

r1,r2,r3,r4 = my_fun05(5,3)
print(r1,r2,r3,r4)

# default 인자가 있는 함수
def my_fun06(x=100,y=200):
    return (x+y)

print( my_fun06(10,20), my_fun06())

# dict가변인자 함수
def my_fun07(name, age, **other):
    print(name)
    print(age)
    print(other)
    for key in other:
        print(other[key])

my_fun07('홍길동',15, address='busan', height=175, weight=75)


