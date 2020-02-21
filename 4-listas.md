# 4. Listas e Tuplas

Uma lista é representada como uma sequência de objetos separados por vírgula e dentro de colchetes [], assim, uma lista vazia, por exemplo, pode ser representada por colchetes sem nenhum conteúdo.

Listas são similares a strings, que são uma sequência de caracteres, no entanto, diferentemente de strings, os itens de uma lista podem ser de tipos diferentes.

```python
numbers = [1, 2, 3, 4, 5]

vazia = []

got_houses = ['Lannister', 'Stark', 'Targaryen']

compras = ["tomate", "alface", "macarrão", "carne"]

lista_mista = ["olá", 2.0, 5*2, [10, 20], {"hello": "World"}]
```

Cada valor na lista é identificado por um *índice*. O valores que formam uma lista são chamados elementos ou itens.  Contamos o índice da lista a partir do zero:

```
+-----------+-------+-----------+-------------+
|"Lannister"|"Stark"|"Targaryen"|lança um erro|
+-----------+-------+-----------+-------------+
      0         1         2            3         
```

```python
got_houses[1]

>>> 'Stark'

got_houses[3]
-----------------------------------------------------------------------
IndexError Traceback (most recent call last)
<ipython-input-5-d7761c43e340> in <module>
----> 1 got_houses[3]

IndexError: list index out of range
```

### Comprimento de uma Lista

É obtida com a função `len()`:

```python
print(len(lista_mista))

>>> 5
```

### Percorrendo os Elementos de uma Lista

```python
lst = [1, 6, 7, 12, 5, 0]

for elem in lst:
   print(elem)
   
>>> 1
>>> 6
>>> 7
>>> 12
>>> 5
>>> 0
```

### Adicionando Novos Elementos

```python
bolo = ['farinha de trigo', 'ovo', 'leite', 'manteiga']

bolo.extend(['açucar', 'fermento'])

bolo + ['chocolate']

bolo.append('ameixa')
```

### Removendo Elementos

Utilizando a função `remove()`é possível remover um elemento através do seu valor:

```python
animals = ["ant", "bat", "cat"]
animals.remove("ant")
print(animals) # ["bat", "cat"]
```

Já a função `pop()` remove através do índice (retorna o valor removido).

```python
animals = ["ant", "bat", "cat"]
animals.pop(0) # 'ant'
print(animals) # ["bat", "cat"]
```

### Ordenando os Elementos

```python
lista = ["c", "b", "a"]
print(lista) # ['c', 'b', 'a']

lista.sort()
print(lista) # ['a', 'b', 'c']
```

```python
lista = ["c", "b", "a"]
print(sorted(lista))
# ['a', 'b', 'c']
```

💡 a diferença entre a função `sort()` e a função `sorted` é que em `sort()` você altera a lista em si, e em `sorted()` você tem um valor que pode ser utilizado em uma nova variável.

## Tuplas

uma tupla é uma lista **imutável**. O que diferencia a estrutura de dados lista da estrutura de dados tupla é que a primeira pode ter elementos adicionados a qualquer momento, enquanto que a segunda estrutura, após definida, não permite a adição ou remoção de elementos.

Exemplo de tuplas:

```python
t = (1, 2, 3)

cond = (True, False)

sexo = (
  ('M', 'Masculino'),
  ('F', 'Feminino'),
)

t2 = tuple("a", "b", "c")
```





