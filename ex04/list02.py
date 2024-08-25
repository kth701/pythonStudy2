# 리스트 내포: list안에 for와 if를 사용
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
print(list_of_list1[4])