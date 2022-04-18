N, M = map(int,input().split(' '))
N1 = N - 7 # 행을 8개씩 몇번을 계산해야될지.
M1 = M - 7 # 열을 계산
counts, W_B, B_W, board = list(), list(), list(), list()
B = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
W = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
answer = 64
# W_B 규칙 8x8 배열 보드 생성
for _ in range(4):
    W_B.append(W)
    W_B.append(B)
    B_W.append(B)
    B_W.append(W)

# 보드 생성
for _ in range(N):
    row = list(input())
    board.append(row)

# test 용
# board1 = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'B', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
# board = [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'W', 'B', 'W', 'B', 'W'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'W', 'B', 'W', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'W', 'B', 'W', 'B', 'W'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'W', 'B', 'W', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'W', 'B', 'W', 'B', 'W'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'W', 'B', 'W', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'W', 'B', 'W', 'B', 'W'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'W', 'B', 'W', 'B'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'B', 'W', 'B'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'B', 'W', 'B']]


for x in range(N1):
    for y in range(M1):
        W_count, B_count = 0, 0
        for i in range(8): # 8x8 체스판 확인
            for j in range(8):
                if board[i+x][j+y] != W_B[i][j]: # W_B 일때 계산
                    W_count +=1
                if board[i+x][j+y] != B_W[i][j]: # B_W 일때 계산
                    B_count +=1
        answer = min(answer, W_count, B_count)
print(answer)