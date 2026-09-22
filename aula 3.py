#variables

nome_atendente = input("Nome d@ Atendente:")

produtos = {
    "001": "Xis Salada",
    "Xis Salada": "Xis Salada",
    "002": "Xis Bacon",
    "Xis Bacon": "Xis Bacon",
    "003": "Xis Frango",
    "Xis Frango": "Xis Frango",
}

#main loops

while True:

    produto_input = input("Produto (Código ou Nome): ")
    if produto_input in produtos:
        produto = produtos[produto_input]
        print(f"Produto selecionado: {produto}")
        break #isso aqui serve para encerrar o loop caso o produto seja encontrado
    else:
        print("Produto não encontrado no Banco de dados. Por favor, tente novamente.\n")


while True: #pra impedir q o script seja parado com o erro do usuario
    try:
        valor_unitario = float(input("Valor unitário do produto: "))
        break  
    except ValueError:
        print("O valor unitário do produto é inválido. Por favor insira um valor numérico.\n")

quantidade_input = input("Quantidade: ")

while True: #pra impedir q o script seja parado com o erro do usuario
    try:
        quantidade = int(quantidade_input)
        break  
    except ValueError:
        print("A quantidade é inválida. Por favor insira um valor numérico inteiro.\n")
        quantidade_input = input("Quantidade:")


#functions

def calcular_total(valor_unitario, quantidade):
    return valor_unitario * quantidade

print("\nResumo da Compra:")
print("\n================================")
print(f"Atendente: {nome_atendente}")
print(f"Produto: {produto}")
print(f"Quantidade: {quantidade}")
print(f"Valor Unitário: R$ {valor_unitario:.2f}")
print(f"Total: R$ {calcular_total(valor_unitario, quantidade):.2f}")
print("================================")
