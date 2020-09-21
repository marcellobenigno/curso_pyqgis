# encoding: utf-8
# -----------------------------------------------------------
# Copyright (C) 2018 Matthias Kuhn
# -----------------------------------------------------------
# Licensed under the terms of GNU GPL 2
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# ---------------------------------------------------------------------

from qgis.core import QgsProject
from PyQt5 import uic
import os
from qgis.core import QgsVectorLayer

DialogBase, DialogType = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'geometry_operation_dialog_base.ui'))


class GeometryOperationDialog(DialogType, DialogBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.loadLayers()

        self.bufferButton.clicked.connect(self.buffer)

    def loadLayers(self):
        """
        Load all layers from the project and show them in the combobox
        """
        for layer in QgsProject.instance().mapLayers().values():
            self.layerComboBox.addItem(layer.name(), layer)

    def buffer(self):
        """
        Buffer all geometries of the input layer and copy attributes.
        Everything is put into a new temporary scratch memory layer.
        """

        # Get the layer from the combobox
        layer = self.layerComboBox.currentData()
        # Get the buffer size value
        buffer_size = self.bufferSize.value()

        # Create a new scratch layer based on the original layer
        uri = "Polygon?crs={authid}&index=yes".format(authid=layer.crs().authid())
        layer_name = "Buffer ({layername})".format(layername=layer.name())
        new_layer = QgsVectorLayer(uri, layer_name, "memory")

        new_layer.startEditing()

        # Add all attribute definitions from the source layer
        for field in layer.fields():
            new_layer.addAttribute(field)

        # Process all features
        for feature in layer.getFeatures():
            # Here is the important call: create a buffer
            geom = feature.geometry().buffer(buffer_size, 5)

            feature.setGeometry(geom)
            new_layer.addFeature(feature)

        # Save the features to the memory layer
        new_layer.commitChanges()

        QgsProject.instance().addMapLayer(new_layer)