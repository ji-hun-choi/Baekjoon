N=int(input())
s=0
row=0
column=0
for x in range(5000):
    s+=x
    if N == 1 :
        row = 1
        column= 1
        break
    elif N<=s:
        if x%2==0:
            row+=x-s+N
            column+=s-N+1
        if x%2!=0:
            row+=s-N+1
            column+=x-s+N
        break
print(f'{row}/{column}')