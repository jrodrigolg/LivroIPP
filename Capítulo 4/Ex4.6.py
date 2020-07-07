distancia=int(input("distancia : "))
if distancia <= 200:
    preco = distancia*0.5
else:
    preco = distancia*0.45
print(f"preço: R${preco:.2f}")
