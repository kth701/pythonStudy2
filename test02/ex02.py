# 저장시=> key:value 쌍

p1 = {"apple":10, "grap":100}
print(p1)
p2 = dict(apple=10, grap=100)
print(p2)

print( p1['apple'], p1.get('apple'))

for data in p1:
    print(p1[data])

print(p1.keys())
print(p1.values())

for k in p1.keys():
    print(k)

for v in p1.values():
    print(v)   

list_keys = list(   p1.keys()   )
list_values = list(  p1.values()   )
print(list_keys, list_values)
print(list_keys[0], list_values[0])

for i in p1.items():
    print(i)   

list_items = list(  p1.items()   )
print(list_items)