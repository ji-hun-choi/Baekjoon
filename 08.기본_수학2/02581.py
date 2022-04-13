m = int(input())
n = int(input())
res = []
for i in range(m,n+1):
    cnt = 0
    if i == 1 :
        continue
    for j in range(2, i+1):
        if(i % j == 0):
            cnt+=1
    if(cnt == 1):
        res.append(i)
if res == []:
    print(-1)
else :
    print(sum(res))
    print(res[0])