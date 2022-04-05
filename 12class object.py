#class 名字:
#    def __init__(self,變數1,變數2):
#        self.變數1 = 變數1
#        self.變數2 = 變數2


#class相當於一個自定義的變數
class aboutme:
    def __init__(self,name,age,where):
        self.N = name
        self.A = age
        self.W = where

Name = input("你的名字: ")
Age = input("你的年齡: ")
Where = input("你哪裡人: ")
#myself包含aboutme的三種變數
myself = aboutme(Name,Age,Where)
#                self.N,self.A,self.W依次輸入

print("我是 "+myself.N +"\n"+"我 "+myself.A +" 歲"+"\n"+"我來自 "+myself.W)
with open("./file/12 namecard.txt",mode="w",encoding='utf-8') as File:
    File.write("我是 "+myself.N +"\n"+"我 "+myself.A +" 歲"+"\n"+"我來自 "+myself.W)
