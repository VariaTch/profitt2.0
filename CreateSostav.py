import pymysql
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from config1 import *

class Creator:
    def __init__(self):
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name

    def create_file_sostav(self, selected_id):
        try:
            connection = pymysql.connect(
                host=self.host,
                port=3306,
                user=self.user,
                password=self.password,
                database=self.db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            mycursor = connection.cursor()
            all_results = []
            for id in selected_id:
                query = 'SELECT b.block_code, b.block_name, s.decimal_num_sch, s.author_sch, s.dec_num_pcb, ' \
                        's.author_pcb, b.date, b.notes FROM blocks b JOIN sch s ON b.sch = s.decimal_num_sch WHERE b.id =%s'
                value = id
                mycursor.execute(query, value)
                result = mycursor.fetchall()
                all_results.extend(result)
            fname = QFileDialog.getSaveFileName(None, 'Save File', '', 'Text Files (*.txt)')[0]
            lists = []
            for i in all_results:
                item = [i['block_code'], i['block_name'], i['decimal_num_sch'], i['author_sch'], i['dec_num_pcb'],
                        i['author_pcb'], i['date']]
                item = item + ['__________________________']
                lists.append(item)
            with open(fname, 'w') as file:
                for lst in lists:
                    for item in lst:
                        file.write(str(item) + '\n')
            QtWidgets.QMessageBox.information(None, "Файл создан",
                                              "Файл состава успешно создан", QtWidgets.QMessageBox.Ok)
        except Exception as e:
            print("Ошибка : {}".format(e))
        finally:
            with connection.cursor() as cursor:
                cursor.close()
                connection.close()
