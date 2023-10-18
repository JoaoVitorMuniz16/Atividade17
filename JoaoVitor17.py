ano_nascimento = int(input("informe seu ano de nascimento"))

import datetime
ano_atual = datetime.datetime.now().year
idade = ano_nascimento - ano_atual
if idade < 18:
    anos_restantes = 18 - idade
    print(f"você tem {idade} e precisa se alistar daqui a {anos_restantes} anos")
elif idade == 18:
    print("Você tem 18 anos e precisa se alistar")
else:
    anos_passados = idade - 18
    print(f"Você tem {idade} anos e já se passaram {anos_passados} anos do prazo de alistamento.")
