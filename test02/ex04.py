numbers = {1,2,3,5,6,3,5,5,3,2,54,1,6,1,3,1,2,3,1,3,2}
counters = {}
for number in numbers:
    pass



char = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
    },
    "skill": ["베기","세게 베기", "아주 세게 베기"]
}

for key in char:
    # print(char[key], type(char[key]))

    if type(char[key]) is dict:
        for small_key in char[key]:
            print(char[key][small_key])
    elif type(char[key]) is list:
        print(key)
    else:
        print(char[key])