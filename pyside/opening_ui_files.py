
import sys
from PySide import QtUiTools
from PySide.QtGui import *

app = QApplication(sys.argv)
window = QtUiTools.QUiLoader().load("interface.ui")
window.show()
sys.exit(app.exec_())