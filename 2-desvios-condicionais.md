# 2. Desvios Condicionais

Desvios condicionais permitem que o programa tome **decisões** com base em condições. O bloco de código só é executado se a condição for avaliada como `True`.

---

## `if` / `else`

```python
if <condição>:
    # executado se a condição for True
else:
    # executado se a condição for False
```

> A indentação (recuo de 4 espaços) delimita o bloco. Não há chaves `{}` como em outras linguagens.

**Exemplo:**

```python
area_ha = 8.5

if area_ha >= 10:
    print('Imóvel rural — área mínima atingida')
else:
    print('Imóvel rural — área abaixo do mínimo')
```

Com entrada do usuário:

```python
area_ha = float(input('Digite a área em hectares: '))

if area_ha >= 10:
    print('Área suficiente')
else:
    print('Área insuficiente')
```

💣 `input()` sempre retorna `str` — converta com `int()` ou `float()` antes de comparar com números.

---

## `elif` — múltiplas condições

Quando há mais de dois casos, use `elif` (abreviação de *else if*):

```python
if <condição 1>:
    ...
elif <condição 2>:
    ...
elif <condição 3>:
    ...
else:
    ...
```

**Exemplo — classificação de declividade (EMBRAPA):**

```python
declividade = 18  # em graus

if declividade <= 3:
    classe = 'Plano'
elif declividade <= 8:
    classe = 'Suave ondulado'
elif declividade <= 20:
    classe = 'Ondulado'
elif declividade <= 45:
    classe = 'Forte ondulado'
else:
    classe = 'Montanhoso / Escarpado'

print(f'Classe de relevo: {classe}')
```

💡 O Python avalia as condições de cima para baixo e executa apenas o **primeiro bloco** cuja condição seja verdadeira.

---

## Operadores de Comparação

Retornam `True` ou `False`.

| Operador | Significado | Exemplo |
|---|---|---|
| `==` | Igual a | `crs == 'EPSG:4326'` |
| `!=` | Diferente de | `tipo != 'Ponto'` |
| `>` | Maior que | `area > 100` |
| `<` | Menor que | `vertices < 500` |
| `>=` | Maior ou igual | `escala >= 1000` |
| `<=` | Menor ou igual | `populacao <= 50000` |

---

## Operadores Lógicos

Combinam duas ou mais condições.

| Operador | Resultado `True` quando... | Exemplo |
|---|---|---|
| `and` | **ambas** as condições são `True` | `area > 5 and municipio == 'RN'` |
| `or` | **ao menos uma** condição é `True` | `tipo == 'Rio' or tipo == 'Lago'` |
| `not` | a condição é `False` | `not reprojetado` |

```python
lon = -36.5
lat = -5.8

# Verificar se o ponto está dentro de uma bounding box
if lon >= -38.0 and lon <= -35.0 and lat >= -7.0 and lat <= -4.0:
    print('Ponto dentro da área de interesse')
else:
    print('Ponto fora da área de interesse')
```

---

## Operadores de Pertencimento e Identidade

| Operador | Uso |
|---|---|
| `in` | Verifica se um valor está em uma sequência |
| `not in` | Verifica se um valor **não** está em uma sequência |
| `is` | Verifica se dois nomes apontam para o **mesmo objeto** |
| `is not` | Negação do `is` |

```python
formatos_suportados = ['shp', 'gpkg', 'geojson', 'kml']
extensao = 'gpkg'

if extensao in formatos_suportados:
    print('Formato aceito')
else:
    print('Formato não suportado')
```

```python
resultado = None

if resultado is None:
    print('Sem resultado — verifique a camada de entrada')
```

---

## Operador Ternário

Forma compacta para `if/else` em uma única linha:

```python
<valor_se_true> if <condição> else <valor_se_false>
```

```python
area_ha = 23.5
situacao = 'apto' if area_ha >= 10 else 'inapto'
print(f'Imóvel: {situacao}')  # Imóvel: apto
```

Use com moderação — prefira o `if/else` convencional quando a lógica for mais complexa.

---

## O Statement `pass`

Usado como **marcador** quando a sintaxe exige um bloco mas ainda não há lógica definida:

```python
tipo_geometria = 'Polígono'

if tipo_geometria == 'Ponto':
    pass  # TODO: implementar lógica para pontos
elif tipo_geometria == 'Linha':
    pass  # TODO: implementar lógica para linhas
else:
    print('Geometria do tipo Polígono')
```

---

## Exercícios

### Exercício 1

Solicite ao usuário um número inteiro e informe se ele é **positivo**, **negativo** ou **zero**.

---

### Exercício 2

Solicite ao usuário duas notas (de 0 a 10) e calcule a média. Exiba a situação do aluno conforme a tabela:

| Média | Situação |
|---|---|
| `>= 7.0` | Aprovado |
| `>= 5.0` e `< 7.0` | Recuperação |
| `< 5.0` | Reprovado |

---

### Exercício 3 — Contexto GIS

O **INCRA** classifica imóveis rurais por módulos fiscais. Escreva um programa que:

1. Solicite ao usuário a **área do imóvel em hectares** e o **módulo fiscal do município** (em hectares)
2. Calcule a quantidade de módulos fiscais do imóvel
3. Classifique e exiba o imóvel conforme a tabela abaixo:

| Tamanho | Classificação |
|---|---|
| Até 1 módulo fiscal | Minifúndio |
| De 1 a 4 módulos fiscais | Pequena propriedade |
| De 4 a 15 módulos fiscais | Média propriedade |
| Acima de 15 módulos fiscais | Grande propriedade |

Exemplo de saída esperada:
```
Área: 85.0 ha | Módulo fiscal: 20 ha
Quantidade de módulos: 4.25
Classificação: Média propriedade
```
