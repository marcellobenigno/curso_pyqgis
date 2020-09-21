sedes = QgsProject.instance().mapLayersByName('sedes')[0]

root = QgsProject.instance().layerTreeRoot()
for ch in root.children():
    if ch.name() == sedes.name():
        _ch = ch.clone()
        root.insertChildNode(0, _ch)
        root.removeChildNode(ch)