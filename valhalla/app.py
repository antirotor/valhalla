import sys
from Qt import QtGui, QtWidgets, QtCore
from .main_window import MainWindow


def run():
    print('>>> running')
    app = QtWidgets.QApplication(sys.argv)
    widget = MainWindow()
    widget.show()

    sys.exit(app.exec_())