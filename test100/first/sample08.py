# 리스트 내장 함수
words = ["orange", "apple", "grape"]
print(words)

# 리스트에 요소 추가 : append()
words.append("banana")
print(words)

words.append([10,20,30])
print(words)

print(words[0])
print(words[1])
print(words[2])
print(words[3])
print(words[4])
print(words[4][0])
print(words[4][1])
print(words[4][2])

# 리스트에 해당 요소위치번호 찾기
print("apple index:", words.index("apple"))
print("orange index:", words.index("orange"))
print("grape index:", words.index("grape"))

nums = [8,5,3,0,1,3]
print( nums.index(3)) # 리스트 전체 범위해서 검색
print( nums.index(3, 0,4)) # 특정범위(0~4사이에서 검색)
print( nums.index(3, 4))

# 리스트에서 요소 제거하기(인덱스번호를 찾아서 제거)
print(nums)

remove_item = nums.pop(1) # 특정 위치의 요소 제거
print( nums, "," , remove_item )

remove_item = nums.pop()
print( nums, "," , remove_item )

# 리스트 요소를 찾아서 제거
remove_item = nums.remove(1)
print( nums, "," , remove_item )



