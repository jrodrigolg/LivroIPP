import os
x = 4
for i in range(8):
    y = str(x)
    pasta = "Capítulo "+y

    os.chdir(pasta)
    arquivot = open("anotacoes.py", "w")
    for j in range(4):
        n = str(x+((j+4)/10))
        arquivo = open("Ex" + n + ".py", "w")
        arquivo.close()
    arquivot.close()
    os.chdir("..")
    x += 1
