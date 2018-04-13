# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_main.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import DBCon
from Statistics import plot,plot1,plot2
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

global ID
ID = "N"

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
#======================= center Main ============================
    def center(self, Form):
        frameGm = Form.frameGeometry()
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        Form.move(frameGm.topLeft())
#======================= center  Main ============================
    def Action1(self):
        from resetpassword import Ui_ResetPassword
        self.window = QtGui.QMainWindow()
        self.ui = Ui_ResetPassword()
        self.ui.setupUi(self.window)
        self.window.show()

    def Action2(self):
        from Login import Ui_Form
        self.window =QtGui.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
        self.MainWindow.close()

    #============ Select from table ==============
    def cell_was_clicked(self, row, column):
        global ID
        ID = self.tableWidget.item(row, column)

    #============ Select from table ==============

    #===============GoToNewWindow===================
    def OpenCreate(self):
        from admincreate import Ui_CreateWindow
        self.window =QtGui.QMainWindow()
        self.ui = Ui_CreateWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.MainWindow.close()
    #===============GoToNewWindow===================

    #===============GoToEditWindow===================
    def OpenEdit(self):
        msgBox = QtGui.QMessageBox()
        if ID == "N":
            msgBox.setText("Please select one user to edit ")
            msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
            msgBox.exec_()
        else:
            from admincreate import Ui_CreateWindow
            self.window =QtGui.QMainWindow()
            self.ui = Ui_CreateWindow()
            self.ui.setupUi(self.window)
            self.ui.pbsubmit.setText("Update User")
            m,con = DBCon.DBConnect()
            m.execute("SELECT * FROM User WHERE User_ID='%s' " %ID.text())
            rez=m.fetchall()
            for data in rez:
                First_name = data[2]
                Father_name = data[3]
                Gfather_name = data[4]
                Family_name = data[5]
                Email = data[6]
                Phone_number = data[7]
                User_Role = data[8]
                Branch_ID = data[9]

            self.ui.lineEdit_13.setText(ID.text())
            self.ui.lineEdit_13.setReadOnly(True)
            self.ui.lineEdit_9.setText(First_name)
            self.ui.lineEdit_11.setText(Father_name)
            self.ui.lineEdit_12.setText(Gfather_name)
            self.ui.lineEdit_10.setText(Family_name)
            self.ui.leemail.setText(Email)
            self.ui.lephone.setText(Phone_number)
            if User_Role == 'Station Officer':
                 indexRole = 1
            elif User_Role == 'Scene Officer':
                 indexRole = 2
            self.ui.comboBoxrole_3.setCurrentIndex(indexRole)
            self.ui.comboBoxbranch_3.setCurrentIndex(Branch_ID)

            self.window.show()
            self.MainWindow.close()
    #===============GoToEditWindow===================

    #===============Delete User======================
    def AlertM(self):
        global ID
        msgBox = QtGui.QMessageBox()
        if ID == "N":
            msgBox.setText("Please select one user to delete ")
            msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
            msgBox.exec_()
        else:
            choice = QtGui.QMessageBox.question(None,'Alert',"Are you sure you want to delete the user account?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            if choice == QtGui.QMessageBox.Yes:
                m,con= DBCon.DBConnect()
                m.execute("DELETE FROM User WHERE User_ID='%s' " %ID.text())
                con.commit()
                con.close()
                msgBox.setText("User has been deleted successfully")
                msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
                msgBox.exec_()
            else:
                pass
    #===============Delete User======================


    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1340, 804)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(251, 251, 251)\n""#QLineEdit { \n""background-color: rgb(255, 255, 255)\n""}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.logo = QtGui.QLabel(self.centralwidget)
        self.logo.setObjectName(_fromUtf8("logo"))
        self.horizontalLayout.addWidget(self.logo)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

####################################****************************
        self.pushbutton = QtGui.QPushButton('User Name ')
        self.pushbutton.setStyleSheet(_fromUtf8("  border: 0px; font-size=1000px;"))
        menu = QtGui.QMenu()
        menu.addAction('Reset Password', self.Action1)
        menu.addAction('Log out', self.Action2)
        self.pushbutton.setMenu(menu)

####################################****************************

        self.horizontalLayout.addWidget(self.pushbutton)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.menuframe = QtGui.QFrame(self.centralwidget)
        self.menuframe.setMinimumSize(QtCore.QSize(160, 0))
        self.menuframe.setMaximumSize(QtCore.QSize(160, 16777215))
        self.menuframe.setStyleSheet(_fromUtf8("border-color: rgb(22, 65, 74);"))
        self.menuframe.setFrameShape(QtGui.QFrame.StyledPanel)
        self.menuframe.setFrameShadow(QtGui.QFrame.Raised)
        self.menuframe.setObjectName(_fromUtf8("menuframe"))
        self.frame_dates = QtGui.QFrame(self.menuframe)
        self.frame_dates.setGeometry(QtCore.QRect(10, 70, 141, 261))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_dates.sizePolicy().hasHeightForWidth())
        self.frame_dates.setSizePolicy(sizePolicy)
        self.frame_dates.setMinimumSize(QtCore.QSize(0, 261))
        self.frame_dates.setStyleSheet(_fromUtf8("QLabel {\n"
"font: 75 13pt \"Verdana\";\n"
"}"))
        self.frame_dates.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_dates.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_dates.setObjectName(_fromUtf8("frame_dates"))
        self.gridLayout_8 = QtGui.QGridLayout(self.frame_dates)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.labeltimespan = QtGui.QLabel(self.frame_dates)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.labeltimespan.setFont(font)
        self.labeltimespan.setStyleSheet(_fromUtf8("color: rgb(22, 65, 74);\n"
""))
        self.labeltimespan.setObjectName(_fromUtf8("labeltimespan"))
        self.gridLayout_8.addWidget(self.labeltimespan, 5, 0, 1, 1)
        self.dateEditfrom = QtGui.QDateEdit(self.frame_dates)
        self.dateEditfrom.setObjectName(_fromUtf8("dateEditfrom"))
        self.gridLayout_8.addWidget(self.dateEditfrom, 2, 0, 1, 1)
        self.labelfromdate = QtGui.QLabel(self.frame_dates)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.labelfromdate.setFont(font)
        self.labelfromdate.setStyleSheet(_fromUtf8("color: rgb(22, 65, 74);\n"
""))
        self.labelfromdate.setObjectName(_fromUtf8("labelfromdate"))
        self.gridLayout_8.addWidget(self.labelfromdate, 1, 0, 1, 1)
        self.labeltodate = QtGui.QLabel(self.frame_dates)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.labeltodate.setFont(font)
        self.labeltodate.setStyleSheet(_fromUtf8("color: rgb(22, 65, 74);"))
        self.labeltodate.setObjectName(_fromUtf8("labeltodate"))
        self.gridLayout_8.addWidget(self.labeltodate, 3, 0, 1, 1)
        self.timeEdit = QtGui.QTimeEdit(self.frame_dates)
        self.timeEdit.setObjectName(_fromUtf8("timeEdit"))
        self.gridLayout_8.addWidget(self.timeEdit, 6, 0, 1, 1)
        self.dateEditto = QtGui.QDateEdit(self.frame_dates)
        self.dateEditto.setObjectName(_fromUtf8("dateEditto"))
        self.gridLayout_8.addWidget(self.dateEditto, 4, 0, 1, 1)
        self.labeldate = QtGui.QLabel(self.frame_dates)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.labeldate.setFont(font)
        self.labeldate.setStyleSheet(_fromUtf8("color: rgb(22, 65, 74);"))
        self.labeldate.setObjectName(_fromUtf8("labeldate"))
        self.gridLayout_8.addWidget(self.labeldate, 0, 0, 1, 1)
        self.filtermenutab = QtGui.QLabel(self.menuframe)
        self.filtermenutab.setGeometry(QtCore.QRect(0, 10, 91, 21))
        self.filtermenutab.setStyleSheet(_fromUtf8("font: 75 11pt \"Verdana\";"))
        self.filtermenutab.setObjectName(_fromUtf8("filtermenutab"))
        self.burgermenu = QtGui.QLabel(self.menuframe)
        self.burgermenu.setGeometry(QtCore.QRect(130, 10, 21, 21))
        self.burgermenu.setObjectName(_fromUtf8("burgermenu"))
        self.gridLayout_3.addWidget(self.menuframe, 1, 0, 1, 1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_4.addWidget(self.line)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 2, 0, 1, 2)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(540, 200, 141, 121))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.tab_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(15, 0, 1121, 600))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))

        #=============================
        self.figure = plt.figure()
        self.figure.patch.set_facecolor("None")
        self.canvas1 = FigureCanvas(self.figure)
        self.canvas1.setStyleSheet("background-color:transparent;")
        plot(self)
        #=================================

        self.horizontalLayout_2.addWidget(self.canvas1)

        #=============================
        self.figure = plt.figure()
        self.figure.patch.set_facecolor("None")
        self.canvas1 = FigureCanvas(self.figure)
        self.canvas1.setStyleSheet("background-color:transparent;")
        plot2(self)
        #=================================

        self.horizontalLayout_2.addWidget(self.canvas1)

        #=============================
        self.figure = plt.figure()
        self.figure.patch.set_facecolor("None")
        self.canvas1 = FigureCanvas(self.figure)
        self.canvas1.setStyleSheet("background-color:transparent;")
        plot1(self)
        #=================================
        self.horizontalLayout_2.addWidget(self.canvas1)

        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.DeleteUserB = QtGui.QPushButton(self.tab_3)
        self.DeleteUserB.setMaximumSize(QtCore.QSize(100, 16777215))
        self.DeleteUserB.setStyleSheet(_fromUtf8("color: rgb(22, 65, 74);\n"
"background-color: rgb(240, 240, 240);"))
        self.DeleteUserB.setObjectName(_fromUtf8("DeleteUserB"))
        self.gridLayout_2.addWidget(self.DeleteUserB, 2, 2, 1, 1)
        self.EditUserB = QtGui.QPushButton(self.tab_3)
        self.EditUserB.setMaximumSize(QtCore.QSize(100, 16777215))
        self.EditUserB.setStyleSheet(_fromUtf8("color: rgb(22, 65, 74);\n"
"background-color: rgb(240, 240, 240);\n"
""))
        self.EditUserB.setObjectName(_fromUtf8("EditUserB"))
        self.gridLayout_2.addWidget(self.EditUserB, 2, 1, 1, 1)
        self.tableWidget = QtGui.QTableWidget(self.tab_3)
        self.tableWidget.setStyleSheet(_fromUtf8("border-color: rgb(22, 65, 74);\n"
""))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        #=================
        #selection to be by row instead of cell.
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        # enable sorting
        self.tableWidget.setSortingEnabled(True)
        #=================
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(0)
        #=======ConnectToDatabase==========
        m,con = DBCon.DBConnect()
        q="SELECT User_ID,First_name,Father_name,Gfather_name,Family_name,Email,Phone_number,User_Role,Branch_ID FROM User WHERE User_Role = 'Station Officer' or  User_Role = 'Scene Officer'"
        m.execute(q)
        rez=m.fetchall()
        for row_num, row_data in enumerate(rez):
            self.tableWidget.insertRow(row_num)
            for col_num, data in enumerate(row_data):
                self.tableWidget.setItem(row_num,col_num, QtGui.QTableWidgetItem(str(data)))
        con.close()

        #=======ConnectToDatabase==========
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.gridLayout_2.addWidget(self.tableWidget, 1, 0, 1, 3)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        self.comboBox = QtGui.QComboBox(self.tab_3)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox, 0, 2, 1, 1)
        self.SearchB = QtGui.QPushButton(self.tab_3)
        self.SearchB.setStyleSheet(_fromUtf8("color: rgb(22, 65, 74);\n"
"background-color: rgb(240, 240, 240);\n"
"\n"
""))
        self.SearchB.setObjectName(_fromUtf8("SearchB"))
        self.gridLayout.addWidget(self.SearchB, 0, 4, 1, 1)
        self.CreateUserB = QtGui.QPushButton(self.tab_3)
        self.CreateUserB.setStyleSheet(_fromUtf8("color: rgb(22, 65, 74);\n"
"background-color: rgb(240, 240, 240);"))
        self.CreateUserB.setObjectName(_fromUtf8("CreateUserB"))
        #=======add a new user==========
        self.CreateUserB.clicked.connect(self.OpenCreate)
        #=======add a new user==========
        self.gridLayout.addWidget(self.CreateUserB, 0, 0, 1, 1)
        self.lesearchbox = QtGui.QLineEdit(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lesearchbox.sizePolicy().hasHeightForWidth())
        self.lesearchbox.setSizePolicy(sizePolicy)
        self.lesearchbox.setObjectName(_fromUtf8("lesearchbox"))
        self.gridLayout.addWidget(self.lesearchbox, 0, 3, 1, 1, QtCore.Qt.AlignLeft)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 3)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.tabWidget, 1, 1, 1, 1)
        self.tabWidget.raise_()
        self.menuframe.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        #=======Edit a new user==========
        self.EditUserB.clicked.connect(self.OpenEdit)
        #=======Edit a new user==========
        #=======Delete user==========
        self.DeleteUserB.clicked.connect(self.AlertM)
        #=======Delete user==========
        #============ Select from table ==============
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.cellClicked.connect(self.cell_was_clicked)
        #============ Select from table ==============
        #=======Edit a new user==========
        self.CreateUserB.clicked.connect(self.OpenCreate)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lesearchbox, self.CreateUserB)
        MainWindow.setTabOrder(self.CreateUserB, self.dateEditfrom)
        MainWindow.setTabOrder(self.dateEditfrom, self.dateEditto)
        MainWindow.setTabOrder(self.dateEditto, self.timeEdit)
        MainWindow.setTabOrder(self.timeEdit, self.EditUserB)
        MainWindow.setTabOrder(self.EditUserB, self.tableWidget)
        MainWindow.setTabOrder(self.tableWidget, self.DeleteUserB)
        MainWindow.setTabOrder(self.DeleteUserB, self.SearchB)
        MainWindow.setTabOrder(self.SearchB, self.comboBox)
        MainWindow.setTabOrder(self.comboBox, self.tabWidget)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "DARB", None))
        #======================= center ============================
        self.center(MainWindow)
        #======================= center ============================
        self.logo.setText(_translate("MainWindow", "", None))
        self.logo.setPixmap(QtGui.QPixmap("Img/logosmall-min.png"))
        self.labeltimespan.setText(_translate("MainWindow", "Time:", None))
        self.labelfromdate.setText(_translate("MainWindow", "From:", None))
        self.labeltodate.setText(_translate("MainWindow", "To:", None))
        self.labeldate.setText(_translate("MainWindow", "Date:", None))
        self.filtermenutab.setText(_translate("MainWindow", "Map\'s Filter", None))
        self.burgermenu.setText(_translate("MainWindow", "", None))
        self.burgermenu.setPixmap(QtGui.QPixmap("Img/menu.png"))
        self.label_3.setText(_translate("MainWindow", "Need Help?", None))
        self.label_5.setText(_translate("MainWindow", "MAP", None))
        # This Map tab
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Map", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Statistics ", None))
        self.DeleteUserB.setText(_translate("MainWindow", "Delete User", None))
        self.EditUserB.setText(_translate("MainWindow", "Edit User", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "First Name", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Column", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Father Name", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Family Name", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Email", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Phone", None))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Role", None))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Branch ID", None))
        #========================================
        # set column width to fit contents
        header = self.tableWidget.horizontalHeader()
        header.setResizeMode(0, QtGui.QHeaderView.Stretch)
        header.setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(2, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(3, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(4, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(5, QtGui.QHeaderView.Stretch)
        header.setResizeMode(6, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(7, QtGui.QHeaderView.Stretch)
        header.setResizeMode(8, QtGui.QHeaderView.ResizeToContents)
        #========================================

        self.comboBox.setItemText(0, _translate("MainWindow", "-Filter by Role-", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "Station Officer ", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "Scene Officer ", None))
        self.SearchB.setText(_translate("MainWindow", "Search", None))
        self.CreateUserB.setText(_translate("MainWindow", "Create User ", None))
        self.lesearchbox.setToolTip(_translate("MainWindow", "<html><head/><body><p>Enter the name or ID of the officer you want to look up.</p></body></html>", None))
        self.lesearchbox.setPlaceholderText(_translate("MainWindow", "Q search", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Manage Users ", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
