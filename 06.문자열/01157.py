a = input().lower()

result = [0]*26

for i in a:
    result[97-ord(i)]+=1

if result.count(max(result)) > 1 :
    print('?')
else :
    print(chr(result.index(max(result))))