#entrada dos dados
codigo_origem = int(input("Digite o código do estado de origem da carga (1 a 5): "))
peso_toneladas = float(input("Digite o peso da carga (em toneladas): "))
codigo_carga = int(input("Digite o código da carga (10 a 40): "))


#conversão para kg
peso_kg = peso_toneladas * 1000

#preço por kg em cada estado
if 10 <= codigo_carga <= 20:
    preco_kg = 100
elif 21 <= codigo_carga <= 30:
    preco_kg = 250
elif 31 <= codigo_carga <= 40:
    preco_kg = 340
else:
    print('Código de carga inválido')
    exit()

#preço total da carga sem impostos
preco_carga = peso_kg * preco_kg

#calculo dos impostos em cada estado

if codigo_origem == 1:
    imposto = preco_carga * 0.35
elif codigo_origem == 2:
    imposto = preco_carga * 0.25
elif codigo_origem == 3:
    imposto = preco_carga * 0.15
elif codigo_origem == 4:
    imposto = preco_carga * 0.05
elif codigo_origem == 5:
    imposto = 0
else:
    print('Código do estado de origem inválido')
    exit()

#calculo do preço total com impostos
preco_total = preco_carga + imposto

#saída dos dados
print("\n------------------------------")
print(f"Peso da carga: {peso_kg}Kg")
print(f"Preço da carga: R$ {preco_carga:.2f}")
print(f"Imposto: R$ {imposto:.2f}")
print(f"Valor total: R$ {preco_total:.2f}")