dias = int(input("dias"))
horas = int(input("horas"))
minutos = int(input("miuntos"))
segundos = int(input("segundos"))
horas += dias*24
minutos += horas*60
segundos += minutos*60
print(segundos)
