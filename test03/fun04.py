# 중첩함수
# 조건1> 외부함수 : bank_account(): 잔액(balance) outer변수
# 조건2> 내부함수: getBalance(): 잔액확인
#                  deposit(money): 입금하기
#                  widthdraw(money) : 출금하기
# 조건3> 출금액이 잔액보다 많은 경우 '잔액이 부족' 메시지 출력
# 조건4> 기타 나머지 출력 

# 출력예시
# 최초 계좌의 잔액을 입력하세요: 1000
# 현재 계좌 잔액은 1000원 입니다.
# 입금액을 입력하세요: 15000
# 15000원 입금후 잔액은 16000원 입니다.
# 출금액을 입력하세요: 3000
# 3000원 출금후 잔액은 13000원 입니다.

# 함수 정의: 기능 설계

# del bank_account(bal):
    # 잔액 초기화
    # balance = bal   
 
    # def getBalance():   # 잔액 확인
    #     pass
    # def deposit(money): # 입금하기
    #     pass
    # def withdraw(money):    # 출금하기
    #     pass

def bank_account(bal):  
    balance = bal               # 잔액 초기화(1000)
    def getBalance():           # 잔액확인(getter)
        return balance
    def deposit(money):         # 입금입력(setter)
        nonlocal balance        # 내부 함수에서 외부함수에 선언된 변수을 사용할 때 적용
        balance += money
    def withdraw(money):        #출금(setter)
        nonlocal balance
        if balance < money:
            print("잔액이 부족")
        else:
            balance -= money

    # bank_account()함수 반환=> 선언된 함수를 모두 반환
    return getBalance, deposit, withdraw # 클로저 함수 리턴

# 함수 호출
getBalance, getDeposit, getWithdraw = bank_account(1000)
print(  "현재 계좌 잔액은 {} 입니다.".format(getBalance())  )

print(  "입금액을 입력하세요: 15000"  )
getDeposit(15000)
print(  "현재 계좌 잔액은 {} 입니다.".format(getBalance())  )

print(  "출금액을 입력하세요: 3000"  )
getWithdraw(3000)
print(  "현재 계좌 잔액은 {} 입니다.".format(getBalance())  )
