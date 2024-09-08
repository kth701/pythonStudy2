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
