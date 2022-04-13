lamb = lambda a : int(a)**2
while 1 :
    a, b, c = map(lamb,input().split(' '))
    if a==0 and b==0 and c==0:
        break
    lis = [a,b,c]
    lis.sort()
    if lis[0]==lis[1]==lis[2] : # 정삼각형
        print('right')
    elif lis[0]+lis[1] == lis[2] :
        print('right')
    else :
        print('wrong')