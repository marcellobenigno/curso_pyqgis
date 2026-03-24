# 5. Dicionários

Um dicionário (`dict`) é uma coleção de pares **chave → valor**, não ordenada por inserção¹, mutável e sem chaves duplicadas. É ideal para representar objetos com atributos nomeados — como feições geográficas.

¹ *A partir do Python 3.7 a ordem de inserção é preservada.*

```python
municipio = {
    'nome':     'Mossoró',
    'uf':       'RN',
    'area_km2': 2099.33,
    'pop':      295000,
    'capital':  False,
}
```

Chaves podem ser qualquer tipo **imutável** (`str`, `int`, `float`, `tuple`). Valores podem ser qualquer tipo, inclusive outros dicionários ou listas.

---

## Criação

```python
# Literal
ponto = {'id': 1, 'lon': -35.74, 'lat': -7.22}

# dict() com argumentos nomeados
ponto = dict(id=1, lon=-35.74, lat=-7.22)

# Dicionário vazio
metadados = {}
```

---

## Acesso e Modificação

```python
municipio = {'nome': 'Natal', 'area_km2': 167.26, 'pop': 890480}

# Leitura por chave
municipio['nome']          # 'Natal'

# .get() — retorna None (ou padrão) se a chave não existir
municipio.get('crs')           # None
municipio.get('crs', 'EPSG:4674')  # 'EPSG:4674'  (valor padrão)

# Adicionar ou alterar
municipio['crs'] = 'EPSG:4674'
municipio['pop'] = 903804

# Remover
del municipio['crs']
removido = municipio.pop('pop')   # remove e retorna o valor
```

💣 Acessar uma chave inexistente com `[]` lança `KeyError`. Prefira `.get()` quando a chave puder não existir.

---

## Métodos Principais

```python
camada = {'nome': 'municipios', 'tipo': 'Polígono', 'feicoes': 167, 'crs': 'EPSG:4674'}

camada.keys()     # dict_keys(['nome', 'tipo', 'feicoes', 'crs'])
camada.values()   # dict_values(['municipios', 'Polígono', 167, 'EPSG:4674'])
camada.items()    # dict_items([('nome', 'municipios'), ('tipo', 'Polígono'), ...])

# Mesclar outro dicionário (chaves existentes são sobrescritas)
camada.update({'feicoes': 170, 'encoding': 'UTF-8'})

# Verificar existência de chave
'crs' in camada          # True
'escala' in camada       # False

# Tamanho
len(camada)              # 5
```

### Tabela resumo dos métodos

| Método | O que faz |
|---|---|
| `.keys()` | Retorna as chaves |
| `.values()` | Retorna os valores |
| `.items()` | Retorna pares `(chave, valor)` |
| `.get(k, padrão)` | Retorna o valor de `k` ou `padrão` se não existir |
| `.update(d)` | Mescla `d` no dicionário (sobrescreve chaves iguais) |
| `.pop(k)` | Remove e retorna o valor de `k` |
| `.setdefault(k, v)` | Define `k=v` apenas se `k` não existir |
| `.clear()` | Remove todos os itens |
| `.copy()` | Retorna uma cópia rasa |

---

## Iteração

```python
camada = {'nome': 'rodovias', 'tipo': 'Linha', 'feicoes': 4312}

# Iterar sobre chaves (padrão)
for chave in camada:
    print(chave)

# Iterar sobre valores
for valor in camada.values():
    print(valor)

# Iterar sobre pares chave-valor (forma mais comum)
for chave, valor in camada.items():
    print(f'{chave}: {valor}')
```

Saída do último exemplo:
```
nome: rodovias
tipo: Linha
feicoes: 4312
```
---

## Dicionários Aninhados

Um valor pode ser outro dicionário, permitindo estruturas hierárquicas:

```python
shapefile = {
    'nome': 'municipios_rn',
    'geometria': 'Polígono',
    'crs': {
        'codigo': 4674,
        'nome': 'SIRGAS 2000',
        'tipo': 'geográfico',
    },
    'bbox': {
        'xmin': -38.00,
        'ymin': -8.00,
        'xmax': -34.97,
        'ymax': -4.49,
    },
    'campos': ['cd_mun', 'nm_mun', 'area_km2', 'pop_2022'],
}

# Acessar valores aninhados
shapefile['crs']['nome']        # 'SIRGAS 2000'
shapefile['bbox']['xmin']       # -38.0
shapefile['campos'][0]          # 'cd_mun'
```

### Lista de dicionários — padrão comum em GIS

```python
feicoes = [
    {'id': 1, 'municipio': 'Natal',      'area_km2': 167.26},
    {'id': 2, 'municipio': 'Mossoró',    'area_km2': 2099.33},
    {'id': 3, 'municipio': 'Parnamirim', 'area_km2': 123.47},
]

# Acessar um atributo de uma feição específica
feicoes[1]['municipio']   # 'Mossoró'

# Iterar e exibir
for f in feicoes:
    print(f'{f["id"]:>2} | {f["municipio"]:<12} | {f["area_km2"]:>8.2f} km²')
```

---

## Exercícios

### Exercício 1 — Contexto GIS

Represente os atributos de uma feição geográfica (ponto de controle topográfico) como dicionário e escreva um programa que:

1. Crie um dicionário com os campos: `id`, `nome`, `longitude`, `latitude`, `altitude_m`, `datum`, `metodo_levantamento`
2. Exiba cada atributo no formato `campo: valor`
3. Atualize a altitude com um novo valor informado pelo usuário
4. Adicione um novo campo `data_coleta` com a data atual (`'2024-03-15'`)
5. Exiba o dicionário atualizado

---

### Exercício 2 — Contexto GIS

Dada a lista de camadas abaixo, use **dict comprehension** para criar:

1. Um dicionário `{nome_camada: tipo_geometria}`
2. Um dicionário `{nome_camada: quantidade_feicoes}` apenas para camadas com mais de 100 feições
3. Um dicionário `{nome_camada: crs}` apenas para camadas com CRS `'EPSG:4674'`

```python
camadas = [
    {'nome': 'municipios_rn',   'tipo': 'Polígono', 'feicoes': 167,   'crs': 'EPSG:4674'},
    {'nome': 'rodovias_br',     'tipo': 'Linha',    'feicoes': 4312,  'crs': 'EPSG:4674'},
    {'nome': 'capitais_br',     'tipo': 'Ponto',    'feicoes': 26,    'crs': 'EPSG:4326'},
    {'nome': 'biomas_brasil',   'tipo': 'Polígono', 'feicoes': 6,     'crs': 'EPSG:4674'},
    {'nome': 'estacoes_hidro',  'tipo': 'Ponto',    'feicoes': 891,   'crs': 'EPSG:4326'},
]
```

---

### Exercício 3 — Contexto GIS

Você recebeu metadados de três shapefiles em dicionários separados. Escreva um programa que:

1. Mescle os dicionários de metadados base e metadados de qualidade em um único dicionário por shapefile usando `.update()`
2. Calcule e adicione ao dicionário final a chave `densidade_feicoes` (feições por km²)
3. Exiba um relatório formatado para cada shapefile

```python
metadados_base = [
    {'nome': 'municipios_rn', 'feicoes': 167, 'area_total_km2': 52811.0},
    {'nome': 'distritos_rn',  'feicoes': 228, 'area_total_km2': 52811.0},
    {'nome': 'setores_rn',    'feicoes': 3613, 'area_total_km2': 52811.0},
]

metadados_qualidade = [
    {'crs': 'EPSG:4674', 'encoding': 'UTF-8',   'geometrias_invalidas': 0},
    {'crs': 'EPSG:4674', 'encoding': 'UTF-8',   'geometrias_invalidas': 3},
    {'crs': 'EPSG:4674', 'encoding': 'Latin-1', 'geometrias_invalidas': 12},
]
```

Saída esperada (exemplo para o primeiro):
```
--- municipios_rn ---
feicoes             : 167
area_total_km2      : 52811.0
crs                 : EPSG:4674
encoding            : UTF-8
geometrias_invalidas: 0
densidade_feicoes   : 0.0032 feições/km²
```
