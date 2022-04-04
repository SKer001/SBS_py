#分  定義&命名   過程   回傳結果
def ame():
    print("ground pound")
ame()

#函式內變數 函式外不可用 一開始要是字串
def add(num1,num2):
    num1 = int(num1)
    num2 = int(num2)
    return num1 + num2  #return 是回傳結果  可以當參數值or輸出
   #return 回傳結果後 就不會繼續執行
print(add(10,20))


#範例
NUM1 = input("輸入第一數: ") #str
NUM2 = input("輸入第二數: ") #str
print(add(NUM1,NUM2))