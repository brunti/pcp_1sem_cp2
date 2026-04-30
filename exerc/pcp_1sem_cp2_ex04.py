#funcao para calcular horas extras
def calcular_horas_extras(salario_base, horas):
    return  horas * (salario_base * 0.015)

#funcao para calcular o desconto por faltas
def calcular_descontos_faltas(salario_base, faltas):
    return faltas * (salario_base * 0.02)

#funcao para calcular bonus por cargo
def calcular_bonus(cargo, bonus):

    if bonus == 'N':
        return 0

    if cargo == 1:
        return 1000

    elif cargo == 2:
        return 500

    elif cargo == 3:
        return 300

    elif cargo == 4:
        return 100

#entrada de dados
nome = input('Digite o nome do Funcionário: ')

cargo = int(input('Digite o número referente ao Cargo '
                  '(1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário): '))
if cargo < 1 or cargo > 4:
    print("Entrada inválida, por favor, digite apenas o número referente ao cargo.")
    exit()

salario_base = float(input('Digite o Salário base: '))

horas = int(input('Digite a quantidade de horas extras trabalhadas: '))

faltas = int(input('Digite a quantidade de faltas no mês: '))

bonus = input('Digite se o funcionário recebeu bônus por desempenho (S/N): ').upper()
if bonus != 'S' and bonus != 'N':
    print("Entrada inválida, por favor, digite apenas 'S' ou 'N'.")
    exit()

#calculos
valor_horas_extras = calcular_horas_extras(salario_base, horas)

valor_descontos = calcular_descontos_faltas(salario_base, faltas)

valor_bonus = calcular_bonus(cargo, bonus)

total_acrescimos = valor_horas_extras + valor_bonus

salario_bruto = salario_base + total_acrescimos

salario_final = salario_bruto - valor_descontos

#saida de dados
print('\n------------- RESULTADOS -------------')
print(f'Funcionário: {nome}')
print(f'Salário Bruto: R$ {salario_bruto}')
print(f'Total de Acréscimos: R$ {total_acrescimos}')
print(f'Total de Descontos: R$ {valor_descontos}')
print(f'Salário Final: R$ {salario_final:}')