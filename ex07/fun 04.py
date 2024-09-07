#재귀함수(recursion function)

# 재귀함수 => 끝내기 조건을 반드시 기술
# 4! = 4*3*2*1
def factorial(n):
    print(n)
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    # 3*f(2) -> 2*f(1) -> 1*f(0)
    
print("result:", factorial(3) )
