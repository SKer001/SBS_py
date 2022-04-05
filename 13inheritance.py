#繼承  要有相似處
from module131 import work
Name = input("你的名字: ")
Age = input("你的年齡: ")
Where = input("在哪工作: ")
Time = input("啥時工作: ")

ME = work(Name,Age,Where,Time)
#         module132的name與age後來加進來所以就會被排到最前面
ME.workwhere()
ME.whattime()
ME.yourname()
ME.yourage()