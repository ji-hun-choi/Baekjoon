def printMat(mat, N):
    for r in range(0, N):
        for c in range(0, N):
            print(mat[N * r + c], end = '')
        if N-1 > r:
            print()

def MakeStar(mat, step, N, beg, end):
    if 3 == N:
        mat[(beg + end) // 2] = ' '
        return
    else:
        nextN = N // 3
        for r in range(0, 3):
            for c in range(0, 3):
                b = beg + (r * step * nextN) + c * nextN
                e = beg + step * ((r + 1) * nextN - 1) + (c + 1) * nextN - 1
                if 1 == r and 1 == c:
                    for i in range(b, e + 1, step):
                        for j in range(0, nextN):
                            mat[i + j] = ' '
                    continue
                MakeStar(mat, step, nextN, b, e)

N = int(input())
mat = ['*' for i in range(0, N*N)]
MakeStar(mat, N, N, 0, N*N-1)
printMat(mat, N)