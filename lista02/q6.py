ganho_hora = float(input("Ganho por hora: "))
horas = int(input("Horas trabalhadas: "))
salario_bruto = ganho_hora * horas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
print(f"+ Salário bruto: R$ {salario_bruto:.2f}")
print(f"- IR (11%): R$ {ir:.2f}")
print(f"- INSS (8%): R$ {inss:.2f}")
print(f"- Sindicato (5%): {sindicato:.2f}")
salario = salario_bruto - ir - inss - sindicato
print(f"= Salário líquido: R$ {salario:.2f}")
