# 3. Strings

Uma string em Python é objeto do tipo str.

```python
nome = 'João'
type(nome)
>>> <class 'str'>
```

### Métodos da Classe String:

```python
dir(nome)
>>> ['__add__', '__class__', '__contains__', '__delattr__', '__dir__',
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
'__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__',
'__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__',
'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
'__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__',
'__subclasshook__', 'capitalize', 'casefold', 'center', 'count',
'encode', 'endswith', 'expandtabs', 'find', 'format',
'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal',
'isdigit', 'isidentifier', 'islower', 'isnumeric',
'isprintable', 'isspace', 'istitle', 'isupper', 'join',
'ljust', 'lower', 'lstrip', 'maketrans', 'partition',
'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
'rsplit', 'rstrip', 'split', 'splitlines', 'startswith',
'strip', 'swapcase', 'title', 'translate', 'upper','zfill']
```

```python
help(nome.upper)

Help on built-in function upper:

upper(...) method of builtins.str instance
    S.upper() -> str

    Return a copy of S converted to uppercase.
    
nome.upper()    
>>> 'JOÃO'
```

### Comprimento de uma String

É obtida através da função len():

```python
print(len('IFPB'))

>>> 4
```

### Concatenação de Strings:

```python
nome = 'Rodrigo'
sobrenome = 'Santos'
nome + sobrenome
>>> 'RodrigoSantos'
nome + ' ' + sobrenome
>>> 'Rodrigo Santos'
```

### Operador `in`:

```python
texto = 'hoje tem aula no IFPB'
'aula' in texto
>>> True
'Hoje' in texto
>>> False
'z' in texto
>>> False 
```

### A função format()

```python
nome = 'José'
idade = 25

print('O meu nome é {} e a minha idade é {}'.format(nome, idade))
```

### f-trings:

💥  f-strings só estão disponíveis a partir do Python >= 3.6:

```python
nome = 'José'
idade = 25

print(f'O meu nome é {nome} e a minha idade é {idade}')
```

### Fatiamento de strings ou *Slicing*:

![](.pastes/2019-09-11-07-58-25.png)

```python
palavra = 'benigno'
len(palavra)
>>> 7
palavra[0]
>>> 'b'
palavra[6]
>>> 'o'
palavra[0:3]
>>> 'ben'
# mesmo resultado da anterior:
palavra[:3]
>>> 'ben'
palavra[1:4]
>>> 'eni'
palavra[-1]
>>> 'o'
palavra[-3]
>>> 'g'
palavra[2:-2]
>>> 'nig'
```
