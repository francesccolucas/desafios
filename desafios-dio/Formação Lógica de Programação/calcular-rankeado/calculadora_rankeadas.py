# 1️⃣ Função para calcular o saldo e o nível
def calcular_nivel_rankeado(vitorias, derrotas):
    # Cálculo do saldo
    saldo_vitorias = vitorias - derrotas
    nivel = ""

    # 2️⃣ Estrutura de decisão baseada na quantidade de VITÓRIAS
    # Nota: Ajustei as faixas para não deixar "buracos" (como o número 10)
    if vitorias <= 10:
        nivel = "Ferro"
    elif 11 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    else:  # Maior ou igual a 101
        nivel = "Imortal"
    
    return saldo_vitorias, nivel

# 3️⃣ Laço de repetição para testar vários cenários
# Lista de tuplas: (vitorias, derrotas)
partidas = [
    (10, 2),   # Ferro
    (18, 5),   # Bronze
    (45, 10),  # Prata
    (75, 15),  # Ouro
    (85, 5),   # Diamante
    (95, 3),   # Lendário
    (120, 20)  # Imortal
]

print("--- RESULTADO DAS RANKEADAS ---")

for v, d in partidas:
    # Chamando a função e recebendo os dois valores de retorno
    saldo, nivel_alcançado = calcular_nivel_rankeado(v, d)
    
    # 4️⃣ Saída formatada
    print(f"O Herói tem de saldo de **{saldo}** e está no nível de **{nivel_alcançado}**")