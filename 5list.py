#可以兩種以上變數在一起
L = ['rex',12,False]
print(L)    #結果 ['rex', 12, False]

#單選1個 由0開始
L = [0,2,4,6,8,10]
print(L[0])    #不會有[]

#選範圍 [n,m]  n=開始值  m-1=最後一個 由0開始
print(L[0:5])  #結果是[0, 2, 4, 6, 8]
#字串是用字數 符號跟空格都算
#n or m 不填就是從頭或到尾
print(L[:5])
print(L[5:])  #結果是[10]

#改變
#L[0] = int(input("這是改第一個值: "))
L[0] = 10 
print(L[0])


L = [0,2,4,6,8,10]
R = [20,30,40,50,60,70]

#接多個list
L.extend(R)
print(L)

#重製 重設變數
L = [0,2,4,6,8,10]
R = [20,30,40,50,60,70]


#新增 往後加
R.append(80)
print(R)

R = [20,30,40,50,60,70]

#插入 (n,m) 第n前不動 第n改m 剩下往後動
R.insert(1,25)
print(R)

R = [20,30,40,50,60,70]

#刪除 特定物件 不是位置
R.remove(70)
print(R)

#清除
R.clear() #變[]

R = [20,30,40,50,60,70]

#移除最後一位
R.pop()
print(R)

R = [20,30,40,50,60,70]

#排列 小到大
R.sort()
print(R)

R = [20,30,40,50,60,70]

#反轉
R.reverse()
print(R)

R = [20,30,40,50,60,70]

#