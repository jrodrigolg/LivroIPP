valor_casa = float(input("valor da casa"))
salario = float(input("salario : "))
anos = int(input("tempo de pagamento"))
val_prest = valor_casa/(anos*12)
if val_prest>(salario*0.3):
    print(" emprestimo negado")
else:
    print(f"valor da prestaçao: R$ {val_prest}")
