path = '/Users/marcellodebarrosfilho/code/script_cod_ibge_m/dados.gpkg|layername=imoveis'

lyr = QgsVectorLayer(path, 'imoveis', 'ogr')

exp = '"fid"=2244'

sel = lyr.getFeatures(QgsFeatureRequest().setFilterExpression(exp))

with edit(lyr):
    for feature in sel:
        feature["nome_area"] = "Test name"
        lyr.updateFeature(feature)
    
    
for feat in lyr.getFeatures():
    if feat['fid'] == 2244:
        print(feat['nome_area'])
