# 9. Tratamento de Exceções

Uma **exceção** é um erro detectado em tempo de execução que interrompe o fluxo normal do programa. Tratar exceções torna o código mais robusto e evita que um erro inesperado derrube toda a execução — essencial em scripts de geoprocessamento que lidam com arquivos externos e dados de qualidade variável.

---

## `try` / `except` / `else` / `finally`

```python
try:
    # código que pode falhar
except TipoDeErro as e:
    # o que fazer se ocorrer o erro
else:
    # executado apenas se NÃO houve exceção
finally:
    # executado SEMPRE (com ou sem erro)
```

```python
caminho = 'dados/municipios.shp'

try:
    arquivo = open(caminho, 'r')
    conteudo = arquivo.read()
except FileNotFoundError as e:
    print(f'Arquivo não encontrado: {e}')
else:
    print(f'Arquivo lido: {len(conteudo)} bytes')
    arquivo.close()
finally:
    print('Operação de leitura encerrada.')
```

---

## Exceções Comuns

| Exceção | Quando ocorre | Contexto GIS |
|---|---|---|
| `FileNotFoundError` | Arquivo não existe | Caminho de shapefile incorreto |
| `ValueError` | Valor com tipo correto mas inválido | `float('abc')`, EPSG inválido |
| `TypeError` | Operação com tipo errado | Somar `str` com `float` em atributo |
| `KeyError` | Chave inexistente em dicionário | Acessar campo ausente nos metadados |
| `IndexError` | Índice fora do intervalo | Lista de vértices menor que o esperado |
| `ZeroDivisionError` | Divisão por zero | Densidade com área = 0 |
| `AttributeError` | Atributo inexistente no objeto | Método chamado em `None` |
| `PermissionError` | Sem permissão de leitura/escrita | Arquivo de camada bloqueado pelo QGIS |
| `OSError` | Erro genérico de sistema de arquivos | Disco cheio ao exportar raster |

---

## Captura de Múltiplas Exceções

```python
def ler_epsg(entrada):
    try:
        codigo = int(entrada)
        if codigo <= 0:
            raise ValueError(f'Código EPSG inválido: {codigo}')
        return f'EPSG:{codigo}'
    except ValueError as e:
        print(f'Erro de valor: {e}')
    except TypeError as e:
        print(f'Erro de tipo: {e}')
    return None

ler_epsg('4674')    # 'EPSG:4674'
ler_epsg('abc')     # Erro de valor
ler_epsg(None)      # Erro de tipo
```

### Capturando várias na mesma cláusula

```python
try:
    dado = metadados['area_km2'] / metadados['feicoes']
except (KeyError, ZeroDivisionError) as e:
    print(f'Erro ao calcular densidade: {type(e).__name__}: {e}')
```

---

## `raise` — Lançando Exceções

Use `raise` para sinalizar que algo está errado na lógica do seu código.

```python
def validar_crs(crs):
    if not isinstance(crs, str):
        raise TypeError(f'CRS deve ser str, recebido: {type(crs).__name__}')
    if not crs.startswith('EPSG:'):
        raise ValueError(f'Formato inválido. Esperado "EPSG:XXXX", recebido: {crs!r}')
    return True

validar_crs('EPSG:4674')   # True
validar_crs('sirgas2000')  # ValueError
validar_crs(4674)          # TypeError
```

### Re-lançar uma exceção após registrar

```python
try:
    resultado = processar_camada(caminho)
except Exception as e:
    print(f'[LOG] Falha em processar_camada: {e}')
    raise   # propaga a exceção original
```

---

## Exceções Personalizadas

```python
class ErroGIS(Exception):
    """Erro base para operações GIS."""

class CRSInvalidoError(ErroGIS):
    """CRS não reconhecido ou mal formatado."""

class GeometriaInvalidaError(ErroGIS):
    """Geometria com estrutura inválida."""


def reprojetar(camada, crs_destino):
    if not crs_destino.startswith('EPSG:'):
        raise CRSInvalidoError(f'CRS inválido: {crs_destino!r}')
    print(f'Reprojetando {camada} para {crs_destino}')

try:
    reprojetar('municipios', 'sirgas')
except CRSInvalidoError as e:
    print(f'Erro de CRS: {e}')
```

---

## Boas Práticas

```python
# EVITE: except genérico silencia erros inesperados
try:
    processar()
except:
    pass   # nunca faça isso — erros são engolidos silenciosamente

# PREFIRA: captura específica
try:
    processar()
except FileNotFoundError as e:
    print(f'Arquivo não encontrado: {e}')
except ValueError as e:
    print(f'Dado inválido: {e}')

# SE precisar capturar tudo, registre o erro
try:
    processar()
except Exception as e:
    print(f'[ERRO] {type(e).__name__}: {e}')
    raise
```

💡 Use `finally` para liberar recursos (fechar arquivos, conexões) — ou melhor ainda, use `with` que faz isso automaticamente.

---

## Exercícios

### Exercício 1 — Contexto GIS

Escreva uma função `abrir_camada(caminho)` que simule a abertura de um arquivo vetorial. A função deve:

1. Verificar se o arquivo existe (`os.path.exists`); se não, lançar `FileNotFoundError`
2. Verificar se a extensão é suportada (`.shp`, `.gpkg`, `.geojson`); se não, lançar `ValueError`
3. Retornar um dicionário com `{'caminho': caminho, 'extensao': ext, 'status': 'aberto'}`
4. Chamar a função três vezes: com caminho válido simulado, extensão inválida e caminho inexistente — capturando cada erro separadamente

---

### Exercício 2 — Contexto GIS

Dada a lista de registros de atributos abaixo (com dados sujos), escreva um programa que processe cada registro e:

1. Converta `'area_km2'` para `float` — trate `ValueError` se o valor não for numérico
2. Acesse a chave `'populacao'` — trate `KeyError` se estiver ausente
3. Calcule a densidade demográfica — trate `ZeroDivisionError` se área for zero
4. Acumule os resultados válidos em uma nova lista e exiba um resumo ao final

```python
registros = [
    {'municipio': 'Natal',      'area_km2': '167.3',  'populacao': 890480},
    {'municipio': 'Mossoró',    'area_km2': 'N/D',    'populacao': 295000},
    {'municipio': 'Caicó',      'area_km2': '1228.5'},              # sem populacao
    {'municipio': 'Lote Teste', 'area_km2': '0',      'populacao': 150},
    {'municipio': 'Parnamirim', 'area_km2': '123.5',  'populacao': 280000},
]
```

---

### Exercício 3 — Contexto GIS

Escreva uma função `validar_ponto(lon, lat)` que:

1. Verifique se `lon` e `lat` são `int` ou `float`; se não, lance `TypeError` com mensagem clara
2. Verifique se `lon` ∈ [-180, 180] e `lat` ∈ [-90, 90]; se não, lance `ValueError`
3. Retorne `True` se tudo estiver correto

Em seguida, crie uma função `processar_pontos(pontos)` que receba uma lista de tuplas `(lon, lat)`, chame `validar_ponto` para cada uma usando `try/except`, e retorne dois dicionários:
- `validos`: `{(lon, lat): True}`
- `invalidos`: `{(lon, lat): mensagem_do_erro}`

```python
pontos = [
    (-35.74, -7.22),
    (200.0, -7.22),       # lon inválida
    (-35.74, 'sete'),     # tipo inválido
    (-36.10, -5.80),
    (-37.05, -95.0),      # lat inválida
]
```
