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

    def getBalance(self):
        return self.__balance, self.__accName,self.__accNo

acc = Account(10000, '홍길순', '126-1234-1234')
print(acc.getBalance())