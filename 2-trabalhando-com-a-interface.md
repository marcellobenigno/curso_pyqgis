# 2. Trabalhando com a Interface do QGIS

Para manipular a interface do QGIS, iremos utilizar uma variável chamada`iface`. Ela  é criada toda vez que o QGIS é aberto. `iface` é uma instância da classe `QgisInterface` e pode ser utilizada pde diversas formas. tanto para modificar a interface ( alterar menus, toolbars, etc), ou pode ser utilizada para acessar o `map canvas`, que é a área onde os layers são exibidos (área do mapa).

Podemos criar uma variável que referencie o Canvas da seguinte forma:

```python
mc = iface.mapCanvas()
```

Através da manipulação da variável `mc` é possível modificar o nível de zoom, alterar a escala, trocar a cor do background, dentre outras possibilidades, tais como:

```python
# obter o layer corrente:
current_layer = mc.currentLayer()

# obter a lista dos layers que estão visíveis:
checked_layers = mc.layers()
```

## Obtendo um layer através do seu nome:

Este procedimento é feito da seguinte forma:

```python
# obtendo uma camada chamada lotes:
lotes = QgsProject.instance().mapLayersByName('lotes')[0]
```

💡 Explicando: acessamos a instância do projeto atual `QgsProject.instance()` e através do método `mapLayersByName()` passamos como parâmetro o nome da camada em questão. o resultado deste processo é uma lista com um único elemento e por essa razão, utilizamos o índice `[0]` para pegar o primeiro elemento desta lista.