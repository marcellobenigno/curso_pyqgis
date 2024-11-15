poligono = QgsVectorLayer("Polygon?crs=epsg:4326", "area_teste", "memory")

QgsProject.instance().addMapLayer(poligono)

dp_poligono = poligono.dataProvider()

fields = [QgsField('id', QVariant.Int), QgsField('nome', QVariant.String)]

poligono.dataProvider().addAttributes(fields)

poligono.updateFields()

pontos_list = [
    QgsPointXY(-36.29812, -7.33219),
    QgsPointXY(-36.29345,-6.85121),
    QgsPointXY(-35.84049,-6.83253),
    QgsPointXY(-35.88830,-7.29987)
]

geom = QgsGeometry.fromPolygonXY([pontos_list])

feature = QgsFeature(poligono.fields())

feature.setAttributes([1, 'Polígono de teste...'])

feature.setGeometry(geom)

poligono.dataProvider().addFeature(feature)

poligono.updateFields()

poligono.updateExtents()

iface.mapCanvas().refresh()

iface.mapCanvas().setExtent(poligono.extent().buffered(0.3))

iface.mapCanvas().refresh()