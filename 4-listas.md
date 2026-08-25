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

1. Ordene os pontos por **latitude** (do mais ao sul para o mais ao norte) (dica: pesquise na internet sobre `key=lambda` para ordenação de listas)
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


## Exercício 4 — Painel de Camadas de um Projeto QGIS

### Contexto

Todo projeto no QGIS mantém um **painel de camadas**: uma sequência ordenada em que a posição importa. A camada do topo da lista é a primeira a ser desenhada sobre as demais — por isso pontos e rótulos ficam acima, e polígonos de base ficam abaixo. Adicionar, remover e reposicionar camadas é a operação mais rotineira de quem monta um mapa.

Você está montando o projeto **`municipio_acu.qgz`** e vai simular esse painel com uma lista Python.

```python
projeto = ['limite_municipal', 'hidrografia', 'rodovias']
```

### Tarefas

1. **Carregar novas camadas.** Adicione `'curvas_nivel'` ao final do painel com `.append()`. Exiba a lista.

2. **Reposicionar no topo.** A camada `'sede_urbana'` precisa ficar visível acima de todas. Insira-a na posição `0` com `.insert()`. Exiba a lista.

3. **Importar um pacote de camadas.** Um colega enviou duas camadas de uma vez: `['uso_solo', 'hidrografia']`. Anexe as duas ao painel usando `.extend()` — em **uma única chamada**. Exiba a lista.

4. **Auditar o painel.** Responda no terminal, usando `in`, `.count()` e `len()`:
   - A camada `'rodovias'` está carregada?
   - E a camada `'geologia'`?
   - Quantas vezes `'hidrografia'` aparece? (o `.extend()` acabou de gerar uma duplicata)
   - Quantas camadas o projeto tem no total?

5. **Remover a duplicata.** Use `.remove('hidrografia')` e exiba a lista. Observe **qual das duas ocorrências foi removida** e comente no código o motivo.

6. **Descarregar a camada do fim da fila.** Use `.pop()` sem argumento para remover a última camada, guarde o valor retornado em uma variável e exiba a mensagem `Camada descarregada: <nome>`.

7. **Localizar uma camada.** Use `.index('rodovias')` para descobrir em que posição do painel ela está e exiba `'rodovias' está na posição N`.

### Saída esperada (parcial)

```
1. Após .append():   ['limite_municipal', 'hidrografia', 'rodovias', 'curvas_nivel']
2. Após .insert(0):  ['sede_urbana', 'limite_municipal', 'hidrografia', 'rodovias', 'curvas_nivel']
3. Após .extend():   ['sede_urbana', 'limite_municipal', 'hidrografia', 'rodovias', 'curvas_nivel', 'uso_solo', 'hidrografia']

4. 'rodovias' carregada?  True
   'geologia' carregada?  False
   Ocorrências de 'hidrografia': 2
   Total de camadas: 7

5. Após .remove():   ['sede_urbana', 'limite_municipal', 'rodovias', 'curvas_nivel', 'uso_solo', 'hidrografia']
6. Camada descarregada: hidrografia
7. 'rodovias' está na posição 2
```

### Desafio

Depois de tudo, inverta a ordem de desenho do projeto com `.reverse()` e exiba o painel resultante. Em uma linha de comentário, explique o que aconteceria visualmente no mapa.

---

## Exercício 5 — Rede de Marcos Geodésicos

### Contexto

Um **marco geodésico** é um ponto materializado no terreno com coordenadas conhecidas, usado como referência para levantamentos topográficos. Cada marco é descrito por uma **tupla** `(codigo, longitude, latitude, altitude_m)` — e tupla é a estrutura certa aqui: uma vez homologado pelo IBGE, o marco **não muda**; alterar uma coordenada individualmente seria um erro grave.

O conjunto de marcos, por outro lado, é uma **lista**: cresce a cada campanha de campo e precisa ser ordenado para relatório.

```python
marcos = [
    ('RN-004', -35.2098, -5.7942,  48.30),
    ('RN-001', -37.0541, -8.1337, 210.55),
    ('RN-003', -36.1023, -5.8012, 122.10),
    ('RN-002', -35.7431, -7.2256,  87.44),
]
```

### Tarefas

1. **Ordenar por código.** Use `.sort()`. Como o primeiro elemento de cada tupla é o código, a ordenação padrão já resolve — não é necessário nenhum recurso adicional.

2. **Emitir a caderneta de campo.** Percorra a lista com `enumerate()` e, dentro do laço, **desempacote a tupla** (`codigo, lon, lat, alt = marco`). Exiba uma tabela alinhada com 4 casas decimais para as coordenadas e 2 para a altitude.

3. **Inverter a listagem.** Aplique `.reverse()` e exiba apenas os códigos, do último para o primeiro. Em seguida ordene novamente em ordem crescente com `.sort()`.

4. **Consultar um marco.** Crie a lista de códigos com list comprehension (`codigos = [m[0] for m in marcos]`), use `.index('RN-003')` para achar a posição e exiba a **tupla completa** desse marco acessando `marcos[posicao]`.

5. **Extremos da rede.** Com a lista já ordenada por código, exiba o **primeiro** e o **último** marco usando `marcos[0]` e `marcos[-1]`.

6. **Amplitude altimétrica.** Extraia as altitudes com list comprehension, ordene essa nova lista com `.sort()` e exiba a menor (`[0]`) e a maior (`[-1]`). Calcule e exiba a diferença entre elas.

### Saída esperada (parcial)

```
2. Caderneta de campo:
 #  | Código   |  Longitude |  Latitude | Altitude
 0  | RN-001   |   -37.0541 |   -8.1337 |  210.55 m
 1  | RN-002   |   -35.7431 |   -7.2256 |   87.44 m
 2  | RN-003   |   -36.1023 |   -5.8012 |  122.10 m
 3  | RN-004   |   -35.2098 |   -5.7942 |   48.30 m

3. Ordem invertida: ['RN-004', 'RN-003', 'RN-002', 'RN-001']

4. RN-003 está na posição 2 → ('RN-003', -36.1023, -5.8012, 122.1)

5. Primeiro marco: RN-001   |  Último marco: RN-004

6. Altitude mínima : 48.30 m
   Altitude máxima : 210.55 m
   Amplitude       : 162.25 m
```

### Desafio

Tente executar `marcos[0][3] = 50.0` para "corrigir" a altitude do primeiro marco. Registre em um comentário o erro que o Python devolve e explique, em uma frase, por que a imutabilidade da tupla é **desejável** no cadastro de um marco geodésico.

---

## Exercício 6 — Inventário de um Diretório de Dados Geoespaciais

### Contexto

Antes de publicar um geosserviço, o analista precisa **inventariar o acervo**: separar o que é vetorial (`.shp`, `.gpkg`) do que é matricial (`.tif`), conferir a geometria de cada camada e contar feições. Aqui as informações chegam em **listas paralelas** — a i-ésima posição de cada lista descreve a mesma camada. É exatamente o cenário em que `zip()` existe para resolver.

```python
arquivos = [
    'municipios_rn.shp',
    'modelo_digital_terreno.tif',
    'rodovias_federais.gpkg',
    'uso_solo_2024.tif',
    'hidrografia_trechos.shp',
    'ortofoto_natal.tif',
    'pontos_controle.gpkg',
    'setores_censitarios.shp',
]

geometrias = ['Polígono', 'Raster', 'Linha', 'Raster', 'Linha', 'Raster', 'Ponto', 'Polígono']

feicoes    = [167, 1, 4312, 1, 2890, 1, 58, 3613]
```

### Tarefas

1. **Amostrar o acervo com fatiamento.** Exiba:
   - as **3 primeiras** camadas — `arquivos[:3]`
   - as **2 últimas** camadas — `arquivos[-2:]`
   - as camadas de **índice par** — `arquivos[::2]`

2. **Separar raster de vetor.** Com list comprehension e `.endswith('.tif')`, crie e exiba duas listas: `rasters` e `vetoriais`.

3. **Padronizar nomes para o catálogo.** Com list comprehension, gere a lista `nomes_catalogo` removendo as extensões (`.replace()` encadeado) e convertendo para maiúsculas (`.upper()`).
   Exemplo: `'municipios_rn.shp'` → `'MUNICIPIOS_RN'`.

4. **Emitir o relatório do inventário.** Percorra as **três listas ao mesmo tempo** com `zip()` e imprima uma tabela alinhada com arquivo, geometria e número de feições.

5. **Filtrar durante o pareamento.** Com list comprehension sobre `zip(arquivos, geometrias)`, monte a lista `pares_vetoriais` contendo apenas as tuplas `(arquivo, geometria)` cuja geometria **não** seja `'Raster'`. Exiba as tuplas, uma por linha.

6. **Contabilizar por tipo de geometria.** Use `.count()` sobre `geometrias` para exibir quantas camadas são Polígono, Linha, Ponto e Raster. Confira se a soma bate com `len(geometrias)`.

### Saída esperada (parcial)

```
1. Três primeiras : ['municipios_rn.shp', 'modelo_digital_terreno.tif', 'rodovias_federais.gpkg']
   Duas últimas   : ['pontos_controle.gpkg', 'setores_censitarios.shp']
   Índices pares  : ['municipios_rn.shp', 'rodovias_federais.gpkg', 'hidrografia_trechos.shp', 'pontos_controle.gpkg']

2. Rasters   : ['modelo_digital_terreno.tif', 'uso_solo_2024.tif', 'ortofoto_natal.tif']
   Vetoriais : ['municipios_rn.shp', 'rodovias_federais.gpkg', 'hidrografia_trechos.shp', 'pontos_controle.gpkg', 'setores_censitarios.shp']

4. Inventário:
municipios_rn.shp            | Polígono  |   167
modelo_digital_terreno.tif   | Raster    |     1
rodovias_federais.gpkg       | Linha     |  4312
uso_solo_2024.tif            | Raster    |     1
hidrografia_trechos.shp      | Linha     |  2890
ortofoto_natal.tif           | Raster    |     1
pontos_controle.gpkg         | Ponto     |    58
setores_censitarios.shp      | Polígono  |  3613

6. Polígono: 2 | Linha: 2 | Ponto: 1 | Raster: 3  (total: 8)
```

### Desafio

Monte com list comprehension a lista `feicoes_vetoriais`, contendo o número de feições **apenas** das camadas vetoriais (use `zip(feicoes, geometrias)` com um `if`). Depois percorra essa lista com um `for` acumulando o total em uma variável e exiba:

```
Feições vetoriais: [167, 4312, 2890, 58, 3613]
Total de feições vetoriais: 11040
```

---

## Consulta rápida

| Preciso de… | Recurso |
|---|---|
| Adicionar uma camada ao final | `.append(x)` |
| Colocar uma camada no topo | `.insert(0, x)` |
| Anexar várias de uma vez | `.extend(lista)` |
| Tirar uma camada pelo nome | `.remove(x)` |
| Tirar e aproveitar o valor | `.pop()` / `.pop(i)` |
| Ordenar a lista no lugar | `.sort()` / `.reverse()` |
| Saber onde está / quantas vezes | `.index(x)` / `.count(x)` |
| Verificar se existe / tamanho | `x in lista` / `len(lista)` |
| Pegar um pedaço da lista | `lista[:3]`, `lista[-2:]`, `lista[::2]` |
| Iterar com a posição | `for i, item in enumerate(lista)` |
| Iterar em listas paralelas | `for a, b in zip(lista1, lista2)` |
| Transformar ou filtrar | `[expr for x in lista if cond]` |
| Abrir uma tupla em variáveis | `cod, lon, lat, alt = marco` |

3. Crie uma lista de tuplas `(nome, densidade)` com a **densidade demográfica** (hab/km²) de cada município, com 2 casas decimais
4. Filtre apenas os municípios da **região Oeste**
