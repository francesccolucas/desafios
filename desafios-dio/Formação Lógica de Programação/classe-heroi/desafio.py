# 1️⃣ Lista de heróis (usando Tuplas dentro de uma Lista)
herois = [
    ("Fox", 950),
    ("Artorias", 2500),
    ("Malenia", 10001),
    ("Link", 7500),
    ("Solaire", 8500)
]

# 2️⃣ Laço de Repetição (mais simples que no JS)
for nome, xp in herois:
    nivel = ""

    # 3️⃣ Estrutura de Decisão (usando o 'elif' e comparação simplificada)
    if xp < 1000:
        nivel = "Ferro"
    elif 1001 <= xp <= 2000:
        nivel = "Bronze"
    elif 2001 <= xp <= 5000:
        nivel = "Prata"
    elif 5001 <= xp <= 7000:
        nivel = "Ouro"
    elif 7001 <= xp <= 8000:
        nivel = "Platina"
    elif 8001 <= xp <= 9000:
        nivel = "Ascendente"
    elif 9001 <= xp <= 10000:
        nivel = "Imortal"
    else:
        nivel = "Radiante"

    # 4️⃣ Saída com f-string (formatação moderna do Python)
    print(f"O Herói de nome **{nome}** está no nível de **{nivel}**")