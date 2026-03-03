# 4. Listas e Tuplas

---

## Listas

Uma lista é uma **sequência ordenada e mutável** de elementos, delimitada por colchetes `[]`. Os itens podem ser de tipos diferentes e a lista pode crescer ou encolher em tempo de execução.

```python
camadas = ['municipios', 'rodovias', 'hidrografia', 'curvas_nivel']
altitudes = [450.0, 512.3, 389.7, 601.1]
vazia = []
mista = ['Natal', -5.79, True, [0, 0]]   # tipos mistos são permitidos
```

---

## Acesso por Índice e Fatiamento

O índice começa em `0`; índices negativos contam a partir do final.

```
 'municipios'  'rodovias'  'hidrografia'  'curvas_nivel'
       0            1             2              3
      -4           -3            -2             -1
```

```python
camadas[0]      # 'municipios'
camadas[-1]     # 'curvas_nivel'
camadas[1:3]    # ['rodovias', 'hidrografia']
camadas[:2]     # ['municipios', 'rodovias']
camadas[::2]    # ['municipios', 'hidrografia']   (de 2 em 2)
```

💣 Acessar um índice inexistente lança `IndexError`. Use `len()` para verificar o tamanho antes.

### Alterando elementos

Diferente de strings, listas são **mutáveis**:

```python
camadas[0] = 'limite_municipal'
print(camadas)  # ['limite_municipal', 'rodovias', 'hidrografia', 'curvas_nivel']
```

---

## Métodos de Lista

### Adicionar elementos

```python
pontos = [(-35.74, -7.22), (-36.10, -8.01)]

pontos.append((-37.05, -5.80))        # adiciona ao final
pontos.insert(1, (-35.90, -7.50))     # insere na posição 1
pontos.extend([(-38.0, -6.0), (-34.5, -7.9)])  # une outra lista ao final
```

### Remover elementos

```python
camadas = ['municipios', 'rodovias', 'lixo', 'hidrografia']

camadas.remove('lixo')      # remove pelo valor (primeiro encontrado)
ultima = camadas.pop()      # remove e retorna o último elemento
segunda = camadas.pop(1)    # remove e retorna o elemento do índice 1
del camadas[0]              # remove pelo índice (sem retornar)
```

💡 `remove()` lança `ValueError` se o elemento não existir. Use `in` para verificar antes.

### Ordenar

```python
areas = [230.5, 89.1, 512.0, 45.3, 310.7]

areas.sort()                    # ordena no lugar (ascendente)
areas.sort(reverse=True)        # ordena no lugar (descendente)
ordenadas = sorted(areas)       # retorna nova lista, original intacta
```

```python
camadas = ['rodovias', 'municipios', 'hidrografia']
camadas.sort()          # ['hidrografia', 'municipios', 'rodovias']
camadas.reverse()       # inverte a ordem atual no lugar
```

💡 `sort()` modifica a lista original. `sorted()` retorna uma cópia — prefira `sorted()` quando quiser preservar a lista original.

### Busca e contagem

```python
camadas = ['municipios', 'rodovias', 'hidrografia', 'rodovias']

'hidrografia' in camadas        # True
camadas.index('rodovias')       # 1  (índice da primeira ocorrência)
camadas.count('rodovias')       # 2
len(camadas)                    # 4
```

### Tabela resumo dos métodos

| Método | O que faz |
|---|---|
| `.append(x)` | Adiciona `x` ao final |
| `.insert(i, x)` | Insere `x` na posição `i` |
| `.extend(lst)` | Concatena `lst` ao final |
| `.remove(x)` | Remove a primeira ocorrência de `x` |
| `.pop(i)` | Remove e retorna o elemento de índice `i` (padrão: último) |
| `.sort()` | Ordena no lugar |
| `.reverse()` | Inverte a ordem no lugar |
| `.index(x)` | Retorna o índice da primeira ocorrência de `x` |
| `.count(x)` | Conta ocorrências de `x` |
| `.clear()` | Remove todos os elementos |
| `.copy()` | Retorna uma cópia rasa da lista |

---

## Iterando sobre Listas

```python
camadas = ['municipios', 'rodovias', 'hidrografia']

# Iteração simples
for camada in camadas:
    print(camada)

# Com índice — enumerate()
for i, camada in enumerate(camadas):
    print(f'{i}: {camada}')

# Dois em dois — zip()
nomes  = ['municipios', 'rodovias']
tipos  = ['Polígono', 'Linha']

for nome, tipo in zip(nomes, tipos):
    print(f'{nome} → {tipo}')
```

---

## List Comprehension

Forma concisa de criar listas a partir de iterações e condições:

```python
# Sintaxe
[<expressão> for <item> in <iterável> if <condição>]
```

```python
# Converter lista de áreas de m² para ha
areas_m2 = [15000, 83200, 4500, 210000, 9800]
areas_ha = [a / 10000 for a in areas_m2]
# [1.5, 8.32, 0.45, 21.0, 0.98]

# Filtrar apenas camadas vetoriais
todas = ['municipios.shp', 'dem.tif', 'rodovias.gpkg', 'relevo.tif']
vetoriais = [c for c in todas if not c.endswith('.tif')]
# ['municipios.shp', 'rodovias.gpkg']

# Gerar lista de nomes padronizados (sem espaços, em minúsculas)
nomes_brutos = ['  Municípios RN ', 'RODOVIAS FEDERAIS', 'hidrografia ']
nomes_ok = [n.strip().lower().replace(' ', '_') for n in nomes_brutos]
# ['municípios_rn', 'rodovias_federais', 'hidrografia']
```

💡 List comprehension substitui loops `for` + `append()` de forma mais legível e eficiente. Prefira-a para transformações simples; para lógicas complexas, mantenha o `for` convencional.

---

## Tuplas

Uma tupla é uma **sequência ordenada e imutável**, delimitada por parênteses `()`. Após criada, não é possível adicionar, remover ou alterar elementos.

```python
ponto = (-35.74, -7.22)          # (longitude, latitude)
ponto_3d = (-35.74, -7.22, 450)  # (lon, lat, altitude)
bbox = (-38.0, -8.5, -34.5, -4.0)  # (xmin, ymin, xmax, ymax)

# Tupla com um único elemento — a vírgula é obrigatória
unitaria = (42,)
```

### Acesso e fatiamento — igual às listas

```python
lon = ponto[0]     # -35.74
lat = ponto[1]     # -7.22
lon, lat = ponto   # desempacotamento
xmin, ymin, xmax, ymax = bbox
```

### Imutabilidade

```python
ponto[0] = -36.0
# TypeError: 'tuple' object does not support item assignment
```

Tuplas suportam os métodos de leitura (`.index()`, `.count()`) mas não os de modificação.

### Quando usar tupla em vez de lista?

| Situação | Estrutura recomendada |
|---|---|
| Dados que não devem mudar (coordenada de um ponto) | **Tupla** |
| Retorno de múltiplos valores de uma função | **Tupla** |
| Coleção que vai crescer ou mudar (lista de camadas) | **Lista** |
| Chave de dicionário (listas não podem ser chaves) | **Tupla** |
| Iteração simples sem modificação | Ambas |

```python
# Tupla como chave de dicionário — útil em geocodificação
elevacoes = {
    (-35.74, -7.22): 450.0,
    (-36.10, -8.01): 312.5,
}
elevacoes[(-35.74, -7.22)]  # 450.0
```

### Lista vs. Tupla — resumo

| Característica | Lista | Tupla |
|---|---|---|
| Sintaxe | `[a, b, c]` | `(a, b, c)` |
| Mutável | Sim | Não |
| Métodos de modificação | Sim | Não |
| Pode ser chave de dicionário | Não | Sim |
| Uso típico em GIS | Lista de camadas, resultados | Coordenada, bbox, par (x, y) |

---

## Exercícios

### Exercício 1

Dada a lista de camadas abaixo, escreva um programa que:

1. Exiba o total de camadas
2. Filtre e exiba apenas as camadas **vetoriais** (`.shp` e `.gpkg`)
3. Filtre e exiba apenas as camadas **raster** (`.tif`)
4. Exiba as camadas vetoriais em ordem alfabética

```python
camadas = [
    'municipios_rn.shp',
    'modelo_digital_terreno.tif',
    'rodovias_federais.gpkg',
    'uso_solo.tif',
    'hidrografia.shp',
    'ortofoto_natal.tif',
    'pontos_controle.gpkg',
]
```

---

### Exercício 2 — Contexto GIS

Você tem uma lista de pontos de amostragem no formato `(nome, longitude, latitude)`. Escreva um programa que:

1. Ordene os pontos por **latitude** (do mais ao sul para o mais ao norte)
2. Exiba os pontos ordenados com nome e coordenadas formatadas com 4 casas decimais
3. Identifique e exiba o ponto mais ao norte e o mais ao sul

```python
pontos = [
    ('P01', -35.7431, -7.2256),
    ('P02', -36.1023, -5.8012),
    ('P03', -37.0541, -8.1337),
    ('P04', -35.2198, -6.4501),
    ('P05', -36.8812, -4.9723),
]
```

---

### Exercício 3 — Contexto GIS

Use **list comprehension** para resolver os itens abaixo a partir da lista de municípios:

```python
municipios = [
    {'nome': 'Natal',        'area_km2': 167.26,  'pop': 890480,  'regiao': 'Leste'},
    {'nome': 'Mossoró',      'area_km2': 2099.33, 'pop': 295000,  'regiao': 'Oeste'},
    {'nome': 'Caicó',        'area_km2': 1228.49, 'pop': 68900,   'regiao': 'Central'},
    {'nome': 'Parnamirim',   'area_km2': 123.47,  'pop': 280000,  'regiao': 'Leste'},
    {'nome': 'Açu',          'area_km2': 1601.12, 'pop': 55500,   'regiao': 'Oeste'},
]
```

1. Crie uma lista com os **nomes** de todos os municípios
2. Crie uma lista com os municípios cuja **área seja maior que 500 km²**
3. Crie uma lista de tuplas `(nome, densidade)` com a **densidade demográfica** (hab/km²) de cada município, com 2 casas decimais
4. Filtre apenas os municípios da **região Oeste**
