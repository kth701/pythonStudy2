# 함수(메서드) : 특정 기능을 수행하는 미리 만들어 놓은 프로그램
# ex) random => random(), randint(),...
# 제조사에서 프로그램 설치시 제공하는 함수  -> 내장함수 -> import 호출하여 사용
# 내장함수와 사용자 정의함수

# 내장함수 -> 호출 사용
# import 모듈명 => import된 모듈에 있는 모든 함수 사용가능
# from 모듈명 import 함수명, .... 

# builtins모듈 -> 별도의 import없이 바로 사용 할 수 있는 내장함수
# len(), sum(),....

# import builtins # 묵시적으로 자동 import됨

list_a = [1,2,3]
print(  len(list_a) )

# import명령어로 이용하여 외부 모듀을 포함 시캐 사용 할 수 있는 함수
import random
num = random.randint(1,10)


# import builtins
# print( dir(builtins)  ) # builtins모듈에 있는 함수 목록

# 절대값 반환
print(  abs(10), abs(-10))
# 모든 요소가 True이면 True, 그렇지 않으면 False
print( all([1, True, 10, -15.2]))
# 하나라도 True이면 True, 그렇지 않으면 False
print( any([False,False,True, False]))
# 문자열 수식을 계산할 수 있는 수식변환
print( "10+20", eval("10+20")  )
# 정수: 10진형, 8진형, 16진형
print( 10, hex(10), oct(10)) # 10진수 -> 16진수,8진수
# 아스키 코드값 \
print( ord('A'), ord('B'), ord('a'),ord('b')  )
# 제곱 계산
print( pow(10,2), pow(2,3), pow(10,-1), pow(10,-2))
# 반올림
print( round(3.141592, 3))