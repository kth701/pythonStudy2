# 상속 => 재사용, 상위클래스(공통기능), 하위클래스(기능확장)

# 부모클래스(상위클래스) : 공통된 기능 구현
class Super:
    # 생성자: 객체 초기화 작업
    def __init__(self, name, age):
        #생성자를 통해 멤버 변수 설정
        self.name = name
        self.age = age
    
    # 멤버(객체) 메서드
    def display1(self):
        print('name: %s, age: %d' %(self.name, self.age))

print("- Super Class로 생성한 객체 ")
sup = Super('부모',55 )
sup.display1()

# 자식클래스(하위클래스): 기능 확장
# 형식=> 클래스(상속받을 부모클래스)
class Sub(Super):
    gender = None

    def __init__(self, name, age, gender):
        # super(): 부모생성자 호출
        super().__init__(name, age)

        # 상속받은 멤버변수(부모클래스)
        # self.name = name
        # self.age = age

        # 자식클래스 멤버변수
        self.gender = gender

    def display2(self):
        print('name: {}, age: {}, gender: {}'.format(self.name, self.age, self.gender))

sub = Sub('자식',25,'여자')
sub.display2()
sub.display1() # 부모클래스에 있는 메서드
    


