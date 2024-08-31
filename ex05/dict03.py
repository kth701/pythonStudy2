# 단어 빈도수 구하기

# 리스트 구조 => 원시데이터 보관
charset = ['abc','code','band','abc', '홍길동','동순이','홍길동']
# 비어 있는 dictionary 구조
word_count = {}

for key in charset:
    # key => 'abc','code','band','abc', '홍길동','동순이','홍길동'
    # word_count[key] 유무 체크
    # ex => word_count['abc']
    # 없으면 word_count[key]생성하여 0으로 초기화 한 후 + 1 
    # 있으면 word_count[key]에 1을 추가
    
    word_count[key] = word_count.get(key,0) + 1

print(word_count)

print("---- 비어 있는 dict")
dict_test = {}
print(dict_test)

# dict_test['abc'] = 1000  # dict에 키와 값을 추가
# print(dict_test)

# key에 대한 값이 없으면 초기값 설정
# dict_test['count'] = 0
dict_test['count'] = dict_test.get('count', 1000)
print( dict_test)

# key가 있으면 불어와서 1추가 
dict_test['count'] = dict_test.get('count', 1000) + 100
print(dict_test)

print("--- is type")
print( type("홍길동"), type("홍길동") is str, type(100) is str)
print( type([]) is list, type([]) is tuple) 
print( type({}) is dict)

print("--- object copy")
# 모듈 호출
import copy

name = ["홍길동"] # object대상 
copy_name = name # 주소 복사(내용, 주소 동일)
print(name, copy_name)
print(id(name), id(copy_name))

copy_name2 = copy.deepcopy(name) # 내용복사(내용동일, 주소다름)
print(name, copy_name2)
print(id(name))
print(id(copy_name2))



