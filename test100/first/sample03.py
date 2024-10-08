# 인덱싱:문자1개, 슬라이싱 : 문자, 문자열(문자집합)
print("--- indexing -----")

print("0123456789")
print("0123456789"[0])
print("0123456789"[1])
print("0123456789"[5])
print("0123456789"[-1]) # 오른쪽에서 첫번째문자
print("0123456789"[-2])
# print("0123456789"[100]) # index out of range
print("--- slicing -----")
print("0123456789"[:])
print("0123456789"[0:3]) # 시작번호:마지막번호-1
print("0123456789"[5:]) # 시작번호:생략 (마지막번호)
print("0123456789"[::2])
print("0123456789"[3:8:2])
print("0123456789"[::-1])
print("-----------")
str1 = "0123456789"
print(str1[4])
print(str1[:4])
print("-----------")


# 이스케이프 문자: 문자에 특정기능을 부여
print("홍길동'안녕")
print('홍길\'순안녕')
print("김\t길\t동")
print("Hello\n\n\n\nPython!!!")
print("Hello \\ c: \\") # "\"문자 자체를 출력
print("문자열 선언방법: 따옴표로 글자 데이터를 감싸서 문자열을 표현합니다.")
print("문자열 선언방법: \n따옴표로 글자 데이터를\n 감싸서 문자열을 \n표현합니다.")
print("""\
홍길동
동순이
길순이
김길동\
""")
