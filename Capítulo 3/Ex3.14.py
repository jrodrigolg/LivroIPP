km = float(input(""))
dias = int(input(""))
preco_dias = dias*60
preco_km = km * 0.15
preco = preco_km + preco_dias
print(f"preço: R$ {preco:.2f}")
