# Mensagem de boas-vindas
print("Bem-vindo Raniff Barroncas Silva")

# Variáveis para o cálculo do valor total
total = 0

while True:
    # Entrada do sabor do sorvete
    sabor = input("Digite o sabor do sorvete (tr/pr/es): ")

    # Verifica se o sabor é válido
    if sabor not in ["tr", "pr", "es"]:
        print("Sabor de Sorvete Inválido.")
        continue

    # Entrada do número de bolas de sorvete
    quantidade = input("Digite a quantidade de bolas de sorvete (1, 2 ou 3): ")

    # Verifica se a quantidade é válida
    if quantidade not in ["1", "2", "3"]:
        print("Quantidade de Bolas de Sorvete Inválida.")
        continue

    # Cálculo do valor do pedido
    if sabor == "tr":
        if quantidade == "1":
            total += 6
        elif quantidade == "2":
            total += 11
        else:
            total += 15
    elif sabor == "pr":
        if quantidade == "1":
            total += 7
        elif quantidade == "2":
            total += 13
        else:
            total += 18
    else:
        if quantidade == "1":
            total += 8
        elif quantidade == "2":
            total += 15
        else:
            total += 21

    # Pergunta se o cliente deseja pedir mais alguma coisa
    mais_pedidos = input("Deseja pedir mais alguma coisa? (S/N): ")

    # Verifica a resposta do cliente
    if mais_pedidos.upper() != "S":
        break

# Apresentação do valor total
print("Valor total do pedido: R${}".format(total))