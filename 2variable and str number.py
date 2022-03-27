from cmath import phase
from operator import truediv

#變數 = variable

#數字變數
number = 11
#布林值變數
bool = True
#字串變數
Str = "早安你好"

print(number)
print(bool)
print(Str)

#   \" 在字串 = "
Str = "HI \" nice" 
print(Str)

# \n = 換行
Str = "HI \n nice" 


#多個字串
print("HelloWorld " + "python!")

text = "HelloWorld"
#全小寫                      #!!lower and upper只改輸出值  不改變數值
print(text.lower())
#是否全小寫 回傳True or false
print(text.islower())
#全大寫
print(text.upper())
#是否全大寫 回傳True or false
print(text.isupper())

#可以連續
print(text.lower().islower())
print(text.upper().isupper())


#只輸出第[n]個數  輸出str  0 first
 #         HelloWorld
print(text[0])


#引索  優先最先的 還傳數值
print(text.index("W"))

#替換   W > w  優先最先的   只改輸出值  不改變數值
print(text.replace("W", "w"))

