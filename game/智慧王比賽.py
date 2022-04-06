from QA import Q
test = [
    "1+9=?\n(A)19\n(B)10\n(C)8\n(D)好難喔",
    "如果我放入更多的檔案，我的筆電會變重嗎？\n(A)Yes\n(B)No",
    "鳥類是不是有兩個生日？\n(A)不，是下蛋的日子才算生日\n(B)不，是孵化的日子才算生日\n(C)對，下蛋&孵化都是",
    "椰子伏特加適合搭配什麼？\n(A)自尊心低落、道德觀念有問題的未成年少女\n(B)花生\n(C)泡麵"
]
QS = [
    Q(test[0],"B"),
    Q(test[1],"B"),
    Q(test[2],"A"),
    Q(test[3],"A")
]

def runtest(QS):
    score = 0
    for q in QS:
        answer = input(q.description+"\n")
        if answer == q.answer:
            score += 25

    print("你得到 "+str(score)+" 分，"+"共"+str(len(QS))+"題")

runtest(QS)