salario = float(input("salario : "))
aumento = 0
if salario > 1250.0:
    aumento = salario*0.1
if salario <= 1250.0:
    aumento = salario*0.15
print(f"aumento: S$ {aumento}\n salario atual : R${salario+aumento}")
