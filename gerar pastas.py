import os
x = 3
for i in range(8):
    y = str(x)
    pasta = "Capítulo "+y
    os.chdir(pasta)
    for j in range(7):
        n = str(j+8)
        arquivo = open("Ex" + y + "." + n + ".py", "w")
        arquivo.close()
    os.chdir("..")
    x += 1
