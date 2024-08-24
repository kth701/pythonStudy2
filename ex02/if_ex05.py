# 삼항 조건문: 단순 조건처리

num = 3
rs = 100

if num>=5:
    rs = num * 2
    print("홍길동")
    print(num)
else:
    rs = num + 2
print(num, rs)

# 삼항 연산자
rs2 = num*2 if num>=5 else num + 2
print(num, rs2)
