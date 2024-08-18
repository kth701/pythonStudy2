
# 지방의 그램을 입력하세요: 25
# 탄수화물의 그램을 입력하세요: 520
# 단백질의 그램을 입력하세요: 45
# 총칼로리: 2.485 cal 
# (총칼로리 = 지방*9+단백질*4+탄수화물*4)

fat = int(input('지방의 그램을 입력하세요:'))
carbo = int(input('탄수화물의 그램을 입력하세요:'))
protein = int(input(' 단백질의 그램을 입력하세요:'))

totCalorie = fat*9 + carbo*4 + protein*4

print(fat, carbo, protein)
# "{:전체자리수,d(f:실수,x:16진, o:8진)}".format(데이터
print( "총칼로리: {:10,d} cal".format(totCalorie))

