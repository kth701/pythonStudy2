# dictionary: 사전형 , key(키),value(값) 쌍으로 구성
# 중복 제거, index 없음, key통해 value을 참조(추출)

dict1 = dict(key1=100,key2=200, key3=300)
dict2 = {
    "name"  : "홍길동",
    "age"   : 10,
    "address": "busan"
    }
print(dict1)
print(dict2)

# 키 => 값
print( dict2['name'], dict2['age'], dict2['address'] )
print(dict2.get('name'))
print(type(dict1))

# 수정: 키로 통해 값 수정하기
dict2['name'] = '홍길순'
print(dict2.get('name'))
print(dict2)

# 삭제
del dict2['address']
print(dict2)

# 추가
dict2['head'] = '새로운 정신'
dict2['body'] = '새로운 몸'
print(dict2)

# 반복자로 통해 키, 값, (키,값) 추출하기






