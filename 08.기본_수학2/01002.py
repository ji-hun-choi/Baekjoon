import math
num = int(input())
for _ in range(num):
    x1, y1, r1, x2, y2, r2 =map(int,input().split(' '))
    x1_x2_distance = math.sqrt(math.pow((x1-x2),2) + math.pow((y1-y2),2))
    if r1 == r2 and x1_x2_distance ==0: # 원이 서로 겹쳐있고 거리도 같을때
        print(-1)
    elif abs(r1-r2) < x1_x2_distance < r1+r2  : # 두 원이 두점에서 만날때
        print(2)
    elif abs(r1-r2)==x1_x2_distance or r1+r2 == x1_x2_distance: #원 내접 or 밖에서 만날때
        print(1)
    else :
        print(0)