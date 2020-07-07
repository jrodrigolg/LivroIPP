cig_p_dias = int(input("cigarros por dia"))
cig_anos = int(input("anos fumados"))
tempo = cig_anos*365
perda_min = cig_p_dias*tempo*10
perda_dias = perda_min / 1440
print(f"dias mais proximos da morte {perda_dias}")
