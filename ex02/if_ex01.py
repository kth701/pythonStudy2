# 산술연사자 => 계산 결과값 => 1+2 => 3
# 관계연산자(논리연산자) => True, False

# 제어문 : 프로그램의 흐름을 변경
# if, for , while,.....

# if 조건식(불린값):
# (들여쓰기) 처리할 문장
num = 1
if num>2: # True    
    print('조건이참인 경우1 처리하는내용')
    num+=10 # 6-> 16

print(num)

# 리스트 자료형=>여러개의 자료를 저장할 수 있는 저장소
if sum([1,2,3])>10:
    print([1,2,3])

print("out of if")

if True:
    print("True입니다.")

if False:
    print("False입니다.")

num2 = 2 # 짝수의 특징 =>2의 배수 => 2나누어 나머지가 0
if num2 % 2 == 0:
    print("짝수")

if num2 % 2 != 0:
    print("홀수")
