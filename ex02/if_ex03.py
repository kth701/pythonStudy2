# if else

# 100을 키보드입력 => "100"문자열로 전송 => int("100"):숫자100변환
#num = int( input("숫자입력>") )
num = 100
if num >= 0:
    print("양수 or 영")
else:
    print("음수")

if num%2 == 0:
    print(num, "짝수")
else:
    print(num, "홀수")


# 값이 None, 0, 0.0, 빈컨테이이너(빈문자열,...) => False
if "": # 0,0.0, "",...
    print("True")
else:
    print("False")
