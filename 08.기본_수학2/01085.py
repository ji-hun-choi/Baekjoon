x, y, w, h = map(int,input().split(' '))
lis1 = [x, y, w-x, h-y]
print(min(lis1))

# (0, 0) 즉 x축과 y축으로 탈출이 제일 짧은 길이인 x, y를 넣고
# 도형 겉 경계선인 w와 h로 탈출하는 길이
# w-x, h-y 에서 최소값.