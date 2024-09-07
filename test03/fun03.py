# 변수 = 함수
mul = lambda x,y :  x*y
print( mul(2,3))
print( (lambda x,y: x+y)(1,2))

# nums = ['a','b','c']
# rs = "-".join(nums)
# print(rs)

# slash_join = lambda x : "/".join(x)
# print( slash_join(["apple","banana"]))

# 람다함수 
# fillter(함수, 리스트): x->n, 
# map(함수, 리스트) : x -> x

# 일반 함수
def power(item):
    return item*item

def under_3(item):
    return item < 3 # boolean : True, False

list_input_a = [1,2,3,4,5]
print(list_input_a)
# map()
output_a = map(power, list_input_a)
print(output_a, list(output_a))
# for a in output_a:
#     print(a, end=' ')
# print()

# fillter() : 조건에 결과가 True이면 반환
output_b = filter(under_3, list_input_a)
print(output_b, list(output_b))
# for a in output_b:
#     print(a, end=' ')
# print()

# 람다 함수
lambda_a = map(lambda x : x*x, list_input_a)
print(lambda_a, list(lambda_a))

lambda_b = filter(lambda x : x < 3, list_input_a)
print(lambda_b, list(lambda_b))



