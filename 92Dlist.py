#2D list 
D = [
    [0,      1     ,2     ],
    [True,   False],
    ["我好帥"]
]

#指定
print(D[0][2])



#巢式迴圈
for row in D:
    for col in row:
        print(col)