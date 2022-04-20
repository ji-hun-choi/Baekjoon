input = int(input())
nums = [str(i) for i in range(1,input+1)] # input 만큼의 숫자를 받아옴
ok = True # print를 못했을 때 조치. flag 설정
for num in nums: # 역 순으로 했을때 답이 이상하게 나옴.
    total = 0
    total += int(num) # 1~nums를 차례대로 더해줌
    for n in num: # num의 숫자를 분해
        total += int(n) # 한글자 한글자 더해줌
    if total == input : # 답이 입력과 같으면 출력 후 종료
        print(int(num))
        ok = False # 프린트 시 flag 설정
        break
if ok :
    print(0)