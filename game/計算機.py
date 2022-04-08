

N1 = float(input("第一數: "))
N2 = float(input("第二數: "))
OP = input("運算符號 + - * /: ")
S = 1
while S==1:
    if OP=="+":
        print(N1 + N2)
    elif OP=="-":
        print(N1 - N2)
    elif OP=="*":
        print(N1 * N2)
    elif OP=="/":
        print(N1 / N2)
    
    print("是否結束?(是=0 or 否=1):")
    S = float(input(":"))
    
    if S>0:
        N1 = float(input("第一數: "))
        N2 = float(input("第二數: "))
        OP = input("運算符號 + - * /: ")

print("結束")