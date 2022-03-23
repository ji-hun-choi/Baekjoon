k = list()
for _ in range(9):
    k.append(int(input()))
maxi = max(k)
print(maxi, k.index(maxi)+1)