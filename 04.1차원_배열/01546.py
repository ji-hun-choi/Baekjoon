import sys
lr = sys.stdin.readline

num = int(lr())
k = list()
num2 = lr().split(' ')
for i in num2:
    k.append(int(i))
maxi = max(k)
index = k.index(maxi)
yam=0
while yam<num:
    if k == index:
        yam +=1
        continue
    else:
        k[yam]=k[yam]/maxi*100
        yam+=1
print(sum(k)/num)
