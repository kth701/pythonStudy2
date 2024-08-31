# 반복자로 통해 키, 값, (키,값) 추출하기
dict1 = {
    "name": '7D 건조망고',
    "type":"당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨","치자황색소"],
    "orgin": "필리핀"
}

# print(dict1)
# print(dict1['name'], dict1['ingredient'],dict1['ingredient'][0] )

# for key in dict1:  # (키:값) 쌍으로 저장된 상태

#     # 값의 type이 list구조이면 처리
#     if type(dict1[key]) is list: # type => list, set, tuple 등

#         print("[{}] key".format(key))

#         for list_data in dict1[key]:
#             print(list_data)
#     else:
#         print(key, "=>",dict1[key])

# print("-- keys() : 키만 추출")
# for key in dict1.keys():
#     print(key)
# print("-- values() : 값만 추출")
# for key in dict1.values():
#     print(key)
# print("-- items() : 키와값 추출")
# for key in dict1.items():
#     print(key)

print("--- 키에 해당하는 값이 없을경우 처리")
rs1 = dict1.get('name')
rs2 = dict1.get('address')
rs3 = dict1.get('age','10')
print(rs1)
print(rs2)
print(rs3)
