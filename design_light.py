from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_light(object):
    def setupUi(self, MainWindow_light):
        MainWindow_light.setObjectName("MainWindow_light")
        MainWindow_light.resize(1497, 842)
        MainWindow_light.setMinimumSize(QtCore.QSize(1000, 500))
        MainWindow_light.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.centralwidget = QtWidgets.QWidget(MainWindow_light)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Top_Bar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Top_Bar.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top_Bar.setObjectName("Top_Bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_toggle = QtWidgets.QFrame(self.Top_Bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_toggle.sizePolicy().hasHeightForWidth())
        self.frame_toggle.setSizePolicy(sizePolicy)
        self.frame_toggle.setMinimumSize(QtCore.QSize(70, 40))
        self.frame_toggle.setMaximumSize(QtCore.QSize(70, 40))
        self.frame_toggle.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_toggle)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Btn_Toggle = QtWidgets.QPushButton(self.frame_toggle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;\n"
"")
        self.Btn_Toggle.setObjectName("Btn_Toggle")
        self.horizontalLayout_3.addWidget(self.Btn_Toggle)
        self.horizontalLayout.addWidget(self.frame_toggle)
        self.frame_top = QtWidgets.QFrame(self.Top_Bar)
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout.addWidget(self.frame_top)
        self.verticalLayout.addWidget(self.Top_Bar)
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.Content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_top_menus = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_top_menus.setMinimumSize(QtCore.QSize(70, 0))
        self.frame_top_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_menus.setObjectName("frame_top_menus")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Btn_menu_2 = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_menu_2.setMinimumSize(QtCore.QSize(0, 40))
        self.Btn_menu_2.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border:0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.Btn_menu_2.setObjectName("Btn_menu_2")
        self.verticalLayout_3.addWidget(self.Btn_menu_2)
        self.Btn_menu_4 = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_menu_4.setMinimumSize(QtCore.QSize(0, 40))
        self.Btn_menu_4.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border:0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.Btn_menu_4.setObjectName("Btn_menu_4")
        self.verticalLayout_3.addWidget(self.Btn_menu_4)
        self.Btn_menu_5 = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_menu_5.setMinimumSize(QtCore.QSize(0, 40))
        self.Btn_menu_5.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border:0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.Btn_menu_5.setObjectName("Btn_menu_5")
        self.verticalLayout_3.addWidget(self.Btn_menu_5)
        self.Btn_menu_6 = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_menu_6.setMinimumSize(QtCore.QSize(0, 40))
        self.Btn_menu_6.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border:0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.Btn_menu_6.setObjectName("Btn_menu_6")
        self.verticalLayout_3.addWidget(self.Btn_menu_6)
        self.verticalLayout_2.addWidget(self.frame_top_menus, 0, QtCore.Qt.AlignTop)
        self.frame = QtWidgets.QFrame(self.frame_left_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(70, 70))
        self.frame.setStyleSheet("\n"
"QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_2.addWidget(self.frame)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_pages = QtWidgets.QFrame(self.Content)
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Pages_Widget = QtWidgets.QStackedWidget(self.frame_pages)
        self.Pages_Widget.setObjectName("Pages_Widget")
        self.page_2 = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        self.page_2.setFont(font)
        self.page_2.setObjectName("page_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.page_label_2 = QtWidgets.QLabel(self.page_2)
        self.page_label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(29)
        self.page_label_2.setFont(font)
        self.page_label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.page_label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.page_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.page_label_2.setObjectName("page_label_2")
        self.verticalLayout_6.addWidget(self.page_label_2)
        self.frame_4 = QtWidgets.QFrame(self.page_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QtCore.QSize(1400, 80))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_5.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background_color: rgba(255,255,255,30);\n"
"    border: 1px solid rgba(255,255,255,40);\n"
"    border-radius:7px;\n"
"    width: 230px;\n"
"    height: 50px;\n"
"}\n"
"QPushButton: hover {\n"
"background_color: rgba(255,255,255,40);\n"
"}\n"
"QPushButton: pressed{\n"
"background_color: rgba(255,255,255,70);\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.pb_preview = QtWidgets.QPushButton(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(13)
        self.pb_preview.setFont(font)
        self.pb_preview.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background_color: rgba(255,255,255,30);\n"
"    border: 1px solid rgba(255,255,255,40);\n"
"    border-radius:7px;\n"
"    width: 230px;\n"
"    height: 50px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton: pressed{\n"
"background_color: rgba(255,255,255,70);\n"
"}")
        self.pb_preview.setObjectName("pb_preview")
        self.horizontalLayout_5.addWidget(self.pb_preview)
        self.pb_print = QtWidgets.QPushButton(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(13)
        self.pb_print.setFont(font)
        self.pb_print.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background_color: rgba(255,255,255,30);\n"
"    border: 1px solid rgba(255,255,255,40);\n"
"    border-radius:7px;\n"
"    width: 230px;\n"
"    height: 50px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton: pressed{\n"
"background_color: rgba(255,255,255,70);\n"
"}")
        self.pb_print.setObjectName("pb_print")
        self.horizontalLayout_5.addWidget(self.pb_print)
        self.verticalLayout_10.addWidget(self.frame_5)
        self.lineEdit_filter = QtWidgets.QLineEdit(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(14)
        self.lineEdit_filter.setFont(font)
        self.lineEdit_filter.setStyleSheet("color: rgb(255, 255, 255);\n"
"    border: 1px solid rgba(255,255,255,40);\n"
"    border-radius:7px;\n"
"font-size:14pt;\n"
"padding-left:10px;\n"
"")
        self.lineEdit_filter.setObjectName("lineEdit_filter")
        self.verticalLayout_10.addWidget(self.lineEdit_filter)
        self.tableView = QtWidgets.QTableView(self.frame_4)
        self.tableView.setStyleSheet("\n"
"background-color: rgb(210, 210, 210);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"\n"
"\n"
"")
        self.tableView.setObjectName("tableView")
        self.verticalLayout_10.addWidget(self.tableView)
        self.verticalLayout_6.addWidget(self.frame_4)
        self.Pages_Widget.addWidget(self.page_2)
        self.page_8 = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(26)
        self.page_8.setFont(font)
        self.page_8.setObjectName("page_8")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.page_8)
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.label_people = QtWidgets.QLabel(self.page_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.label_people.sizePolicy().hasHeightForWidth())
        self.label_people.setSizePolicy(sizePolicy)
        self.label_people.setMinimumSize(QtCore.QSize(0, 40))
        self.label_people.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(30)
        self.label_people.setFont(font)
        self.label_people.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_people.setAlignment(QtCore.Qt.AlignCenter)
        self.label_people.setObjectName("label_people")
        self.verticalLayout_24.addWidget(self.label_people)
        self.frame_14 = QtWidgets.QFrame(self.page_8)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.frame_15 = QtWidgets.QFrame(self.frame_14)
        self.frame_15.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_15.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem1 = QtWidgets.QSpacerItem(694, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.verticalLayout_25.addWidget(self.frame_15)
        self.frame_26 = QtWidgets.QFrame(self.frame_14)
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_26)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.tableView_3 = QtWidgets.QTableView(self.frame_26)
        self.tableView_3.setStyleSheet("\n"
"background-color: rgb(210, 210, 210);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"\n"
"")
        self.tableView_3.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableView_3.setObjectName("tableView_3")
        self.tableView_3.horizontalHeader().setDefaultSectionSize(200)
        self.horizontalLayout_16.addWidget(self.tableView_3)
        self.verticalLayout_25.addWidget(self.frame_26)
        self.verticalLayout_24.addWidget(self.frame_14)
        self.Pages_Widget.addWidget(self.page_8)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.page_9)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_blocks = QtWidgets.QLabel(self.page_9)
        self.label_blocks.setMinimumSize(QtCore.QSize(0, 40))
        self.label_blocks.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(31)
        self.label_blocks.setFont(font)
        self.label_blocks.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_blocks.setAlignment(QtCore.Qt.AlignCenter)
        self.label_blocks.setObjectName("label_blocks")
        self.verticalLayout_22.addWidget(self.label_blocks)
        self.frame_12 = QtWidgets.QFrame(self.page_9)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.frame_13 = QtWidgets.QFrame(self.frame_12)
        self.frame_13.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_13.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem2 = QtWidgets.QSpacerItem(483, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.pb_create_file_sostav = QtWidgets.QPushButton(self.frame_13)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(12)
        self.pb_create_file_sostav.setFont(font)
        self.pb_create_file_sostav.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background_color: rgba(255,255,255,30);\n"
"    border: 1px solid rgba(255,255,255,40);\n"
"    border-radius:7px;\n"
"    width: 230px;\n"
"    height: 50px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton: pressed{\n"
"background_color: rgba(255,255,255,70);\n"
"}")
        self.pb_create_file_sostav.setObjectName("pb_create_file_sostav")
        self.horizontalLayout_8.addWidget(self.pb_create_file_sostav)
        self.verticalLayout_23.addWidget(self.frame_13)
        self.le_search_blocks = QtWidgets.QLineEdit(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_search_blocks.sizePolicy().hasHeightForWidth())
        self.le_search_blocks.setSizePolicy(sizePolicy)
        self.le_search_blocks.setMinimumSize(QtCore.QSize(1000, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(14)
        self.le_search_blocks.setFont(font)
        self.le_search_blocks.setStyleSheet("color: rgb(255, 255, 255);\n"
"    border: 1px solid rgba(255,255,255,40);\n"
"    border-radius:7px;\n"
"font-size:14pt;\n"
"padding-left:10px;")
        self.le_search_blocks.setObjectName("le_search_blocks")
        self.verticalLayout_23.addWidget(self.le_search_blocks)
        self.frame_29 = QtWidgets.QFrame(self.frame_12)
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_29)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.tableView_2 = QtWidgets.QTableView(self.frame_29)
        self.tableView_2.setMinimumSize(QtCore.QSize(1100, 0))
        self.tableView_2.setMaximumSize(QtCore.QSize(1201, 16777215))
        self.tableView_2.setStyleSheet("\n"
"background-color: rgb(210, 210, 210);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"\n"
"")
        self.tableView_2.setObjectName("tableView_2")
        self.horizontalLayout_18.addWidget(self.tableView_2)
        self.frame_30 = QtWidgets.QFrame(self.frame_29)
        self.frame_30.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.frame_30)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.frame_31 = QtWidgets.QFrame(self.frame_30)
        self.frame_31.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_31.setMaximumSize(QtCore.QSize(16777215, 90))
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_31)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        spacerItem3 = QtWidgets.QSpacerItem(268, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem3)
        self.verticalLayout_35.addWidget(self.frame_31)
        self.horizontalLayout_18.addWidget(self.frame_30)
        self.verticalLayout_23.addWidget(self.frame_29)
        self.verticalLayout_22.addWidget(self.frame_12)
        self.Pages_Widget.addWidget(self.page_9)
        self.page_11 = QtWidgets.QWidget()
        self.page_11.setObjectName("page_11")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.page_11)
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.label_add_sch = QtWidgets.QLabel(self.page_11)
        self.label_add_sch.setMinimumSize(QtCore.QSize(0, 40))
        self.label_add_sch.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_add_sch.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 25 26pt \"Calibri Light\";")
        self.label_add_sch.setAlignment(QtCore.Qt.AlignCenter)
        self.label_add_sch.setObjectName("label_add_sch")
        self.verticalLayout_28.addWidget(self.label_add_sch)
        self.frame_18 = QtWidgets.QFrame(self.page_11)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_20 = QtWidgets.QFrame(self.frame_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.frame_20)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.frame_9 = QtWidgets.QFrame(self.frame_20)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem4 = QtWidgets.QSpacerItem(651, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        self.verticalLayout_30.addWidget(self.frame_9)
        self.lineEdit_search_sch = QtWidgets.QLineEdit(self.frame_20)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(14)
        self.lineEdit_search_sch.setFont(font)
        self.lineEdit_search_sch.setStyleSheet("color: rgb(255, 255, 255);\n"
"    border: 1px solid rgba(255,255,255,40);\n"
"    border-radius:7px;\n"
"font-size:14pt;\n"
"padding-left:10px;")
        self.lineEdit_search_sch.setObjectName("lineEdit_search_sch")
        self.verticalLayout_30.addWidget(self.lineEdit_search_sch)
        self.tableView_sch = QtWidgets.QTableView(self.frame_20)
        self.tableView_sch.setStyleSheet("background-color: rgb(210, 210, 210);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"\n"
"")
        self.tableView_sch.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableView_sch.setObjectName("tableView_sch")
        self.tableView_sch.horizontalHeader().setDefaultSectionSize(200)
        self.verticalLayout_30.addWidget(self.tableView_sch)
        self.horizontalLayout_12.addWidget(self.frame_20)
        self.frame_19 = QtWidgets.QFrame(self.frame_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy)
        self.frame_19.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        self.frame_19.setFont(font)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.frame_19)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.frame_21 = QtWidgets.QFrame(self.frame_19)
        self.frame_21.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem5 = QtWidgets.QSpacerItem(447, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem5)
        self.verticalLayout_29.addWidget(self.frame_21)
        self.horizontalLayout_12.addWidget(self.frame_19)
        self.verticalLayout_28.addWidget(self.frame_18)
        self.Pages_Widget.addWidget(self.page_11)
        self.page_12 = QtWidgets.QWidget()
        self.page_12.setObjectName("page_12")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.page_12)
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.label = QtWidgets.QLabel(self.page_12)
        self.label.setMinimumSize(QtCore.QSize(0, 60))
        self.label.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_31.addWidget(self.label)
        self.frame_22 = QtWidgets.QFrame(self.page_12)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.verticalLayout_31.addWidget(self.frame_22)
        self.Pages_Widget.addWidget(self.page_12)
        self.verticalLayout_4.addWidget(self.Pages_Widget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        MainWindow_light.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_light)
        self.Pages_Widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_light)

    def retranslateUi(self, MainWindow_light):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_light.setWindowTitle(_translate("MainWindow_light", "MainWindow"))
        self.Btn_Toggle.setText(_translate("MainWindow_light", "MENU"))
        self.Btn_menu_2.setText(_translate("MainWindow_light", "VIEW"))
        self.Btn_menu_4.setText(_translate("MainWindow_light", "BLOCKS"))
        self.Btn_menu_5.setText(_translate("MainWindow_light", "PEOPLE"))
        self.Btn_menu_6.setText(_translate("MainWindow_light", "SCH/PCB"))
        self.page_label_2.setToolTip(_translate("MainWindow_light", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.page_label_2.setText(_translate("MainWindow_light", "База устройств"))
        self.pb_preview.setText(_translate("MainWindow_light", "Распечатать"))
        self.pb_print.setText(_translate("MainWindow_light", "Распечатать все"))
        self.lineEdit_filter.setPlaceholderText(_translate("MainWindow_light", "Поиск"))
        self.label_people.setText(_translate("MainWindow_light", "Сотрудники"))
        self.label_blocks.setText(_translate("MainWindow_light", "Блоки"))
        self.pb_create_file_sostav.setText(_translate("MainWindow_light", "Create SOSTAV"))
        self.le_search_blocks.setPlaceholderText(_translate("MainWindow_light", "Поиск"))
        self.label_add_sch.setText(_translate("MainWindow_light", "Схемы/платы"))
        self.lineEdit_search_sch.setPlaceholderText(_translate("MainWindow_light", "Поиск"))
        self.label.setText(_translate("MainWindow_light", "Формируем файл"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_light = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_light()
    ui.setupUi(MainWindow_light)
    MainWindow_light.show()
    sys.exit(app.exec_())
