# gerar as Listas
frutas = ['Maçã', 'pera', 'jabouticaba', 'Manga', 'Uva', 'Kiwi', 'laranja']
alergias = ['Amendoim', 'Laticínios', 'aveia']

# add fruta a lista de alergias
fruta_alergica = 'Kiwi'
alergias.append(fruta_alergica)

print('Listas iniciais:')
print(f"Frutas disponíveis: {frutas}")
print(f"Lista de Alergias Atualizada: {alergias}")
print("-" * 35)

#verifica se ha frutas alergicas 
print(" Verificação de Alergias:")

#vericar a lista de frutas 
for fruta in frutas:
    if fruta in alergias:
         #mensagem de cuidado
        print(f"cuidado! A fruta '{fruta}' está na lista de alergias.")
    
    # print(f"A fruta {fruta} é segura.")
    # print("-" * 35)
print("Verificação concluída.")