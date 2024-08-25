# 중첩 for

print("== 중첩 for")
for i in range(2,10):
    print("----")
    for j in range(1,10):
        print("{:03d}x{:03d}={:03d}".format(i,j,i*j))

# 키보드로 단을 입력하면 단에 대한 곱출력하기\
# dan = int( input("구하고자 하는 단을 입력하세요>") )
# for i in range(1, 10): # 1,... 9
#     rs = i*dan
#     print("{}x{}={}".format(dan, i, rs))

numbers = [10,20,30,40,50]
cnt = len(numbers)
print("len(numbers)", cnt)

for i in range( len(numbers) ): # len(numbers)=> 5
    print(i) # 0~4
