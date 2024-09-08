# 텍스트 => CSV, JSON, XML

# CSV : Comma Separated Values
# 홍길동, 90,80,90 

import random

hanguls = list("가나다라마바사아자차카타파하")
print(hanguls)

try:
    with open('ex09\\info.txt', 'w', encoding="UTF-8") as f1:
        for i in range(30):
            name = random.choice(hanguls) + random.choice(hanguls)

            w = random.randrange(40, 100) # 40~99사이 난수
            h = random.randrange(140, 200) # 140~199 사이 난수

            f1.write("{},{},{}\n".format(name, w,h))
except Exception as e:
    print("Error :",e)

print("---- CSV 읽기")
try:
    with open('ex09\\info.txt', 'r', encoding="UTF-8") as f1:
        for line in f1:
            (name, w, h) = line.strip().split(",")
            print("이름:{}, 몸무게:{}, 키:{}\n".format(name, w, h))

         

except Exception as e:
    print("Error :",e)

