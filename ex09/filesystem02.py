import os # os모듈 불러오기

# 1.텍스트 디렉터리 경로 지정
print(os.getcwd())
# 절대경로 : d:/pythonStudy2/ex08
txt_data = 'test100' # 상대 경로 지정

# 2. 텍스트 디렉터리 목록 반환
sub_dir = os.listdir(txt_data)
print(sub_dir)


# 3. 각 디렉터리의 텍스트 자료 수집하는 함수 정의
def textPro(sub_dir):
    first_txt   = [] # first 디렉터리 텍스트 저장
    second_txt  = [] # second 디렉터리 텍스트 저장

    for sdir in sub_dir: # ['first', 'second']
        # 디렉터리 구성 => 'test100' + '/first', 'test100' + '/second'
        dirname = txt_data + '/'+sdir # test100/first,test100/second
        file_list = os.listdir(dirname)

        # 파일 구성
        for fname in file_list:
            # 파일: test100/first/파일이름.확장자
            file_path = dirname + '/'+fname 

            # 파일 선택
            if os.path.isfile(file_path):
                try:
                    file = open(file_path, 'r', encoding="utf-8")

                    if sdir == 'first':
                        first_txt.append(file.read())
                    else:
                        second_txt.append(file.read())

                except Exception as e:
                    print('예외발생:', e)
                finally:
                    file.close()

    # 텍스트 자료 반환( 2개 반환)
    return first_txt, second_txt 

# 함수 호출
first_txt, second_txt = textPro(sub_dir) 

# 수집한 텍스트 자료 확인
print('first_txt길이=', len(first_txt))
print('second_txt길이=', len(second_txt))
# 텍스트 자료 결합
tot_texts = first_txt + second_txt

# 전체 텍스트 내용
print(tot_texts)
print(type(tot_texts))




