
# 이미만들어 놓은 프로그램 불러오기
import datetime

now = datetime.datetime.now()

print(now.year)
print(now.month)
print(now.day)

print(now.hour)
print(now.minute)
print(now.second)

print("형식에 맞추어서 날짜와 시간 출력")
print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month, 
    now.day, 
    now.hour, 
    now.minute, 
    now.second))

print("특정 월에 대한 조건 처리")
if 3<= now.month <= 5:
    print("이번 달은 {}월로 봄입니다".format(now.month))

if 6<= now.month <= 8:
    print("이번 달은 {}월로 여름입니다.".format(now.month))

if 9<= now.month <= 11:
    print("이번 달은 {}월로 가을 입니다.".format(now.month))

if now.month == 12 or 1<= now.month <= 2:
    print("이번 달은 {}월로 겨울입니다.".format(now.month))

# 중첩if문
id = "hong"
pw = "1234"

if id=="hong":
    if pw=="1234":
        print("아이디와 패스워드 모두 일치")
