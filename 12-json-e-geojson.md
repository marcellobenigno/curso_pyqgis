# 12. Manipulação de JSON e GeoJSON

**JSON** (JavaScript Object Notation) é o formato de troca de dados mais usado na web. **GeoJSON** é um padrão baseado em JSON para representar dados geoespaciais — geometrias, feições e coleções de feições.

---

## Módulo `json`

| Função | Direção | Uso |
|---|---|---|
| `json.dumps(obj)` | Python → string JSON | Serializar para enviar/exibir |
| `json.loads(txt)` | string JSON → Python | Deserializar resposta de API |
| `json.dump(obj, f)` | Python → arquivo | Salvar em disco |
| `json.load(f)` | arquivo → Python | Ler do disco |

```python
import json

# dict → string JSON
dados = {'nome': 'Natal', 'lon': -35.20, 'lat': -5.79}
txt = json.dumps(dados, indent=2, ensure_ascii=False)
print(txt)
# {
#   "nome": "Natal",
#   "lon": -35.2,
#   "lat": -5.79
# }

# string JSON → dict
de_volta = json.loads(txt)
de_volta['nome']   # 'Natal'

# Salvar em arquivo
with open('cidade.json', 'w', encoding='utf-8') as f:
    json.dump(dados, f, indent=2, ensure_ascii=False)

# Ler de arquivo
with open('cidade.json', 'r', encoding='utf-8') as f:
    lido = json.load(f)
```

💡 `ensure_ascii=False` preserva caracteres acentuados no JSON. `indent=2` formata com recuo para leitura humana.

---

## Estrutura do GeoJSON

O GeoJSON define objetos geoespaciais em JSON seguindo a especificação [RFC 7946](https://datatracker.ietf.org/doc/html/rfc7946). Os tipos principais são:

### Geometrias

```json
{"type": "Point",           "coordinates": [-35.74, -7.22]}
{"type": "LineString",      "coordinates": [[-35.74,-7.22], [-36.10,-5.80]]}
{"type": "Polygon",         "coordinates": [[[-38,-6],[-35,-6],[-35,-4.5],[-38,-4.5],[-38,-6]]]}
{"type": "MultiPoint",      "coordinates": [[-35.74,-7.22], [-36.10,-5.80]]}
{"type": "MultiLineString", "coordinates": [...]}
{"type": "MultiPolygon",    "coordinates": [...]}
```

💡 Em polígonos, o anel exterior segue a orientação **anti-horária** e deve ser **fechado** (primeiro = último vértice).

### Feature

Combina uma geometria com propriedades arbitrárias:

```json
{
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [-35.74, -7.22]
  },
  "properties": {
    "nome": "Marco Geodésico I",
    "altitude": 45.2,
    "datum": "SIRGAS 2000"
  }
}
```

### FeatureCollection

Agrupamento de `Feature`s — equivalente a uma camada vetorial:

```json
{
  "type": "FeatureCollection",
  "features": [
    { "type": "Feature", "geometry": {...}, "properties": {...} },
    { "type": "Feature", "geometry": {...}, "properties": {...} }
  ]
}
```

---

## Criando GeoJSON com Python

```python
import json

def criar_feature_ponto(lon, lat, **propriedades):
    return {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [lon, lat]
        },
        'properties': propriedades
    }

pontos = [
    ('Marco I',   -35.7431, -7.2256, 45.2),
    ('Marco II',  -36.1023, -5.8012, 312.8),
    ('Marco III', -37.0541, -8.1337, 189.4),
]

colecao = {
    'type': 'FeatureCollection',
    'features': [
        criar_feature_ponto(lon, lat, nome=nome, altitude=alt)
        for nome, lon, lat, alt in pontos
    ]
}

with open('marcos.geojson', 'w', encoding='utf-8') as f:
    json.dump(colecao, f, indent=2, ensure_ascii=False)

print(f'{len(colecao["features"])} feições salvas.')
```

---

## Lendo GeoJSON com Python

```python
import json

with open('marcos.geojson', 'r', encoding='utf-8') as f:
    geojson = json.load(f)

# Acessar feições
for feature in geojson['features']:
    props  = feature['properties']
    coords = feature['geometry']['coordinates']
    print(f'{props["nome"]}: ({coords[0]:.4f}, {coords[1]:.4f}) | {props["altitude"]} m')
```

---

## Acesso a Geometrias Aninhadas

```python
# Polígono — acesso aos vértices do anel exterior
with open('municipio.geojson', 'r', encoding='utf-8') as f:
    fc = json.load(f)

feature = fc['features'][0]
tipo_geom = feature['geometry']['type']         # 'Polygon'
anel_ext  = feature['geometry']['coordinates'][0]  # lista de [lon, lat]

print(f'Tipo: {tipo_geom}')
print(f'Vértices no anel exterior: {len(anel_ext)}')
print(f'Primeiro vértice: {anel_ext[0]}')
```

---

## Filtrando e Modificando Feições

```python
import json

with open('municipios_rn.geojson', 'r', encoding='utf-8') as f:
    fc = json.load(f)

# Filtrar feições por propriedade
grandes = [
    f for f in fc['features']
    if f['properties'].get('area_km2', 0) > 500
]

# Adicionar nova propriedade calculada
for feat in fc['features']:
    pop  = feat['properties'].get('populacao', 0)
    area = feat['properties'].get('area_km2', 1)
    feat['properties']['densidade'] = round(pop / area, 2)

# Salvar versão modificada
fc_modificado = {'type': 'FeatureCollection', 'features': grandes}
with open('municipios_grandes.geojson', 'w', encoding='utf-8') as f:
    json.dump(fc_modificado, f, indent=2, ensure_ascii=False)
```

---

## GeoJSON vs Shapefile

| Critério | GeoJSON | Shapefile |
|---|---|---|
| Formato | Texto (JSON) | Binário (múltiplos arquivos) |
| Legibilidade | Alta — editável em qualquer editor | Baixa |
| Suporte a CRS | Apenas WGS 84 (EPSG:4326) | Qualquer CRS via `.prj` |
| Tamanho do arquivo | Maior para dados densos | Menor (binário) |
| Limite de campos | Sem limite | 255 campos, nomes até 10 chars |
| Uso ideal | APIs web, troca de dados, versionamento git | Geoprocessamento desktop, grandes volumes |
| Suporte em ferramentas | Universal (QGIS, ArcGIS, web) | Universal |

---

## Exemplo Completo: FeatureCollection do Zero

```python
import json
from datetime import date

def criar_feature(tipo_geom, coordenadas, **props):
    return {
        'type': 'Feature',
        'geometry': {'type': tipo_geom, 'coordinates': coordenadas},
        'properties': props
    }

# Municípios como polígonos simplificados (bounding boxes)
municipios = [
    {
        'nome': 'Natal', 'cod_ibge': 2408102, 'area_km2': 167.3,
        'coords': [
            [[-35.30,-5.95],[-35.15,-5.95],[-35.15,-5.73],[-35.30,-5.73],[-35.30,-5.95]]
        ]
    },
    {
        'nome': 'Mossoró', 'cod_ibge': 2408003, 'area_km2': 2099.3,
        'coords': [
            [[-37.50,-5.40],[-36.90,-5.40],[-36.90,-4.90],[-37.50,-4.90],[-37.50,-5.40]]
        ]
    },
]

colecao = {
    'type': 'FeatureCollection',
    'name': 'municipios_rn_simplificado',
    'crs': {
        'type': 'name',
        'properties': {'name': 'urn:ogc:def:crs:OGC:1.3:CRS84'}
    },
    'features': [
        criar_feature(
            'Polygon',
            m['coords'],
            nome=m['nome'],
            cod_ibge=m['cod_ibge'],
            area_km2=m['area_km2'],
            data_geracao=str(date.today()),
        )
        for m in municipios
    ]
}

caminho = 'municipios_simplificado.geojson'
with open(caminho, 'w', encoding='utf-8') as f:
    json.dump(colecao, f, indent=2, ensure_ascii=False)

print(f'Arquivo gerado: {caminho}')
print(f'Feições: {len(colecao["features"])}')
```

---

## Exercícios

### Exercício 1 — Contexto GIS

Dado o arquivo `estacoes.csv` abaixo, escreva um programa que:

1. Leia os dados com o módulo `csv`
2. Converta cada linha em uma `Feature` GeoJSON do tipo `Point`
3. Monte uma `FeatureCollection`
4. Salve o resultado em `estacoes.geojson`
5. Leia o arquivo gerado e exiba as propriedades de cada estação

```
codigo,nome,lon,lat,altitude,tipo
82397,Natal/Augusto Severo,-35.20,-5.91,49.0,meteorologica
82280,Mossoró,-37.37,-5.18,18.0,meteorologica
82678,Caicó,-37.09,-6.46,290.0,pluviometrica
82385,Macau,-36.62,-5.11,3.0,pluviometrica
```

---

### Exercício 2 — Contexto GIS

Crie um programa que:

1. Gere uma `FeatureCollection` de **linhas** (rotas de campo) a partir das listas abaixo
2. Calcule o comprimento aproximado de cada rota somando as distâncias euclidianas entre os vértices
3. Adicione `comprimento_aprox_graus` como propriedade de cada feição
4. Salve em `rotas_campo.geojson`

```python
rotas = [
    {
        'nome': 'Rota Litorânea',
        'vertices': [(-35.20, -5.79), (-35.74, -7.22), (-36.10, -8.35)]
    },
    {
        'nome': 'Rota Sertão',
        'vertices': [(-37.34, -5.19), (-37.09, -6.46), (-36.55, -7.88)]
    },
]
```

---

### Exercício 3 — Contexto GIS

Escreva um programa que leia o GeoJSON gerado no **Exemplo Completo** (`municipios_simplificado.geojson`) e:

1. Exiba o nome e a área de cada feição
2. Calcule e exiba a área total somada das feições
3. Crie uma nova `FeatureCollection` contendo apenas as feições com `area_km2 > 500` e salve em `municipios_grandes.geojson`
4. Adicione a propriedade `porte` a cada feição do novo arquivo:
   - `'Grande'` se `area_km2 > 1000`
   - `'Médio'` se `area_km2 > 500`
