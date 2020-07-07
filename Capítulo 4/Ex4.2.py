vel = int(input("velocidade: "))

if vel > 80:
    multa = (vel-80)*5
    print(f"voce foi multado em R${multa:.2f}")
