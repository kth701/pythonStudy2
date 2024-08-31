# 최댓값, 최솟갑(max, min)

import random;
dataset = [] # 난수 저장소

for i in range(5):
    rnd = random.randint(1,100)
    dataset.append(rnd)

print(dataset)

# 최댓값, 최솟값 저장소
vmax = vmin = dataset[0]

for i in dataset:
    if vmax < i:
        vmax = i

    if vmin > i:
        vmin = i



print("{}중에서 가장 큰값: {}".format(dataset, vmax))
print("{}중에서 가장 작은값: {}".format(dataset, vmin))