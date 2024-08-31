# 비순서 자료구조 : 인덱스가 없음 : set, dict
# set : 중복제거
set_names = {10,10,10,10,10,20,20,20,20}
print(set_names)
# print(set_names[0]) # error

s1 = {1,2,3,4,5}
s2 = {4,5,6,7}

# u1 = s1.union(s2)
u1 = s1 | s2
u2 = s1 & s2 # 교집합
u3 = s1 - s2 # 차집합
print(u1)
print(u2)
print(u3)

