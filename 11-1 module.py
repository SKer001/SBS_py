#引入其他檔案   就可以使用該檔案的變數,函式
#其他很多個預設模組 現在我用的python版本是3.9.10
import module

#可以找預設模組   as S 可以把sys名改成S
import sys as S

#第三方模組
# pip 套件管理工具
#在終端機打 "pip install 模組名"  大多都是這樣裝  Ex: pip install numpy

NAME = str(input("輸入你的名字: "))
    #(模組名.函式名)
print(module.good(NAME))

print(S.path)