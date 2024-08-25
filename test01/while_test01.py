# while : 반복횟수가 일정하지 않을 경우
cnt=0
total=0
# 합계값이 30을 초과하는 최초의 수 구하기
while total <= 30:     # 참인동안에 반복 수행
    cnt+=1          # 1,2,3,...
    total += cnt    # +1,+2,+3...
    print(cnt, total)

print("합계가 30초과한 최초의 수는:", cnt)
