# 1. Introdução à Linguagem Python

## O que é Python?

Python é uma linguagem de programação **open source**, de **alto nível** e **interpretada**, criada em 1989 por **Guido van Rossum**. Seu design prioriza legibilidade e simplicidade — o mesmo programa escrito em Java ou C pode ser expresso em Python com muito menos linhas de código.

```python
# Python — simples e direto
nome = input('Digite seu nome: ')
print('Olá,', nome)
```

## Por que Python em GIS?

Python é a linguagem padrão do ecossistema geoespacial. Ela está integrada nativamente nas principais ferramentas do mercado:

| Ferramenta | Uso |
|---|---|
| **QGIS** | Console Python embutido, plugins e automação via PyQGIS |
| **ArcGIS / ArcPy** | Automação de geoprocessamento na plataforma Esri |
| **GeoPandas** | Análise de dados vetoriais (shapefiles, GeoJSON) |
| **Shapely** | Operações geométricas (buffer, interseção, união) |
| **Fiona** | Leitura e escrita de formatos vetoriais |
| **Rasterio** | Leitura e processamento de dados raster |
| **pyProj** | Transformação de sistemas de coordenadas |

---

## Ambiente de Desenvolvimento

### Console Python do QGIS

O QGIS possui um console Python integrado, acessível pelo menu **Plugins → Console Python** (atalho: `Ctrl+Alt+P`). É o ponto de entrada mais direto para automação de tarefas no QGIS.

```python
# Exemplo no console do QGIS: listar camadas carregadas
projeto = QgsProject.instance()
for nome, camada in projeto.mapLayers().items():
    print(camada.name())
```

### Python fora do QGIS

Para scripts independentes, instale o Python via [python.org](https://www.python.org) e gerencie pacotes com `pip`:

```bash
pip install geopandas shapely fiona
```

Para ambientes isolados, recomenda-se o uso de `venv` ou `conda`.

---

## Variáveis e Atribuição

Uma variável é um nome que aponta para um valor na memória. A atribuição é feita com `=`:

```python
municipio = 'Campina Grande'
populacao = 422000
area_km2 = 593.96
capital = False
```

### Boas práticas de nomenclatura

- Use **letras minúsculas** e **underline** para separar palavras (`snake_case`)
- Use nomes **descritivos**: `area_ha` é melhor que `a`
- Constantes em **maiúsculas**: `FATOR_CONVERSAO = 10000`
- Evite acentos e caracteres especiais em nomes de variáveis

```python
# Bom
area_m2 = 15000
crs_destino = 'EPSG:4326'
FATOR_HA = 10000

# Evite
a = 15000
x1 = 'EPSG:4326'
```

### Atribuição múltipla

```python
longitude, latitude = -35.74, -7.22
print(longitude, latitude)  # -35.74 -7.22

# Desempacotar uma tupla
ponto = (-30.11, -8.25, 17.00)
x, y, z = ponto
```

### Palavras reservadas

Não podem ser usadas como nomes de variáveis:

```
and    as     assert  break   class   continue  def     del
elif   else   except  False   finally for       from    global
if     import in      is      lambda  None      nonlocal not
or     pass   raise   return  True    try       while   with  yield
```

---

## Tipos de Dados Primitivos

### `int` — Inteiro

Números sem parte decimal.

```python
zona_utm = 24
numero_feicoes = 1500
```

### `float` — Ponto flutuante

Números com parte decimal.

```python
latitude = -8.234
area_ha = 157.83
escala = 1.25e-5  # notação científica: 0.0000125
```

### `str` — String (texto)

Sequência de caracteres, delimitada por aspas simples ou duplas.

```python
sistema_ref = 'SIRGAS 2000'
epsg = "EPSG:4674"
```

### `bool` — Booleano

Armazena apenas `True` ou `False`.

```python
reprojetado = True
tem_z = False
```

### Verificando o tipo com `type()`

```python
>>> type(zona_utm)
<class 'int'>
>>> type(area_ha)
<class 'float'>
>>> type(sistema_ref)
<class 'str'>
>>> type(reprojetado)
<class 'bool'>
```

### Conversão entre tipos (*casting*)

```python
area_str = '15000'
area_num = float(area_str)   # '15000' → 15000.0
zona_str = str(24)            # 24 → '24'
flag = bool(1)                # 1 → True
```

### Tabela resumo dos tipos primitivos

| Tipo | Palavra-chave | Exemplo | Uso em GIS |
|---|---|---|---|
| Inteiro | `int` | `24` | Zona UTM, número de feições |
| Ponto flutuante | `float` | `-8.234` | Coordenadas, áreas, distâncias |
| Texto | `str` | `'SIRGAS 2000'` | Nome de camada, CRS, atributos |
| Booleano | `bool` | `True` | Flags, resultados de consulta |

---

## Operadores

### Aritméticos

| Operador | Operação | Exemplo | Resultado |
|---|---|---|---|
| `+` | Adição | `3 + 2` | `5` |
| `-` | Subtração | `10 - 4` | `6` |
| `*` | Multiplicação | `3 * 4` | `12` |
| `/` | Divisão | `7 / 2` | `3.5` |
| `//` | Divisão inteira | `7 // 2` | `3` |
| `%` | Resto (módulo) | `7 % 2` | `1` |
| `**` | Potenciação | `2 ** 8` | `256` |

**Precedência:** Parênteses > Exponenciação > `*` `/` > `+` `-` (da esquerda para a direita)

```python
# Converter área de m² para hectares
area_m2 = 235000
area_ha = area_m2 / 10000
print(area_ha)  # 23.5
```

### Relacionais (Comparação)

Retornam `True` ou `False`.

| Operador | Significado | Exemplo |
|---|---|---|
| `==` | Igual a | `zona == 24` |
| `!=` | Diferente de | `crs != 'EPSG:4326'` |
| `>` | Maior que | `area > 100` |
| `<` | Menor que | `pop < 50000` |
| `>=` | Maior ou igual | `escala >= 1000` |
| `<=` | Menor ou igual | `vertices <= 500` |

```python
>>> area_ha = 23.5
>>> area_ha > 10
True
>>> area_ha == 23.5
True
```

### Lógicos

Combinam expressões booleanas.

| Operador | Significado | Resultado |
|---|---|---|
| `and` | E lógico | `True` só se ambos forem `True` |
| `or` | OU lógico | `True` se ao menos um for `True` |
| `not` | NÃO lógico | Inverte o valor |

```python
area_ha = 23.5
municipio_rn = True

# Feição dentro do RN com área maior que 10 ha?
if area_ha > 10 and municipio_rn:
    print('Feição relevante no RN')

# Verificar se está fora de uma faixa de coordenadas
lon = -36.5
if lon < -35 or lon > -34:
    print('Fora da região de interesse')
```

---

## Comentários

Comentários são ignorados pelo interpretador e servem para documentar o código.

```python
# Isto é um comentário de linha

area_m2 = 15000  # área do lote em metros quadrados

"""
Este é um comentário de múltiplas linhas.
Também chamado de docstring quando usado em funções e classes.
"""

# Converter de m² para hectares
area_ha = area_m2 / 10000
```

---

## Funções `print()` e `input()`

### `print()`

Exibe valores na saída padrão.

```python
crs = 'SIRGAS 2000'
zona = 24
area = 157.83

print(crs)                          # SIRGAS 2000
print('Zona UTM:', zona)            # Zona UTM: 24
print(f'Área: {area:.2f} ha')       # Área: 157.83 ha
print('x =', -36.5, 'y =', -8.2)   # x = -36.5 y = -8.2
```

Parâmetros úteis:

```python
# sep: separador entre valores (padrão é espaço)
print('lon', 'lat', sep=', ')  # lon, lat

# end: caractere final (padrão é quebra de linha \n)
print('Carregando', end='...')
print('OK')  # Carregando...OK
```

### `input()`

Lê uma entrada do usuário como **string**.

```python
nome_camada = input('Nome da camada: ')
print('Camada selecionada:', nome_camada)
```

> **Atenção:** `input()` sempre retorna `str`. Use `int()` ou `float()` para converter:

```python
area_str = input('Digite a área em m²: ')
area_m2 = float(area_str)
area_ha = area_m2 / 10000
print(f'Área em hectares: {area_ha:.4f} ha')
```

---

## Exercícios

### Exercício 1

Escreva um programa que solicite ao usuário o **nome** e a **idade** e exiba uma mensagem de apresentação no formato:

```
Nome: Ana Silva | Idade: 22 anos
```

---

### Exercício 2

Declare variáveis para armazenar o nome de um município, sua população e sua área em km². Calcule e exiba a **densidade demográfica** (habitantes/km²) com duas casas decimais.

Exemplo de saída esperada:
```
Município: Mossoró
Área: 2099.33 km²
População: 295000
Densidade: 140.52 hab/km²
```

---

### Exercício 3 — Contexto GIS

Um levantamento topográfico registrou as coordenadas de um ponto em **UTM** (zona 24S, SIRGAS 2000):

- Este: `290543.72` m
- Norte: `9195820.14` m

Escreva um programa que:

1. Armazene as coordenadas em variáveis com nomes adequados
2. Exiba as coordenadas formatadas com 2 casas decimais
3. Verifique e informe se o ponto está **ao norte** do paralelo de referência 9.180.000 m N
4. Calcule a **distância** desse ponto a um segundo ponto de coordenadas `E = 291200.00` e `N = 9196500.00` usando a fórmula da distância euclidiana: `d = ((dE² + dN²) ** 0.5)`

Saída esperada:
```
Ponto P1: E = 290543.72 m | N = 9195820.14 m
Ponto P2: E = 291200.00 m | N = 9196500.00 m
Ponto está ao norte do paralelo de referência? True
Distância entre P1 e P2: 919.88 m
```
