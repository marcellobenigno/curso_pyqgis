# 8. Laços de Repetição

Laços permitem **executar um bloco de código repetidamente**, seja um número fixo de vezes ou enquanto uma condição for verdadeira.

---

## `for` com `range()`

`range()` gera uma sequência de inteiros sem criar uma lista em memória.

```python
range(n)         # 0, 1, ..., n-1
range(a, b)      # a, a+1, ..., b-1
range(a, b, step)# a, a+step, ..., até b (exclusive)
```

```python
# Processar 5 feições
for i in range(5):
    print(f'Feição {i}')         # 0, 1, 2, 3, 4

# Zonas UTM do Brasil (18 a 25)
for zona in range(18, 26):
    print(f'UTM Zona {zona}S')   # 18S, 19S, ..., 25S

# Escala descendente de 10.000 em 10.000
for escala in range(100000, 0, -10000):
    print(f'1:{escala}')         # 1:100000, 1:90000, ..., 1:10000
```

---

## `for` sobre Sequências

### Listas

```python
camadas = ['municipios', 'rodovias', 'hidrografia', 'curvas_nivel']

for camada in camadas:
    print(f'Carregando: {camada}')
```

### Strings

```python
epsg = 'EPSG:4674'

for char in epsg:
    print(char)       # E, P, S, G, :, 4, 6, 7, 4
```

### Dicionários

```python
metadados = {'nome': 'municipios_rn', 'tipo': 'Polígono', 'feicoes': 167}

for chave, valor in metadados.items():
    print(f'{chave:10}: {valor}')
```

---

## `enumerate()` — índice + valor

Retorna pares `(índice, elemento)`. Evita o padrão `for i in range(len(lista))`.

```python
municipios = ['Natal', 'Mossoró', 'Caicó', 'Parnamirim', 'Açu']

for i, nome in enumerate(municipios):
    print(f'{i+1:>2}. {nome}')
```

Saída:
```
 1. Natal
 2. Mossoró
 3. Caicó
 4. Parnamirim
 5. Açu
```

```python
# Iniciar contagem em outro valor
for i, nome in enumerate(municipios, start=100):
    print(f'ID {i}: {nome}')    # ID 100: Natal, ID 101: Mossoró, ...
```

---

## `zip()` — iteração paralela

Combina dois ou mais iteráveis elemento a elemento.

```python
nomes = ['P01', 'P02', 'P03']
lons  = [-35.74, -36.10, -37.05]
lats  = [-7.22,  -5.80,  -8.13]

for nome, lon, lat in zip(nomes, lons, lats):
    print(f'{nome}: ({lon:.4f}, {lat:.4f})')
```

```python
# Criar lista de dicionários com zip
pontos = [
    {'nome': n, 'lon': x, 'lat': y}
    for n, x, y in zip(nomes, lons, lats)
]
```

💡 `zip()` para no iterável mais curto. Use `itertools.zip_longest()` se precisar percorrer o mais longo.

---

## `while` — condição de parada

Executa enquanto a condição for `True`.

```python
tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    epsg = input('Digite o código EPSG (ex: 4674): ').strip()
    if epsg.isdigit():
        print(f'EPSG:{epsg} aceito.')
        break
    tentativas += 1
    print(f'Entrada inválida. Tentativa {tentativas}/{max_tentativas}')
else:
    # Executado se o while terminar sem break
    print('Número máximo de tentativas atingido.')
```

### `break` — interrompe o laço

```python
camadas = ['municipios', 'rodovias', None, 'hidrografia']

for camada in camadas:
    if camada is None:
        print('Camada inválida encontrada — interrompendo.')
        break
    print(f'Processando: {camada}')
```

### `continue` — pula para a próxima iteração

```python
arquivos = ['mapa.shp', 'foto.tif', 'notas.txt', 'rios.gpkg', 'lixo.bak']
vetoriais = ['.shp', '.gpkg', '.geojson']

for arq in arquivos:
    ext = '.' + arq.split('.')[-1]
    if ext not in vetoriais:
        continue              # ignora não-vetoriais
    print(f'Vetorial encontrado: {arq}')
```

### `pass` — bloco vazio (placeholder)

```python
for camada in camadas:
    if camada is None:
        pass    # TODO: registrar no log
    else:
        print(f'OK: {camada}')
```

---

## Laços Aninhados

```python
zonas = [23, 24, 25]
hemisferios = ['N', 'S']

for zona in zonas:
    for hem in hemisferios:
        epsg = 32600 + zona if hem == 'N' else 32700 + zona
        print(f'UTM {zona}{hem} → EPSG:{epsg}')
```

```python
# Grade de pontos regulares (lon/lat)
lons = [-38.0, -37.0, -36.0, -35.0]
lats = [-8.0, -7.0, -6.0, -5.0]

grade = [(lon, lat) for lat in lats for lon in lons]
print(f'{len(grade)} pontos na grade')   # 16 pontos
```

---

## Tabela Comparativa: `for` vs `while`

| Critério | `for` | `while` |
|---|---|---|
| Quando usar | Número de iterações conhecido | Condição de parada dinâmica |
| Iterável necessário | Sim | Não |
| Risco de loop infinito | Não | Sim (se condição nunca for `False`) |
| Uso típico | Listas, ranges, dicionários | Aguardar entrada, polling, retry |
| Exemplo GIS | Iterar feições de uma camada | Aguardar carregamento de tile |

---

## Exercícios

### Exercício 1

Dada a lista de feições simuladas abaixo, use `for` com `enumerate()` para:

1. Exibir cada feição com seu índice iniciando em 1
2. Calcular e exibir a área total somada de todas as feições
3. Identificar e exibir a feição com maior área

```python
feicoes = [
    {'id': 1, 'municipio': 'Natal',        'area_km2': 167.3},
    {'id': 2, 'municipio': 'Mossoró',      'area_km2': 2099.3},
    {'id': 3, 'municipio': 'Caicó',        'area_km2': 1228.5},
    {'id': 4, 'municipio': 'Parnamirim',   'area_km2': 123.5},
    {'id': 5, 'municipio': 'Açu',          'area_km2': 1601.1},
]
```

---

### Exercício 2 — Contexto GIS

Use `zip()` para combinar as três listas abaixo e gerar um relatório de pontos de controle. Em seguida, use um laço `while` para solicitar ao usuário que filtre os pontos com altitude acima de um valor informado, exibindo apenas os que atendem ao critério.

```python
nomes     = ['PC-01', 'PC-02', 'PC-03', 'PC-04', 'PC-05']
coords    = [(-35.74, -7.22), (-36.10, -5.80), (-37.05, -8.13),
             (-35.22, -6.45), (-36.88, -4.97)]
altitudes = [45.2, 312.8, 189.4, 78.1, 520.6]
```

---

### Exercício 3 — Contexto GIS

Use laços aninhados para gerar uma **grade de pontos regulares** sobre o estado do RN (bounding box aproximada: lon de -38,0 a -35,0; lat de -6,5 a -4,5), com espaçamento de 0,5 grau.

1. Gere a grade com list comprehension ou laços aninhados
2. Exiba o total de pontos gerados
3. Filtre e exiba apenas os pontos com longitude menor que -36,5 (porção oeste)
4. Use `continue` para ignorar o ponto central aproximado `(-36.5, -5.5)`

