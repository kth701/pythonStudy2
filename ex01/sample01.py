# 변수와 상수
# 변수: 기억장소
# 상수: 기억장소에 넣을 값(데이터)
# 할당문, 대문입
# 변수=데이터, 변수=수식, 변수=변수
a = 10
b = 20
c = 100+200
d = c

print(a)
print(b)
print(c)
print(d)

print("----")
# 동시 대입
x,y = 100, "python"
print(x,y)

# 소문자 구성 : 변수
animal_name = "gildong"
# animal() # 함수(메서드)이름
# AnimalName #클래스이름

# 자료형(데이터타입)
var1 = "Hello Python"
var2 = 100
var3 = 10.24
var4 = True # False

print(var1, type(var1))
print(var2, type(var2))
print(var3, type(var3))
print(var4, type(var4))
print("5>2",5>2, type(5>2))

# 키워드 알아보기
import keyword #외부 모듈 가져오기

# 변수 = 객체.속성
python_keyword = keyword.kwlist

print("-- keyword --")
print(python_keyword)



# 자료형 변환
# 실수 -> 정수 : int(실수값)
print("---")
print(int(10.5), type(10.5), type(int(10.5)))
# 정수 -> 실수 : float(정수값)
print(float(10), type(10), type(float(10)))
# 논리형 -> 정수
print(5>2,  int(5>2), int(False))
# 문자형 -> 숫자
print("12"+"23", int("12")+int("23"))




