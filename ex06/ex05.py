nums = [1,-3, 5 ,4]
print(nums, sorted(nums))

names = ["banana","grape", "apple"]
print(names, sorted(names))

# 특정 조건 부과하여 정렬
print(nums)
print(sorted(nums))
print(sorted(nums, key=abs )) # 정렬할 데이터에 abs()함수 적용

names2 = ["BANANA","GRAPE", "apple"]
print( names2 )
print( sorted(names2))
print( sorted(names2, key=lambda x: x.lower()))

# all()=> and유사, any() => or유사
num = 30
check_num = [ num%2 == 0, num%3==0, num%5 == 0]
if all(check_num): # 모든 요소가 True -> True 판별
    print("all: and")

if  num%2 == 0 and num%3==0 and num%5 == 0:
    print(True)  

num2 = 12
check_num = [ num2%2 == 0, num2%3==0, num2%5 == 0] # 모든 요소가 False -> False
if any(check_num):
    print("any: or")

