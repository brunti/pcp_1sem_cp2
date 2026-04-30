#funcao para verificar se o emprestimo pode ser aprovado
def pode_aprovar(idade, renda, valor):

    if idade >= 18 and valor <= (renda * 20):
        return True

    else:
        return False

#funcao para definir a taxa de juros
def definir_taxa(parcelas):

    if parcelas <= 6:
        return 0.05

    elif parcelas <= 12:
        return 0.08

    else:
        return 0.10

#funcao para calcular o valor da parcela
def calcular_parcela(valor, taxa, parcelas):

    parcela = valor * (
            (taxa * (1 + taxa) ** parcelas)
            /
            ((1 + taxa) ** parcelas - 1)
    )

    return parcela

#funcao para calcular o total pago
def calcular_total(parcela, parcelas):

    total = parcela * parcelas

    return total

#funcao para calcular os juros pagos
def calcular_juros(total, valor):

    juros = total - valor

    return juros

#entrada de dados
nome = input('Digite o nome do cliente: ')

idade = int(input('Digite a idade do cliente: '))

renda = float(input('Digite a renda mensal: R$ '))

valor = float(input('Digite o valor desejado do empréstimo: R$ '))

parcelas = int(input('Digite o número de parcelas (3 até 24): '))

if parcelas < 3 or parcelas > 24:
    print('Número de parcelas inválido.')
    exit()

#verificando aprovacao
aprovado = pode_aprovar(idade, renda, valor)

if aprovado:

    taxa = definir_taxa(parcelas)

    valor_parcela = calcular_parcela(valor, taxa, parcelas)

    total_pago = calcular_total(valor_parcela, parcelas)

    juros_pagos = calcular_juros(total_pago, valor)

    #saida de dados
    print('\n------------- FINANCIAMENTO APROVADO -------------')

    print(f'Cliente: {nome}')

    print(f'Valor financiado: R$ {valor}')

    print(f'Taxa de juros aplicada: {taxa * 100}% ao mês')

    print(f'Valor da parcela: R$ {valor_parcela:.2f}')

    print(f'Valor total pago: R$ {total_pago:.2f}')

    print(f'Total de juros pagos: R$ {juros_pagos:.2f}')

else:

    print('\n------------- FINANCIAMENTO NEGADO -------------')

    print('O cliente não atende aos requisitos mínimos.')