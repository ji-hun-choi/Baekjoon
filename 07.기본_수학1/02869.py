a, b, c = map(int, input().split())
count = 1
sub = a - b
final = c - a
t = 0

if b < a and a == c: # b가 a보다 크고 a와 c가 같을때
    print(count)
elif final // sub == 0: # 한번에 올라갈 경우?
    count += 1
    print(count)
else:
    t = int(round((final / sub), 0)) # final 에서 올라갔다 내려갔다 횟수
    if (t < (final / sub)): # 만약 t보다 크면 증가.
        t += 1
    count += t
    print(count)

