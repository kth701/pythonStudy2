# 외부 패키지 설치
import pandas as pd
import os 

print(os.getcwd())

# csv 파일 읽기
score = pd.read_csv("ex10/data/score.csv")
print(score.info) # 파일 정보
print(score.head) # 칼럼명 포함
