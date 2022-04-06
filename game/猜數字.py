import random
IO = int(1)
while IO>0:
    num = random.randrange(0,100)
    cerect = 0
    Front = 0
    Behind = 100
    Stepcount = int(0)
    print("隨機數已經生成好了!")
    while cerect<1:
        yournum = int(input("輸入你的猜測: "))
        if yournum == num:
            print("你猜對了!!!")
            cerect = 1
            Stepcount += 1
        elif yournum > num:
            print("數字大了!")
            Front = str(Front)
            Behind = str(yournum)
            print("現在介於"+str(Behind)+"到"+str(Front)+"之間")
            Stepcount += 1
        elif yournum < num:
            print("數字小了!")
            print("現在介於"+str(Behind)+"到"+str(Front)+"之間")
            Stepcount += 1
        else:
            print("重複了!")
    print("你用了 "+str(Stepcount)+" 步")
    IO = int(input("是否再一次? Y=1,NO=0 : "))