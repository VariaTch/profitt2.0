import os
from WindowLogIn import *
from enter import *
from MyWidget import *
from MyProxyModel import MyProxyModel
from CreateSostav import Creator


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.widget = MyWidget()
        self.creator = Creator()

        self.ui.Btn_Toggle.clicked.connect(lambda: self.toggleMenu(250, True))
        # page Add
        self.ui.Btn_menu_1.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_1))
        # page View
        self.ui.Btn_menu_2.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_2))
        # page Change
        self.ui.Btn_menu_3.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_3))
        # page Blocks
        self.ui.Btn_menu_4.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_9))
        # page People
        self.ui.Btn_menu_5.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_8))
        # page SCH/PCB
        self.ui.Btn_menu_6.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_11))

        self.setWindowIcon(QtGui.QIcon('ssss.png'))
        self.show()

        # self.ui.pb_exit.clicked.connect(self.return_to_login)

        # кнопки на главном меню страницы View
        self.ui.add_pushButton.clicked.connect(self.button_tracking)
        self.ui.edit_pushButton.clicked.connect(self.button_tracking)
        self.ui.delete_pushButton.clicked.connect(self.delete_element)

        self.ui.pb_preview.clicked.connect(self.open_new_window_print)
        self.ui.pb_print.clicked.connect(self.handlePreview)

        # кнопки на странице BLOCKS
        self.ui.pb_create_file_sostav.clicked.connect(self.btn_tracking_on_blocks)
        self.ui.pb_change_block_2.clicked.connect(self.btn_tracking_on_blocks)
        self.ui.pb_delete_block.clicked.connect(self.btn_tracking_on_blocks)


        # кнопки на странице PEOPLE
        self.ui.pb_delete_people.clicked.connect(self.btn_tracking_on_people)
        self.ui.pb_create_people.clicked.connect(self.btn_tracking_on_people)

        # кнопки на странице SCH/PCB
        self.ui.pb_save_sch.clicked.connect(self.btn_tracking_on_schemas)
        self.ui.pb_delete_sch.clicked.connect(self.btn_tracking_on_schemas)

        # вывод бд
        self.create_connection_1()
        self.connect_people_base()
        self.connect_blocks_base()
        self.connect_sch_pcb_base()

        # обновление бд по нажатию кнопки
        self.ui.Btn_menu_2.clicked.connect(self.create_connection_1)
        self.ui.Btn_menu_5.clicked.connect(self.connect_people_base)
        self.ui.Btn_menu_4.clicked.connect(self.connect_blocks_base)
        self.ui.Btn_menu_6.clicked.connect(self.connect_sch_pcb_base)

        # открытие файлов по двойному клику
        self.ui.tableView.doubleClicked.connect(self.go_to_file)
        # переключение на другие страницы
        self.ui.Btn_adding.clicked.connect(self.add_new_element)
        self.ui.Btn_change.clicked.connect(self.edit_element)

        # вывод папок SOSTAV
        self.ui.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.treeView.customContextMenuRequested.connect(self.context_menu_folder)
        self.open_folder_sostav()

        # вывод папок DESIGN
        self.ui.tv_choose_design.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.tv_choose_design.customContextMenuRequested.connect(self.context_menu_folder)
        self.open_design_folder()
        #self.folders_action.open_design_folder()

        # вывод папок SOFT
        self.ui.tv_choose_soft.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.tv_choose_soft.customContextMenuRequested.connect(self.context_menu_folder)
        self.open_soft_folder()
        #self.folders_action.open_soft_folder()

        # вывод в комбобоксы других таблиц
        self.getDevTypes()
        self.getDesignerTypes()
        self.getProgrammerTypes()
        self.getAllCategories()

        # # ввод описания объекта
        # self.ui.edit_add_description.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        # self.ui.edit_add_description.customContextMenuRequested.connect(self.createMenuBar)
        self.ui.pb_save_desc.clicked.connect(self.action_clicked)
        self.ui.pb_ch_save_desc.clicked.connect(self.action_clicked)

        # переход на страницу состава
        self.ui.pb_sostav.clicked.connect(self.button_tracking)
        self.ui.pb_ch_sostav.clicked.connect(self.button_tracking)
        self.ui.pb_return.clicked.connect(self.button_tracking)
        self.ui.pb_return.clicked.connect(self.sostav_folder)

        # переход на страницу дизайна
        self.ui.pb_design.clicked.connect(self.button_tracking)
        self.ui.pb_ch_design.clicked.connect(self.button_tracking)
        self.ui.pb_return_design.clicked.connect(self.button_tracking)
        self.ui.pb_return_design.clicked.connect(self.design_folder)

        # переход на страницу soft
        self.ui.pb_soft.clicked.connect(self.button_tracking)
        self.ui.pb_ch_soft.clicked.connect(self.button_tracking)
        self.ui.pb_return_soft.clicked.connect(self.button_tracking)
        self.ui.pb_return_soft.clicked.connect(self.soft_folder)

    @staticmethod
    def return_to_login():
        try:
            QtCore.QCoreApplication.quit()
            status = QtCore.QProcess.startDetached(sys.executable, sys.argv)
            print(status)
        except Exception as e:
            print(e)

    def open_new_window_print(self):
        try:
            sender = self.sender()
            if sender.text() == "Распечатать":
                self.ui.pb_preview.clicked.connect(self.handlePreview_new_window)
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
            for id in selected_id:       # идем по списку id
                query = "SELECT id, device_code, device_name, id_decimal_number_vipr, desc_name, " \
                        "sost_name, design_name, software_name, id_developer, id_designer, id_programmer, " \
                        "date FROM devices WHERE id=%s;"
                value = id
                mycursor.execute(query, value)   # по id вытаскиваем строку из базы
                result = mycursor.fetchall()
                all_results.extend(result)  # список всех строк-словариков
            document = QtGui.QTextDocument()
            cursor = QtGui.QTextCursor(document)
            i = len(all_results)
            table = cursor.insertTable(i, 12)
            lists = []
            try:
                for i in all_results:
                    item = [i['id'], i['device_code'], i['device_name'], i['id_decimal_number_vipr'], i['desc_name'],
                            i['sost_name'], i['design_name'], i['software_name'], i['id_developer'], i['id_designer'],
                            i['id_programmer'], i['date']] # из словаря строки вытаскиваем только нужную информацию
                    lists.append(item)
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
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70
            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard
            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    ###########################################
    # ДВЕ ФУНКЦИИ ДЛЯ КОНТЕКСТНОГО МЕНЮ ВСЕХ СТРАНИЦ
    # 1
    def context_menu_folder(self):
        menu = QtWidgets.QMenu()
        open = menu.addAction("Open")
        open.triggered.connect(self.open_file)
        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())

    # 2
    def open_file(self):
        index_sostav = self.ui.treeView.currentIndex()
        file_path_sostav = self.model.filePath(index_sostav)
        os.startfile(file_path_sostav)

        index_design = self.ui.tv_choose_design.currentIndex()
        file_path_design = self.model_design.filePath(index_design)
        os.startfile(file_path_design)

        index_soft = self.ui.tv_choose_soft.currentIndex()
        file_path_soft = self.model_soft.filePath(index_soft)
        os.startfile(file_path_soft)

    ###########################################
    # функции для открытия содержимого папки
    def open_folder_sostav(self):
        path = "C://Users//Varia//Documents"
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath((QtCore.QDir.rootPath()))
        self.ui.treeView.setModel(self.model)
        self.ui.treeView.setRootIndex(self.model.index(path))
        self.ui.treeView.setSortingEnabled(True)

    def sostav_folder(self):
        index = self.ui.treeView.currentIndex()
        file_path = self.model.filePath(index)
        print(file_path)
        file_name_sostav = os.path.basename(file_path)
        print(file_name_sostav)
        self.ui.edit_sostav.setText(file_name_sostav)
        self.ui.edit_ch_sostav.setText(file_name_sostav)

        return file_path

    def get_short_filename(self, file_path):
        file_name = os.path.basename(file_path)
        return file_name

    def open_design_folder(self):
        path = "//192.168.1.4"
        self.model_design = QtWidgets.QFileSystemModel()
        self.model_design.setRootPath((QtCore.QDir.rootPath()))
        self.ui.tv_choose_design.setModel(self.model_design)
        self.ui.tv_choose_design.setRootIndex(self.model_design.index(path))
        self.ui.tv_choose_design.setSortingEnabled(True)

    def design_folder(self):
        index = self.ui.tv_choose_design.currentIndex()
        file_path_design = self.model_design.filePath(index)
        print(file_path_design)
        file_name_design = os.path.basename(file_path_design)
        self.ui.edit_design.setText(file_name_design)
        self.ui.edit_ch_design.setText(file_name_design)
        return file_path_design

    def open_soft_folder(self):
        path = "//192.168.1.4"
        self.model_soft = QtWidgets.QFileSystemModel()
        self.model_soft.setRootPath((QtCore.QDir.rootPath()))
        self.ui.tv_choose_soft.setModel(self.model_soft)
        self.ui.tv_choose_soft.setRootIndex(self.model_soft.index(path))
        self.ui.tv_choose_soft.setSortingEnabled(True)

    def soft_folder(self):
        index = self.ui.tv_choose_soft.currentIndex()
        file_path_soft = self.model_soft.filePath(index)
        print(file_path_soft)
        file_name_soft = os.path.basename(file_path_soft)
        self.ui.edit_software.setText(file_name_soft)
        self.ui.edit_ch_software.setText(file_name_soft)
        return file_path_soft

        # трекер кнопок основной страницы, страниц добавления, изменения

    def button_tracking(self):
        actions = {
            "Добавить": lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_1),
            "Изменить": lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_3),
            " Выбрать состав": lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_4),
            "Изменить состав": lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_4),
            "Ок": lambda: self.ui.Pages_Widget.setCurrentIndex(self.widget.get_last_visited_page()),
            "Ok": lambda: self.ui.Pages_Widget.setCurrentIndex(self.widget.get_last_visited_page()),
            "Oк": lambda: self.ui.Pages_Widget.setCurrentIndex(self.widget.get_last_visited_page()),
            "Выбрать детали": lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_6),
            "Выбрать ПО": lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_7),
            "Изменить детали": lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_6),
            "Изменить ПО": lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_7)
        }

        sender_text = self.sender().text()
        if sender_text in actions:
            actions[sender_text]()

    # трекер кнопок страницы sch/pcb
    def btn_tracking_on_schemas(self):
        actions = {
            'Сохранить': self.add_new_sch_pcb,
            'Delete': self.delete_sch
        }
        sender_text = self.sender().text()
        action = actions.get(sender_text)
        if action:
            action()

    # трекер кнопок страницы блоков
    # Функция btn_tracking_on_blocks
    def btn_tracking_on_blocks(self):
        selected_id = self.get_selected_cells()
        actions = {
            "Create SOSTAV": lambda: self.ui.pb_create_file_sostav.clicked.connect(self.creator.create_file_sostav(selected_id)),
            "Добавить": lambda: self.ui.pb_change_block_2.clicked.connect(self.add_new_block),
            "Delete": lambda: self.ui.pb_delete_block.clicked.connect(self.delete_block)
        }

        sender_text = self.sender().text()
        action = actions.get(sender_text)
        if action:
            action()

    # Функция btn_tracking_on_people
    def btn_tracking_on_people(self):
        actions = {
            "Delete": lambda: self.ui.pb_delete_people.clicked.connect(self.delete_people),
            "Добавить": lambda: self.ui.pb_create_people.clicked.connect(self.add_new_people)
        }

        sender_text = self.sender().text()
        action = actions.get(sender_text)
        if action:
            action()

    # КНОПКИ СТРАНИЦЫ SCH
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
            self.model_data_sch = QStandardItemModel()
            self.model_data_sch.setHorizontalHeaderLabels(['ID', 'SCH', 'Автор схемы', 'PCB', 'Автор платы'])
            for e in result:
                self.model_data_sch.appendRow([
                    QtGui.QStandardItem(str(e['id'])),
                    QtGui.QStandardItem(str(e['decimal_num_sch'])),
                    QtGui.QStandardItem(str(e['author_sch'])),
                    QtGui.QStandardItem(str(e['dec_num_pcb'])),
                    QtGui.QStandardItem(str(e['author_pcb'])),
                    ])
            self.ui.tableView_sch.setModel(self.model_data_sch)
            self.proxy_model_sch = MyProxyModel()
            self.proxy_model_sch.setSourceModel(self.model_data_sch)
            self.ui.tableView_sch.setModel(self.proxy_model_sch)

            self.ui.lineEdit_search_sch.textChanged.connect(self.search_in_all_columns)
        except Exception as error:
            print("Не удалось установить соединение с базой данных MySQL:{}".format(error))
        finally:
            with connection.cursor() as cursor:
                cursor.close()
                connection.close()

    # добавление нового
    def add_new_sch_pcb(self):
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        decimal_num_sch = self.ui.edit_dec_num_sch.text()
        author_sch = self.ui.edit_author_sch.text()
        dec_num_pcb = self.ui.edit_dec_num_pcb.text()
        author_pcb = self.ui.edit_author_pcb.text()
        query = 'INSERT INTO sch(decimal_num_sch, author_sch, dec_num_pcb, author_pcb) VALUES (%s, %s, %s, %s)'
        values = (decimal_num_sch, author_sch, dec_num_pcb, author_pcb)
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, values)  # выполнение запроса
                connection.commit()  # подтверждение изменений
                print("successfully connected...")
                QtWidgets.QMessageBox.information(None, "Добавлено",
                                                  "Запись успешно добавлена в Базу данных", QtWidgets.QMessageBox.Ok)
                self.connect_sch_pcb_base()
        except pymysql.Error as error:
            print("Ошибка при добавлении элемента в базу данных: {}".format(error))
        finally:
            with connection.cursor() as cursor:
                cursor.close()
                connection.close()

    # удаление
    def delete_sch(self):
        try:
            connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            index = self.ui.tableView_sch.selectedIndexes()[0]
            id = str(self.ui.tableView_sch.model().data(index))

            query = "DELETE FROM sch WHERE id=%s"
            values = id

            with connection.cursor() as cursor:
                cursor.execute(query, values)  # выполнение запроса
                connection.commit()  # подтверждение изменений
                print("successfully deleted...")
                self.connect_sch_pcb_base()
        except pymysql.Error as error:
            print("Ошибка при удалении элемента из базы данных: {}".format(error))
        except IndexError as e:
            print(e)
            pass
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
            self.model_data_blocks = QStandardItemModel()
            self.model_data_blocks.setHorizontalHeaderLabels(['ID', 'Шифр', 'Название', 'SCH', 'Автор схемы', 'PCB',
                                                              'Автор платы', 'Дата', 'Примечания'])
            for e in result:
                self.model_data_blocks.appendRow([
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
            self.ui.tableView_2.setModel(self.model_data_blocks)

            self.proxy_model_blocks = MyProxyModel()
            self.proxy_model_blocks.setSourceModel(self.model_data_blocks)
            self.ui.tableView_2.setModel(self.proxy_model_blocks)

            self.ui.le_search_blocks.textChanged.connect(self.search_in_all_columns)
        except Exception as error:
            print("Не удалось установить соединение с базой данных MySQL:{}".format(error))
        finally:
            with connection.cursor() as cursor:
                cursor.close()
                connection.close()

    def get_selected_cells(self):
        self.ui.tableView_2.setSelectionMode(QAbstractItemView.MultiSelection)
        self.selection_model = self.ui.tableView_2.selectionModel()
        selected_indexes = self.ui.tableView_2.selectedIndexes()
        selected_cells = []
        for index in selected_indexes:
            selected_cells.append(str(self.ui.tableView_2.model().data(index)))
        return selected_cells

    def get_selected_cells_all(self):
        self.ui.tableView.setSelectionMode(QAbstractItemView.MultiSelection)
        self.selection_model_all = self.ui.tableView.selectionModel()
        selected_indexes = self.ui.tableView.selectedIndexes()
        selected_cells = []
        for index in selected_indexes:
            selected_cells.append(str(self.ui.tableView.model().data(index)))
        return selected_cells

    # добавление нового
    def add_new_block(self):
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        block_code = self.ui.le_change_block_code_2.text()
        block_name = self.ui.le_change_block_name_2.text()
        sch = self.ui.le_change_sch_block_2.text()
        date = self.ui.date_change_block.text()
        notes = self.ui.lineEdit.text()
        query = 'INSERT INTO blocks(block_code, block_name, SCH, date, notes) VALUES (%s, %s, %s, %s, %s)'
        values = (block_code, block_name, sch, date, notes)
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, values)  # выполнение запроса
                connection.commit()  # подтверждение изменений
                print("successfully connected...")
                QtWidgets.QMessageBox.information(None, "Добавлено",
                                                  "Запись успешно добавлена в Базу данных", QtWidgets.QMessageBox.Ok)
                self.connect_blocks_base()
        except pymysql.Error as error:
            print("Ошибка при добавлении элемента в базу данных: {}".format(error))
        finally:
            with connection.cursor() as cursor:
                cursor.close()
                connection.close()

    #  удаление
    def delete_block(self):
        try:
            connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            index = self.ui.tableView_2.selectedIndexes()[0]
            id = str(self.ui.tableView_2.model().data(index))

            query = "DELETE FROM blocks WHERE id=%s"
            values = id

            with connection.cursor() as cursor:
                cursor.execute(query, values)  # выполнение запроса
                connection.commit()  # подтверждение изменений
                print("successfully deleted...")
                self.connect_blocks_base()
        except pymysql.Error as error:
            print("Ошибка при удалении элемента из базы данных: {}".format(error))
        except IndexError as e:
            print(e)
            pass
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
            self.model_data_people = QStandardItemModel()
            self.model_data_people.setHorizontalHeaderLabels(['ID', 'Имя', 'Фамилия', 'Должность'])
            for e in result:
                self.model_data_people.appendRow([
                    QtGui.QStandardItem(str(e['id'])),
                    QtGui.QStandardItem(str(e['first_name'])),
                    QtGui.QStandardItem(str(e['last_name'])),
                    QtGui.QStandardItem(str(e['job_title']))])
            self.ui.tableView_3.setModel(self.model_data_people)

        except Exception as error:
            print("Не удалось установить соединение с базой данных MySQL:{}".format(error))
        finally:
            with connection.cursor() as cursor:
                cursor.close()
                connection.close()

    # добавление нового
    def add_new_people(self):
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        first_name = self.ui.le_first_name_people.text()
        last_name = self.ui.le_last_name_people.text()
        job_title = self.ui.cb_job_title_for_base.currentText()
        query = 'INSERT INTO users(first_name, last_name, job_title) VALUES (%s, %s, %s)'
        values = (first_name, last_name, job_title)
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, values)  # выполнение запроса
                connection.commit()  # подтверждение изменений
                print("successfully connected...")
                QtWidgets.QMessageBox.information(None, "Добавлено",
                                                  "Запись успешно добавлена в Базу данных", QtWidgets.QMessageBox.Ok)
                self.connect_people_base()
        except pymysql.Error as error:
            print("Ошибка при добавлении элемента в базу данных: {}".format(error))
        finally:
            with connection.cursor() as cursor:
                cursor.close()
                connection.close()

    #  удаление
    def delete_people(self):
        try:
            connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            index = self.ui.tableView_3.selectedIndexes()[0]
            id = str(self.ui.tableView_3.model().data(index))

            query = "DELETE FROM users WHERE id=%s"
            values = id
            try:
                with connection.cursor() as cursor:
                    cursor.execute(query, values)  # выполнение запроса
                    connection.commit()  # подтверждение изменений
                    print("successfully deleted...")
                    self.connect_people_base()
            except pymysql.Error as error:
                print("Ошибка при удалении элемента из базы данных: {}".format(error))

            finally:
                with connection.cursor() as cursor:
                    cursor.close()
                    connection.close()

        except IndexError as e:
            print(e)
            QtWidgets.QMessageBox.information(None, "Ошибка",
                                              "Вы не выбрали ID", QtWidgets.QMessageBox.Ok)

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

            self.model_data = QStandardItemModel()
            self.model_data.setHorizontalHeaderLabels(['ID', 'Code', 'Name', 'DecNum', 'Desc',
                                                       'Sostav', 'Design', 'Soft',
                                                       'Developer', 'Designer', 'Progr', 'Date'])

            for e in result:
                self.model_data.appendRow([
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

            self.ui.tableView.setModel(self.model_data)

            self.proxy_model = MyProxyModel()
            self.proxy_model.setSourceModel(self.model_data)
            self.ui.tableView.setModel(self.proxy_model)

            self.ui.lineEdit_filter.textChanged.connect(self.search_in_all_columns)

        except Exception as error:
            print("Не удалось установить соединение с базой данных MySQL:{}".format(error))
        finally:
            with connection.cursor() as cursor:
                cursor.close()
                connection.close()

    def setFilterRegExp(self, pattern):
        # Функция для установки регулярного выражения фильтрации
        self.proxy_model.setFilterRegExp(pattern)
        self.proxy_model.invalidateFilter()

    # ФУНКЦИЯ ПОИСКА ПО ТАБЛИЦЕ
    def search_in_all_columns(self, search_text):
        num_columns = self.model_data.columnCount()
        num_columns_blocks = self.model_data_blocks.columnCount()
        num_columns_sch = self.model_data_sch.columnCount()
        self.proxy_model.setFilterRegExp(search_text)
        self.proxy_model_blocks.setFilterRegExp(search_text)
        self.proxy_model_sch.setFilterRegExp(search_text)

        # Очищаем текущее выделение
        self.ui.tableView.clearSelection()
        self.ui.tableView_2.clearSelection()
        self.ui.tableView_sch.clearSelection()

        for column in range(num_columns):
            # Устанавливаем флаг выделения для текущей колонки
            self.ui.tableView.selectColumn(column)
            # Получаем выделенные ячейки
            selected_indexes = self.ui.tableView.selectedIndexes()
            # Перебираем выделенные ячейки и сравниваем содержимое с введенным текстом
            for index in selected_indexes:
                item = self.model_data.itemFromIndex(index)
                if item and search_text in item.text():
                    # Если найдено соответствие, то выделяем ячейку
                    self.ui.tableView.setCurrentIndex(index)
                    self.ui.tableView.scrollTo(index)
                    return
            # Сбрасываем флаг выделения для текущей колонки
            self.ui.tableView.clearSelection()

        for column in range(num_columns_blocks):
            # Устанавливаем флаг выделения для текущей колонки
            self.ui.tableView_2.selectColumn(column)
            # Получаем выделенные ячейки
            selected_indexes = self.ui.tableView_2.selectedIndexes()
            # Перебираем выделенные ячейки и сравниваем содержимое с введенным текстом
            for index in selected_indexes:
                item = self.model_data_blocks.itemFromIndex(index)
                if item and search_text in item.text():
                    # Если найдено соответствие, то выделяем ячейку
                    self.ui.tableView_2.setCurrentIndex(index)
                    self.ui.tableView_2.scrollTo(index)
                    return
            # Сбрасываем флаг выделения для текущей колонки
            self.ui.tableView_2.clearSelection()

        for column in range(num_columns_sch):
            # Устанавливаем флаг выделения для текущей колонки
            self.ui.tableView_sch.selectColumn(column)
            # Получаем выделенные ячейки
            selected_indexes = self.ui.tableView_sch.selectedIndexes()
            # Перебираем выделенные ячейки и сравниваем содержимое с введенным текстом
            for index in selected_indexes:
                item = self.model_data_sch.itemFromIndex(index)
                if item and search_text in item.text():
                    # Если найдено соответствие, то выделяем ячейку
                    self.ui.tableView_sch.setCurrentIndex(index)
                    self.ui.tableView_sch.scrollTo(index)
                    return
            # Сбрасываем флаг выделения для текущей колонки
            self.ui.tableView_sch.clearSelection()

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
            selected_index = self.ui.tableView.selectedIndexes()[0]
            row = selected_index.row()
            column = selected_index.column()

            if column == 5:
                sost_name = str(self.ui.tableView.model().data(selected_index))
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
                desc_name = str(self.ui.tableView.model().data(selected_index))
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
                design_name = str(self.ui.tableView.model().data(selected_index))
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
                software_name = str(self.ui.tableView.model().data(selected_index))
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
    # 4 ФУНКЦИИ ДЛЯ ВЫВОДА В КОМБОБОКСЫ ИНФ-И ИЗ БД
    def getAllCategories(self):
        try:
            listOfCategories = []
            connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            cur = connection.cursor()
            cur.execute(
                " SELECT * FROM profitt_db.category;")
            for row in cur:
                catType = [row['category']]
                if catType not in listOfCategories:
                    listOfCategories.append(catType)
            self.ui.cb_job_title_for_base.clear()
            for i in listOfCategories:
                self.ui.cb_job_title_for_base.addItem(' '.join(i))
            return listOfCategories
        except Exception as e:
            print(e)
        finally:
            connection.close()

    def getDevTypes(self):
        try:
            listOfDevTypes = []
            connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            cur = connection.cursor()
            cur.execute(
                "SELECT u.last_name AS фамилия, first_name FROM users u JOIN category c ON u.job_title = c.category "
                "WHERE c.category = 'Разработчик' ")
            for row in cur:
                devType = [row['фамилия'], row['first_name']]
                if devType not in listOfDevTypes:
                    listOfDevTypes.append(devType)
            self.ui.comboBox_developer.clear()
            # for i in listOfDevTypes:
            #     print(i, listOfDevTypes, type(listOfDevTypes))
            for i in listOfDevTypes:
                self.ui.comboBox_developer.addItem(' '.join(i))
                self.ui.change_cb_developer.addItem(' '.join(i))

            return listOfDevTypes
        except Exception as e:
            print(e)
        finally:
            connection.close()

    def getDesignerTypes(self):
        try:
            listOfDesignerTypes = []
            connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            cur = connection.cursor()
            cur.execute(
                "SELECT u.last_name AS фамилия, first_name FROM users u JOIN category c ON u.job_title = c.category "
                "WHERE c.category = 'Конструктор' ")
            for row in cur:
                designerType = [row['фамилия'], row['first_name']]
                if designerType not in listOfDesignerTypes:
                    listOfDesignerTypes.append(designerType)
            self.ui.comboBox_designer.clear()
            for i in listOfDesignerTypes:
                self.ui.comboBox_designer.addItem(' '.join(i))
                self.ui.change_cb_designer.addItem(' '.join(i))
            return listOfDesignerTypes
        except Exception as e:
            print(e)
        finally:
            connection.close()

    def getProgrammerTypes(self):
        try:
            listOfProgrammerTypes = []
            connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            cur = connection.cursor()
            cur.execute(
                "SELECT u.last_name AS фамилия, first_name FROM users u JOIN category c ON u.job_title = c.category "
                "WHERE c.category = 'Программист' ")
            for row in cur:
                programmerType = [row['фамилия'], row['first_name']]
                listOfProgrammerTypes.append(programmerType)
            for i in listOfProgrammerTypes:
                self.ui.comboBox_programmer.addItem(' '.join(i))
                self.ui.change_cb_programmer.addItem(' '.join(i))

            return listOfProgrammerTypes
        except Exception as e:
            print(e)
        finally:
            connection.close()
    ###########################################

    #  КЛИКЕР И 3 ФУНКЦИИ ДЛЯ ОСНОВНОЙ СТРАНИЦЫ
    ###########################################
    @QtCore.pyqtSlot()
    def action_clicked(self):
        fname = QFileDialog.getSaveFileName(self)[0]
        global fname_return
        fname_return = fname
        print(fname, fname_return)
        try:
            f = open(fname, 'w')
            if self.ui.Pages_Widget.currentIndex() == 0:
                description = self.ui.edit_add_description.toPlainText()
                f.write(description)
                f.close()
            if self.ui.Pages_Widget.currentIndex() == 3:
                description1 = self.ui.edit_ch_description.toPlainText()
                f.write(description1)
                f.close()
        except FileNotFoundError:
            print('No such file')

    def add_new_element(self):
        # global description
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        device_code = self.ui.edit_device_code.text()
        device_name = self.ui.edit_device_name.text()
        id_decimal_number_vipr = self.ui.edit_decimal_number.text()
        description = fname_return
        desc_name = self.get_short_filename(fname_return)
        id_sostav = self.sostav_folder()
        sost_name = self.get_short_filename(self.sostav_folder())  # izm
        id_engineering_design = self.design_folder()
        design_name = self.get_short_filename(self.design_folder())
        id_software = self.soft_folder()
        software_name = self.get_short_filename(self.soft_folder())
        id_developer = self.ui.comboBox_developer.currentText()
        id_designer = self.ui.comboBox_designer.currentText()
        id_programmer = self.ui.comboBox_programmer.currentText()
        date = self.ui.dateEdit.text()

        # izm
        query = "INSERT INTO devices (device_code, device_name, id_decimal_number_vipr, description, desc_name, id_sostav," \
                "sost_name, id_engineering_design, design_name, id_software, software_name, id_developer, id_designer, " \
                "id_programmer, date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        # izm
        values = (device_code, device_name, id_decimal_number_vipr, description, desc_name, id_sostav, sost_name,
                  id_engineering_design, design_name, id_software, software_name, id_developer, id_designer,
                  id_programmer, date)

        try:
            with connection.cursor() as cursor:
                cursor.execute(query, values)  # выполнение запроса
                connection.commit()  # подтверждение изменений
                print("successfully connected...")
                QtWidgets.QMessageBox.information(None, "Добавлено",
                                                  "Запись успешно добавлена в Базу данных", QtWidgets.QMessageBox.Ok)

        except pymysql.Error as error:
            print("Ошибка при добавлении элемента в базу данных: {}".format(error))

        finally:
            with connection.cursor() as cursor:
                cursor.close()
                connection.close()

    def edit_element(self):
        try:
            connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            index = self.ui.tableView.selectedIndexes()[0]
            id = str(self.ui.tableView.model().data(index))

            device_code = self.ui.edit_ch_devCode.text()
            device_name = self.ui.edit_ch_devName.text()
            id_decimal_number_vipr = self.ui.edit_ch_decNum.text()
            description = fname_return
            desc_name = self.get_short_filename(fname_return)
            id_sostav = self.sostav_folder()
            sost_name = self.get_short_filename(self.sostav_folder())  # izm
            id_engineering_design = self.design_folder()
            design_name = self.get_short_filename(self.design_folder())
            id_software = self.soft_folder()
            software_name = self.get_short_filename(self.soft_folder())
            id_developer = self.ui.change_cb_developer.currentText()
            id_designer = self.ui.change_cb_designer.currentText()
            id_programmer = self.ui.change_cb_programmer.currentText()
            date = self.ui.edit_ch_date.text()

            query = "UPDATE devices SET device_code=%s, device_name=%s, id_decimal_number_vipr=%s, description = %s, " \
                    "desc_name=%s, id_sostav = %s, sost_name=%s, id_engineering_design = %s," \
                    " design_name=%s, id_software = %s, software_name=%s, id_developer=%s, id_designer=%s, id_programmer=%s, date=%s " \
                    "WHERE id=%s"
            values = (device_code, device_name, id_decimal_number_vipr, description, desc_name, id_sostav, sost_name,
                      id_engineering_design, design_name, id_software, software_name, id_developer, id_designer,
                      id_programmer, date, id)

            with connection.cursor() as cursor:
                cursor.execute(query, values)  # выполнение запроса
                connection.commit()  # подтверждение изменений
                print("successfully edited...")
                QtWidgets.QMessageBox.information(None, "Изменено",
                                                  "Запись успешно изменена", QtWidgets.QMessageBox.Ok)
        except Exception as error:
            print("Ошибка при изменении элемента в базе данных: {}".format(error))

        finally:
            with connection.cursor() as cursor:
                cursor.close()
                connection.close()

    def delete_element(self):
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().data(index))

        query = "DELETE FROM devices WHERE id=%s"
        values = id
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, values)  # выполнение запроса
                connection.commit()  # подтверждение изменений
                print("successfully deleted...")
                self.create_connection_1()
        except pymysql.Error as error:
            print("Ошибка при удалении элемента из базы данных: {}".format(error))

        finally:
            with connection.cursor() as cursor:
                cursor.close()
                connection.close()

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
        table = cursor.insertTable(self.model_data.rowCount(), self.model_data.columnCount())
        for row in range(table.rows()):
            for column in range(table.columns()):
                cursor.insertText(self.model_data.item(row, column).text())
                cursor.movePosition(QtGui.QTextCursor.NextCell)
        document.print_(printer)
    ###########################################


if __name__ == "__main__":
    import sys
    global app
    app = QApplication(sys.argv)
    window1 = WindowLogIn()
    window1.show()

    sys.exit(app.exec_())
