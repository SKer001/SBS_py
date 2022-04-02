from cmath import phase
from operator import truediv
from math import *

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


################################       STR

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

#替換   W -> w  優先最先的   只改輸出值  不改變數值
print(text.replace("W", "w"))



################################    number

#可以負數 小數點
print(-87.5)

#可以直接運算 有先乘除
print(1+1*8)

# / 有小數   // 取整數
print(10/3)
print(10//3)

#絕對值
N = -10
N = abs(N)
print(N)

#次方  (N,M) N=基數  M=指數
N = 2
N = pow(N,N)
print(N)

#回傳最大值
print(max(2,3,10,100))

#回傳最小值
print(max(2,3,10,100))

#四捨五入  取個位
print(round(1.53))

        #math的引入

#無條件捨去 取個位
print(floor(8.6))

#無條件進位 取個位
print(ceil(8.6))

#開根號
print(sqrt(4))