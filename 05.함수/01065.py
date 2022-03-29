# 한수인지 여부 구하기
def d(n: int):
    cnt = 0
    s = []
    Q = set()
    k = n

    while k > 0:
        k = k // 10
        cnt += 1
        if k == 0:
            break

    for i in range(cnt):
        s.append(n % 10)
        n = n // 10
        if n == 0:
            break

    if len(s) > 1:
        for i in range(len(s) - 1):
            Q.add(s[i] - s[i + 1])
    else:  #
        Q.add(1)

    if len(Q) == 1:
        return len(Q)


# 한수의 갯수를 구하는 함수
def N(n: int):
    d_cnt = 0

    for i in range(1, n + 1):
        if d(i) == 1:
            d_cnt += 1

    return d_cnt


# 입력값 받기
a = int(input())
print(N(a))