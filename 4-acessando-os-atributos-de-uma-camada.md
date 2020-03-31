# Acessando os Atributos de uma Camada

Podemos visualizar os campos de uma camada da seguinte forma:

```python
layer = QgsProject.instance().mapLayersByName('municipios')[0]

fields = layer.fields()

for field in fields:
    print(field.name())
````

Como saída, temos a lista dos nomes dos campos:

![](.pastes/2020-02-06-08-45-30.png)

💡 também é possível abrir a tabela de atributos da camada:

```python
iface.showAttributeTable(layer)
```

Muitas vezes precisamos percorrer os atributos de uma camada, seja para realizar algum teste, seja para filtrar um conjunto de dados.

O código abaixo exemplifica esse procedimento:

```python
layer = QgsProject.instance().mapLayersByName('municipios')[0]

if layer.isValid():
   for feature in layer.getFeatures():
       print(f"NOME: {feature['nome']}, ÁREA KM2: {feature['area_km2']}")
```

Também podemos aplicar um filtro neste loop, selecionando apenas os municípios com uma determinada característica, como por exemplo, todos aqueles que possuem área maior que 500 km<sup>2</sup>:

```python
layer = QgsProject.instance().mapLayersByName('municipios')[0]

sql_filter = '"area_km2" > 500'

request = QgsFeatureRequest() 

request.setFilterExpression(sql_filter)

if layer.isValid():
   for feature in layer.getFeatures(request):
       print(f"NOME: {feature['nome']}, ÁREA KM2: {feature['area_km2']}")
```
