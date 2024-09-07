# 함수(function),메서드(method): 
# 특정 기능을 수행하는 내용을 미리 많들어놓은 프로그램
# 독립된 단위 프로그램

#함수 - 내장함수, 사용자 정의 함수
# 함수 형식
# 1. 매개변수 없고, 반환값이 없는
# 2. 매개변수 있고, 반환값이 없는
# 3. 매개변수 있고, 반환값이 있는

# 함수 선언
def userFunc1():
    print('인수가 없는 함수')
    print('반환값이 없는 함수')


# 함수 호출(실행)
userFunc1()

def userFunc2(x,y): # 매개변수
    print("전달받은 인자값은 {}, {}".format(x,y))
    print("인자 값이 있는 함수")
    print("{}+{}={}".format( x, y, (x+y))  )

userFunc2(10,20) # 인자=>전달하는 값, 데이터,함수
userFunc2(100,200)

def userFunc3(x,y):
    print("인자값 있고, 반환 값")
    return x+y # 반환값은 함수이름에 저장(함수는 변수기능)

# print( userFunc3(1000,20) )

add = userFunc3(10,20)
print(add)

# 반환 값이 여러개 일 경우
def userFunc4(x,y):
    print("여러개의 데이터를 반환하는 함수")
    return (x+y, x-y, x*y, x/y)

add,sub,mul,div = userFunc4(10,20)
print(add, sub, mul, div)

# 가변인자(수) 함수 : 기호(*, **)

# 튜플 가변인자
def fun1(num1, num2, *names):
    print("튜플 가변인자")
    print(num1, num2, names)
    for name in names:
        print(name+"님")
        print("-----")

fun1(100, 200,"홍길동")
fun1(100,"길순이","갑순이","이순신")











