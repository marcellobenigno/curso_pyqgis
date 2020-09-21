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

DialogBase, DialogType = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'geometry_operation_dialog_base.ui'))


class GeometryOperationDialog(DialogType, DialogBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.loadLayers()

    def loadLayers(self):
        """
        Load all layers from the project and show them in the combobox
        """
        for layer in QgsProject.instance().mapLayers().values():
            self.layerComboBox.addItem(layer.name(), layer)
