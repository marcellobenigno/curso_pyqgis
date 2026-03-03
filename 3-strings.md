# 3. Strings

Uma string (`str`) é uma **sequência imutável de caracteres**. Em Python, pode ser delimitada por aspas simples, duplas ou triplas:

```python
nome_camada = 'Municípios_RN'
sistema_ref = "SIRGAS 2000"
descricao = """Camada de municípios do
Rio Grande do Norte — IBGE 2022"""
```

Strings são **imutáveis**: não é possível alterar um caractere diretamente; qualquer operação gera uma nova string.

---

## Criando e Inspecionando Strings

```python
crs = 'EPSG:4674'

type(crs)       # <class 'str'>
len(crs)        # 9
print(crs)      # EPSG:4674
```

### Aspas dentro de strings

```python
msg1 = "O arquivo 'municipios.shp' foi carregado"
msg2 = 'Sistema de referência: "SIRGAS 2000"'
msg3 = 'Caminho: C:\\Users\\geo\\dados\\'   # barra invertida com escape
msg4 = r'Caminho: C:\Users\geo\dados\'      # raw string — sem escape
```

---

## Concatenação e Repetição

```python
prefixo = 'municipios'
sufixo = '_rn'
nome_arquivo = prefixo + sufixo + '.shp'
print(nome_arquivo)  # municipios_rn.shp

separador = '-' * 30
print(separador)     # ------------------------------
```

---

## Formatação de Strings

### f-strings (recomendado — Python >= 3.6)

```python
municipio = 'Mossoró'
area_km2 = 2099.33
pop = 295000

print(f'Município: {municipio}')
print(f'Área: {area_km2:.2f} km²')        # 2 casas decimais
print(f'População: {pop:,}')               # separador de milhar
print(f'Densidade: {pop / area_km2:.1f} hab/km²')
```

Saída:
```
Município: Mossoró
Área: 2099.33 km²
População: 295,000
Densidade: 140.5 hab/km²
```

### Especificadores de formato mais usados

| Especificador | Significado | Exemplo | Saída |
|---|---|---|---|
| `:.2f` | 2 casas decimais | `f'{3.14159:.2f}'` | `3.14` |
| `:d` | Inteiro | `f'{1000:d}'` | `1000` |
| `:,` | Separador de milhar | `f'{1000000:,}'` | `1,000,000` |
| `:>10` | Alinha à direita em 10 chars | `f'{'RN':>10}'` | `'        RN'` |
| `:<10` | Alinha à esquerda em 10 chars | `f'{'RN':<10}'` | `'RN        '` |
| `:e` | Notação científica | `f'{0.00015:.2e}'` | `1.50e-04` |

### `.format()` (alternativa)

```python
print('Município: {} | Área: {:.1f} km²'.format(municipio, area_km2))
```

---

## Métodos Principais de String

Strings são objetos e possuem métodos acessados com ponto (`.`). Use `dir('texto')` para listar todos, ou `help(str.método)` para ver a documentação.

### Caso (maiúsculas/minúsculas)

```python
camada = 'Limite_Municipal_RN'

camada.upper()       # 'LIMITE_MUNICIPAL_RN'
camada.lower()       # 'limite_municipal_rn'
camada.capitalize()  # 'Limite_municipal_rn'
camada.title()       # 'Limite_Municipal_Rn'
```

### Busca e verificação

```python
epsg = 'EPSG:4674'

epsg.startswith('EPSG')   # True
epsg.endswith('4674')     # True
epsg.find('4674')         # 5  (índice onde começa)
epsg.count(':')           # 1

'EPSG' in epsg            # True  (operador in)
```

### Limpeza

```python
entrada = '  municipios_rn.shp   '

entrada.strip()    # 'municipios_rn.shp'   (remove espaços nas bordas)
entrada.lstrip()   # 'municipios_rn.shp   '
entrada.rstrip()   # '  municipios_rn.shp'
```

### Substituição e divisão

```python
nome = 'municipios_rn_2022.shp'

nome.replace('_', '-')       # 'municipios-rn-2022.shp'
nome.replace('.shp', '')     # 'municipios_rn_2022'

partes = nome.split('_')     # ['municipios', 'rn', '2022.shp']
partes[0]                    # 'municipios'
partes[-1]                   # '2022.shp'

# Juntar de volta com outro separador
'-'.join(partes)             # 'municipios-rn-2022.shp'
```

### Tabela resumo dos métodos mais usados

| Método | O que faz |
|---|---|
| `.upper()` / `.lower()` | Converte para maiúsculas / minúsculas |
| `.strip()` | Remove espaços (e `\n`) das bordas |
| `.replace(a, b)` | Substitui `a` por `b` |
| `.split(sep)` | Divide em lista usando `sep` como separador |
| `.join(lista)` | Une uma lista em string com o separador dado |
| `.startswith(s)` / `.endswith(s)` | Verifica início / fim |
| `.find(s)` | Retorna o índice da primeira ocorrência de `s` |
| `.count(s)` | Conta ocorrências de `s` |
| `.strip()` / `.lstrip()` / `.rstrip()` | Remove bordas |

---

## Fatiamento (*Slicing*)

Strings podem ser acessadas por índice. O índice começa em `0`; índices negativos contam a partir do final.

```
 E  P  S  G  :  4  6  7  4
 0  1  2  3  4  5  6  7  8
-9 -8 -7 -6 -5 -4 -3 -2 -1
```

```python
crs = 'EPSG:4674'

crs[0]      # 'E'
crs[-1]     # '4'
crs[0:4]    # 'EPSG'
crs[5:]     # '4674'   (do índice 5 até o fim)
crs[:4]     # 'EPSG'   (do início até o índice 4, exclusive)
crs[::2]    # 'EG46'   (de 2 em 2)
crs[::-1]   # '4764:GSPE'  (invertida)
```

Sintaxe geral: `string[início:fim:passo]`

💡 Slicing nunca lança erro por índice fora do intervalo — retorna o máximo possível.

---

## Strings Multilinha

```python
cabecalho = """
Relatório de Área
=================
Município: Natal
Data: 2024-01
"""
print(cabecalho)
```

---

## Exercícios

### Exercício 1

Dada a string `'   Rio Grande do Norte   '`, use métodos de string para:

1. Remover os espaços das bordas
2. Converter para maiúsculas
3. Substituir os espaços por underline (`_`)
4. Exibir o resultado: `RIO_GRANDE_DO_NORTE`

---

### Exercício 2

Solicite ao usuário um nome de arquivo (ex: `municipios_rn_2022.shp`) e exiba:

1. O nome sem a extensão
2. A extensão do arquivo
3. O nome do arquivo em maiúsculas
4. Se o arquivo é um shapefile (`True`/`False`)

Exemplo de saída:
```
Nome sem extensão: municipios_rn_2022
Extensão: .shp
Nome em maiúsculas: MUNICIPIOS_RN_2022.SHP
É shapefile? True
```

---

### Exercício 3 — Contexto GIS

Serviços WFS (Web Feature Service) recebem requisições por URL com parâmetros no formato:

```
https://servidor/wfs?SERVICE=WFS&VERSION=2.0.0&REQUEST=GetFeature&TYPENAMES=camada&SRSNAME=EPSG:XXXX&COUNT=N
```

Escreva um programa que solicite ao usuário:

1. O endereço base do servidor (ex: `https://geoserver.meu.gov.br/ows`)
2. O nome da camada (ex: `ibge:municipios_rn`)
3. O código EPSG (ex: `4674`)
4. O número máximo de feições (ex: `100`)

E construa e exiba a URL completa da requisição WFS usando f-string.

Além disso:
- Converta o nome da camada para **minúsculas** com `.lower()`
- Remova espaços extras do endereço base com `.strip()`

Exemplo de saída:
```
URL gerada:
https://geoserver.meu.gov.br/ows?SERVICE=WFS&VERSION=2.0.0&REQUEST=GetFeature&TYPENAMES=ibge:municipios_rn&SRSNAME=EPSG:4674&COUNT=100
```

---

### Exercício 4

Um arquivo de log de geoprocessamento contém linhas no seguinte formato:

```
'2024-03-15 | ERRO | reprojetar_camada | CRS de destino não informado'
'2024-03-15 | OK   | carregar_shapefile | municipios_rn.shp carregado'
'2024-03-16 | ERRO | calcular_area | Geometria inválida na feição 42'
```

Dada a string abaixo, escreva um programa que:

1. Divida a linha pelo separador `' | '`
2. Extraia e exiba separadamente: data, status, operação e mensagem
3. Verifique se o status é `'ERRO'` e, em caso afirmativo, exiba um aviso em maiúsculas

```python
linha = '2024-03-16 | ERRO | calcular_area | Geometria inválida na feição 42'
```

Saída esperada:
```
Data: 2024-03-16
Status: ERRO
Operação: calcular_area
Mensagem: Geometria inválida na feição 42
⚠ ATENÇÃO: LINHA COM ERRO DETECTADA
```

---

### Exercício 5 — Contexto GIS

Coordenadas geográficas podem ser representadas em diferentes formatos de texto. Um sistema legado exporta coordenadas no formato grau-minuto-segundo (DMS):

```
'22°54\'14"S 43°10\'21"W'
```

Escreva um programa que receba uma string no formato simplificado `'22 54 14 S'` (grau, minuto, segundo, hemisfério separados por espaço) e converta para graus decimais usando a fórmula:

```
decimal = grau + minuto/60 + segundo/3600
```

Aplique sinal negativo se o hemisfério for `'S'` ou `'W'`.

Exiba o resultado formatado com 6 casas decimais.

Exemplo de entrada e saída:
```
Coordenada DMS: 22 54 14 S
Graus decimais: -22.904000°
```
