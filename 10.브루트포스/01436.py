def movie_title(n):
    i = 0
    cnt = 0
    title = 0
    while True:
        i += 1
        j = str(i)
        if j.count("666") >= 1: # j = i 안에 666이 들어가 있으면 True
            title = i
            cnt += 1
        if cnt == n: # cnt가 n이랑 같으면 종료
            break
    print(title)

n = int(input())
movie_title(n)