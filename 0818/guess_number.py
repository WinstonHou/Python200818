import random
num=random. randint(1,20)
i=0
while i<5:
    ans=int(input("請輸入數字:"))
    if ans==num:
        print("恭喜答對")
        print(i+1)
        break
    else:
        print("錯了")
        i=i+1
    if num<ans:
        print("太大")
    elif num>ans:
        print("太小")
    if i>4:
        print("失敗")
    
        