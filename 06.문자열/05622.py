a=input()
result = 0

for i in a:
    num = ord(i)-65
    if 3>num>=0 :
        result+=3
    elif 6>num>=3:
        result+=4
    elif 9>num>=6:
        result+=5
    elif 12>num>=9:
        result+=6
    elif 15>num>=12:
        result+=7
    elif 19>num>=15:
        result+=8
    elif 22>num>=19:
        result+=9
    else:
        result+=10
print(result)
