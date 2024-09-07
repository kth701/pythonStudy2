
def deco(f): # f매개변수에는  hi()함수가 전달됨.
    def new_f():
        print("f() is called ")
        return f() # f()은 hi()함수를 으미
    return new_f

@deco
def hi():
    print("hi")

hi()