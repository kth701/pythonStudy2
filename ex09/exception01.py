# 예외처리 : 예기치 않은 에러가 발생했을 때 정상적으로 종료
# try:
#     예외발생 코드
# except 예외처리 클래스 as 변수
#     예외처리코드
# finally:
#     항상 실행하는 코드

print("-- start")

x = [10,20,25.2,'num', 14,51]
for i in x:
    try:
        print(i)
        y = i**2
        print('y=',y)
    except:
        print('데이터 타입 문제가 발새하였음', i)

print("-- end")


# 중첩 예외 처리
print("---------------")
print("\n유형별 예외처리")
try:
    div = 100 / 2.53
    print('div=%5.2f' %(div)) # 정상 처리

    #div = 1000 / 0              # 1차에러
    #f = open('c:\\text.txt')    # 2차에러
    num = int(input('숫자 입력:'))  #3차 기타에러

except ZeroDivisionError as e: # 산술적인 예외 처리
    print('오류 정보:',e)
except FileNotFoundError as e: # 파일 예외 처리
    print('오류 정보:',e)
except Exception as e: # 모든 예외 처리
    print('오류 정보:',e)        
finally:
    print('항상 실행하는 영역')

print("정상 종료")