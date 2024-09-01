# 변수의 범위 : scope(스코프)
# 지역변수 : 특정 지역에서만 사용되는 변수 , 함수내에서 선언한 변수
# 전역변수 : 전 지역에 사용된 변수, 함수 밖에서 선언된 변수

x = 100
print(x)

print("-- local func")
def local_func(x):
    # 전역변수와 지역변수 중첩 => 지역변수 우선
    x += 100
    print(x)

local_func(x)
print("-- ")
print(x)

print("-- local func2")
def local_func2():
    # 지역변수 선언된 변수가 없으면 전역변수를 호출
    print(x)

local_func2()

print("-- global func3")
def global_func3():
    global x # 명시적으로 global 전역변수
    print(x)

global_func3()

# 람다 함수 : 기존에 함수식 간결하게 프로그래밍
# lambda 매개변수 : 실행문 내용 => 익명 함수
def Add(x,y):
    add = x+y
    return add
print("일반함수 더하기 기능 : " , Add(10,20))

# 람다 함수 정의
print('람다 함수식:',(lambda x,y : x+y)(100,200))


