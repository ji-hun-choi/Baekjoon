N, M = map(int,input().split(' '))
N1 = N - 7 # 행을 8개씩 몇번을 계산해야될지.
M1 = M - 7 # 열을 계산
counts, W_B, B_W, board = list(), list(), list(), list()
B = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'] # B 부터 시작하는 리스트 생성
W = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'] # W 부터 시작하는 리스트 생성
answer = 64
# W_B 과 B_W 규칙 8x8 배열 보드 생성
for _ in range(4):
    W_B.append(W)
    W_B.append(B)
    B_W.append(B)
    B_W.append(W)

# 문제 보드 받기
for _ in range(N):
    row = list(input())
    board.append(row)

for x in range(N1):
    for y in range(M1):
        W_count, B_count = 0, 0
        for i in range(8): # 8x8 체스판 확인
            for j in range(8):
                if board[i+x][j+y] != W_B[i][j]: # W_B 일때 계산
                    W_count +=1
                if board[i+x][j+y] != B_W[i][j]: # B_W 일때 계산
                    B_count +=1
        answer = min(answer, W_count, B_count) # for 문을 반복하며 제일 적은 답
print(answer)