n1 = int(input("n1: "))
n2 = int(input("n2: "))
n3 = int(input("n3: "))
maior = n1
menor = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print(f"M:{maior}\n m:{menor}")
