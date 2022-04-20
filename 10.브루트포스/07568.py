num = int(input())
people = []
rank = [1 for i in range(num)] # A~E 까지 기본 1로 표시
for i in range(num):
    a= list(map(int,input().split(' ')))
    people.append(a)

for i in range(0,len(people)-1): # (A~D)
    for j in range(i+1,len(people)): #(B~E)
        if (people[i][0] > people[j][0] and people[i][1] > people[j][1]): # i가 이겼을 경우 j의 패배여서 j의 랭크가 1 올라감
            rank[j] += 1
        elif (people[i][0] < people[j][0] and people[i][1] < people[j][1]): # j가 이겼을 경우 i의 패배여서 i의 랭크가 1 올라감
            rank[i] += 1
print(*rank)