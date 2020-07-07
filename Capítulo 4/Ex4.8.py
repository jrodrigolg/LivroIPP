n1 = float(input("n1: "))
n2 = float(input("n1: "))
operacao = input("opreraçao: ")
if operacao == "+":
    resultado = n1+n2
elif operacao == "-":
    resultado = n1-n2
elif operacao == "*":
    resultado = n1*n2
elif operacao == "/":
    resultado = n1/n2
else:
    print("operaçao invalida")
    resultado = 0
print(f"resultado {resultado}")
