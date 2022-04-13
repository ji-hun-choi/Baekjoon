# while True:
#     n = int(input())
#     cnt = 0
#     if n == 0:
#         break
#     for i in range(n, n*2+1):
#         cnt_e = 0
#         for j in range(2, i+1):
#             if i % j == 0 : cnt_e += 1
#             if cnt_e > 2 :
#                 break
#         if cnt_e == 1:
#             cnt += 1
#     print(cnt)

# 시간초과.
# 2중 for문으로 계속 소수를 구해서 그런듯.
# 전에 만들었던 함수를 참고
import math
def isPrime(num): # 소수인지 구별해주는 함수
    if num == 1 : return False
    elif num == 2 : return True
    else :
        k = int(math.sqrt(num))
        for i in range(2, k+1):
            if num % i == 0 : return False
        return True

a_list = list(range(2,123456*2)) # 범위의 리스트를 미리 생성
p_list = [] # 빈 리스트를 생성
for i in a_list:
    if isPrime(i): # a_list에서 모든 리스트를 조회하며 소수를 찾아 p_list에 생성
        p_list.append(i)

while True: # 무한 반복문
    n = int(input())
    if n == 0 : # 조건 0 일경우 스탑
        break
    count = 0
    for i in p_list: # p_list를 조회
        if n < i <= n*2: # 범위 안에 p_list(소수) 값이 있는지
            count+=1
    print(count)