# 5. Funções

Em Python, uma **função** é uma sequência de comandos que executa alguma tarefa e que possui um nome.  
A sua principal finalidade é nos ajudar a **organizar programas** em pedaços reutilizáveis e legíveis, que correspondem à forma como pensamos a solução de um problema.

---

## 5.1 Sintaxe básica

A sintaxe de definição de uma função é:

```python
def nome_da_funcao(parametros):
    <corpo_da_funcao>
    return valor
```

- **`def`** → palavra-chave para criar a função.  
- **`nome_da_funcao`** → identificador escolhido pelo programador.  
- **`parametros`** → valores de entrada (opcional).  
- **`return`** → define o que a função devolve (opcional).  

---

### Exemplos básicos

```python
def ola_mundo():
    return 'Olá Mundo!'

print(ola_mundo())
# >>> Olá Mundo!
```

```python
def maior_idade():
    idade = int(input('Digite uma idade: '))
    msg = 'menor de idade'
    if idade >= 18:
        msg = 'maior de idade'
    return msg

print(maior_idade())
# >>> Digite uma idade: 17
# >>> menor de idade
```

```python
def triangulo(base, altura):
    """Calcula a área de um triângulo"""
    area = (base * altura) / 2
    return area

print(triangulo(7, 10))
# >>> 35
```

---

## 5.2 Parâmetros e argumentos

Parâmetros são variáveis declaradas na função; argumentos são os valores passados na chamada.

```python
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Maria"))
# >>> Olá, Maria!
```

🧭 **Dica prática**

👉 Uma boa forma de lembrar:

- **Parâmetro** → aparece na definição

- **Argumento** → aparece na execução

Funções podem ter **valores padrão**:

```python
def potencia(base, expoente=2):
    return base ** expoente

print(potencia(5))     # usa expoente=2
print(potencia(5, 3))  # expoente=3
# >>> 25
# >>> 125
```

---

## 5.3 Funções com número arbitrário de argumentos

Às vezes não sabemos com antecedência quantos argumentos a função receberá. Para isso:

### `*args` → múltiplos argumentos posicionais

```python
def calc_media(*args):
    media = sum(args)/len(args)
    return media

print(calc_media(10, 7, 7))
# >>> 8.0
```

### `**kwargs` → múltiplos argumentos nomeados

```python
def concatenar(**kwargs):
    resultado = ""
    for arg in kwargs.values():
        resultado += f" {arg}"
    return resultado

print(concatenar(a="Python", b="é", c="muito", d="massa!"))
# >>> Python é muito massa!
```

---

## 5.4 Escopo de variáveis

- **Variáveis locais** → criadas dentro da função.  
- **Variáveis globais** → declaradas fora da função.  

```python
x = 10  # variável global

def exemplo():
    x = 5  # variável local
    print("Dentro da função:", x)

exemplo()
print("Fora da função:", x)
# >>> Dentro da função: 5
# >>> Fora da função: 10
```

---

## 5.5 Funções anônimas (lambda)

Funções `lambda` são **curtas** e **sem nome**. Geralmente usadas em operações simples.

```python
quadrado = lambda x: x**2
print(quadrado(4))
# >>> 16
```

Outro exemplo:  

```python
lista = [1, 2, 3, 4, 5]
dobro = list(map(lambda x: x*2, lista))
print(dobro)
# >>> [2, 4, 6, 8, 10]
```

---

## 5.6 Funções internas (funções dentro de funções)

```python
def externa(x):
    def interna(y):
        return y * 2
    return interna(x) + 5

print(externa(10))
# >>> 25
```

---

## 5.7 Documentação de funções (Docstrings)

É recomendável documentar funções com **docstrings**:

```python
def soma(a, b):
    """Retorna a soma de dois números a e b."""
    return a + b

print(soma.__doc__)
# >>> Retorna a soma de dois números a e b.
```

---

# 6. Exercícios resolvidos

### Exercício 1
Crie uma função que receba dois números e retorne o maior deles.

```python
def maior(a, b):
    return a if a > b else b

print(maior(10, 7))
# >>> 10
```

---

### Exercício 2
Crie uma função que calcule o fatorial de um número.

```python
def fatorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

print(fatorial(5))
# >>> 120
```

---

### Exercício 3
Crie uma função que conte quantas vogais existem em uma string.

```python
def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    return sum(1 for letra in texto if letra in vogais)

print(contar_vogais("Python é incrível"))
# >>> 6
```

---

# 7. Lista de exercícios propostos (com soluções)

1. **Função que retorna o quadrado de um número.**

```python
def quadrado(n):
    return n ** 2
```

---

2. **Função que receba uma lista de números e retorne a soma.**

```python
def soma_lista(lista):
    return sum(lista)
```

---

3. **Função que calcule a média de uma lista.**

```python
def media(lista):
    return sum(lista) / len(lista)
```

---

4. **Função que inverta uma string.**

```python
def inverter(texto):
    return texto[::-1]
```

---

5. **Função que receba dois números e retorne o MDC (máximo divisor comum).**

```python
def mdc(a, b):
    while b:
        a, b = b, a % b
    return a
```

---

6. **Função que receba uma lista e retorne apenas os números pares.**

```python
def pares(lista):
    return [x for x in lista if x % 2 == 0]
```

---

7. **Função que calcule a sequência de Fibonacci até `n` termos.**

```python
def fibonacci(n):
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]
```

---

8. **Função que converta Celsius para Fahrenheit.**

```python
def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32
```

---

9. **Função que conte palavras em uma frase.**

```python
def contar_palavras(frase):
    return len(frase.split())
```
