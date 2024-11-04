# idade: int = 35
# altura: float = 1.75
# nome: str = 'André'
# is_estudante: bool = True

# import json

# lista: list = ['Sapato', 39, 10.38, True]

# produto01: dict = {
#     "nome": "Sapato",
#     "quantidade": 39,
#     "preco": 10.38,
#     "disponibilidade": True
# }

# produto02: dict = {
#     "nome": "Televisao",
#     "quantidade": 10,
#     "preco": 70.38,
#     "disponibilidade": False
# }

# carrinho: list = []

# carrinho.append(produto01)
# carrinho.append(produto02)

# print(carrinho)

# carrinho_json = json.dumps(carrinho)
# print(carrinho_json)

# Desafio Tipar Código da aula Passada

nome_valido: bool = False
salario_valido: bool = False
bonus_valido: bool = False

while not nome_valido:
    try:
        nome: str = input("Digite seu nome: ")

        # Verifica se o nome está vazio
        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio.")
        # Verifica se há números no nome
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")
        else:
            print("Nome válido:", nome)
            nome_valido = True
    except ValueError as e:
        print(e)

# Solicita ao usuário que digite o valor do seu salário e converte para float

try:
    salario: float = float(input("Digite o valor do seu salário: "))
    if salario < 0:
        print("Por favor, digite um valor positivo para o salário.")
except ValueError:
    print("Entrada inválida para o salário. Por favor, digite um número.")
    exit()

# Solicita ao usuário que digite o valor do bônus recebido e converte para float
try:
    bonus: float = float(input("Digite o valor do bônus recebido: "))
    if bonus < 0:
        print("Por favor, digite um valor positivo para o bônus.")
except ValueError:
    print("Entrada inválida para o bônus. Por favor, digite um número.")
    exit()

bonus_recebido: float = 1000 + salario * bonus  # Exemplo simples de KPI

# Imprime as informações para o usuário
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")

### Crie dicionário para armazenar informações de um livro
### Incluindo título, autor e ano de publicação. Imprima cada informação.

from typing import Dict, Any

livro_01: Dict[str, Any] = {
    "Titulo": "Harry Potter e a Pedra Filosofal",
    "Autor": "J.K Rolling",
    "Ano": 2000
}

livro_02: Dict[str, Any] = {
    "Titulo": "Harry Potter e a Câmara Secreta",
    "Autor": "J.K Rolling",
    "Ano": 2002
}

lista_de_livros = []

lista_de_livros.append(livro_01)
lista_de_livros.append(livro_02)

print(lista_de_livros)

lista_de_livros_usando_dict: dict = {
    "livro_01": {"Titulo": "Harry Potter e a Pedra Filosofal",
    "Autor": "J.K Rolling",
    "Ano": 2000},

    "livro_02": {"Titulo": "Harry Potter e a Câmara Secreta",
    "Autor": "J.K Rolling",
    "Ano": 2002}
}

print(lista_de_livros_usando_dict['livro_01'])
print(lista_de_livros_usando_dict["livro_01"]['Titulo'])
