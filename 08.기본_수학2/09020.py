'''
def isPrime(num):
    if num == 1 : return False
    elif num == 2 : return True
    else :
        k = int(num**(0.5))
        for i in range(2, k+1):
            if num % i == 0 : return False
        return True

a_list = list(range(2,6000)) # 범위의 리스트를 미리 생성
p_list = [] # 빈 리스트를 생성
for i in a_list:
    if isPrime(i): # a_list에서 모든 리스트를 조회하며 소수를 찾아 p_list에 생성
        p_list.append(i)

num = int(input())
for _ in range(num): #반복문
    n = int(input())
    k = n // 2
    s_i = 0
    r_i = n
    count = 0
    for i in p_list: # p_list를 조회
        if n == 4:
            s_i = i
            break
        elif (n-i) in p_list:
            if n-i*2 >= 0:
                if r_i > n-2*i:
                    r_i = n-i*2
                    s_i = i
    print(s_i, n-s_i)
'''

# 위에 코드는 처음에 짠 것이다.
# 낮은 수부터 차이를 비교 해서 차이가 제일 적은 것을 저장 후 출력을 했더니
# 시간 초과가 나왔다.
# 생각을 바꿔서 절반부터 아래로 조회를 하는 것으로 변경을 하였다.
def isPrime(num):
    if num == 1 : return False
    elif num == 2 : return True
    else :
        k = int(num**(0.5))
        for i in range(2, k+1):
            if num % i == 0 : return False
        return True

a_list = list(range(2,6000)) # 범위의 리스트를 미리 생성
p_list = [] # 빈 리스트를 생성
for i in a_list:
    if isPrime(i): # a_list에서 모든 리스트를 조회하며 소수를 찾아 p_list에 생성
        p_list.append(i)

num = int(input())
for _ in range(num): #반복문
    n = int(input())
    k = n // 2
    count = 0
    for i in range(k,1,-1):
        if i in p_list and (n-i) in p_list:
            print(i, n-i)
            break