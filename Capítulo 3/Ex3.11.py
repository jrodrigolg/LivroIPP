preco = float(input("digite o preço do produto: "))
porc_desconto = float(input("porcentagem de desconto: "))
desconto = preco * (porc_desconto/100)
preco -= desconto
print(f"desconto: R$ {desconto:.2f}")
print(f"preco: R$ {preco:.2f}")
