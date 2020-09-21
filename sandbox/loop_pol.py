lyr = iface.mapCanvas().currentLayer()

#for feat in lyr.getFeatures():
#    geom_txt = (feat.geometry().asWkt().\
#        replace('Polygon ', '').
#        replace('))', '').\
#        replace('((', '')
#    )
#    geom_lst = geom_txt.split(',')


for feat in lyr.getFeatures():
    geom = feat.geometry().asPolygon()[0]