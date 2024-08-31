# set 객체: 비순서 자료구조, "{}" 기호로 표현
# 추가,삭제, 집합 연산 등 가능, index 사용 할 수 없다.
# set 데이터 보관시 고유식별자 용도

s1 = {1,3,4,3,2}
print(s1)
print(len(s1))

for i in s1:
    print(i, end=' ') # 수평 출력

print()

# 집합 연산 : 합집합, 교집합, 차집합
print("-- set 집합연산")
s2 = {3,6}
print(s1,s2)
print(s1.union(s2)) #합집합
print(s1.difference(s2)) #차집합친
print(s1.intersection(s2)) #교집합

s2.add(7)
s2.add(8)
print(s2)

s2.discard(100) # 삭제할 요소값, 데이터가 없어도 에러발생 안됨
# s2.remove(100) # 데이터가 없으면 에러
print(s2)

print("----")

# 중복이 허용된 데이터 수집
list_a = ["홍길동","동순이","동길이","홍길동","동순이"]

# 중복 제거
set_name = set(list_a) # list -> set
list_b = list(set_name) # set -> list

print(list_a)
print(list_b)
