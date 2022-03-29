a= input()
numstring = [-1]*26
count = 0
k =[]
for i in range(len(a)):
    if i > 0 :
        if a[i] in k:
            count+=1
        else :
            numstring[int(ord(a[i])-97)] = count
            k.append(a[i])
            count+=1
    else :
        numstring[int(ord(a[i]) - 97)] = count
        k.append(a[i])
        count += 1
for i in range(len(numstring)):
    if len(numstring)-1 == i:
        print(numstring[i])
    else :
        print(numstring[i], end=' ')