# 7. Classes

## 7.1 Definição

Uma classe é uma estrutura que abstrai um conjunto de objetos com características similares. Uma classe define:
- O comportamento de seus objetos através de **métodos**, 
- e os estados possíveis destes objetos, através de **atributos**.

Exemplo:  um veículo possui atributos como: fabricante, número de rodas, cor, quantidade de portas, etc. e métodos como: acelerar, freiar, trocar de marcha, dentre outros.

Uma classe em python é criada a partir da utilização da palavra reservada `class`:

```python
class Veiculo:
    pass
```

Desta forma definimos uma classe `Veiculo`, e a instanciação da mesma, é feita da seguinte forma:

```python
v = Veiculo()
```

## 7.1 Atributos de Classe

Digamos que dentro do escopo do nosso projeto definiu-se que seria um padrão os veículos possuírem 4 rodas. Neste caso, faz sentido criar um atributo de classe com esse valor:

```python
class Veiculo:
    rodas = 4
```

O que acontece então se instanciarmos essa classe novamente?

```python
>>> v1 = Veiculo()
>>> print(v1.rodas)
>>> 4

>>> v2 = Veiculo()
>>> v2.rodas
>>> 4
```

Observe que podemos trocar o valor do atributo `rodas` de uma instância e isso não vai alterar o valor do atributo de classe:

```python
>>> v2.rodas = 6
>>> print(v2.rodas)
6

>>> print(Veiculo.rodas)
4
```

Mas se alteramos o valor do atributo de classe, todos os objetos que possuem a quantidade de rodas padrão (4), terão seus valores alterados, pois o padrão do python é primeiro verificar se existe um valor definido para o atributo de instância, caso contrário, ele utilizará o valor definido no atributo de classe. 

```python
>>>Veiculo.rodas = 2
>>> print(v1.rodas)
2

>>>print(v2.rodas)
6 
```

## 7.2 Utilizando o  método `__init__()`

O método `__init__()` é utilizado para inicializar as instâncias de classe com determinados valores definidos dentro do escopo do seu projeto.

Digamos que ao criar a classe `Veiculo`gostaríamos de informar o fabricante, a cor, e a potência do motor:

```python
class Veiculo:
    rodas = 4

    def __init__(self, fabricante, cor, potencia):
        self.fabricante = fabricante
        self.cor = cor
        self.potencia = potencia
```

```python
>>> v1 = Veiculo(fabricante='Hyundai', cor='Branco', potencia=130)
>>> v2 = Veiculo(fabricante='Ford', cor='Preto', potencia=110)

>>> print(v1.fabricante, v1.cor, v1.potencia)
Hyundai Branco 130

>>> print(v2.fabricante, v2.cor, v2.potencia)
Ford Preto 110
```

Observe que todo método dentro de uma classe em python deve possuir como primeiro parâmetro o nome reservado `self`, assim como o `this` em outras linguagens, é uma forma de referenciar o valor daquela instância que está sendo criada ou manipulada.

