# 변수 : 단일 기억장소
# 리스트 : 여러자료를 저장하는 기억장소
num = 100
num = 200
print(num)

nums = [10,20,30,"홍길동", 5>2, True]
print(nums)

print(nums[0], nums[1], nums[-1], nums[-2])
print(nums[:]) # 전체
print(nums[:3]) # 인덱스번호 3번 이전까지 추출
print(nums[3:])
print(nums[1:4])

list_a = [1,2,3]
list_b = [4,5,6]
list_c = list_a + list_b

print(list_c)
print(len(list_a), len(list_b), len(list_c))
