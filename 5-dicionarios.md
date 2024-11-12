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


### Exemplo de uso:

Crie um programa que possibilite armazenar em um dicionário, os nomes dos alunoes e as notas de 3 disciplinas. Calcule a média das notas e exiba um relatório, com o nome de cada aluno, suas respectivas notas e a média.

```python

alunos = {}

for i in range(1, 4):
    nome = input(f"Digite o nome do Aluno {i}: ")
    fisica = float(input(f"Digite a nota de Física para {nome}: "))
    matematica = float(input(f"Digite a nota de Matemática para {nome}: "))
    quimica = float(input(f"Digite a nota de Química para {nome}: "))
    
    # Armazenando as notas no dicionário
    alunos[nome] = {
        "Física": fisica,
        "Matemática": matematica,
        "Química": quimica
    }

# Exibindo as notas de cada aluno e a média
for aluno, notas in alunos.items():
    print(f"\n{aluno}:")
    for disciplina, nota in notas.items():
        print(f"  {disciplina}: {nota}")
    
    # Calculando a média das notas do aluno
    media = sum(notas.values()) / len(notas)
    print(f"  Média: {media:.2f}")
```

Exercícios:

1. Crie um dicionário para armazenar as notas de um único aluno em três disciplinas: física, matemática e química. Em seguida, peça ao usuário que insira as notas de cada disciplina e armazene-as no dicionário. Imprima o dicionário completo ao final.

**Resposta Esperada:** Um dicionário com as três disciplinas como chaves e as notas inseridas pelo usuário como valores.


2. Com o dicionário de notas criado no Exercício 1, verifique se uma nota está presente no dicionário (por exemplo, se existe uma nota para a disciplina “Biologia”). Se a nota não existir, exiba uma mensagem indicando que a disciplina não foi encontrada.

**Dica:** Use o operador `in` para verificar se a chave está presente no dicionário.


3. Expanda o programa anterior para calcular a média das notas. Crie uma função chamada calcula_media(notas) que receba o dicionário de notas como parâmetro e retorne a média. Em seguida, imprima a média na tela chamando a função.

**Resposta Esperada:** A média das notas, calculada por meio da função.


4. Modifique o dicionário de notas de forma que, para cada disciplina, o valor seja uma lista de notas (três notas por disciplina). Em seguida, escreva um código para calcular a média de cada disciplina e exiba essas médias.

```python

notas = {
    "Física": [7.5, 8.0, 6.5],
    "Matemática": [9.0, 8.5, 7.0],
    "Química": [6.0, 7.5, 8.0]
}
```

5. Expanda o programa para armazenar dados de três alunos, onde cada aluno tem suas notas em três disciplinas (física, matemática e química). Imprima o nome de cada aluno, suas notas e a média das notas para cada aluno, como fizemos no exercício resolvido anteriormente.

**Dica:** Use um dicionário aninhado onde as chaves principais são os nomes dos alunos, e os valores são outros dicionários que contêm as notas por disciplina.

**Resposta Esperada:** A média para cada disciplina.

6. Usando o dicionário criado no Exercício 5, encontre o aluno com a maior média e o aluno com a menor média. Imprima o nome do aluno e a média correspondente.

**Dica:** Calcule a média de cada aluno e armazene essas médias em outro dicionário ou lista, de forma que você possa facilmente identificar as médias máxima e mínima.



