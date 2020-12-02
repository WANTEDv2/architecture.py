import sys

from PyQt5.QtWidgets import QApplication

from application_services.implements.create_dvd import CreateOrUpdateDvd
from application_services.implements.get_all_dvd import GetAllDvd
from application_services.implements.remove_dvd import RemoveDvd
from infrastructure.data_access.dvd_repository import DvdRepository
from ui.presenter.dvd_presenter import DvdPresenter

from ui.views.q_dvd_main import QDvdMain

app = QApplication(sys.argv)
main_win = QDvdMain()

repository = DvdRepository()
c = CreateOrUpdateDvd(repository)
presenter = DvdPresenter(main_win, c, c, GetAllDvd(repository), RemoveDvd(repository))
main_win.show()
app.exec()