# 캡슐화, 상속(자원의 재사용)

class Account:

    # 은닉 멤버변수
    # '__'기호 => private
    __balance = 0       # 잔액 
    __accName = None    # 예금주
    __accNo = None      # 계좌번호

    # 생성자
    def __init__(self, bal, name, no) :
        self.__balance = bal
        self.__accName = name
        self.__accNo = no


    # 멤버변수 값 출력: 계좌 정보 확인
    def getBalance(self):
        return self.__balance, self.__accName,self.__accNo
    
    # getter: 객체안에 있는 변수 값을 읽어오기 기능
    def test1(self):
        print("getter:", self.__balance)
        return self.__balance
    
    # setter: 
    def test2(self, data):
        self.__balance = data
        print("setter:", self.__balance)

acc = Account(10000, '홍길순', '126-1234-1234')
print(acc.getBalance())


# print(acc.__balance) # private 설정 => 접근 불가능
# getter를 통해 접근
# acc.getterTest()

print("- 외부에서 객체변수값 접근 불가능")
acc.__balance = 20 # private 설정된 변수값은 변경불가능
print(acc.getBalance())

print("- setter, getter")
acc.test2(20)
acc.test1()
print(acc.getBalance())

