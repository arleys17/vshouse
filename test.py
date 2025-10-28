# Criar uma tupla com 5 dados
dados = (10, 20, 30, 40, 50)

# Converter a tupla para uma lista
lista_dados = list(dados)

# Inserir 2 dados extras na lista
lista_dados.append(60)
lista_dados.append(70)

# Remover o primeiro dado da lista
lista_dados.pop(0)

# Remover o último dado da lista
lista_dados.pop()

# Imprimir o primeiro dado da lista
print("Primeiro dado da lista:", lista_dados[0])

# Imprimir a quantidade de dados na lista
print("Quantidade de dados na lista:", len(lista_dados))

# Criar um dicionário com Nome, Idade e Profissão
pessoa = {"Nome": "João", "Idade": 30, "Profissão": "Engenheiro"}

# Imprimir o valor contido na chave "Nome" do dicionário
print("Nome:", pessoa["Nome"])
 

 