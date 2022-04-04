#用法
#  if [變數](==,>,<,>=,<=)(數值,字串,布林值,變數):
#  elif [變數](==,>,<,>=,<=)(數值,字串,布林值,變數):     
#  else:
#
#
#
#數字
G = 10
if G>9:
    print("昏迷")
elif G>-3:
    print("正常")
elif G == 1:
    print("原始")
else:
    print("昏迷")

#字串
day = "rainy"
if day=="rainy":
    print("下雨")
elif day=="clear":
    print("晴天")
elif day=="dark":
    print("陰天")

#布林值
TF1 = False
if TF1:
    print(1)
else:
    print(0)

#and  且
TF1 = True
TF2 = False
if TF1 and TF2:
    print(1)
else:
    print(0)

#or 或
TF1 = True
TF2 = False
if TF1 or TF2:
    print(1)
else:
    print(0)

#not 沒有   (數值是用!=)
TF1 = True
TF2 = False
if TF1 and not(TF2):
    print(1)
else:
    print(0)