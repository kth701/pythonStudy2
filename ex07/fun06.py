
def deco(f): # f매개변수에는  hi()함수가 전달됨.
    def new_f():
        print("f() is called ")
        return f() # f()은 hi()함수를 으미
    return new_f

@deco
def hi():
    print("hi")

hi()



print("-----")
def fn_01(): #fn_01함수 선언(정의) => 설계도

    print("fn_01 내용") #1.

    def fun_02():   #2.
        print("fun_02 내용")

    return fun_02 #3.


# print(fn_01) # 함수 저장소 주소
# fn_01() # 선언된 함수는  함수 호출했을 때 내용을 동작
# return_fn_02 = fn_01() # fn_01()함수 실행후 반환값(함수식) 저장하기
# return_fn_02() #함수 호출(실행)

