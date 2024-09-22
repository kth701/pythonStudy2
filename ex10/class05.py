# 다형성(Polymorphism): 여러가지 형태를 가질 수 있는 형태
# => 하나의 참조변수로 여러 타입(type)의 객체를 참조 할 수 있는 기능
# 날다(비행기), 날다(새), 날다(종이비행기)

# 부모 클래스
class Flight():
    def fly(self):
        print('날다 : fly 원형 메서드')

# 자식 클래스 : 비행기
class Airplane(Flight):
    # 함수 재정의: 부모와 같은 메서드 선언
    def fly(self):
        print('비행기가 날다')


# 자식 클래스 : 새
class Bird(Flight):
    # 함수 재정의: 부모와 같은 메서드 선언
    def fly(self):
        print('새가 날다')


# 자식 클래스 : 종이비행기
class PaperAirplane(Flight):
    # 함수 재정의: 부모와 같은 메서드 선언
    def fly(self):
        print('종이비행기가 날다')

# 부모 객체 생성 하기
flight = Flight()

# 자식 객체 생성하기
air = Airplane()
bird = Bird()
pager = PaperAirplane()

# 다형성
flight.fly()

# 부모 객체 주소 = 자식 객체 주소
flight = air
flight.fly()

flight = bird
flight.fly()

flight = pager
flight.fly()




