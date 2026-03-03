# 11. Módulos e Bibliotecas

Um **módulo** é um arquivo `.py` que contém funções, classes e variáveis reutilizáveis. Uma **biblioteca** (ou pacote) é um conjunto de módulos distribuídos juntos. Reutilizar código de terceiros é um dos maiores trunfos do ecossistema Python.

---

## Importando Módulos

```python
import math                        # importa o módulo inteiro
from math import pi, sqrt          # importa nomes específicos
import numpy as np                 # importa com alias
from os.path import join, exists   # importa múltiplos de um módulo
```

```python
import math
math.pi           # 3.14159...
math.sqrt(144)    # 12.0
math.radians(90)  # 1.5707...

from math import pi, atan2, sqrt
pi                # 3.14159... — sem prefixo
```

💡 Prefira `import modulo` para módulos grandes e `from modulo import nome` para funções específicas muito usadas. Evite `from modulo import *` — polui o namespace.

---

## Módulos da Biblioteca Padrão Úteis para GIS

### `math`

```python
import math

# Fórmula de Haversine — distância entre dois pontos em graus decimais
def haversine(lon1, lat1, lon2, lat2):
    R = 6371  # raio médio da Terra em km
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    return 2 * R * math.asin(math.sqrt(a))

haversine(-35.74, -7.22, -36.10, -5.80)   # ~164 km
```

### `os` e `sys`

```python
import os, sys

os.getcwd()                       # diretório atual
os.environ.get('QGIS_PREFIX_PATH', '')   # variável de ambiente
sys.path                          # caminhos de busca de módulos
sys.version                       # versão do Python
```

### `json`

```python
import json

dados = {'type': 'Feature', 'geometry': {'type': 'Point', 'coordinates': [-35.74, -7.22]}}
json_str = json.dumps(dados, indent=2)     # dict → string JSON
de_volta  = json.loads(json_str)           # string JSON → dict

with open('ponto.geojson', 'w') as f:
    json.dump(dados, f, indent=2)          # dict → arquivo
```

### `csv`

Ver seção 10 para exemplos completos.

### `datetime`

```python
from datetime import date, datetime

hoje = date.today()                        # 2024-03-15
agora = datetime.now()                     # 2024-03-15 10:23:45
agora.strftime('%d/%m/%Y %H:%M')          # '15/03/2024 10:23'

# Registrar data de coleta de dado
metadado = {'camada': 'municipios_rn', 'data_atualizacao': str(hoje)}
```

### `re` — Expressões Regulares

```python
import re

epsg = 'EPSG:4674'
match = re.match(r'EPSG:(\d+)', epsg)
if match:
    codigo = int(match.group(1))   # 4674
```

---

## `pip` — Gerenciador de Pacotes

```bash
# Instalar
pip install geopandas shapely fiona

# Versão específica
pip install geopandas==0.14.0

# Listar instalados
pip list

# Exportar dependências
pip freeze > requirements.txt

# Instalar de requirements.txt
pip install -r requirements.txt
```

💡 Dentro do QGIS, use o console do OSGeo4W Shell (Windows) ou o terminal com o Python do QGIS para instalar pacotes acessíveis ao PyQGIS.

---

## Principais Bibliotecas Python para GIS

| Biblioteca | Finalidade | Exemplo rápido |
|---|---|---|
| **Shapely** | Geometrias e operações espaciais (buffer, união, interseção) | `from shapely.geometry import Point; Point(-35.7, -7.2).buffer(0.1)` |
| **Fiona** | Leitura e escrita de formatos vetoriais (SHP, GeoJSON, GPKG) | `import fiona; fiona.open('mun.shp')` |
| **GeoPandas** | DataFrames com suporte a geometrias e CRS | `import geopandas as gpd; gpd.read_file('mun.shp')` |
| **pyproj** | Transformação de sistemas de coordenadas (PROJ) | `from pyproj import Transformer; Transformer.from_crs(4674, 32724)` |
| **Rasterio** | Leitura, escrita e análise de dados raster | `import rasterio; rasterio.open('dem.tif')` |
| **GDAL/OGR** | Baixo nível: vetores (OGR) e rasters (GDAL) | `from osgeo import ogr, gdal` |
| **PyQGIS** | API completa do QGIS via Python | `QgsVectorLayer('mun.shp', 'mun', 'ogr')` |
| **Folium** | Mapas interativos baseados em Leaflet.js | `import folium; folium.Map(location=[-7.2, -35.7])` |
| **Matplotlib** | Visualização e plotagem de dados espaciais | `import matplotlib.pyplot as plt` |

---

## Criando um Módulo Próprio

Crie um arquivo `geo_utils.py` no mesmo diretório do seu script:

```python
# geo_utils.py
import math

RAIO_TERRA_KM = 6371.0


def dd_para_dms(decimal):
    """Converte graus decimais para string DMS."""
    grau = int(abs(decimal))
    resto = (abs(decimal) - grau) * 60
    minuto = int(resto)
    segundo = (resto - minuto) * 60
    sinal = '-' if decimal < 0 else ''
    return f'{sinal}{grau}°{minuto:02d}\'{segundo:05.2f}"'


def haversine(lon1, lat1, lon2, lat2):
    """Distância em km entre dois pontos em graus decimais."""
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    return 2 * RAIO_TERRA_KM * math.asin(math.sqrt(a))


def area_poligono_shoelace(vertices):
    """Calcula área pelo teorema de Shoelace. Vértices: lista de (x, y)."""
    n = len(vertices)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0
```

Usando o módulo:

```python
import geo_utils

geo_utils.dd_para_dms(-35.7431)           # "-35°44'35.16\""
geo_utils.haversine(-35.74, -7.22, -36.10, -5.80)  # ~164 km

vertices = [(0,0), (4,0), (4,3), (0,3)]
geo_utils.area_poligono_shoelace(vertices)  # 12.0
```

---

## Exercícios

### Exercício 1 — Contexto GIS

Use o módulo `math` para calcular a **área de um polígono** pela **Fórmula de Shoelace** (Teorema de Gauss):

```
Área = (1/2) × |Σ (xᵢ × yᵢ₊₁ − xᵢ₊₁ × yᵢ)|
```

Calcule a área dos polígonos abaixo em unidades do sistema de coordenadas (graus²) e, depois, converta para km² usando o fator de aproximação `1° ≈ 111 km`.

```python
poligono_rn = [
    (-38.00, -6.00), (-35.00, -6.00),
    (-35.00, -4.50), (-38.00, -4.50),
]

poligono_lote = [
    (290000, 9195000), (290300, 9195000),
    (290300, 9195200), (290000, 9195200),
]  # coordenadas UTM em metros
```

---

### Exercício 2 — Contexto GIS

Crie e salve um arquivo `ponto_referencia.geojson` usando o módulo `json` com a seguinte estrutura GeoJSON:

1. Uma `FeatureCollection` com 3 `Feature`s do tipo `Point`
2. Cada feição deve ter propriedades: `nome`, `altitude` e `datum`
3. Leia o arquivo gerado de volta e exiba as propriedades de cada feição formatadas

```python
pontos = [
    {'nome': 'Marco I',   'lon': -35.7431, 'lat': -7.2256,  'altitude': 45.2,  'datum': 'SIRGAS2000'},
    {'nome': 'Marco II',  'lon': -36.1023, 'lat': -5.8012,  'altitude': 312.8, 'datum': 'SIRGAS2000'},
    {'nome': 'Marco III', 'lon': -37.0541, 'lat': -8.1337,  'altitude': 189.4, 'datum': 'SIRGAS2000'},
]
```

---

### Exercício 3 — Contexto GIS

Crie um módulo `coord_utils.py` com as seguintes funções e importe-o no seu script principal:

1. `dd_para_dms(decimal, eixo)` — converte graus decimais para string DMS; `eixo` aceita `'lon'` ou `'lat'` e define o sufixo (`E/W` ou `N/S`)
2. `utm_para_epsg(zona, hemisferio, datum='SIRGAS2000')` — retorna o código EPSG; suporte a `'SIRGAS2000'` e `'WGS84'`
3. `distancia_euclidiana(p1, p2)` — distância entre dois pontos em coordenadas projetadas (metros)

No script principal, use as três funções para processar a lista de pontos abaixo e exibir um relatório:

```python
pontos = [
    {'nome': 'PC-01', 'lon': -35.7431, 'lat': -7.2256},
    {'nome': 'PC-02', 'lon': -36.1023, 'lat': -5.8012},
    {'nome': 'PC-03', 'lon': -37.0541, 'lat': -8.1337},
]
```
