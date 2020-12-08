import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QApplication



class QDvdEdit(QDialog):
    def __init__(self, parent, name=''):
        super().__init__(parent)
        uic.loadUi("views/dvd_edit.ui", self)
        self.name_edit.setText(name)




    def get_current_name(self):
        return self.dvd_edit.text()
    if __name__ == '__main__':
        app=QApplication(sys.argv)
        dialog = QDialog(None)
        app.exec()