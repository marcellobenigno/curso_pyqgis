# 5. Funções

Em Python, uma **função** é uma sequência de comandos que executa alguma tarefa e que possui um nome. A sua principal finalidade é nos ajudar a organizar programas em pedaços que correspondam a como imaginamos uma solução do problema.

A sintaxe de uma definição de função é:

```python
def nome_da_funcao(arg1, arg2, arg_n):
    <codigo>
```

Exemplos:

```python
def ola_mundo():
    return 'Olá Mundo!'
 
print(ola_mundo())

# >>> Olá Mundo!

def maior_idade():
    idade = int(input('digite uma idade: '))
    msg = 'menor de idade'
    if idade >= 18:
        msg = 'maior de idade'
    return msg

print(maior_idade())

# >>> digite uma idade: 17
# >>> menor de idade

def triangulo(base, altura):
    """Calcula a área de um triângulo"""
    area = (base * altura) / 2
    return area

print(triangulo(7, 10))

# >>> 35
```

## 5.1 Funções com um número arbitrário de argumentos

As vezes não sabemos com antecedência quantos argumentos a função vai receber, podemos criar um parâmetro onde simplesmente adicionamos um asterisco na frente do parâmetro e ele pode receber quantos argumentos forem necessários ou nenhum argumento:

```python
def calc_media(*args):
    media = sum(args)/len(args)
    return media
    
calc_media(10, 7, 7)

# >>> 8
```

```python
def concatenar(**kwargs):
    resultado = ""
    for arg in kwargs.values():
        resultado += f' {arg}'
    return resultado

print(concatenar(a="Python", b="é", c="muito", d="massa!"))

# >>> Python é muito massa! 
```
