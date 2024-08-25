# 1-100사이에서 3의 배수이면서 2의배수가 아닌 수를 
# 한 줄에 출력하고, 누적합을 출력하시오.

# <출력결과>
# 수열 = 3 9 15 21 27 .... 93 99
# 누적합 = 867
numbers = []
total = 0
for i in range(1,100+1):
    #if i%2==0 and i%2 != 0:
    if i%3==0:  # 3의 배수 판별
        if i%2 != 0: # 2의 배수 판별
            # 3의배수이고, 2의배수가 아닌 수를 누적
            numbers.append(i)
            total += i 
            
            print(i, end=" ")
print()
print("수열=",numbers)
print("누적합={}".format(total))



