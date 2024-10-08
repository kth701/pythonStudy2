# 자연어 전처리 예

from re import findall , sub

# 텍스트
texts = [
    '우리나라 대한민국', 
    '우리나라%$ 만세',
    '비아그&라 500GRAM 정려 최고',
    '나는 대한민국 사람', 
    '보험료 15000원에 평생 보장 마감 임박',
    '나는 홍길동'
]

# # 1. 소문자 변경
# texts_re1 = [ t.lower()  for t in texts] # 리스트 구조로 저장
# print('texts_rel:', texts_re1)

# # 2. 숫자 제거
# texts_re2 =[ sub("[0-9]", '', text) for text in texts_re1]
# print("--------------")
# print('text_re2:', texts_re2)

# # 3. 문장부호 제거
# texts_re3 = [ sub('[,.?!:;]','', text) for text in texts_re2]
# print("--------------")
# print('texts_re3:', texts_re3) 

# # 4. 특수문자 제거
# texts_re4 = [ sub('[@#$%^&*()]','', text) for text in texts_re3]
# print("--------------")
# print('texts_re4:', texts_re4) 

# # 5. 영문자 제거
# texts_re5 = [ ''.join( findall("[^a-z]",text)  ) for text in texts_re4]
# print("--------------")
# print('texts_re5:', texts_re5) 

# # 6. 공백 제거
# texts_re6 = [ ' '.join(text.split())   for text in texts_re5]
# print("--------------")
# print('texts_re6:', texts_re6) 

print("--- 전처리 함수 정의하기")
# 1. 텍스트 전처리 함수 선언
def crean_text(text):
    # 1-6단계
    text_rs = text.lower()
    text_rs2 = sub("[0-9]", '', text_rs)
    text_rs3 = sub('[,.?!:;]','', text_rs2)
    text_rs4 = sub('[@#$%^&*()]','', text_rs3)
    #text_rs5 = sub('[^a-z]','',text_rs4) # 영문자를 제외한 모든 문자 삭제
    text_rs5 = sub('[a-z]','',text_rs4)
    text_rs6 = ' '.join(text_rs5.split()) 

    return text_rs6
    
# 2. 함수 호출
# clean_text("문자열")
texts_result = [ crean_text(text)  for text in texts]

# 3. 최종 결과
print(texts_result)


