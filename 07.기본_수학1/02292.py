a = int(input())
count = 0
b = 1
while a > b+count*6 :
    b += count*6
    count+=1
print(count+1)