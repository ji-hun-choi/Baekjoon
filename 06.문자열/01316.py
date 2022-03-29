num = int(input())
result = num
for _ in range(num):
    st1 = [0]*26
    a = input()
    for i in range(len(a)):
        if i == 0 :
            st1[ord(a[i])-97] +=1
        else :
            if a[i] != a[i-1]:
                if st1[ord(a[i])-97] > 0 :
                    num-=1
                    break
                else :
                    st1[ord(a[i])-97] +=1
print(num)