# 클래스 : 함수 + 변수
# 사용자가 정의하는 자료형 타입

# 함수정의
# def 함수이름(매개변수):
#     처리할 내용
#     return 반환 값

# 클래스 형식
# class 클래스이름:
#     변수 선언
#     def 생성자(매개변수):
#         pass
#     def 함수이름(매개변수):
#         pass

# 함수
def calc_func(a,b):
    # 함수내에서 선언 변수 지역변수
    x = a
    y = b

    def plus(): #내부함수
        p = x+y
        return p
    def minus():
        m = x-y
        return m
    
    # 함수 반환(함수의 주소반환)
    return plus, minus

# 함수 호출
p, m = calc_func(10,20)
print('plus=', p())  # p() => plus()
print('minus=', m())

# 클래스
class calc_class:
    # 멤버변수
    x = y = 0

    # 생성자=> 특수함수 => 객체 초기화 작업
    # 객체가 생성될 때 자동으로 호출
    # 생성자를 생략(묵시적 생성자가 자동으로 생성됨)
    # def __init__(self):
    #     pass

    def __init__(self, a,b):
        # self=>자기 자신을 지칭하는 키워드
        self.x = a
        self.y = b

    # 멤버메서드(외부로부터 전달 받은 인자가없으면 , self인자만 선언)
    def plus(self):
        p = self.x + self.y
        return p
    def minus(self):
        m = self.x - self.y
        return m
    
# 객체 생성
# list_a = list() # 리스트 자료구조의 타입(클래스)
# list_b = list()
# print(list_a, list_b)

my_calc1 = calc_class(10,20)
my_calc2 = calc_class(100,200)
my_calc3 = calc_class(-10,-20)

print("my_calc1=>", my_calc1.plus(), my_calc1.minus())

