# 5. Dicionários

Um dicionário é um tipo de dado integrado do python e é usado basicamente para mapear chaves e valores. Esse comportamento é utilizado tanto para manipulação quanto para armazenamento de dados.

Os índices(chaves) podem ser de praticamente qualquer tipo de valor e estão associadas a somente um valor.

Exemplo de uma estrutura dicionário:

```python
imovel = { 'matricula' : 111 , 'quadra' : 10 , 'area_m2': 300 }
```

### Acessando os Dados do Dicionário

Para acessar um determinado valor que compõe o dicionário, podemos fazer:

```python
print(imovel['matricula'])

>>> 111
```

Os dicionários também possuem métodos para o acesso do seu conteúdo:

* `dict.items()` -> retorna uma tupla com o formato(chave , valor)
* `dict.keys()` -> retorna as chaves do dicionário

### Iterando um Dicionário:

A forma mais usual de iterar um dicionário é realizada da seguinte forma:

```python
for key, value in imovel.items():
    print(value, 'é o valor da', key)
    
    
>>> 111 é o valor da matricula
>>> 10 é o valor da quadra
>>> 300 é o valor da area_m2
```

### Alterando o Valor de uma Chave

```python
imovel['matricula'] = 222

print(imovel)

>>> {'matricula': 222, 'quadra': 10, 'area_m2': 300}
```

Também podemos atualizar um dicionário com o método `dict.update()`:


```python
imovel.update({'quadra': 25, 'area_m2': 630, 'proprietario': 'João'})

print(imovel)

>>> {'matricula': 222, 'quadra': 25, 'area_m2': 630, 'proprietario': 'João'}
```

Caso uma chave não exista, ela é então adicionada, como é o caso de `proprietario`.
 

### Excluindo Itens

Para remover uma chave-valor de um dicionário, podemos usar o `del dict[key]`:

```python
del imovel['proprietario']

print(imovel)

>>> {'matricula': 222, 'quadra': 25, 'area_m2': 630}
```