num = int(input())

for i in range(num):
    H,W,N = map(int,input().split())
    floor = N % H
    line = (N // H)
    if floor == 0 : # 꼭대기
        if line-1 >= 9 : # 호수 -1 후 검사.
            print('{}{}'.format(H,line))
        else :
            print('{}0{}'.format(H,line))
    else :
        if line >= 9 :
            print('{}{}'.format(floor,line+1))
        else :
            print('{}0{}'.format(floor,line+1))