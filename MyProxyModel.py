from PyQt5.QtCore import QSortFilterProxyModel


# устанавливаем свою модель для поиска в бд
class MyProxyModel(QSortFilterProxyModel):
    def filterAcceptsRow(self, source_row, source_parent):
        # Функция, которая определяет, будет ли строка отображаться в модели
        for column in range(self.sourceModel().columnCount()):
            if self.filterAcceptsCell(source_row, column, source_parent):
                return True
        return False

    def filterAcceptsCell(self, row, column, parent):
        # Функция, которая определяет, будет ли ячейка отображаться в модели
        source_index = self.sourceModel().index(row, column, parent)
        data = self.sourceModel().data(source_index)
        filter_string = self.filterRegExp().pattern()
        if filter_string == "":
            return True
        elif filter_string in data:
            return True
        else:
            return False
