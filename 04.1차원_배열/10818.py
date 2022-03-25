a=int(input())
j= input().split(' ')
l = list()
for i in range(a):
    l.append(int(j[i]))
print(min(l),max(l))
