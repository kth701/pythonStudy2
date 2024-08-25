# break, continue

for i in range(1,10+1):
    if i%6 == 0: 
        break  # 반복문을 강제로 빠져나옴

    if i%3 == 0: # 3의배수 판별
        continue # 다음 제어문으로 이동

    print(i, end=" ")

# 문자열 "+"
str1 = "A"
str2 = "B"

print()
print(str1+str2, "홍길동"+"님")

print(str1)
str1 +="B"
print(str1)

str1 +="C"
print(str1)

# 중첩 for
print()
for i in range(1,3+1):
    for j in range(1,3+1):
        print(i, j) # 9번 반복

print("삼각형 모양만들기")
out_str = ""
for i in range(1,10):

    for j in range(0, i):
        out_str += "*"

    out_str += "\n"

print(out_str)

# 문장과 단어 추출
string ="바나나,수박,사과,딸기,배"
str_result = string.split(",") # 특정문자 기준으로 분리

print(string)
print(str_result, str_result[1],str_result[-1])

string2 = """나는 홍길동입니다.
거주지는 서울시 입니다.
나이는 10세입니다.
전화번호는 010-1234-1234입니다."""
# print(string2)

sents = []  # 문장 저장
words = []  # 단어 저장

# 문단 -> 문장
for sen in string2.split(sep="\n"):
    print(sen)
    sents.append(sen)

    # 문장 -> 단어
    for word in sen.split(): # 공백 기준을 분리
        words.append(word)

print("----")
print('문장:',sents)
print('문장수:', len(sents))
print("----")
print('단어:', words)
print('단어수:', len(words))





