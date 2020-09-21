
# a python script as a layer action to reverse a line

# get the layer you are working on
layer = QgsProject.instance().mapLayer("_your_layer_id_")

# create a feature request with the specific id of the feature
r = QgsFeatureRequest([% $id %])

features = layer.getFeatures(r)

# obviously, there should be a single result
feature = next(features)

if feature.isValid():
    # Reverse the line
    geom = QgsGeometry(feature.geometry().constGet().reversed())

    # update the geometry of the feature at the given id
    if layer.changeGeometry([% $id %], geom):
        # display a message in case of success
        qgis.utils.iface.messageBar().pushMessage("Line swaped", Qgis.Info, 2)
        layer.triggerRepaint()
    else:
        # otherwise, ask to turn the layer editing on
        # programmaticaly it would be layer.startEditing()
        qgis.utils.iface.messageBar().pushMessage("Cannot swap line. Turn editing on.", Qgis.Warning, 3)
else:
    qgis.utils.iface.messageBar().pushMessage("Feature not found. This is weird", Qgis.Critical, 3)
