salario = float(input("salario: "))
porcentagem = float(input("aumento(%)"))
aumento = salario * (porcentagem/100)
salario += aumento
print(f"aumento: R$ {aumento:.2f}")
print(f"salario atual: R$ {salario:.2f}")
