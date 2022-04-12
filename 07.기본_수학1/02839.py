a = int(input())
FirstN = a%10
if a<= 9:
    if a == 3 or a==6 or a==9: print(int(a/3))
    elif a==8: print(2)
    elif a==5: print(1)
    else: print(-1)
elif FirstN == 1 or FirstN == 6: print(int(((a-6)/5)+2))
elif FirstN == 2 or FirstN == 7: print(int(((a-12)/5)+4))
elif FirstN == 3 or FirstN == 8: print(int(((a-3)/5)+1))
elif FirstN == 4 or FirstN == 9: print(int(((a-9)/5)+3))
elif FirstN == 5 or FirstN == 0: print(int(a/5))
else: print(-1)