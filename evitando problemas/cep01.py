import requests

integrantes = {
    "Dione": "11633422",
    "Pacheco": "11633010",
    "Cecilia": "04013001"
}

#  exibir nome e cidade
for nome, cep in integrantes.items():
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        cidade = dados.get("localidade", "Cidade não encontrada")
        print(f"{nome} mora em {cidade}.")
    else:
        print(f"Não foi possível localizar os dados de {nome}.")

#salvar informações no arquivo enderecos.txt
with open('enderecos.txt', 'w', encoding='utf-8') as arquivo:
    for nome, cep in integrantes.items():
        url = f"https://viacep.com.br/ws/{cep}/json/"
        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados_cep = resposta.json()
            if 'erro' not in dados_cep:
                logradouro = dados_cep.get('logradouro', 'Sem logradouro')
                bairro = dados_cep.get('bairro', 'Sem bairro')
                cidade = dados_cep.get('localidade', 'Sem cidade')
                uf = dados_cep.get('uf', 'Sem UF')

                arquivo.write(f"{nome}: {logradouro}, {bairro}, {cidade}-{uf}\n")