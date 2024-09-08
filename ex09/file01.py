# 테스트 파일
# open(path+filename, mode, encoding)
# mode => r,w, a, x, b,..

# 파일 열기
# file1 = open('basic.txt', 'w')
# # 파일 처리
# file1.write("Hello Python Programming..")
# # 파일 닫기
# file1.close()

with open("basic.txt","w", encoding="UTF-8") as file1:
    file1.write("파일 쓰기 연습!!!")
    
# 파일 읽기
with open("basic.txt", "r", encoding="UTF-8") as file2:
    contents = file2.read()

print(contents)

# 파일관련 모듈
import os
print("현재 폴더 위치:",os.getcwd() )
# "ex09\basic2.txt"
with open("ex09\\basic2.txt","w", encoding="UTF-8") as file1:
    file1.write("파일 쓰기2 연습!!!")

with open("ex09\\basic2.txt","r", encoding="UTF-8") as file2:
    contents2 = file2.read()

print(contents2)



    