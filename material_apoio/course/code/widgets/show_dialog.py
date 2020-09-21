from PyQt5 import uic

# Load the .ui file
DialogUi, DialogType = uic.loadUiType('/home/mkuhn/dev/PyQGIS-course/code/widgets/dialog.ui')

# A class for logic defined in the user interface
class MyDialog(DialogType, DialogUi):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

dialog = MyDialog()

dialog.show()
# or
# dialog.exec_()
