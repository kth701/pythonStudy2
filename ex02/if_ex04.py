# elif문 => else if문

num = -10
if num > 0:
    print("0보다 크다")
elif num == 0:
    print("0과 같다")
else:
    print("0보다 작다")

score = int( input("점수입력>") )
if score >= 85 and score <= 100:
    print("{}점은 우수".format(score))
elif score >= 70: #85보다 작고, 70이상
    print("{}점은 보통".format(score))
elif score >=60: #70보다 작고, 60이상
    print("{}점은 미흡".format(score))
else:   # 60미만
     print("{}점은 매우미흡".format(score))