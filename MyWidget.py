from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal


class MyWidget(QtWidgets.QStackedWidget):
    page_changed = pyqtSignal(int)  # В этом примере предполагаем, что номер страницы является целым числом

    def __init__(self):
        super().__init__()
        self.last_visited_page = 0  # Изначально устанавливаем последнюю посещенную страницу как 0

    def set_last_visited_page(self, page):
        self.last_visited_page = page
        self.page_changed.emit(page)  # Отправляем сигнал с номером последней посещенной страницы

    def get_last_visited_page(self):
        return self.last_visited_page
