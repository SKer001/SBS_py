#重製
File = open("./file/10file.txt",mode="w",encoding='utf-8')
File.write("1\n2\n3\n4\n5")






#開啟檔案
File = open("./file/10file.txt",mode="r",encoding='utf-8') #r 讀寫 w 覆寫 a 添加
print(File.read())
File.close() #關掉以節省資源

#一個一個讀 會記錄
File = open("./file/10file.txt",mode="r",encoding='utf-8') #r 讀寫 w 覆寫 a 添加
print(File.readline())
print(File.readline())
File.close()

#一次讀完 會計入換行
File = open("./file/10file.txt",mode="r",encoding='utf-8') #r 讀寫 w 覆寫 a 添加
for line in File:
    print(line)
File.close()

#每行資料放list
File = open("./file/10file.txt",mode="r",encoding='utf-8')
print(File.readlines())
File.close()

#改寫
File = open("./file/10file.txt",mode="w",encoding='utf-8')
File.write(input("覆寫: "))
File = open("./file/10file.txt",mode="r",encoding='utf-8')
print(File.read())
File.close()

#重製
File = open("./file/10file.txt",mode="w",encoding='utf-8')
File.write("1\n2\n3\n4\n5")

#增加
File = open("./file/10file.txt",mode="a",encoding='utf-8')
File.write("\n6\n7\n8\n9\n10")
File = open("./file/10file.txt",mode="r",encoding='utf-8')
print(File.read())
File.close()

#節省寫法  開 然後 關                    推薦這寫法
with open("./file/10file.txt",mode="w",encoding='utf-8') as File:
    File.write("1\n2\n3\n4\n5")