#함수 장식자(decoration) : 
# 기존 함수의 시작부분과 종료 부분에 기능을 장식해서 추가해주는 
# 별도의 함수
# 함수 장식자 : @함수명

# 래퍼함수
def wrap(func): # 매개변수에 hello()함수가 전달
    def decorated():
        print('방가워요!')
        func()
        print('장가요!')

    return decorated # 클로저 함수 반환

# 함수 장식자 적용
@wrap
def hello():
    print('hi~~~~', "동순이")

# 함수 실행
# hello()함수 호출하면 함수 장식자가 호출되면서 hello()함수 실행문 중심으로
# 시작 부분에 '방가워요!', 종료부분에 '잘가요'가 각각 장식으로 추가
hello()
