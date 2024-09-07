# 반환 값이 1개
def calc_area(h,w):
    area = h*w
    border = h*2+w*2
    return area, border

# print( calc_area(5,4))
# print( calc_area(50,4))

# 반환값 2개
def calc_area_border(h,w):
    area = h*w
    border = h*2+w*2
    return area, border

a,b = calc_area_border(5,4)
# print("area={}, border=f{}".format(a,b))

# 반환값 없는 경우 : None 상태
def none_fun(h,w):
    area = h*w

a = none_fun(5,4)
# print(a) # None출력

# none_fun(5,4,3) #error 인자개수 불일치

print("default")
def my_fun(x=10, y=20):
    print(x,y)

# my_fun()
# my_fun(100)
# my_fun(100,200)

print("----")
def lin_eq(a,b,c=0):
    eq = "{}x+{}y+{}=0".format(a,b,c)
    print(eq)
    #print("{}x+{}y+{}=0".format(a,b,c))

# lin_eq(2,3,5)
# lin_eq(2,3)
# lin_eq(c=5,b=3,a=2)


# dict1 = {"name":"홍길동"}
# print(dict1, dict1["name"])
# dict2 = {"ages":[10,20,30,40]}
# print(dict2, dict2["ages"][2])

# 가변인자(딕트) => 키=값,...
def group_by_age(**kwargs):
    print("전달받은 딕트 자료: {}".format(kwargs))
    # 딕트자료형을 선언
    group = {"adult": [], "non-adult":[]}
    for name, age in kwargs.items():
        print(name, age)
        if age>18:
            group["adult"] = group["adult"] + [name]
            #[] = [] + ["kim"], [] = [kim] + ["park"]
        else:
            group["non-adult"] += [name]
    
    return group

# 함수 호출
result = group_by_age(kim=25, jeong=16,park=28,hong=17)
print(result)

