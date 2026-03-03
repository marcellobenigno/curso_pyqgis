# 10. Leitura e Escrita de Arquivos

Trabalhar com arquivos é fundamental em geoprocessamento: leitura de tabelas de coordenadas, escrita de relatórios, varredura de diretórios em busca de shapefiles. Python oferece recursos nativos para tudo isso.

---

## Abrindo Arquivos com `open()`

```python
f = open('caminho/arquivo.txt', 'r', encoding='utf-8')
# ... operações ...
f.close()
```

| Modo | Significado |
|---|---|
| `'r'` | Leitura (padrão) — erro se não existir |
| `'w'` | Escrita — cria ou **sobrescreve** |
| `'a'` | Append — cria ou adiciona ao final |
| `'x'` | Cria — erro se já existir |
| `'rb'` / `'wb'` | Leitura / escrita em modo binário |

---

## Context Manager — `with open()`

O `with` fecha o arquivo automaticamente ao sair do bloco, mesmo se ocorrer uma exceção. **Prefira sempre esta forma.**

```python
with open('municipios.txt', 'r', encoding='utf-8') as f:
    conteudo = f.read()
# arquivo fechado automaticamente aqui
```

---

## Leitura

```python
# read() — lê o arquivo inteiro como string
with open('relatorio.txt', 'r', encoding='utf-8') as f:
    texto = f.read()

# readline() — lê uma linha por vez
with open('coordenadas.txt', 'r', encoding='utf-8') as f:
    primeira = f.readline()     # 'nome,lon,lat\n'
    segunda  = f.readline()     # 'P01,-35.74,-7.22\n'

# readlines() — retorna lista com todas as linhas
with open('coordenadas.txt', 'r', encoding='utf-8') as f:
    linhas = f.readlines()      # ['\n', 'P01,-35.74,-7.22\n', ...]

# Iterar linha a linha (mais eficiente para arquivos grandes)
with open('coordenadas.txt', 'r', encoding='utf-8') as f:
    for linha in f:
        print(linha.strip())
```

---

## Escrita

```python
# write() — escreve uma string
with open('log.txt', 'w', encoding='utf-8') as f:
    f.write('Início do processamento\n')
    f.write('Camadas carregadas: 3\n')

# writelines() — escreve uma lista de strings
linhas = ['Natal,-35.20,-5.79\n', 'Mossoró,-37.34,-5.19\n']
with open('saida.txt', 'w', encoding='utf-8') as f:
    f.writelines(linhas)

# Modo append — adiciona sem apagar
with open('log.txt', 'a', encoding='utf-8') as f:
    f.write('Processamento concluído.\n')
```

---

## Módulo `csv`

Ideal para ler/escrever tabelas de atributos e listas de coordenadas.

### Leitura

```python
import csv

with open('pontos.csv', 'r', encoding='utf-8', newline='') as f:
    leitor = csv.DictReader(f)       # usa a primeira linha como cabeçalho
    for linha in leitor:
        nome = linha['nome']
        lon  = float(linha['lon'])
        lat  = float(linha['lat'])
        print(f'{nome}: ({lon:.4f}, {lat:.4f})')
```

Exemplo de `pontos.csv`:
```
nome,lon,lat,altitude
P01,-35.7431,-7.2256,45.2
P02,-36.1023,-5.8012,312.8
P03,-37.0541,-8.1337,189.4
```

### Escrita

```python
import csv

pontos = [
    {'nome': 'P01', 'lon': -35.74, 'lat': -7.22, 'altitude': 45.2},
    {'nome': 'P02', 'lon': -36.10, 'lat': -5.80, 'altitude': 312.8},
]

with open('saida.csv', 'w', encoding='utf-8', newline='') as f:
    campos = ['nome', 'lon', 'lat', 'altitude']
    escritor = csv.DictWriter(f, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(pontos)
```

💡 Use sempre `newline=''` ao abrir CSVs para evitar linhas em branco extras no Windows.

---

## Módulo `os` e `os.path`

```python
import os

# Caminhos
os.getcwd()                          # diretório de trabalho atual
os.path.join('dados', 'rn', 'mun.shp')  # 'dados/rn/mun.shp' (multiplataforma)
os.path.basename('/dados/mun.shp')   # 'mun.shp'
os.path.dirname('/dados/mun.shp')    # '/dados'
os.path.splitext('mun.shp')          # ('mun', '.shp')
os.path.exists('/dados/mun.shp')     # True ou False
os.path.isfile('mun.shp')            # True se for arquivo
os.path.isdir('/dados')              # True se for diretório

# Listar arquivos de um diretório
for nome in os.listdir('/dados/shapefiles'):
    print(nome)

# Listar shapefiles recursivamente
for raiz, dirs, arquivos in os.walk('/dados'):
    for arq in arquivos:
        if arq.endswith('.shp'):
            print(os.path.join(raiz, arq))

# Criar diretório
os.makedirs('saida/vetoriais', exist_ok=True)
```

---

## `pathlib.Path` — alternativa moderna

`pathlib` oferece uma interface orientada a objetos para caminhos, mais legível que `os.path`.

```python
from pathlib import Path

pasta = Path('/dados/shapefiles')
arq   = pasta / 'municipios_rn.shp'    # operador / para compor caminhos

arq.name          # 'municipios_rn.shp'
arq.stem          # 'municipios_rn'
arq.suffix        # '.shp'
arq.parent        # Path('/dados/shapefiles')
arq.exists()      # True ou False

# Listar shapefiles
shapefiles = list(pasta.glob('*.shp'))

# Recursivo
todos_shp = list(pasta.rglob('*.shp'))

# Criar diretório
Path('saida/vetoriais').mkdir(parents=True, exist_ok=True)

# Ler e escrever direto
conteudo = arq.with_suffix('.prj').read_text(encoding='utf-8')
Path('saida/log.txt').write_text('OK\n', encoding='utf-8')
```

### `os.path` vs `pathlib` — qual usar?

| Situação | Recomendação |
|---|---|
| Scripts novos | `pathlib` — mais legível e Pythônico |
| Código legado / compatibilidade | `os.path` |
| Integração com APIs que exigem `str` | `str(Path(...))` para converter |

---

## Exercícios

### Exercício 1 — Contexto GIS

Dado o arquivo CSV de pontos de controle abaixo, escreva um programa que:

1. Leia o arquivo com `csv.DictReader`
2. Converta `lon`, `lat` e `altitude` para `float`
3. Calcule a altitude média dos pontos
4. Filtre os pontos com altitude acima da média
5. Escreva um novo CSV `pontos_filtrados.csv` com os pontos filtrados

Conteúdo do arquivo `pontos_controle.csv`:
```
nome,lon,lat,altitude
PC-01,-35.7431,-7.2256,45.2
PC-02,-36.1023,-5.8012,312.8
PC-03,-37.0541,-8.1337,189.4
PC-04,-35.2198,-6.4501,78.1
PC-05,-36.8812,-4.9723,520.6
PC-06,-35.9001,-7.8834,210.3
```

---

### Exercício 2 — Contexto GIS

Escreva um programa que:

1. Receba uma lista de dicionários representando feições (simulada no código)
2. Gere um arquivo `relatorio_feicoes.txt` com um relatório formatado contendo:
   - Cabeçalho com data de geração (`datetime.date.today()`)
   - Linha separadora
   - Para cada feição: id, município, área e densidade demográfica
   - Rodapé com total de feições e área total

```python
feicoes = [
    {'id': 1, 'municipio': 'Natal',        'area_km2': 167.3,  'pop': 890480},
    {'id': 2, 'municipio': 'Mossoró',      'area_km2': 2099.3, 'pop': 295000},
    {'id': 3, 'municipio': 'Caicó',        'area_km2': 1228.5, 'pop': 68900},
    {'id': 4, 'municipio': 'Parnamirim',   'area_km2': 123.5,  'pop': 280000},
]
```

---

### Exercício 3 — Contexto GIS

Usando `pathlib.Path`, escreva uma função `inventariar_dados(pasta)` que:

1. Receba o caminho de um diretório como `str` ou `Path`
2. Liste **recursivamente** todos os arquivos geoespaciais encontrados (`.shp`, `.gpkg`, `.geojson`, `.tif`, `.img`)
3. Agrupe os arquivos por extensão em um dicionário `{ext: [caminhos]}`
4. Exiba um resumo com a contagem por tipo e os caminhos completos
5. Salve o inventário em `inventario.txt` no diretório raiz informado

Exemplo de saída:
```
Inventário de: /dados/projeto_rn
==========================================
.shp       :  4 arquivo(s)
  /dados/projeto_rn/vetorial/municipios.shp
  ...
.tif       :  2 arquivo(s)
  /dados/projeto_rn/raster/dem_30m.tif
  ...
Total: 6 arquivo(s)
```
