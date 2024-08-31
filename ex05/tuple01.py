# tuple : 순서 자료구조, 소괄호=>"()"
# index => 슬라이싱, 연결, 반복, 요소검사 등 가능
# 읽기전용


t1 = (10,)
print(t1)
t2 = (1,2,3,4,4,4,4,5) 
print(t2)
print("----")
print(t2[0],t2[-1], t2[1:4])

# t2[0] = 100 # error 삽입,삭제,수정불가

for i in t2:
    print(i, end=' ')

print("----")
for i in t2:
    if i%3 == 0:
        print(True)
    else:
        print(False)

# 자료 변환
print("---")
print(range(1,6))

# range -> list
list_a = list(range(1,6))
print(list_a)

# list -> tuple
tuple_a = tuple(list_a) + tuple(list_a)
print(tuple_a)


# tuple 함수
print(len(tuple_a), type(tuple_a))
print(tuple_a.count(3)) # tuple있는 요소중 숫자 3의 개수

# tuple에 있는 요소값(데이터) 위치=> 인덱스위치
tuple_b = (10,20,30,40)
print("30이 저장된 위치(인덱스번호): {}".format( tuple_b.index(30)) ) 
