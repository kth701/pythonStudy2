# 중첩함수 : 함수내부에 또 다른 함수
# def 함수1():
#      def 함수2():
#           수행할 내용
#      def 함수3():
#           수행할 내용

# 일급함수(First class Function)
#  - 외부함수나 내부함수를 변수에 저장
# 함수클로저(Function cloure): 외부함수가 종료되어도 내부함수에서 선언된 변수 사용가능
#  - 내부함수는 외부함수의 return명령문을 이용하여 반환하는 형태

# 일급함수
def a(): # outer
    # 1. 문자열 출력
    print("a()함수") 
    # 2. b()함수를 정의(선언)
    def b(): # inner
        print("a()함수 안에 있는 b()함수")

    # a()함수를 반환값을 가지고 복귀
    return b

# print("1.-----")
# a()
print("2.----")
b = a() # 외부함수 호출(실행후 반환값은 b()함수를 반환)
b() # b에는 b()함수주소를 반환되어서 b()함수를 수행


print("----")
def test():
    print("함수식을 변수에 저장하기")

# a = 100
# b = a
# b에는 a와 동일한 값

# print(test)
# test() # 함수 실행

# print("--------")
# fun_var = test # A변수 = B함수 주소를 저장=> A변수는 B함수을 의미

# print(fun_var)
# fun_var()

print("--- 함수 클로즈")
data = list(range(1,101)) #숫자 1,100까지 발생 -> 리스트에 저장

def outer_func(data):
    dataSet = data

    # inner function
    def tot():
        tot_val = sum(dataSet) # list에 있는 data 합계
        return tot_val

    def avg():
        avg_val = sum(dataSet)/ len(data) # list에 있는 data 평균
        return avg_val

    return tot, avg # tot()함수와, avg()함수를 반환

main_tot, main_avg = outer_func(data) # 내부함수 tot(), avg()함수 주소 반환

#내부함수 실행
total = main_tot() 
average = main_avg()

# 내부 함수
print( total, average)
