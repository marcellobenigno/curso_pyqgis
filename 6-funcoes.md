# 6. Funções

Uma **função** é um bloco de código nomeado e reutilizável que executa uma tarefa específica. Funções organizam o programa em partes menores, evitam repetição e facilitam a manutenção.

---

## Definição e Chamada

```python
def nome_da_funcao(parametros):
    """Docstring opcional."""
    # corpo
    return valor
```

- `def` — palavra-chave para criar a função
- Parâmetros são opcionais
- `return` é opcional; sem ele a função retorna `None`

```python
def area_retangulo(base, altura):
    return base * altura

area_retangulo(300, 150)  # 45000
```

---

## Parâmetros e Argumentos

**Parâmetro** → nome na definição. **Argumento** → valor na chamada.

### Posicionais e nomeados

```python
def reprojetar(camada, crs_origem, crs_destino):
    print(f'Reprojetando {camada}: {crs_origem} → {crs_destino}')

reprojetar('municipios', 'EPSG:4674', 'EPSG:32724')   # posicionais
reprojetar('municipios', crs_destino='EPSG:32724', crs_origem='EPSG:4674')  # nomeados
```

### Valores padrão

```python
def buffer(geometria, distancia_m, dissolve=False, quadrant_segs=16):
    print(f'Buffer de {distancia_m} m | dissolve={dissolve} | segs={quadrant_segs}')

buffer('parque', 500)                   # dissolve=False, quadrant_segs=16
buffer('parque', 500, dissolve=True)    # quadrant_segs=16 mantido
buffer('parque', 500, quadrant_segs=8)  # dissolve=False mantido
```

💡 Parâmetros com valor padrão devem vir **depois** dos obrigatórios na definição.

### Retornando múltiplos valores

```python
def bbox(pontos):
    """Retorna (xmin, ymin, xmax, ymax) de uma lista de pontos (x, y)."""
    xs = [p[0] for p in pontos]
    ys = [p[1] for p in pontos]
    return min(xs), min(ys), max(xs), max(ys)

xmin, ymin, xmax, ymax = bbox([(-36.1, -7.2), (-35.4, -8.1), (-37.0, -6.5)])
print(xmin, ymin, xmax, ymax)  # -37.0 -8.1 -35.4 -6.5
```

---

## `*args` e `**kwargs`

Usados quando o número de argumentos não é conhecido antecipadamente.

### `*args` — argumentos posicionais variáveis

Empacota argumentos extras em uma **tupla**.

```python
def media_ponderada(*valores):
    """Calcula a média de N valores."""
    return sum(valores) / len(valores)

media_ponderada(7.5, 8.0, 9.0)        # 8.166...
media_ponderada(6.0, 7.0, 8.0, 9.0)  # 7.5
```

### `**kwargs` — argumentos nomeados variáveis

Empacota argumentos nomeados extras em um **dicionário**.

```python
def criar_camada(nome, **metadados):
    """Cria uma camada com metadados opcionais."""
    print(f'Camada: {nome}')
    for chave, valor in metadados.items():
        print(f'  {chave}: {valor}')

criar_camada('municipios_rn', crs='EPSG:4674', tipo='Polígono', feicoes=167)
```

---

## Docstrings

Documentam a função com uma string logo após `def`. Acessível via `help()` ou `.__doc__`.

```python
def graus_para_radianos(graus):
    """
    Converte um ângulo de graus decimais para radianos.

    Parâmetros
    ----------
    graus : float
        Ângulo em graus decimais.

    Retorna
    -------
    float
        Ângulo em radianos.
    """
    import math
    return graus * (math.pi / 180)

help(graus_para_radianos)
graus_para_radianos(180)  # 3.14159...
```

---

## Escopo de Variáveis

Variáveis criadas dentro de uma função são **locais** — não existem fora dela.

```python
FATOR_M2_HA = 10000   # constante global

def converter_area(area_m2):
    area_ha = area_m2 / FATOR_M2_HA  # lê a global, não altera
    return area_ha

converter_area(55000)   # 5.5
print(area_ha)          # NameError: 'area_ha' não existe fora da função
```

Use `global` apenas quando for estritamente necessário alterar uma variável global — em geral, prefira retornar o valor.

```python
contador = 0

def registrar_feicao():
    global contador
    contador += 1

registrar_feicao()
registrar_feicao()
print(contador)  # 2
```

---

## Funções Lambda (Anônimas)

Funções de uma linha, sem nome, usadas em expressões simples.

```python
# Sintaxe
lambda <parâmetros>: <expressão>
```

```python
m2_para_ha = lambda x: x / 10000
m2_para_ha(75000)   # 7.5

# Ordenar lista de pontos pela latitude (índice 1)
pontos = [('P1', -35.7, -7.2), ('P2', -36.1, -5.8), ('P3', -37.0, -8.1)]
pontos_ord = sorted(pontos, key=lambda p: p[2])
# [('P3', -37.0, -8.1), ('P1', -35.7, -7.2), ('P2', -36.1, -5.8)]

# Extrair campo de lista de dicionários
camadas = [{'nome': 'rodovias', 'feicoes': 4312}, {'nome': 'municipios', 'feicoes': 167}]
camadas.sort(key=lambda c: c['feicoes'], reverse=True)
```

💡 Lambda é útil como argumento de `sorted()`, `map()` e `filter()`. Para lógicas mais complexas, use `def`.

---

## Exercícios

### Exercício 1 — Contexto GIS

Escreva uma função `dd_para_dms(graus_decimais)` que converta coordenadas de **graus decimais** para o formato **grau°minuto'segundo"** e retorne uma string formatada.

Fórmula:
```
grau  = int(abs(decimal))
resto = (abs(decimal) - grau) * 60
min   = int(resto)
seg   = (resto - min) * 60
```

Aplique o sinal negativo ao símbolo do hemisfério (`S`/`N` para latitude, `W`/`E` para longitude).

Exemplos de saída:
```python
dd_para_dms(-7.2256)   # "7°13'32.16\"S"
dd_para_dms(-35.7431)  # "35°44'35.16\"W"
```

---

### Exercício 2 — Contexto GIS

Escreva uma função `distancia_euclidiana(p1, p2)` que calcule a distância entre dois pontos `(x, y)` em um plano cartesiano (coordenadas projetadas em metros).

```
d = sqrt((x2 - x1)² + (y2 - y1)²)
```

Em seguida, escreva uma segunda função `ponto_mais_proximo(referencia, pontos)` que, dado um ponto de referência e uma lista de pontos, retorne o **ponto mais próximo** usando `distancia_euclidiana` e `min()` com `key=`.

Exemplo:
```python
base   = (290000, 9195000)
pontos = [(291200, 9196500), (289500, 9194200), (292000, 9193000)]

ponto_mais_proximo(base, pontos)  # (289500, 9194200)
```

---

### Exercício 3 — Contexto GIS

Escreva uma função `validar_arquivo_vetor(caminho)` que receba um caminho de arquivo como string e retorne um dicionário com o resultado da validação:

- `'valido'`: `True` ou `False`
- `'extensao'`: a extensão encontrada
- `'mensagem'`: descrição do resultado

Extensões vetoriais aceitas: `.shp`, `.gpkg`, `.geojson`, `.kml`, `.gml`

```python
validar_arquivo_vetor('dados/municipios_rn.shp')
# {'valido': True, 'extensao': '.shp', 'mensagem': 'Formato vetorial suportado'}

validar_arquivo_vetor('imagens/relevo.tif')
# {'valido': False, 'extensao': '.tif', 'mensagem': 'Extensão não suportada'}

validar_arquivo_vetor('relatorio')
# {'valido': False, 'extensao': '', 'mensagem': 'Arquivo sem extensão'}
```

---

### Exercício 4 — Contexto GIS

Escreva uma função `classificar_declividade(graus)` que classifique a declividade conforme a tabela EMBRAPA e retorne a classe como string. Depois, use `map()` com **lambda** para classificar uma lista inteira de valores de declividade de uma só vez.

| Faixa (graus) | Classe |
|---|---|
| 0 – 3 | Plano |
| 3 – 8 | Suave ondulado |
| 8 – 20 | Ondulado |
| 20 – 45 | Forte ondulado |
| > 45 | Montanhoso / Escarpado |

```python
amostras = [1.2, 5.7, 14.3, 32.0, 51.5, 8.0, 2.9]

# Usar map() + lambda para aplicar a função à lista inteira
resultados = list(map(lambda d: classificar_declividade(d), amostras))
```

---

### Exercício 5 — Contexto GIS

Escreva uma função `resumo_camada(nome, **atributos)` que use `**kwargs` para receber metadados opcionais de uma camada e exiba um relatório formatado. A função deve:

1. Exibir o nome da camada como cabeçalho
2. Iterar sobre os metadados e exibir cada par `chave: valor`
3. Se `'feicoes'` e `'area_total_km2'` estiverem presentes, calcular e exibir a densidade de feições

```python
resumo_camada(
    'municipios_rn',
    tipo='Polígono',
    crs='EPSG:4674',
    feicoes=167,
    area_total_km2=52811.0,
    encoding='UTF-8',
)
```

Saída esperada:
```
=== municipios_rn ===
tipo           : Polígono
crs            : EPSG:4674
feicoes        : 167
area_total_km2 : 52811.0
encoding       : UTF-8
densidade      : 0.0032 feições/km²
```

---

### Exercício 6 — Contexto GIS

Escreva uma função `snap_para_grade(lon, lat, resolucao=0.5)` que "encaixe" um par de coordenadas geográficas na grade regular mais próxima com a resolução dada.

A lógica de arredondamento para a grade é:
```
valor_grade = round(valor / resolucao) * resolucao
```

Use `resolucao` como parâmetro com **valor padrão** de `0.5` grau.

Em seguida, use **list comprehension** com a função para processar uma lista de pontos:

```python
pontos = [
    ('P1', -35.73, -7.22),
    ('P2', -36.18, -5.89),
    ('P3', -37.04, -8.13),
]

# Resultado esperado com resolucao=0.5:
# [('P1', -36.0, -7.0), ('P2', -36.0, -6.0), ('P3', -37.0, -8.0)]
```

Exiba os pontos originais e os pontos ajustados lado a lado.
