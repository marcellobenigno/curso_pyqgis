def create_point_layer():
    uri = "point?crs=epsg:4326"

    lyr = QgsVectorLayer(uri, 'pontos', 'memory')

    provider = lyr.dataProvider()

    provider.addAttributes([
            QgsField('id', QVariant.Int),
            QgsField('nome', QVariant.String),
            QgsField('x', QVariant.Double),
            QgsField('y', QVariant.Double),
    ])

    lyr.updateFields()

    QgsProject.instance().addMapLayer(lyr)
    
    
def insert_feature(layer_name, id, **kwargs):
    lyr = QgsProject.instance().mapLayersByName(layer_name)[0]
    provider = lyr.dataProvider()
    
    geom = QgsGeometry().fromWkt(f"Point({kwargs['x']} {kwargs['y']})")
    feat = QgsFeature()
    feat.setGeometry(geom)
    feat.setAttributes([
        id,
        kwargs['nome'],
        geom.asPoint().x(),
        geom.asPoint().y()
    ]) 
    provider.addFeatures([feat])
    lyr.commitChanges()
    lyr.updateExtents()
    


create_point_layer()

point_list = [
    {'nome': 'A', 'x': -36.79, 'y': -7.24},
    {'nome': 'B', 'x': -36.87, 'y': -7.94},
    {'nome': 'C', 'x': -35.20, 'y': -7.15},
    {'nome': 'D', 'x': -38.49, 'y': -6.71},
]

for id, pt in enumerate(point_list, start=1):
    insert_feature('pontos', id, **pt)
    
