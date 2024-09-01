# 리스트 내포(List complerehensions)
# 리스트이름 = [표현식 for 반복자 in 반복할 수 있는 것]
array = [ i*i for i in range(0,20,2)]
print(array)

# 리스트이름 = [표현식 for 반복자 in 반복할 수 있는 것 if 조건문]
array2 = ["사과", "자두","초콜릿","체리","바나나"]
print( array2)

arr_output = [ fruit for fruit in array2 if fruit != "초콜릿"]
print( arr_output ) 

join_result = ",".join(arr_output) # 연결할문자.join(데이터)
print(join_result, type(join_result))