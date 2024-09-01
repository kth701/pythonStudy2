# list 적용되는 기본 함수
nums = [103,52,273,32,77]
print(nums)
print(max(nums), min(nums), sum(nums))

list_a = [1,2,3,4,6]
list_a_reversed = reversed(list_a)

# reversed()함수의 결과 : 제너레이터
# 반복문과 조합할 때는 함수의 결과를 여러번 사용할 수 없음.
print(list_a, list_a_reversed)
for n in list_a_reversed:
    print(n, end=' ')

print()
print( list(list_a_reversed)) # list자료형으로 전환

