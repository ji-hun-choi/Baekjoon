def factor(n):
    if n == 0: return 1
    else: return n*factor(n-1)
print(factor(int(input())))
