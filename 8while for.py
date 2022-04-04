#while
N = 1
while N<=100:
    print(N)
    N = N+1 # or N += 1

#for
STR = "我是蔡冠弦"
list = [1,2,3,4,5]

for str in STR:
    print(str)
#for str in "我是蔡冠弦":
#    print(str)
for L in list[1:3]:
    print(L)

#範圍            (n)
for num in range(100):
    print(num)  #0~(n-1)
#範圍(有限制)     (n~(m-1))
for num in range(49,100):
    print(num)

#範例 模仿pow(次方)

N = float(input("選擇基數: "))
M = int(input("選擇指數: "))

#原函式pow
print(round(pow(N,M)))

#模仿函式
def power(n,m):
    N1 = n
    for n1 in range(m-1):
        N1 = N1*n
    return round(N1)
#函式結果
print(power(N,M))