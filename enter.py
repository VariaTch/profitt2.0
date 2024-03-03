import sys

from PyQt5.QtGui import QStandardItemModel, QStandardItem, QDesktopServices, QTextDocument
from PyQt5.QtPrintSupport import QPrintPreviewDialog, QPrintDialog, QPrinter
import pymysql
from config1 import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableView, QTableWidget, QTableWidgetItem, QPlainTextEdit, \
    QTextEdit, QMenu, QMenuBar, QFileDialog, QFileSystemModel, QFrame, QTreeView, QHeaderView, QLineEdit, QVBoxLayout, \
    QDialog, QAbstractItemView, QWidget, qApp
from PyQt5.QtCore import QPropertyAnimation, QAbstractTableModel, QModelIndex, QFile, QTextStream, QDir, \
    QSortFilterProxyModel, QFileInfo, QRegExp, QUrl, QObject, pyqtSignal
from design import *
from design_light import Ui_MainWindow_light
import subprocess

from main import MyProxyModel


class MainWindow_light(QMainWindow):

    def __init__(self, parent=None):
        super().__init__()
        QMainWindow.__init__(self)
        self.ui_m = Ui_MainWindow_light()
        self.ui_m.setupUi(self)

        self.ui_m.Btn_Toggle.clicked.connect(lambda: self.toggleMenu(250, True))

        # page View
        self.ui_m.Btn_menu_2.clicked.connect(lambda: self.ui_m.Pages_Widget.setCurrentWidget(self.ui_m.page_2))
        # page Blocks
        self.ui_m.Btn_menu_4.clicked.connect(lambda: self.ui_m.Pages_Widget.setCurrentWidget(self.ui_m.page_9))
        # page People
        self.ui_m.Btn_menu_5.clicked.connect(lambda: self.ui_m.Pages_Widget.setCurrentWidget(self.ui_m.page_8))
        # page SCH/PCB
        self.ui_m.Btn_menu_6.clicked.connect(lambda: self.ui_m.Pages_Widget.setCurrentWidget(self.ui_m.page_11))

        self.show()

        self.ui_m.pb_preview.clicked.connect(self.open_new_window_print)
        self.ui_m.pb_print.clicked.connect(self.handlePreview)

        # кнопки на странице BLOCKS
        self.ui_m.pb_create_file_sostav.clicked.connect(self.btn_tracking_on_blocks)

        # вывод бд
        self.create_connection_1()
        self.connect_people_base()
        self.connect_blocks_base()
        self.connect_sch_pcb_base()

        # обновление бд по нажатию кнопки
        self.ui_m.Btn_menu_2.clicked.connect(self.create_connection_1)
        self.ui_m.Btn_menu_5.clicked.connect(self.connect_people_base)
        self.ui_m.Btn_menu_4.clicked.connect(self.connect_blocks_base)
        self.ui_m.Btn_menu_6.clicked.connect(self.connect_sch_pcb_base)

        # открытие файлов по двойному клику
        self.ui_m.tableView.doubleClicked.connect(self.go_to_file)

    def create_file_sostav(self):
        try:
            connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            selected_id = self.get_selected_cells()
            mycursor = connection.cursor()
            all_results = []
            for id in selected_id:       # идем по списку id
                query = 'SELECT b.block_code, b.block_name, s.decimal_num_sch, s.author_sch, s.dec_num_pcb, ' \
                        's.author_pcb, b.date, b.notes FROM blocks b JOIN sch s ON b.sch = s.decimal_num_sch WHERE b.id =%s'
                value = id
                mycursor.execute(query, value)   # по id вытаскиваем строку из базы
                result = mycursor.fetchall()
                all_results.extend(result)
            fname = QFileDialog.getSaveFileName(self)[0] # открывается окно сохранения
            lists = []
            try:
                for i in all_results:
                    item = [i['block_code'], i['block_name'], i['decimal_num_sch'], i['author_sch'], i['dec_num_pcb'], i['author_pcb'], i['date']]  # из словаря строки вытаскиваем только нужную информацию
                    item = item + ['____________________']
                    lists.append(item)
                print(lists)
                with open(fname, 'w') as file:
                    for lst in lists:
                        for item in lst:
                            file.write(str(item)+'\n')
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)

    def get_selected_cells(self):
        self.ui_m.tableView_2.setSelectionMode(QAbstractItemView.MultiSelection)
        self.selection_model_new = self.ui_m.tableView_2.selectionModel()
        selected_indexes = self.ui_m.tableView_2.selectedIndexes()
        selected_cells = []
        for index in selected_indexes:
            selected_cells.append(str(self.ui_m.tableView_2.model().data(index)))
            print(selected_cells)
        return selected_cells

    def get_selected_cells_all(self):
        self.ui_m.tableView.setSelectionMode(QAbstractItemView.MultiSelection)
        self.selection_model_all_new = self.ui_m.tableView.selectionModel()
        selected_indexes = self.ui_m.tableView.selectedIndexes()
        selected_cells = []
        for index in selected_indexes:
            selected_cells.append(str(self.ui_m.tableView.model().data(index)))
            print(selected_cells)
        return selected_cells

    def open_new_window_print(self):
        try:
            sender = self.sender()
            if sender.text() == "Распечатать":
                self.ui_m.pb_preview.clicked.connect(self.handlePreview_new_window)
        except Exception as e:
            print(e)

    def handlePreview_new_window(self):
        try:
            dialog = QPrintPreviewDialog()
            dialog.paintRequested.connect(self.handlePaintRequest_nw)
            dialog.exec_()
        except Exception as e:
            print(e)

    def handlePaintRequest_nw(self, printer):
        try:
            connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("successfully connected...")
            selected_id = self.get_selected_cells_all()
            mycursor = connection.cursor()
            all_results = []
            for id in selected_id:  # идем по списку id
                query = "SELECT id, device_code, device_name, id_decimal_number_vipr, desc_name, " \
                        "sost_name, design_name, software_name, id_developer, id_designer, id_programmer, " \
                        "date FROM devices WHERE id=%s;"
                value = id
                mycursor.execute(query, value)  # по id вытаскиваем строку из базы
                result = mycursor.fetchall()
                print(result)
                all_results.extend(result)
            print(all_results)  # список всех строк-словариков
            document = QtGui.QTextDocument()
            cursor = QtGui.QTextCursor(document)
            i = len(all_results)
            table = cursor.insertTable(i, 12)
            lists = []
            try:
                for i in all_results:
                    item = [i['id'], i['device_code'], i['device_name'], i['id_decimal_number_vipr'], i['desc_name'],
                            i['sost_name'], i['design_name'], i['software_name'], i['id_developer'], i['id_designer'],
                            i['id_programmer'], i['date']]  # из словаря строки вытаскиваем только нужную информацию
                    lists.append(item)
                print(lists)
                for lst in lists:
                    for item in lst:
                        cursor.insertText(str(item))
                        cursor.movePosition(QtGui.QTextCursor.NextCell)
                document.print_(printer)
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)

    # функция анимации меню
    def toggleMenu(self, maxWidth, enable):
        if enable:
            # GET WIDTH
            width = self.ui_m.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70
            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard
            # ANIMATION
            self.animation = QPropertyAnimation(self.ui_m.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    ###########################################

    # трекер кнопок страницы блоков
    def btn_tracking_on_blocks(self):
        sender = self.sender()
        if sender.text() == "Create SOSTAV":
            self.ui_m.pb_create_file_sostav.clicked.connect(self.create_file_sostav)
            print('sos')

    # соединение
    def connect_sch_pcb_base(self):
        try:
            connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("successfully connected...")
            mycursor = connection.cursor()
            mycursor.execute("SELECT id, decimal_num_sch, author_sch, dec_num_pcb, author_pcb FROM sch;")
            result = mycursor.fetchall()
            self.model_data_sch_new = QStandardItemModel()
            self.model_data_sch_new.setHorizontalHeaderLabels(['ID', 'SCH', 'Автор схемы', 'PCB', 'Автор платы'])
            for e in result:
                self.model_data_sch_new.appendRow([
                    QtGui.QStandardItem(str(e['id'])),
                    QtGui.QStandardItem(str(e['decimal_num_sch'])),
                    QtGui.QStandardItem(str(e['author_sch'])),
                    QtGui.QStandardItem(str(e['dec_num_pcb'])),
                    QtGui.QStandardItem(str(e['author_pcb'])),
                    ])
            self.ui_m.tableView_sch.setModel(self.model_data_sch_new)
            self.proxy_model_sch_new= MyProxyModel()
            self.proxy_model_sch_new.setSourceModel(self.model_data_sch_new)
            self.ui_m.tableView_sch.setModel(self.proxy_model_sch_new)

            self.ui_m.lineEdit_search_sch.textChanged.connect(self.search_in_all_columns)
        except Exception as error:
            print("Не удалось установить соединение с базой данных MySQL:{}".format(error))
        finally:
            with connection.cursor() as cursor:
                cursor.close()
                connection.close()

    # КНОПКИ СТРАНИЦЫ БЛОКИ
    # соединение
    def connect_blocks_base(self):
        try:
            connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("successfully connected...")
            mycursor = connection.cursor()
            mycursor.execute('SELECT b.id, b.block_code, b.block_name, s.decimal_num_sch, s.author_sch, s.dec_num_pcb, '
                             's.author_pcb, b.date, b.notes FROM blocks b JOIN sch s ON b.sch = s.decimal_num_sch;')
            result = mycursor.fetchall()
            self.model_data_blocks_new = QStandardItemModel()
            self.model_data_blocks_new.setHorizontalHeaderLabels(['ID', 'Шифр', 'Название', 'SCH', 'Автор схемы', 'PCB',
                                                              'Автор платы', 'Дата', 'Примечание'])
            for e in result:
                self.model_data_blocks_new.appendRow([
                    QtGui.QStandardItem(str(e['id'])),
                    QtGui.QStandardItem(str(e['block_code'])),
                    QtGui.QStandardItem(str(e['block_name'])),
                    QtGui.QStandardItem(str(e['decimal_num_sch'])),
                    QtGui.QStandardItem(str(e['author_sch'])),
                    QtGui.QStandardItem(str(e['dec_num_pcb'])),
                    QtGui.QStandardItem(str(e['author_pcb'])),
                    QtGui.QStandardItem(str(e['date'])),
                    QtGui.QStandardItem(str(e['notes'])),
                    ])
            self.ui_m.tableView_2.setModel(self.model_data_blocks_new)
            self.proxy_model_blocks_new = MyProxyModel()
            self.proxy_model_blocks_new.setSourceModel(self.model_data_blocks_new)
            self.ui_m.tableView_2.setModel(self.proxy_model_blocks_new)

            self.ui_m.le_search_blocks.textChanged.connect(self.search_in_all_columns)
        except Exception as error:
            print("Не удалось установить соединение с базой данных MySQL:{}".format(error))
        finally:
            with connection.cursor() as cursor:
                cursor.close()
                connection.close()

    # КНОПКИ СТРАНИЦЫ ЛЮДИ
    # соединение
    def connect_people_base(self):
        try:
            connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("successfully connected...")
            mycursor = connection.cursor()
            mycursor.execute("SELECT id, first_name, last_name, job_title FROM users;")
            result = mycursor.fetchall()
            self.model_data_people_new = QStandardItemModel()
            self.model_data_people_new.setHorizontalHeaderLabels(['ID', 'Имя', 'Фамилия', 'Должность'])
            for e in result:
                self.model_data_people_new.appendRow([
                    QtGui.QStandardItem(str(e['id'])),
                    QtGui.QStandardItem(str(e['first_name'])),
                    QtGui.QStandardItem(str(e['last_name'])),
                    QtGui.QStandardItem(str(e['job_title']))])
            self.ui_m.tableView_3.setModel(self.model_data_people_new)

        except Exception as error:
            print("Не удалось установить соединение с базой данных MySQL:{}".format(error))
        finally:
            with connection.cursor() as cursor:
                cursor.close()
                connection.close()

    def create_connection_1(self):
        try:
            connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("successfully connected...")
            mycursor = connection.cursor()
            mycursor.execute("SELECT id, device_code, device_name, id_decimal_number_vipr, desc_name, "
                             " sost_name, design_name, software_name, id_developer, id_designer, id_programmer, "
                             "date_format(date, '%d.%m.%Y') as date FROM devices;")
            result = mycursor.fetchall()

            self.model_data_new = QStandardItemModel()
            self.model_data_new.setHorizontalHeaderLabels(['ID', 'Code', 'Name', 'DecNum', 'Desc',
                                                       'Sostav', 'Design', 'Soft',
                                                       'Developer', 'Designer', 'Progr', 'Date'])

            for e in result:
                self.model_data_new.appendRow([
                    QtGui.QStandardItem(str(e['id'])),
                    QtGui.QStandardItem(str(e['device_code'])),
                    QtGui.QStandardItem(str(e['device_name'])),
                    QtGui.QStandardItem(str(e['id_decimal_number_vipr'])),
                    QtGui.QStandardItem(str(e['desc_name'])),
                    QtGui.QStandardItem(str(e['sost_name'])),
                    QtGui.QStandardItem(str(e['design_name'])),
                    QtGui.QStandardItem(str(e['software_name'])),
                    QtGui.QStandardItem(str(e['id_developer'])),
                    QtGui.QStandardItem(str(e['id_designer'])),
                    QtGui.QStandardItem(str(e['id_programmer'])),
                    QtGui.QStandardItem(str(e['date']))])

            self.ui_m.tableView.setModel(self.model_data_new)

            self.proxy_model_new = MyProxyModel()
            self.proxy_model_new.setSourceModel(self.model_data_new)
            self.ui_m.tableView.setModel(self.proxy_model_new)

            self.ui_m.lineEdit_filter.textChanged.connect(self.search_in_all_columns)

        except Exception as error:
            print("Не удалось установить соединение с базой данных MySQL:{}".format(error))
        finally:
            with connection.cursor() as cursor:
                cursor.close()
                connection.close()

    def setFilterRegExp(self, pattern):
        # Функция для установки регулярного выражения фильтрации
        self.proxy_model_new.setFilterRegExp(pattern)
        self.proxy_model_new.invalidateFilter()

    # ФУНКЦИЯ ПОИСКА ПО ТАБЛИЦЕ
    def search_in_all_columns(self, search_text):
        num_columns = self.model_data_new.columnCount()
        num_columns_blocks = self.model_data_blocks_new.columnCount()
        num_columns_sch = self.model_data_sch_new.columnCount()
        self.proxy_model_new.setFilterRegExp(search_text)
        self.proxy_model_blocks_new.setFilterRegExp(search_text)
        self.proxy_model_sch_new.setFilterRegExp(search_text)

        # Очищаем текущее выделение
        self.ui_m.tableView.clearSelection()
        self.ui_m.tableView_2.clearSelection()
        self.ui_m.tableView_sch.clearSelection()

        for column in range(num_columns):
            # Устанавливаем флаг выделения для текущей колонки
            self.ui_m.tableView.selectColumn(column)
            # Получаем выделенные ячейки
            selected_indexes = self.ui_m.tableView.selectedIndexes()
            # Перебираем выделенные ячейки и сравниваем содержимое с введенным текстом
            for index in selected_indexes:
                item = self.model_data_new.itemFromIndex(index)
                if item and search_text in item.text():
                    # Если найдено соответствие, то выделяем ячейку
                    self.ui_m.tableView.setCurrentIndex(index)
                    self.ui_m.tableView.scrollTo(index)
                    return
            # Сбрасываем флаг выделения для текущей колонки
            self.ui_m.tableView.clearSelection()

        for column in range(num_columns_blocks):
            # Устанавливаем флаг выделения для текущей колонки
            self.ui_m.tableView_2.selectColumn(column)
            # Получаем выделенные ячейки
            selected_indexes = self.ui_m.tableView_2.selectedIndexes()
            # Перебираем выделенные ячейки и сравниваем содержимое с введенным текстом
            for index in selected_indexes:
                item = self.model_data_blocks_new.itemFromIndex(index)
                if item and search_text in item.text():
                    # Если найдено соответствие, то выделяем ячейку
                    self.ui_m.tableView_2.setCurrentIndex(index)
                    self.ui_m.tableView_2.scrollTo(index)
                    return
            # Сбрасываем флаг выделения для текущей колонки
            self.ui_m.tableView_2.clearSelection()

        for column in range(num_columns_sch):
            # Устанавливаем флаг выделения для текущей колонки
            self.ui_m.tableView_sch.selectColumn(column)
            # Получаем выделенные ячейки
            selected_indexes = self.ui_m.tableView_sch.selectedIndexes()
            # Перебираем выделенные ячейки и сравниваем содержимое с введенным текстом
            for index in selected_indexes:
                item = self.model_data_sch_new.itemFromIndex(index)
                if item and search_text in item.text():
                    # Если найдено соответствие, то выделяем ячейку
                    self.ui_m.tableView_sch.setCurrentIndex(index)
                    self.ui_m.tableView_sch.scrollTo(index)
                    return
            # Сбрасываем флаг выделения для текущей колонки
            self.ui_m.tableView_sch.clearSelection()

    # ФУНКЦИЯ ДЛЯ ОТКРЫВАНИЯ ФАЙЛА ЧЕРЕЗ ТАБЛИЦУ
    def go_to_file(self, index):
        try:
            connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("successfully connected...")
            selected_index = self.ui_m.tableView.selectedIndexes()[0]
            row = selected_index.row()
            column = selected_index.column()

            if column == 5:
                sost_name = str(self.ui_m.tableView.model().data(selected_index))
                mycursor = connection.cursor()
                query = "SELECT id_sostav FROM devices WHERE sost_name=%s;"
                values = sost_name
                mycursor.execute(query, values)
                result = mycursor.fetchall()
                for i in result:
                    print(i['id_sostav'])
                    item = i['id_sostav']
                    if item is not None:
                        subprocess.call(['start', '', item], shell=True)
            if column == 4:
                desc_name = str(self.ui_m.tableView.model().data(selected_index))
                mycursor = connection.cursor()
                query = "SELECT description FROM devices WHERE desc_name=%s;"
                values = desc_name
                mycursor.execute(query, values)
                result = mycursor.fetchall()
                for i in result:
                    print(i['description'])
                    item = i['description']
                    if item is not None:
                        subprocess.call(['start', '', item], shell=True)
            if column == 6:
                design_name = str(self.ui_m.tableView.model().data(selected_index))
                mycursor = connection.cursor()
                query = "SELECT id_engineering_design FROM devices WHERE design_name=%s;"
                values = design_name
                mycursor.execute(query, values)
                result = mycursor.fetchall()
                for i in result:
                    print(i['id_engineering_design'])
                    item = i['id_engineering_design']
                    if item is not None:
                        subprocess.call(['start', '', item], shell=True)
            if column == 7:
                software_name = str(self.ui_m.tableView.model().data(selected_index))
                mycursor = connection.cursor()
                query = "SELECT id_software FROM devices WHERE software_name=%s;"
                values = software_name
                mycursor.execute(query, values)
                result = mycursor.fetchall()
                for i in result:
                    print(i['id_software'])
                    item = i['id_software']
                    if item is not None:
                        subprocess.call(['start', '', item], shell=True)

        except Exception as e:
            print(e)

    ###########################################
    #  3 ФУНКЦИИ ДЛЯ ПРОСМОТРА И ПЕЧАТИ БД
    def handlePrint(self):
        try:
            dialog = QPrintDialog()
            if dialog.exec_() == QDialog.Accepted:
                self.handlePaintRequest(dialog.printer())
        except Exception as e:
            print(e)

    def handlePreview(self):
        try:
            dialog = QPrintPreviewDialog()
            dialog.paintRequested.connect(self.handlePaintRequest)
            dialog.exec_()
        except Exception as e:
            print(e)

    def handlePaintRequest(self, printer):
        document = QtGui.QTextDocument()
        cursor = QtGui.QTextCursor(document)
        table = cursor.insertTable(self.model_data_new.rowCount(), self.model_data_new.columnCount())
        for row in range(table.rows()):
            for column in range(table.columns()):
                cursor.insertText(self.model_data_new.item(row, column).text())
                cursor.movePosition(QtGui.QTextCursor.NextCell)
        document.print_(printer)
    ###########################################

    @staticmethod
    def return_to_login():
        try:
            QtCore.QCoreApplication.quit()
            status = QtCore.QProcess.startDetached(sys.executable, sys.argv)
            print(status)
        except Exception as e:
            print(e)
