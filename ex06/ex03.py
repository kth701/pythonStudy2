# 딕셔너리의 items(), keys(), values()
dict_a = { 
    "키A":"값A",
    "키B":"값B",
    "키C":"값C",
    }
print("-- keys()")
print(dict_a.keys())

for k in dict_a.keys():
    print(k, dict_a[k]) # 객체[키] =>값이 추출

print()


print("-- values()")
print(dict_a.values())

print("-- items()")
print(dict_a.items())

for key, element in dict_a.items(): # dict자료형의 데이터를 키와 값 순차적으로 호출
    print("dict[{}] = {}".format(key, element))
