# enumerate() 함수 : (index, value) 형식으로 구성
list_a = ["A","B","C"]

print(list_a)
for i in list_a:
    print(i, end=' ')

print()

# enumerate()할수를 적용하여 출력
print("-- enumerate()함수 적용")
print( enumerate(list_a) )
print("-- enumerate()함수 적용한 list자료형으로 변환")
print( list( enumerate(list_a) ) ) 

print("----")
for i, value in enumerate(list_a): # 현재요소의 인덱스, 값을 순차적으로 호출
    print("{}번째 요소는 {}입니다".format(i, value))
