
count = 0
dataset = [] #1~100사이 3의 배수 저장
while count<100:
    count = count + 1

    if count%5 == 0: #5의 배수
        dataset.append(count)

print(dataset)

# break: 강제로 제어문 탈출, continue: 다음 제어문으로 이동
count2 = 0
while count2 < 10:
    count2 += 1

    if count2 == 5:
        #break
        continue
    print(count2)

print("while 벗어난 후 출력")

# 난수 발생
import random # 모듈 불러오기

cnt = 0
while cnt < 5:
    cnt += 1
    rnd = random.random()
    print("rnd:", rnd,"=>", int(rnd*10)+1  )



