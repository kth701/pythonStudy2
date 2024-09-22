# 클래스 선언
class DatePro:
    # 멤버변수
    content = "날짜 처리 클래스"
    # 생성자
    def __init__(self, year, month, day):
        # 생성자로 통해 멤버변수 선언 및 값을 할당
        self.year = year
        self.month = month
        self.day = day

    # 멤버 메서드
    def display(self):
        print("%d-%d-%d" %(self.year, self.month, self.day))
    
    # 클래스 메서드(기본인자 'cls' 를 포함)
    # 함수장식자
    @classmethod
    def date_string(cls, dateStr): # '19991011'
        year = dateStr[:4]
        month = dateStr[4:6]
        day = dateStr[6:]

        print(f"{year}년{month}월{day}일")
        print("{}년 {}월 {}일".format(year, month, day))

# 객체 생성하기
# 기본자료형, 숫자(정수,실수), 문자열, 부울린값 => 변수
# 클래스로 선언된 변수 => 객체(인스턴스)
date  = DatePro(1995,10,25)
date2 = DatePro(1995,10,21)
date3 = DatePro(1995,10,22)

print("-- DatePro클래스로 생성된 date객체")
print(date.content)

# 멤버 변수 값을 변경
date.content ="홍길동만세"
print(date.content)

print(date.year, date.month, date.day)

# 멤버메서드 반드시 객체를 생성하여 메서드(함수)를 호출
date.display()  # 다형성=> 하나의 메시지 -> 다른 기능수행
date2.display()
date3.display()

# DatePro.display()
# 클래스메서드는 객체 생성 없이 함수(메서드) 호출 
# 클래스이름으로 함수(메서드) 호출 가능
DatePro.date_string('19991011')




