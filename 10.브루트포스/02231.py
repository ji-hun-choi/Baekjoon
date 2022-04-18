input = int(input())
nums = [str(i) for i in range(1,input+1)] # input 만큼의 숫자를 받아옴
ok = True # print를 못했을 때 조치.
for num in nums: # 역 순으로 했을때 답이 이상하게 나옴.
    total = 0
    total += int(num)
    for n in num:
        total += int(n)
    if total == input :
        print(int(num))
        ok = False
        break
if ok :
    print(0)