from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class QDvdMain(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("views/dvd_main.ui", self)

    def connect_add(self, slot):
        self.add_btn.clicked.connect(slot)


    def connect_del(self, slot):
        self.del_btn.clicked.connect(slot)

    def connect_edit(self, slot):
        self.edit_btn.clicked.connect(slot)

    def set_dvd(self, dvds):
        self.dvd_list.clear()
        for i in dvds:
            self.dvd_list.addItem(i['name'])

    def get_current_dvd_index(self):
        return self.dvd_list.currentRow()