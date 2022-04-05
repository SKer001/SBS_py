#要先引入
from module132 import me

class work(me):
    def __init__(self,where,time,name,age):
        self.where = where
        self.time = time
        self.name = name
        self.age = age
   #def __init__(self,name,age):   就會被引入 但重複的會蓋掉
   #    self.name = name
   #    self.age = age
    def workwhere(self):
        print(self.where)

    def whattime(self):
        print(self.time)

   #def yourname(self):     就會被引入 所以原本的就可以省略
   #    print(self.name)
        
   #def yourage(self):
   #    print(self.age)