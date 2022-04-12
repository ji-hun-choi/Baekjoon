a,b,c = map(int,input().split())
total = 0
tex = c-b

if tex <= 0 :
    print(-1)
else :
    total = int((a+tex)/tex)
    print(total)