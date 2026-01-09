# 🎭 Desafio 3: Escrevendo as Classes de um Jogo

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![POO](https://img.shields.io/badge/Paradigma-Orientado_a_Objetos-blue?style=for-the-badge)

## 📝 Descrição
Este desafio foca na aplicação de **Programação Orientada a Objetos (POO)**. O objetivo foi criar uma classe genérica que representasse um herói, contendo propriedades básicas (nome, idade, tipo) e um método de ação (`atacar`) que se comporta de forma diferente dependendo do tipo do personagem.

> "Classes são como moldes, e objetos são as peças criadas a partir desses moldes."

---

## 🎯 Objetivos do Desafio
- **Criação de Classes:** Estruturar o molde do Herói.
- **Métodos e Atributos:** Definir o que o herói *é* (propriedades) e o que ele *faz* (métodos).
- **Lógica de Seleção:** Implementar decisões dentro de métodos para personalizar comportamentos.

---

## ⚔️ Mecânica de Ataque
O ataque é definido dinamicamente:

| Tipo | Ataque |
| :--- | :--- |
| Mago | Magia |
| Guerreiro | Espada |
| Monge | Artes Marciais |
| Ninja | Shuriken |

---

## 🧠 Por que isso é importante? (Visão Game Dev)
Para o desenvolvimento de jogos, este conceito é o "pão com manteiga". Em motores como a **Unity**, cada personagem ou item no cenário é uma **Instância** de uma classe. 

Ao criar uma classe `Heroi`, podemos criar mil heróis diferentes sem precisar reescrever o código de ataque para cada um. Isso garante **escalabilidade** e **organização** no projeto.

---

## 🚀 Como Executar
1. Acesse a pasta do desafio:
   ```bash
   cd 03-escrevendo-classes-jogo