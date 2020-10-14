municipios = QgsProject.instance().mapLayersByName('municipios')[0]

pontos_interesse = QgsProject.instance().mapLayersByName('pontos_interesse')[0]

poligonos = [feat for feat in municipios.getFeatures()]

pontos = [feat for feat in pontos_interesse.getFeatures()]

pol_ids = []

for ponto in pontos:
    pt_geom = ponto.geometry()
    for pol in poligonos:
        pol_geom = pol.geometry()
        if pol_geom.contains(pt_geom):
            pol_ids.append(pol.id())

municipios.select(pol_ids)
ftsCount = municipios.selectedFeatureCount()


box = municipios.boundingBoxOfSelected()
iface.mapCanvas().setExtent(box)
iface.mapCanvas().refresh()

msgBox = QMessageBox()
msgBox.setText(f'{ftsCount} feições selecionadas')
msgBox.exec_()
