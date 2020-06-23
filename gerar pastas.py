import os
x = 3
for i in range(9):
    y = str(x)
    pasta = "Capítulo "+y
    os.mkdir(pasta)
    os.chdir(pasta)
    for j in range(4):
        n = str(x+((j+1)/10))
        arquivo = open("Ex" + n + ".py", "w")
        arquivo.close()
    os.chdir("..")
    x += 1
