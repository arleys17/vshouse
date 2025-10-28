# 📝 Contador de Vogais

def contar_vogais(palavra):
    vogais = "aeiouAEIOU"  # Considera maiúsculas e minúsculas
    contador = 0

    for letra in palavra:
        if letra in vogais:
            contador += 1

    return contador

palavra_usuario = input("Digite uma palavra: ")

total_vogais =contar_vogais(palavra_usuario)
print(f" A palavra '{palavra_usuario}' possui {total_vogais} vogal(is).")