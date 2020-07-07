consumido = float(input("consumido em KWh"))
tipo_inst = input("tipo de instalaçao")
if tipo_inst == "R":
    if consumido <= 500:
        preco = 0.40
    else:
        preco = 0.65
elif tipo_inst == "C":
    if consumido <= 1000:
        preco = 0.55
    else:
        preco = 0.60
elif tipo_inst == "I":
    if consumido <= 5000:
        preco = 0.55
    else:
        preco = 0.60
print(f"valor a pagar: R${preco*consumido}")
