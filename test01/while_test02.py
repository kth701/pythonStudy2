import random

# while : 숫자 맞추기 게임
# 컴퓨터가 생각하는 숫자: 1-10
com = random.random() # 0 < com < 1
# print(com, com*10, com*10+1, int(com*10+1))
com = int(com*10+1) # 1-10사이 난수 발생

while True:
    
    print('컴퓨터 숫자:',com)
    
    my = input('예상 숫자를 입력하시오: ')
    my = int(my)        # string -> int

    if my == com:
        print('-- 성공 --')
        break
    elif my > com:
        print('더 작은 수를 생각해보세요.')
    elif my < com:
        print('더 큰 수를 생각해보세요.')

print('-- 게임 종료 --')

