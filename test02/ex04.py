# list 자료형에 임의 숫자 보관
numbers = [1,2,3,5,6,3,5,5,3,2,54,1,6,1,3,1,2,3,1,3,2]
counters = {} # set, dict 구조

# 숫자 등장 횟수 출력
for number in numbers: # list에있는 데이터를 순차적으로 호출
    print(number, end=' ')

    if number in counters: # 저장소에 data 유무 판별(True/False)
        # data가 있으면 처리
        counters[number] = counters[number] + 1
    else:
        # data가 없으면 처리
        counters[number] = 1
    
print()
print(counters)



char = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
    },
    "skill": ["베기","세게 베기", "아주 세게 베기"]
}

for key in char: # dict자료형에 있는 key를 순차적으로 호출
    # print(key, char[key], type(char[key]))

    if type(char[key]) is dict:
        for small_key in char[key]: # char[key] dict의 key를 순차적으로 호출
            # key2 = char[key]
            # print(key2[small_key])
            print(char[key][small_key])

    elif type(char[key]) is list: 

        for item in char[key]:# list자료형 데이터를 순차적으로 호출
            print(item)

    else:
        print(char[key])