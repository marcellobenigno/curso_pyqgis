<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis readOnly="0" styleCategories="AllStyleCategories" hasScaleBasedVisibilityFlag="0" labelsEnabled="0" simplifyAlgorithm="0" simplifyLocal="1" minScale="1e+08" simplifyDrawingHints="1" simplifyDrawingTol="1" maxScale="0" simplifyMaxScale="1" version="3.6.2-Noosa">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 symbollevels="0" forceraster="0" type="singleSymbol" enableorderby="0">
    <symbols>
      <symbol name="0" force_rhr="0" type="fill" clip_to_extent="1" alpha="1">
        <layer locked="0" class="SimpleFill" pass="0" enabled="1">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="169,239,127,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="37,148,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.4" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <customproperties>
    <property value="0" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory minimumSize="0" backgroundColor="#ffffff" rotationOffset="270" penWidth="0" backgroundAlpha="255" sizeType="MM" scaleBasedVisibility="0" penColor="#000000" minScaleDenominator="0" diagramOrientation="Up" scaleDependency="Area" height="15" lineSizeScale="3x:0,0,0,0,0,0" lineSizeType="MM" penAlpha="255" sizeScale="3x:0,0,0,0,0,0" labelPlacementMethod="XHeight" opacity="1" enabled="0" width="15" barWidth="5" maxScaleDenominator="1e+08">
      <fontProperties style="" description=".SF NS Text,13,-1,5,50,0,0,0,0,0"/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings dist="0" placement="1" linePlacementFlags="18" showAll="1" priority="0" obstacle="0" zIndex="0">
    <properties>
      <Option type="Map">
        <Option value="" name="name" type="QString"/>
        <Option name="properties"/>
        <Option value="collection" name="type" type="QString"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <fieldConfiguration>
    <field name="fid">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="nome">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="cod_ibge_m">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="area_km2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="slug">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sigla_uf">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="visivel">
      <editWidget type="CheckBox">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="estado_id">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="delegacia_id">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="area_ha">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias field="fid" name="" index="0"/>
    <alias field="nome" name="" index="1"/>
    <alias field="cod_ibge_m" name="" index="2"/>
    <alias field="area_km2" name="" index="3"/>
    <alias field="slug" name="" index="4"/>
    <alias field="sigla_uf" name="" index="5"/>
    <alias field="visivel" name="" index="6"/>
    <alias field="estado_id" name="" index="7"/>
    <alias field="delegacia_id" name="" index="8"/>
    <alias field="area_ha" name="" index="9"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default expression="" field="fid" applyOnUpdate="0"/>
    <default expression="" field="nome" applyOnUpdate="0"/>
    <default expression="" field="cod_ibge_m" applyOnUpdate="0"/>
    <default expression="" field="area_km2" applyOnUpdate="0"/>
    <default expression="" field="slug" applyOnUpdate="0"/>
    <default expression="" field="sigla_uf" applyOnUpdate="0"/>
    <default expression="" field="visivel" applyOnUpdate="0"/>
    <default expression="" field="estado_id" applyOnUpdate="0"/>
    <default expression="" field="delegacia_id" applyOnUpdate="0"/>
    <default expression="" field="area_ha" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint constraints="3" notnull_strength="1" exp_strength="0" field="fid" unique_strength="1"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="nome" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="cod_ibge_m" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="area_km2" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="slug" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="sigla_uf" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="visivel" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="estado_id" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="delegacia_id" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="area_ha" unique_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="fid" desc="" exp=""/>
    <constraint field="nome" desc="" exp=""/>
    <constraint field="cod_ibge_m" desc="" exp=""/>
    <constraint field="area_km2" desc="" exp=""/>
    <constraint field="slug" desc="" exp=""/>
    <constraint field="sigla_uf" desc="" exp=""/>
    <constraint field="visivel" desc="" exp=""/>
    <constraint field="estado_id" desc="" exp=""/>
    <constraint field="delegacia_id" desc="" exp=""/>
    <constraint field="area_ha" desc="" exp=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig sortOrder="0" sortExpression="" actionWidgetStyle="dropDown">
    <columns>
      <column width="-1" name="fid" type="field" hidden="0"/>
      <column width="-1" name="nome" type="field" hidden="0"/>
      <column width="-1" name="cod_ibge_m" type="field" hidden="0"/>
      <column width="-1" name="area_km2" type="field" hidden="0"/>
      <column width="-1" name="slug" type="field" hidden="0"/>
      <column width="-1" name="sigla_uf" type="field" hidden="0"/>
      <column width="-1" name="visivel" type="field" hidden="0"/>
      <column width="-1" name="estado_id" type="field" hidden="0"/>
      <column width="-1" name="delegacia_id" type="field" hidden="0"/>
      <column width="-1" name="area_ha" type="field" hidden="0"/>
      <column width="-1" type="actions" hidden="1"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
QGIS forms can have a Python function that is called when the form is
opened.

Use this function to add extra logic to your forms.

Enter the name of the function in the "Python Init function"
field.
An example follows:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field name="area_ha" editable="1"/>
    <field name="area_km2" editable="1"/>
    <field name="cod_ibge_m" editable="1"/>
    <field name="delegacia_id" editable="1"/>
    <field name="estado_id" editable="1"/>
    <field name="fid" editable="1"/>
    <field name="nome" editable="1"/>
    <field name="sigla_uf" editable="1"/>
    <field name="slug" editable="1"/>
    <field name="visivel" editable="1"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="area_ha"/>
    <field labelOnTop="0" name="area_km2"/>
    <field labelOnTop="0" name="cod_ibge_m"/>
    <field labelOnTop="0" name="delegacia_id"/>
    <field labelOnTop="0" name="estado_id"/>
    <field labelOnTop="0" name="fid"/>
    <field labelOnTop="0" name="nome"/>
    <field labelOnTop="0" name="sigla_uf"/>
    <field labelOnTop="0" name="slug"/>
    <field labelOnTop="0" name="visivel"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>fid</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
