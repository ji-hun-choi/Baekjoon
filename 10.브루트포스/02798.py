num, goal = map(int,input().split(' '))
cards = input().split(' ')
# 정수로 변경
for i in range(len(cards)):
    cards[i] = int(cards[i])

max_num = []
for i in range(0,num-2): # num-2 자리까지
    for j in range(i+1,num-1):# i+1 (앞의 숫자가 겹치지 않기 위해) 부터 num-1 자리까지
        for k in range(j+1,num): # j+1 (앞의 숫가가 겹치지 않기 위해)
            if cards[i]+cards[j]+cards[k] <= goal: # 카드 모두를 더한 값이 goal보다 작거나 같을시
                max_num.append(cards[i]+cards[j]+cards[k])
print(max(max_num))