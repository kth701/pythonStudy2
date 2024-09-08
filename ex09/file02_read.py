# read() : 전체 텍스 자료를 한 번에 읽어오기
# readlines(): 줄단위
# readline(): 한 줄 단위

# 파일 읽기 관련 함수
try:
    with open('ex01\\sample01.py', 'r', encoding='UTF-8') as f1:
        # 1.
        # full_text = f1.read()
        # print("----- read() ")
        # print(full_text)
        # print(type(full_text))

        # 2.
        # full_text = f1.readlines()
        # print("----- readlines() ")
        # print(full_text)
        # print(type(full_text))
        # print('문단 수:', len(full_text))

        # 3.
        print("----- readline() ")
        line = f1.readline() # 한 줄만 읽기
        print(line)
        print(type(line))

        


except Exception as e:
    print('Error 발생:',e)

