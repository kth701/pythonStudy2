num = 300
print(num)
list_a = [10,20,[1,2,[100,200]]]
print(list_a)
list_a[1] = 300
print(list_a[0], list_a[1], list_a[2])
list_a[2][1] = 1000
print(list_a[2][1])

list_b = [1,2,3,4,5]
print(  3 in list_b    )
print(  10 in list_b    )

dict_a = { "name": "홍길동"}
print( dict_a)

print( 10 in dict_a)
dict_a['10'] = 1000
print( dict_a)

print( "name" in dict_a) 
print( dict_a["name"])


