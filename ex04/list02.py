# 리스트 내포(List comprehension): list안에 for와 if를 사용
list_a = [2,4,1,5,7]
list_b = []
for data in list_a:
    if data%2 == 0: # 짝수인 요소만 *2
        list_b.append(data*2)

print(list_a)
print(list_b)

print("-- list안에 for, if 내포")
# 변수 = [실행문 for 변수 in 열거형객체]
list_c =  [2,4,1,5,7]
print(list_c)

resut1 = [ data*2 for data in list_c ]
print(resut1)

print("-----")
result2 = [ data*2 for data in list_c if data%2 == 0]
print(result2)

# 2차원 list
list_of_list1 \
    = [10,20,30, ["홍길동","홍길순","동길이"], True]

print("-- list_of_list")
print(list_of_list1[0])
print(list_of_list1[1])
print(list_of_list1[2])
print(list_of_list1[3])
print(list_of_list1[3][0])
print(list_of_list1[3][1])
print(list_of_list1[3][2])
print(list_of_list1[4])

list_of_list2 = [
                [1,2,3],
                [4,5,6],
                [7,8,9]
            ]
print(list_of_list2,list_of_list2[0][0] )

for items in list_of_list2:
    print(items)    # [1,2,3], [4,5,6],[7,8,9]
    for item in items:
        print(item) # 1,2,3 => 4,5,6 => 7,8,9

# 전개 연산자: 리스트 내용을 전개해서 입력 => "*기호"

a = [1,2,3,4]
b = [*a, *a] # [100,200,300], [ [200,300], [3,3]]
print("a list", a)
print("b list", b)

print("------")
list_temp = [2,4,-1,-5,-7]
# x -> 가공한뒤 -> x결과값
# 절대치 값을 구하는 list
list_temp_rs1 = [ abs(d) for d in list_temp ]

print(list_temp)
print(list_temp_rs1)