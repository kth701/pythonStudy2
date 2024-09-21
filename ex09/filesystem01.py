# 파일 시스템
# 프로그램을 이용해서 운영체제에서 지원하는 파일 시스템 사용
# 예) 폴더생성, 폴더이동, 파일이름 변경 등....

import os

# 현재 디렉토리 확인
print( '현재 폴드 위치:',os.getcwd() )

# 폴더 변경
os.chdir('ex09')
print( '변경후 폴드 위치:',os.getcwd() )

# 현제 폴더 목록보기
# "." 현재 폴더(디렉토리), ".." 현재폴더 부모폴더 지칭
print("-- dir")
list_dir =  os.listdir('.')
# print(list_dir)
for filename in list_dir:
    print(filename)

# 디렉토리(폴더) 만들기
# print('test200 폴더생성하기')
# os.mkdir('test200')

# 상위 디렉토리 이동
os.chdir('..')
print( '현재 폴드 위치:',os.getcwd() )

# 2개이상의 폴더 생성시
# os.makedirs('test100/test101')

# 폴더 삭제
# os.removedirs('test100/test101')

# 유무판단
# 현재 경로 유무 판단
# isPath = os.path.exists('test100/test101')
isPath = os.path.exists('ex01')
print(isPath)

# 폴더가 있으면 생성
if not os.path.exists('test100'):
    os.mkdir('test100')

print("- 파일 유무체크")
print(os.path.isfile('hello.py'))

# 폴더(디렉토리)인지 체크
print("---------------")
print( '현재 위치:',os.getcwd() )
list_dir =  os.listdir('.')

for filename in list_dir:
    if os.path.isdir(filename):
        print("폴더:",filename)
    else:
        print("파일:",filename)









