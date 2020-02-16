# 1. Introdução à Linguagem

![](.pastes/2019-09-01-09-11-58.png)

**Python é uma linguagem de programação com código aberto, de alto nível, tipicamente usada para aplicações web ou linguagens de scripts para administração de sistemas.**

A linguagem foi criada em 1989 por **Guido Van Rossum** e o seu nome foi uma homenagem ao grupo humorístico britânico **Monty Python** (*Monty Python's Flying Circus*), embora muitas pessoas façam associação com o réptil do mesmo nome 🐍 .

![guido](.pastes/2019-09-01-19-31-54.png)

Guido Van Rossum - O pai da criança.

### Por que Python?

*extraído do link: https://pythonhelp.wordpress.com/por-que-python/*

#### Java:
``` java
public class Hello
{
    public static void main(String args[]) {
        java.util.Scanner s = new java.util.Scanner(System.in);
        System.out.print("Digite seu nome: ");
        String nome = s.nextLine();
        System.out.println("Olá, " + nome);
    }
}
```
#### C:
``` c
#include <stdio.h>;
int main()
{
    char nome[200];
    printf("Digite seu nome: ");
    scanf("%s", nome);
    printf("Olá, %s\n", nome);
    return 0;
}
```

#### Pascal:
``` pascal
program HelloWorld(output);
var
    nome: string;
begin
    writeln('Digite seu nome: ');
    read(nome);
    writeln('Olá, ', nome);
end.
```

#### PHP:
```php
$nome = readline("Digite seu nome: ");
echo 'olá: ' . $nome;
```

#### Python: 😍
``` python
nome = input('Digite seu nome: ')
print('Olá, nome)
```

### O Interpretador Python:
```
$ python
Python 3.6.8 (default, May  8 2019, 15:40:17)
[GCC 4.2.1 Compatible Apple LLVM 10.0.1 (clang-1001.0.46.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

### Instruções de atribuição:

Uma instrução de atribuição cria uma nova variável e dá um valor a ela:

``` python
nome = 'Marcello'
idade = 42
peso = 96.50
```

#### Nomes de variáveis:

Podem conter tanto letras como números, mas não podem começar com um número. É convenção utilizar letras minúsculas para nomes de variáveis, porém para indicar constantes, a convenção é colocar o nome da variável em *uppercase* (ex. `VARIAVEL=12`).

O caractere *underline* (_) pode aparecer no nome de uma de variável. Muitas vezes é usado em nomes compostos, como `data_nascimento` ou `area_m2`.

**Exemplos de nomes ilegais para variáveis:**

``` python
>>> 10v = 1000
SyntaxError: invalid syntax
>>> email@ = 'joao@email.com'
SyntaxError: invalid syntax
>>> class = 'Programação'
SyntaxError: invalid syntax
```

`10v` é ilegal porque começa com um número, `email@` possui um caractere ilegal. Já `class` é uma palavra reservada não pode ser utilizada como nome de variável.

São palavras reservadas em Python:

```
and         del         from        None        True
as          elif        global      nonlocal    try
assert      else        if          not         while
break       except      import      or          with
class       False       in          pass        yield
continue    finally     is          raise
def         for         lambda      return
```

### Tipos de Variáveis:

- **Numéricos**: armazenam números. São: inteiros (int), de ponto flutuante (float) e complexos (complex);
- **Literais**: armazenam caracteres (qualquer um do teclado) ou sequências de caracteres (string);
- **Lógicos**: booleanos, armazenam verdadeiro ou falso (bool).

``` python
>>> valor = 100
>>> type(valor)
<class 'int'>
>>> perimetro_m = 237.95
>>> type(perimetro_m)
<class 'float'>
>>> nome = 'Maria'
>>> type(nome)
<class 'str'>
>>> cond = True
>>> type(cond)
<class 'bool'>
```

📚  Sugestão de leitura:  https://realpython.com/python-data-types/

💡 Atribuição múltipla: permite definir diversas variáveis ao mesmo tempo e inclusive trocar os valores entre elas:

```python
>>> longitude, latitude = -36.70, -8.23
>>> longitude
-36.7
>>> latitude
-8.23
>>> ponto_3d = (-30.11, -8.25, 17.00)
>>> x, y, z = ponto_3d
>>> x
-30.11
>>> y
-8.25
>>> z
17.0
```

### Operadores:

Operadores Numéricos Básicos:

- Adição: +
- Subtração: -
- Divisão: /
- Multiplicação: *
- Potenciação: **
- Resto de uma divisão: %

Retirado do livro **Pense em Python 2e**: 📚  https://penseallen.github.io/PensePython2e/

> Quando uma expressão contém mais de um operador, a ordem da avaliação depende da ordem das operações. Para operadores matemáticos, o Python segue a convenção matemática. O acrônimo PEMDAS pode ser útil para lembrar das regras:

> Os **Parênteses** têm a precedência mais alta e podem ser usados para forçar a avaliação de uma expressão na ordem que você quiser. Como as expressões em parênteses são avaliadas primeiro, 2 * (3-1) é 4, e (1+1)**(5-2) é 8. Também é possível usar parênteses para facilitar a leitura de uma expressão, como no caso de (minute * 100) / 60, mesmo se o resultado não for alterado.

> A **Exponenciação** tem a próxima precedência mais alta, então 1 + 2 ** 3 é 9, não 27, e 2 * 3 ** 2 é 18, não 36.

> A **Multiplicação** e a **Divisão** têm precedência mais alta que a **Adição** e a **Subtração**. Assim, 2 * 3 - 1 é 5, não 4, e 6 + 4 / 2 é 8, não 5.

> Os operadores com a mesma precedência são avaliados da esquerda para a direita (exceto na exponenciação). Assim, na expressão degrees / 2 * pi, a divisão acontece primeiro e o resultado é multiplicado por pi. Para dividir por 2π, você pode usar parênteses ou escrever degrees / 2 / pi.

📚  Sugestão de leitura:  https://github.com/PyLadiesSP/Cursos

O exercício abaixo foi retirado deste link.

**Exercício 01:** Defina as variáveis como:

```python
a = 2
b = 3
c = 2.0
d = '2.0'
```
e faça as operações a seguir:
```python
a + b
b ** a
a + c
a + d
```

e também teste as condições a seguir:
```python
a == c
a <= b
a < b and b < c
a < b or b < c
a > c or a >= c
not(a != b and b <= (a**2)-1)
```

📚  Sugestão de leitura:  https://github.com/rg3915/tutoriais

O exercício abaixo foi retirado deste link.

**Exercício 02:** Um jogo de futebol foi programado para ser realizado com duração normal: 2 tempos de 45 minutos, com um intervalo de 15 minutos. O jogo começou pontualmente às 9:00 horas.

Um repórter cronometrou 6 jogadas que considerou as mais importantes a partir do início do jogo e registrou suas marcas da seguinte maneira:

| Jogada    | Tempo desde o início do jogo |
| --------- | ---------------------------- |
| Falta A   | 590 s                        |
| Pênalti   | 785 s                        |
| Gol I     | 1350 s                       |
| Gol II    | 2690 s                       |
| Falta B   | 4332 s                       |
| Bicicleta | 5960 s                       |

A partir das informações acima, assinale a afirmativa correta.

(A) A falta A aconteceu exatamente às 9h e 9 minutos.

(B) O primeiro gol ocorreu no tempo cravado de 22 minutos e 30 segundos do 1º tempo.

(C) A bicicleta surpreendeu o público aos 39 minutos e 20 segundos do 1º tempo.

(D) O pênalti aconteceu aos 22 minutos e 5 segundos do 1º tempo.

(E) O segundo gol aconteceu no segundo tempo.
