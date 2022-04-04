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

#多維迴圈
F = [[['a','b','c'],['d','e','f'],['g','h','i']],[['j','k','l'],['m','n','o'],['p','q','r']],[['s','t','u'],["v","w","x"],["y","z","end"]]]

for x in F:
    for y in x:
        for z in y:
            print(z)