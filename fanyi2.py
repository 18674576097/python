import sys
from fanyi import *
import urllib.request
import urllib.parse
import time
import json


if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


