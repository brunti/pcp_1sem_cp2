#entrada de dados
cp1 = float(input("Digite a nota do Checkpoint 1: "))
cp2 = float(input("Digite a nota do Checkpoint 2: "))
cp3 = float(input("Digite a nota do Checkpoint 3: "))
sp1 = float(input("Digite a nota da Sprint 1: "))
sp2 = float(input("Digite a nota da Sprint 2: "))
gs = float(input("Digite a nota da Global Solution: "))

#encontrando a menor cp
menor_cp = cp1

if cp2 < menor_cp:
    meno_cpr = cp2
if cp3 < menor_cp:
    menor_cp = cp3

#soma dos checkpoints
soma_cp = cp1 + cp2 + cp3 - menor_cp

#média parcial
media_parcial = (soma_cp + sp1 + sp2) / 4

#média do semestre   
media_semestre = (media_parcial * 0.4) + (gs * 0.6)

#média com peso
media_final = media_semestre * 0.4

#saída dos dados
print("\n------ NOTAS ------")
print(f"Média do semestre: {media_semestre:.1f}")
print(f"Média com peso: {media_final:.1f}")