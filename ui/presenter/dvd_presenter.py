from application_services.CreateDvd import CreateDvd
from application_services.get_all_dvd import GetAllDvd
from application_services.Remove_dvd import RemoveDvd
from application_services.UpdateDvd import UpdateDvd
from ui.views.q_dvd_edit import QDvdEdit
from ui.views.q_dvd_main import QDvdMain


class DvdPresenter:
    def __init__(self, view: QDvdMain,
                 create_dvd: CreateDvd,
                 update_dvd : UpdateDvd,
                 get_all_dvd: GetAllDvd,
                 remove_dvd: RemoveDvd):
        self.view = view
        self.create_dvd = create_dvd
        self.update_dvd = update_dvd
        self.get_all_dvd = get_all_dvd
        self.remove_dvd = remove_dvd
        self.setup()

    def setup(self):
        self.view.connect_add(self.add)
        self.view.connect_del(self.remove)
        self.view.connect_edit(self.edit)
        self.get_all()

    def open_dialog(self, cddvd: dict):
        dialog = QDvdEdit(self.view, cddvd['name'])
        if dialog.exec():
            current_name = dialog.get_current_name()
            if not cddvd['id']:
                self.create_dvd.exec({"name": current_name})
            else:
                cddvd['name'] = current_name
                self.update_dvd.exec(cddvd)
            self.get_all()

    def add(self):
        self.open_dialog({'id': None, "name": ""})

    def edit(self):
        index = self.view.get_current_dvd_index()
        self.open_dialog(self.dvds[index])

    def remove(self):
        index = self.view.get_current_dvd_index()
        self.remove_dvd.exec(index)
        self.get_all()

    def get_all(self):
        self.dvds = self.get_all_dvd.exec()         # Получение всех dvd
        self.view.set_dvds(self.dvds)
