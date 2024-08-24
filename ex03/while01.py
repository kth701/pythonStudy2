# 조건에 따라 한번도 수행하지 않을 수도 있음 
# while 조건식:
#      참인동안에 처리할 내용
# a = a + 1 :일정한 크기만큼 증감
cnt = tot = 0

while cnt< 10: # 0 1 2 3 4 5 ...
    cnt += 1    # cnt = cnt + 1
    #cnt += 2   # 2 4 6 8 10
    #cnt += 3    #3 6 9 12
    #print(cnt, end="  ")

    # tot = tot + cnt
    tot += cnt  # +=1, +=2, +=3, +=4,....
    print(cnt, "=>",tot)

    



