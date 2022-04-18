num = int(input())
people = []
rank = [1 for i in range(num)]
for i in range(num):
    a= list(map(int,input().split(' ')))
    people.append(a)

for i in range(0,len(people)-1):
    for j in range(i+1,len(people)):
        pi, pj = 0, 0
        if (people[i][0] > people[j][0] and people[i][1] > people[j][1]) or (people[i][0] > people[j][0] and people[i][1] > people[j][1]):
            rank[j] += 1
        elif (people[i][0] < people[j][0] and people[i][1] < people[j][1]) or (people[i][0] < people[j][0] and people[i][1] < people[j][1]):
            rank[i] += 1
print(*rank)