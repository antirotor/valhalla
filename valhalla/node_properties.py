from Qt import QtCore, QtWidgets, QtGui


class TableWidgetHeaderItem(QtWidgets.QTableWidgetItem):
    """ Read only cells in QTableWidget. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
        self.setBackground(QtGui.QColor(230, 230, 230))


class PropertiesWindow(QtWidgets.QWidget):
    """
    This defines node properties window. Input ports that are not
    connected and are of some primitive type (like float, int, str, etc.) will
    be editable. When connected, editing will be disabled as values are then
    defined by connecting node.
    """

    def __init__(self, node):
        QtWidgets.QWidget.__init__(self)
        self._node = node
        self.setWindowTitle(node.getName())
        self.setLayout(QtWidgets.QVBoxLayout())
        self._layout = self.layout()
        self._table = QtWidgets.QTableWidget()
        self._table.setColumnCount(2)
        self._table.setHorizontalHeaderLabels(['Port', 'Value'])
        self._table.horizontalHeader().setStretchLastSection(True)
        self._table.verticalHeader().setVisible(False)
        self._process_table()
        self._layout.addWidget(self._table)
        self.show()

    def _process_table(self):
        """
        fill in table data
        """
        pos = self._table.rowCount()
        self._table.insertRow(pos)
        self._table.setItem(pos, 0, TableWidgetHeaderItem("name"))
        self._table.setItem(pos, 1, TableWidgetHeaderItem(
            self._node.getName()))
        pos += 1
        self._table.insertRow(pos)
        self._table.setItem(pos, 0, TableWidgetHeaderItem("category"))
        self._table.setItem(pos, 1, QtWidgets.QTableWidgetItem(
            self._node._parent.get_category()))
        pos += 1
        self._table.insertRow(pos)
        self._table.setItem(pos, 0, TableWidgetHeaderItem("type uuid"))
        self._table.setItem(pos, 1, QtWidgets.QTableWidgetItem(
            self._node._parent.id))
