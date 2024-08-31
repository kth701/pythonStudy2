# 리스트 => 순서가 있는 자료구조
list_a = [10,20,30,40,40,40]
print(list_a)
print(list_a[0], list_a[1:3])

# 이터레이터 => 저장소에 있는 데이터를 차례대로 가져오는(추출)기능

for data in list_a:
    if data%2 == 0:
        print( data*2)

print("---")

# 리스트 내포
list_b = [ data*2 for data in list_a ] # 최종 반환값 list구조의미
print(list_b)

# 조건 처리
list_c = [ data*2 for data in list_a if data%2 == 0  ]

