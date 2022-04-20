def movie_title(n):
    i = 0
    cnt = 0
    title = 0
    while True:
        i += 1 # 숫자를 1부터 계속 더해줌
        j = str(i) # 문자형으로 바꾸기
        if j.count("666") >= 1: # j = i 안에 666이 들어가 있으면 True
            title = i
            cnt += 1
        if cnt == n: # cnt가 n이랑 같으면 종료
            break
    print(title)

movie_title(int(input()))