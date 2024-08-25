# for : 반복문 => 일정한 횟수만큼 반복 수행
# iterator : 반복을 직접 수행하는 객체, 
# iterable : iterator를 만들 수 있는 객체

n1 = range(5) # 0,1,2,3,4  => (n-1)
print(n1)
for i in n1:
    print(i, end=" ")
print()

n2 = range(2,5) # 2,3,4 
for i in n2:
    print(i, end=" ")
print()

for i in range(1,5,2):
    print(i, end=" ")
print()

# range객체 => list자료형으로 전환
n3 = list( range(1,11,2)  ) # 1,3,... 9
print(n3)
n4 = range(1,10+1)
print( n4, list(n4) ) # 리스트 자료형으로 변환

for i in range(len([10,2,4])): # len=>3 => range(3)
    print("홍길동",i)

# 반대로 반복
list_a = [1,2,3,4,5]
print(list_a, list_a[1], list_a[:], list_a[1:4])
print(list_a[-1], list_a[-2], list_a[::-1])

for i in range(10,1-1,-2):  # 10부터 1까지 -2감소한 숫자생성
    print(i, end =" ")
