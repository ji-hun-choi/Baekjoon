li_x = []
li_y = []
result_x, result_y = 0, 0
for i in range(3):
    a, b = map(int, input().split(' '))
    li_x.append(a)
    li_y.append(b)
for x,y in zip(li_x,li_y):
    if li_x.count(x) != 2:
        result_x = x
    if li_y.count(y) != 2:
        result_y = y
    if result_x > 0 and result_y >0 :
        break
print(result_x, result_y)