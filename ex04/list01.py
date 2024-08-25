# 자료구조: 프로그램에서 만들어진 객체(data)가 
# 메모리에 배정될 때 기억공간에 적재되는 구조
# - 순서 자료구조, - 비순서 자료구조
# 열거형 객체: 
#    하나의 메모리 영역에 여러 개의 자료가 나열된 집합자료구조
# 순서 자료구조: str, list, tuple등의 클래스

str1 = "abcdefg"
print(str1[0],str1[3], str1[1:4])

# 리스트(list): 여러 개의 자료를 순서대로 적재하는 
#               가변 길이 순차 자료구조를 생성 

list1 = [1,2,3,4]
print(type(list1))

# for i in list1:
#     print(list1[:i]) # list[:1],list[:2],....

# 리스트에 요소 추가: append(), insert()
list_a = [1,2,3]
print(list_a)

list_a.append(4)
list_a.append(5)
print(list_a)

list_a.insert(0,10)   # 리스트객체.insert(인덱스번호, 데이터)
print(list_a)

list_a.insert(3, 100)
print(list_a)

list_b = ["홍길동","홍길순"]
print(list_b)

list_c = list_a + list_b
print("--- (+) 더하기 연산자")
print(list_a)
print(list_c)
print("--- extend()")

list_a.extend(list_b)
print(list_a)

print([10,20]+[30])
# print([10,20]+30) # error type
print([1,2,3]*3)

# 리스트 요소 삭제
print(list_a)




    