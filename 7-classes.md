# 7. Classes e Orientação a Objetos

**Programação Orientada a Objetos (OOP)** organiza o código em torno de **objetos** — entidades que combinam dados (atributos) e comportamento (métodos).

Conceitos fundamentais:

| Conceito | Definição |
|---|---|
| **Classe** | O molde/projeto (ex: `CamadaVetorial`) |
| **Objeto** | Uma instância concreta da classe (ex: `municipios_rn`) |
| **Atributo** | Dado do objeto (ex: `nome`, `crs`, `feicoes`) |
| **Método** | Função do objeto (ex: `reprojetar()`, `exportar()`) |

---

## Definindo uma Classe

```python
class NomeDaClasse:
    def __init__(self, parametros):
        self.atributo = valor   # atributo de instância

    def metodo(self):
        pass
```

```python
class CamadaVetorial:
    def __init__(self, nome, tipo, crs='EPSG:4674'):
        self.nome  = nome
        self.tipo  = tipo
        self.crs   = crs
        self.feicoes = 0   # atributo com valor padrão fixo

camada = CamadaVetorial('municipios_rn', 'Polígono')
print(camada.nome)   # 'municipios_rn'
print(camada.crs)    # 'EPSG:4674'
```

---

## `__init__` e `self`

- `__init__` é o **construtor** — executado automaticamente ao criar o objeto
- `self` é a referência ao próprio objeto e deve ser o primeiro parâmetro de todo método

```python
class PontoGeo:
    def __init__(self, lon, lat, nome=''):
        self.lon  = lon
        self.lat  = lat
        self.nome = nome

    def coordenadas(self):
        return (self.lon, self.lat)

p = PontoGeo(-35.74, -7.22, 'Base Topográfica')
p.coordenadas()   # (-35.74, -7.22)
```

---

## Atributos de Classe vs. de Instância

**Atributos de classe** são compartilhados por todas as instâncias.
**Atributos de instância** pertencem a cada objeto individualmente.

```python
class CamadaVetorial:
    formatos_suportados = ['.shp', '.gpkg', '.geojson']   # atributo de CLASSE

    def __init__(self, nome, tipo):
        self.nome = nome     # atributo de INSTÂNCIA
        self.tipo = tipo

CamadaVetorial.formatos_suportados   # acessado pela classe
camada = CamadaVetorial('rios', 'Linha')
camada.formatos_suportados           # também acessível pela instância
```

---

## Métodos Especiais: `__str__` e `__repr__`

| Método | Quando é chamado | Público para |
|---|---|---|
| `__str__` | `print(obj)` e `str(obj)` | Usuário final — leitura humana |
| `__repr__` | Console interativo, `repr(obj)` | Desenvolvedores — debug |

```python
class PontoGeo:
    def __init__(self, lon, lat, nome=''):
        self.lon  = lon
        self.lat  = lat
        self.nome = nome

    def __str__(self):
        return f'Ponto "{self.nome}": ({self.lon}, {self.lat})'

    def __repr__(self):
        return f'PontoGeo(lon={self.lon}, lat={self.lat}, nome={self.nome!r})'

p = PontoGeo(-35.74, -7.22, 'Sede')
print(p)    # Ponto "Sede": (-35.74, -7.22)
repr(p)     # "PontoGeo(lon=-35.74, lat=-7.22, nome='Sede')"
```

---

## Encapsulamento

Encapsulamento protege atributos de modificação direta inadvertida. Em Python usa-se convenção de nomes:

| Convenção | Significado |
|---|---|
| `self.nome` | Público — acesso livre |
| `self._nome` | Protegido — não altere de fora (convenção) |
| `self.__nome` | Privado — Python aplica *name mangling* |

```python
class CamadaVetorial:
    def __init__(self, nome, feicoes):
        self.nome      = nome
        self._feicoes  = feicoes      # protegido
        self.__encoding = 'UTF-8'     # privado

    def get_encoding(self):
        return self.__encoding

    def set_feicoes(self, n):
        if n < 0:
            raise ValueError('Número de feições não pode ser negativo')
        self._feicoes = n

camada = CamadaVetorial('rios', 320)
camada.get_encoding()       # 'UTF-8'
camada.set_feicoes(321)
camada.__encoding           # AttributeError — name mangling
```

---

## Herança

Uma classe **filha** herda atributos e métodos da classe **pai** e pode especializá-los.

```python
class Geometria:
    """Classe base para geometrias."""
    def __init__(self, crs='EPSG:4674'):
        self.crs = crs

    def tipo(self):
        return 'Geometria'

    def __str__(self):
        return f'{self.tipo()} | CRS: {self.crs}'


class Ponto(Geometria):
    def __init__(self, lon, lat, crs='EPSG:4674'):
        super().__init__(crs)       # chama o __init__ do pai
        self.lon = lon
        self.lat = lat

    def tipo(self):
        return 'Ponto'

    def __str__(self):
        return f'Ponto ({self.lon}, {self.lat}) | CRS: {self.crs}'


class Poligono(Geometria):
    def __init__(self, vertices, crs='EPSG:4674'):
        super().__init__(crs)
        self.vertices = vertices    # lista de tuplas (x, y)

    def tipo(self):
        return 'Polígono'

    def num_vertices(self):
        return len(self.vertices)


p = Ponto(-35.74, -7.22)
print(p)             # Ponto (-35.74, -7.22) | CRS: EPSG:4674
isinstance(p, Geometria)   # True  — Ponto É UMA Geometria
```

`super()` chama o método da classe pai sem precisar nomear a classe explicitamente.

---

## Exercícios

### Exercício 1 — Classe `PontoGeo`

Crie uma classe `PontoGeo` com atributos `lon`, `lat` e `nome` (padrão `''`). Implemente:

1. `__str__` — exibe `'nome: (lon, lat)'`
2. `__repr__` — exibe `'PontoGeo(lon=..., lat=..., nome=...)'`
3. `distancia_para(outro)` — distância euclidiana até outro `PontoGeo`
4. `para_dms()` — retorna uma tupla de strings `(lon_dms, lat_dms)` no formato `35°44'35"W`

```python
p1 = PontoGeo(-35.74, -7.22, 'Marco A')
p2 = PontoGeo(-36.10, -8.01, 'Marco B')

print(p1)                  # Marco A: (-35.74, -7.22)
p1.distancia_para(p2)      # ~0.871 (graus — distância aproximada)
p1.para_dms()              # ("35°44'24\"W", "7°13'12\"S")
```

---

### Exercício 2 — Classe `CamadaVetorial`

Crie uma classe `CamadaVetorial` com:

**Atributo de classe:**
- `formatos_suportados = ['.shp', '.gpkg', '.geojson', '.kml']`

**Atributos de instância (no `__init__`):**
- `nome`, `tipo` (Ponto/Linha/Polígono), `crs` (padrão `'EPSG:4674'`)
- `_feicoes = 0` (protegido)
- `_campos = []` (protegido)

**Métodos:**
- `adicionar_campo(nome_campo)` — adiciona à lista `_campos`
- `definir_feicoes(n)` — valida que `n >= 0` antes de atribuir
- `resumo()` — exibe um relatório formatado com todos os atributos
- `__str__` — retorna `'[tipo] nome (n feições)'`

```python
camada = CamadaVetorial('municipios_rn', 'Polígono')
camada.adicionar_campo('cd_mun')
camada.adicionar_campo('nm_mun')
camada.definir_feicoes(167)
print(camada)      # [Polígono] municipios_rn (167 feições)
camada.resumo()
```

---

### Exercício 3 — Herança: `Geometria`, `Ponto`, `Linha`, `Poligono`

Implemente a hierarquia abaixo usando herança:

```
Geometria  (base)
├── Ponto
├── Linha
└── Poligono
```

**`Geometria` (base):**
- `__init__(self, crs='EPSG:4674')`
- `tipo()` → `'Geometria'`
- `is_valida()` → `NotImplementedError` (força implementação nas filhas)
- `__str__` → `'[tipo] | CRS: crs'`

**`Ponto`:**
- `__init__(lon, lat, crs)` — chama `super()`
- `tipo()` → `'Ponto'`
- `is_valida()` → `True` se lon ∈ [-180, 180] e lat ∈ [-90, 90]

**`Linha`:**
- `__init__(vertices, crs)` — `vertices` é lista de tuplas `(x, y)`
- `tipo()` → `'Linha'`
- `is_valida()` → `True` se tiver ao menos 2 vértices
- `comprimento()` → soma das distâncias euclidianas entre vértices consecutivos

**`Poligono`:**
- `__init__(vertices, crs)` — `vertices` é lista de tuplas `(x, y)`
- `tipo()` → `'Polígono'`
- `is_valida()` → `True` se tiver ao menos 3 vértices
- `perimetro()` → soma das distâncias entre vértices consecutivos (inclusive o fechamento)

```python
p = Ponto(-35.74, -7.22)
l = Linha([(0, 0), (3, 0), (3, 4)])
pol = Poligono([(0,0), (4,0), (4,3), (0,3)])

print(p)            # [Ponto] | CRS: EPSG:4674
p.is_valida()       # True
l.comprimento()     # 7.0
pol.perimetro()     # 14.0

isinstance(l, Geometria)   # True
```

---

### Exercício 4 — Classe `ProjecaoUTM`

Crie uma classe `ProjecaoUTM` que encapsule informações de uma projeção UTM e ofereça métodos de cálculo e validação.

**Atributos de instância:**
- `zona` (int, 1–60)
- `hemisferio` (`'N'` ou `'S'`)
- `datum` (padrão `'SIRGAS2000'`)

**Atributo de classe:**
- `_epsg_base = {'SIRGAS2000': 31900, 'WGS84': 32600}` — base para calcular o código EPSG

**Métodos:**
- `epsg()` — calcula e retorna o código EPSG completo:
  - SIRGAS 2000 Sul: 31900 + zona → ex: zona 24 = `31924`
  - WGS 84 Sul: 32700 + zona → ex: zona 24 = `32724`
  - WGS 84 Norte: 32600 + zona
- `is_valida()` → `True` se zona ∈ [1, 60] e hemisferio ∈ ['N', 'S']
- `__str__` → ex: `'UTM Zona 24S | SIRGAS2000 | EPSG:31924'`

```python
utm = ProjecaoUTM(zona=24, hemisferio='S')
print(utm)          # UTM Zona 24S | SIRGAS2000 | EPSG:31924
utm.epsg()          # 31924
utm.is_valida()     # True

ProjecaoUTM(61, 'S').is_valida()   # False
```

---

### Exercício 5 — Classe `BoundingBox`

Crie uma classe `BoundingBox` para representar e operar sobre extensões espaciais.

**Atributos:** `xmin`, `ymin`, `xmax`, `ymax`

**Métodos:**
- `is_valida()` → `True` se `xmin < xmax` e `ymin < ymax`
- `largura()` e `altura()` → diferença entre os extremos
- `area()` → largura × altura
- `centro()` → tupla `(cx, cy)` com o centroide da bbox
- `contem_ponto(lon, lat)` → `True` se o ponto estiver dentro da bbox
- `intersecta(outra)` → `True` se houver sobreposição com outra `BoundingBox`
- `buffer(distancia)` → retorna uma **nova** `BoundingBox` expandida em `distancia` em todas as direções
- `__str__` → `'BBox: (xmin, ymin, xmax, ymax)'`

```python
rn  = BoundingBox(-38.00, -8.00, -34.97, -4.49)
nat = BoundingBox(-35.30, -5.95, -35.15, -5.73)

print(rn)               # BBox: (-38.0, -8.0, -34.97, -4.49)
rn.area()               # ~9.18
rn.centro()             # (-36.485, -6.245)
rn.contem_ponto(-35.74, -5.79)   # True
rn.intersecta(nat)               # True
rn.buffer(0.5)          # BoundingBox(-38.5, -8.5, -34.47, -3.99)
```
