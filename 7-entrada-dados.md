# 7. Entrada de Dados

## 7.1 O Problema

O QGIS não permite a entrada de dados através da função `input()`.

```python
valor = input('digite o valor: ' )
digite o valor: Traceback (most recent call last):
  File "/Applications/QGIS.app/Contents/MacOS/../Resources/python/code.py", line 90, in runcode
    exec(code, self.locals)
  File "<input>", line 1, in <module>
EOFError: EOF when reading a line
```

## 7.2 A Solução:

```python
field_msg = QInputDialog.getText(None, "Nome do Campo" ,"Digite o nome do campo: ")
field = field_msg[0]
```