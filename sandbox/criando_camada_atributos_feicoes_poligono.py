lyr_pol = QgsVectorLayer("Polygon?crs=epsg:4326", "area_teste", "memory")

QgsProject.instance().addMapLayer(lyr_pol)

dp_lyr_pol = lyr_pol.dataProvider()

fields = [QgsField('id', QVariant.Int), QgsField('nome', QVariant.String)]

lyr_pol.dataProvider().addAttributes(fields)

lyr_pol.updateFields()

ponto_1 = QgsPointXY(-36.29812, -7.33219)

ponto_2 = QgsPointXY(-36.29345,-6.85121)

ponto_3 = QgsPointXY(-35.84049,-6.83253)

ponto_4 = QgsPointXY(-35.88830,-7.29987)

pol_1 = QgsGeometry.fromPolygonXY([[ponto_1, ponto_2, ponto_3, ponto_4]])

feature = QgsFeature(lyr_pol.fields())

feature.setAttributes([1, 'teste'])

feature.setGeometry(pol_1)

lyr_pol.dataProvider().addFeature(feature)

lyr_pol.updateExtents()

iface.mapCanvas().refresh()