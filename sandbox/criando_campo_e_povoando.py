lyr = QgsProject.instance().mapLayersByName('municipios')[0]

exp = """ "nome"= 'Campina Grande' """

lyr.selectByExpression(exp)

memory_layer = lyr.materialize(
  QgsFeatureRequest().setFilterFids(lyr.selectedFeatureIds())
)

QgsProject.instance().addMapLayer(memory_layer)

memory_layer.setName('selecao')

mlayer_provider = memory_layer.dataProvider()

mlayer_provider.addAttributes([QgsField('area_km2', QVariant.Double)])

memory_layer.updateFields()

for f in memory_layer.getFeatures():
    id = f.id()
    area = f.geometry().area() * 12321
    attr_value = {8:area}
    mlayer_provider.changeAttributeValues({id:attr_value})