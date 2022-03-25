k = list()
for _ in range(10):
    num = int(input())
    k.append(num%42) # 42 나머지 리스트 k에 저장
k = set(k) # 반복 숫자 제거
print(len(k)) # 저장된 k 출력