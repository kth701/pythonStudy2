# for => 일정회수 만큼 반복처리

# import random
# for i in range(5):
#     rnd = random.random()
#     print("rnd:", rnd,"=>", int(rnd*10)+1  )

# range객체 생성
num1 = range(5) # range(start)
print('num1:', num1)

num2 = range(1, 5) # range(start, end)
print('num2:', num2)

for n in num1: # 0 1 2 3 4
    print(n, end=' ')
print() # 줄바꿈
for n in num2: # 1 2 3 4
    print(n, end=' ')
print()
for n in range(1,5):
    print(n, end=' ')
print()
for n in range(5):
    print(n, end=' ')
    
print("-----")
list_a = [1,2,3,"홍길동","홍길순", True, 5>2, 5<3,None]
for data in list_a:
    print(data, end = " ")

print()



