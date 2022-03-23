A,B,C = int(input()),int(input()),int(input())
answ = A*B*C
l1 = list()
for i in str(answ):
    l1.append(int(i))
for i in range(10):
    print(l1.count(i))