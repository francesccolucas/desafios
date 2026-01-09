# 1️⃣ Definição da Classe
class Heroi:
    def __init__(self, nome, idade, tipo):
        # Atributos (Propriedades)
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    # 2️⃣ Método Atacar
    def atacar(self):
        # Lógica para definir o tipo de ataque baseado no tipo do herói
        if self.tipo.lower() == "mago":
            ataque = "magia"
        elif self.tipo.lower() == "guerreiro":
            ataque = "espada"
        elif self.tipo.lower() == "monge":
            ataque = "artes marciais"
        elif self.tipo.lower() == "ninja":
            ataque = "shuriken"
        else:
            ataque = "um ataque desconhecido"

        # Exibição da mensagem final
        print(f"O {self.tipo} atacou usando {ataque}")

# 3️⃣ Criando Objetos (Instâncias) e testando
# Aqui simulamos a criação de heróis de diferentes tipos
herois_na_aventura = [
    Heroi("Fox", 32, "Guerreiro"),
    Heroi("Gandalf", 2000, "Mago"),
    Heroi("Lee", 25, "Monge"),
    Heroi("Hanzo", 30, "Ninja")
]

print("--- REGISTRO DE COMBATE ---")
for heroi in herois_na_aventura:
    heroi.atacar()