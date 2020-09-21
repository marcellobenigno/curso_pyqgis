uri = "point?crs=epsg:4326"

lyr = QgsVectorLayer(uri, 'pontos', 'memory')
lyr.startEditing()
provider = lyr.dataProvider()

provider.addAttributes([
        QgsField('id', QVariant.Int),
        QgsField('nome', QVariant.String),
        QgsField('x', QVariant.Double),
        QgsField('y', QVariant.Double),
])

lyr.updateFields()

point_list = [
    {'nome': 'A', 'x': -36.79, 'y': -7.24},
    {'nome': 'B', 'x': -36.87, 'y': -7.94},
    {'nome': 'C', 'x': -35.20, 'y': -7.15},
    {'nome': 'D', 'x': -38.49, 'y': -6.71},
]

for id, elem in enumerate(point_list):
    geom = QgsGeometry().fromWkt(f"Point({elem['x']} {elem['y']})")
    feat = QgsFeature()
    feat.setGeometry(geom)
    feat.setAttributes([
        id + 1,
        elem['nome'],
        geom.asPoint().x(),
        geom.asPoint().y()
    ]) 
    provider.addFeatures([feat])


lyr.commitChanges()
lyr.updateExtents()
QgsProject.instance().addMapLayer(lyr)