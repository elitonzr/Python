pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for c in pessoas.keys():
    print(c)
for i in pessoas.values():
    print(i)
pessoas['nome'] = 'Leandro'
del pessoas['sexo']
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
