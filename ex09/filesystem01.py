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
print("-- dir")
list_dir =  os.listdir('.')
for filename in list_dir:
    print(filename)




