

# 7. Classes e Orientação a Objetos em Python

## 7.1 Definição

Uma Classe é o projeto ou molde para a criação de Objetos. Ela encapsula um conjunto de objetos com características e comportamentos similares.

Uma classe define:

* O estado possível dos seus objetos, através de Atributos (dados/variáveis).

* O comportamento dos seus objetos, através de Métodos (funções).

**Exemplo:** A classe `Veiculo` é o molde.

 - Atributos (estado): `fabricante`, `cor`, `número_de_rodas`, `velocidade_atual`.

 - Métodos (comportamento): `acelerar()`, `frear()`, `ligar_motor()`.

Um **Objeto** é uma instância concreta dessa classe. Se a classe é o projeto de um carro, o objeto é o carro que saiu da linha de montagem.

## Criando e Instanciando uma Classe

Uma classe em Python é definida com a palavra reservada class:

```Python

class Veiculo:
    # Conteúdo da classe (atributos e métodos)
    pass 
```

Instanciação: Criar um objeto a partir da classe é chamado de instanciação.

```Python

# Instanciando a classe Veiculo, criando dois objetos (instâncias)
v = Veiculo()
```

## 7.2 Atributos de Classe vs. Atributos de Instância

Existem duas categorias principais de atributos em uma classe:

**Atributos de Classe (ou Estáticos)** 

São atributos que pertencem à própria classe e são compartilhados por todas as instâncias dessa classe, a menos que uma instância o sobrescreva. São ideais para valores constantes ou padrões.


```Python

class Veiculo:
    # Atributo de CLASSE: o valor padrão para todos os veículos
    rodas = 4 

# Acessando o atributo de CLASSE
print(Veiculo.rodas)
```

**Exemplo de Acesso e Modificação:**


```Python

>>> v1 = Veiculo()
>>> v2 = Veiculo()

# Acessando via instância
>>> print(v1.rodas) 
4

# Sobrescrevendo o atributo APENAS na instância v2
>>> v2.rodas = 6 
>>> print(v2.rodas) 
6

# O atributo de v1 e da CLASSE continua inalterado
>>> print(v1.rodas) 
4
>>> print(Veiculo.rodas) 
4

# Se alterarmos o atributo de CLASSE
>>> Veiculo.rodas = 2 

>>> print(v1.rodas) # Reflete a mudança da classe (pois não foi sobrescrito)
2 

>>> print(v2.rodas) # Continua com o valor sobrescrito
6

```

**Atributos de Instância**

São atributos que pertencem a um objeto específico e não são compartilhados. Cada instância terá sua própria cópia desses atributos. Eles são geralmente inicializados dentro do método especial `__init__()`.

## 7.3 O Método `__init__()` (Construtor)

O método __init__() é o construtor da classe. Ele é chamado automaticamente toda vez que você cria uma nova instância da classe. É o local ideal para receber os dados iniciais e criar os atributos de instância.

**A Palavra-chave `self`**

Todo método dentro de uma classe em Python deve ter o parâmetro obrigatório `self` como o primeiro argumento.

O `self` é uma referência à própria instância que está sendo criada ou manipulada.

Ele permite que você acesse e modifique os atributos e chame outros métodos daquela instância específica (ex: `self.fabricante`).

**Exemplo Completo com `__init__`**

```Python

class Veiculo:
    # Atributo de Classe
    rodas = 4 

    # Método Construtor - Inicializa a instância
    def __init__(self, fabricante, cor, potencia):
        # Atributos de Instância: criados e inicializados para CADA objeto
        self.fabricante = fabricante
        self.cor = cor
        self.potencia = potencia
        self.velocidade_atual = 0 # Valor inicial fixo

# Instanciando com argumentos
v1 = Veiculo(fabricante='Hyundai', cor='Branco', potencia=130)
v2 = Veiculo(fabricante='Ford', cor='Preto', potencia=110)

# Acessando atributos de INSTÂNCIA
print(f"v1 é um {v1.fabricante} {v1.cor} com {v1.potencia}cv.")
# Saída: v1 é um Hyundai Branco com 130cv.
```


## 7.4 Métodos de Instância

Os Métodos definem o comportamento dos objetos. Eles são funções que pertencem à classe e operam sobre os atributos de instância (self).

**Exemplo de Métodos**

Vamos adicionar métodos para simular o comportamento de um veículo:

```Python

class Veiculo:
    def __init__(self, fabricante, cor, potencia):
        self.fabricante = fabricante
        self.cor = cor
        self.potencia = potencia
        self.velocidade_atual = 0

    # Método de Instância para acelerar
    def acelerar(self, incremento):
        self.velocidade_atual += incremento
        print(f"O {self.fabricante} acelerou. Velocidade atual: {self.velocidade_atual} km/h.")

    # Método para apresentar a descrição do objeto
    def descrever(self):
        return f"Veículo: {self.fabricante} | Cor: {self.cor} | Potência: {self.potencia} CV"

# Instanciando e usando os métodos
v3 = Veiculo('Toyota', 'Vermelho', 180)

print(v3.descrever()) 
# Saída: Veículo: Toyota | Cor: Vermelho | Potência: 180 CV

v3.acelerar(50) # O self será o v3
# Saída: O Toyota acelerou. Velocidade atual: 50 km/h.
```


# 8. Exercícios Resolvidos

### Exercício 1: Classe `ImovelRural`.

Crie uma classe `ImovelRural` com os seguintes atributos de instância (definidos no construtor): `nome_fazenda` e `area_hectares`.

**Solução**

```Python
class ImovelRural:
    # O construtor recebe nome e área
    def __init__(self, nome_fazenda, area_hectares):
        self.nome_fazenda = nome_fazenda
        self.area_hectares = area_hectares # Atributo de Instância

    # Método para conversão de área
    def calcular_area_em_alqueires(self):
        # 1 alqueire paulista = 2.42 hectares
        ALQUEIRE_PAULISTA = 2.42
        area_alqueires = self.area_hectares / ALQUEIRE_PAULISTA
        # Usamos round para limitar as casas decimais para melhor visualização
        return round(area_alqueires, 2) 

    # Método para imprimir os detalhes
    def imprimir_detalhes(self):
        area_alqueires = self.calcular_area_em_alqueires()
        print("-" * 30)
        print(f"Nome: {self.nome_fazenda}")
        print(f"Área: {self.area_hectares} hectares")
        print(f"Área: {area_alqueires} alqueires paulistas")
        print("-" * 30)

# Teste
i1 = ImovelRural("Fazenda Paraíso", 121)
i2 = ImovelRural("Sítio Estrela", 48.4)

i1.imprimir_detalhes()
i2.imprimir_detalhes()

# Saída Esperada:
# ------------------------------
# Nome: Fazenda Paraíso
# Área: 121 hectares
# Área: 50.0 alqueires paulistas
# ------------------------------
# ------------------------------
# Nome: Sítio Estrela
# Área: 48.4 hectares
# Área: 20.0 alqueires paulistas
# ------------------------------
```


### Exercício 2: Classe Retangulo com Área

Crie uma classe `Retangulo` com atributos `largura` e `altura`. Adicione um método `calcular_area()` que retorna a área do retângulo.

**Solução** 

```Python

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

# Teste
r1 = Retangulo(10, 5)
area = r1.calcular_area()
print(f"A área do retângulo é: {area}") # Saída: 50
```

### Exercício 3: Atributo de Classe em ContaBancaria

Crie uma classe ContaBancaria com o atributo de classe taxa_saque igual a 5.0. Crie um atributo de instância saldo.

**Solução**

```Python

class ContaBancaria:
    # Atributo de CLASSE
    taxa_saque = 5.0 

    def __init__(self, saldo_inicial):
        # Atributo de INSTÂNCIA
        self.saldo = saldo_inicial 

# Teste
conta1 = ContaBancaria(1000)
print(f"Taxa de saque padrão: R$ {ContaBancaria.taxa_saque}")
print(f"Saldo da Conta 1: R$ {conta1.saldo}")
```


### Exercício 4: Método para Depositar

Adicione à classe `ContaBancaria` do exercício 3 um método `depositar(valor)` que incrementa o saldo.

**Solução**

```Python

class ContaBancaria:
    taxa_saque = 5.0 

    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial 

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor} realizado. Novo saldo: R$ {self.saldo}")
        else:
            print("O valor do depósito deve ser positivo.")

# Teste
c1 = ContaBancaria(100)
c1.depositar(250.50)
```

### Exercício 5: Método para Sacar com Taxa

Adicione à classe ContaBancaria o método sacar(valor). O saque deve debitar o valor mais a taxa_saque do saldo, somente se houver saldo suficiente.

**Solução**

```Python

class ContaBancaria:
    taxa_saque = 5.0 

    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial 

    def sacar(self, valor):
        custo_total = valor + self.taxa_saque
        if self.saldo >= custo_total:
            self.saldo -= custo_total
            print(f"Saque de R$ {valor} (R$ {self.taxa_saque} de taxa) realizado. Novo saldo: R$ {self.saldo}")
        else:
            print(f"Saldo insuficiente. Necessário R$ {custo_total} para saque, mas tem R$ {self.saldo}.")

# Teste
c2 = ContaBancaria(300)
c2.sacar(50)  # Saque de 50 + 5 de taxa = 55. Saldo: 245
c2.sacar(500) # Saldo insuficiente.

```

### Exercício 6: Classe Pessoa com `__str__`

Crie uma classe Pessoa com nome e cidade. Implemente o método especial __str__(self) para retornar uma string formatada que descreve o objeto.

**Solução**

```Python

class Pessoa:
    def __init__(self, nome, cidade):
        self.nome = nome
        self.cidade = cidade

    def __str__(self):
        # O método __str__ é chamado quando usamos print(objeto)
        return f"{self.nome} mora em {self.cidade}"

# Teste
p1 = Pessoa("Alice", "São Paulo")
print(p1) 
# Saída: Alice mora em São Paulo
```


### Exercício 7: Contador de Instâncias

Crie uma classe `Produto` e use um atributo de classe chamado `quantidade_produtos` para rastrear quantas instâncias de Produto foram criadas. O contador deve ser 
incrementado no `__init__`.

**Solução**

```Python

class Produto:
    # Atributo de CLASSE para contar instâncias
    quantidade_produtos = 0

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        # Incrementa o contador de CLASSE toda vez que um objeto é criado
        Produto.quantidade_produtos += 1 

# Teste
prod_a = Produto("Notebook", 3500)
prod_b = Produto("Mouse", 80)

print(f"Total de produtos criados: {Produto.quantidade_produtos}") # Saída: 2
```

### Exercício 9: Classe Livro com Status

Crie uma classe `Livro` com `titulo` e `autor`. Adicione um atributo de instância `emprestado` (booleano) inicializado como `False`. Crie os métodos `emprestar()` e `devolver()` para alterar o status.

**Solução**

```Python

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.emprestado = False # Atributo de instância padrão

    def emprestar(self):
        if not self.emprestado:
            self.emprestado = True
            print(f"O livro '{self.titulo}' foi emprestado.")
        else:
            print(f"Erro: O livro '{self.titulo}' já está emprestado.")

    def devolver(self):
        if self.emprestado:
            self.emprestado = False
            print(f"O livro '{self.titulo}' foi devolvido.")
        else:
            print(f"Erro: O livro '{self.titulo}' já está na biblioteca.")

# Teste
l1 = Livro("Padrões de Projeto", "Gang of Four")
l1.emprestar()      
l1.devolver()       

```