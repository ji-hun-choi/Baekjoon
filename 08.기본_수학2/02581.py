M = int(input())
N = int(input())
res = list()

for i in range(M, N+1):
    cnt = 0
    if i == 1 :
        continue
    for j in range(2, i+1):
        if(i % j == 0):
            cnt+=1
    if(cnt == 1):
        res += 1
print(res)