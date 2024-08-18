# 숫자 관련 내장 함수

print(abs(10), abs(-10), abs(10.3), abs(-10.3))
print( round(3.124), round(3.564))
print( round(41.5559,1), round(41.5559,2), round(41.559,-1))

# 변수 :단일 기억장소, 리스트: 복수 기억장소
num1 = 10
num1 = 20
print(num1)

list1 = [10,20,30,40]
print(list1)
# sum(): list의 합을 구해주는 함수
print(sum(list1, 100))
print(sum([1,2,3,4,5]))
print(max([1,2,3,4]))
print(min([1,2,3,4]))

print(max(["apple","cpple2","cpple1"]))
print(min(["apple","bpple","cpple"]))

numbers = [10,20,-30,-100,1,2,3]
print( sorted(numbers)  ) # 오름차순(작->큰)
print( sorted(numbers, reverse=True) ) # 내림차순(큰->작)
# 정렬기준을 다르게 할 겨우
print( sorted(numbers, key=abs) ) # 오름차순