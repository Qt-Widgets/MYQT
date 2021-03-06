﻿"""
MYQT.Connector é o modulo que gerencia como o aplicativo deve se conectar com o Servidor
e como ele deve agir depois de conectar

Atualmente o conector conta com as seguintes interfaces:

+---------------------------+----+
|Connection Type            |USE?|
+---------------------------+----+
| MYSQL Server     (TCP/IP) | OK |
| Microsoft Server (TCP/IP) | NO |
| Postgree SQL     (TCP/IP) | NO |
+---------------------------+----+
"""

import sys

# import mysql.connector as mysql
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import QFile, QTextStream, pyqtSlot,QSize,Qt
from PyQt5.QtWidgets import (QAction, QApplication, QDialog, QMainWindow,QMenu, QMessageBox, QStyleFactory)

from Core.Manager import ManagerWindow
from assets.UI.Scripts.ConnectorWindow import Ui_Connector

from Lib.icons_manager import win_icon
from Lib.icons_manager import b_mssql,b_mysql,b_postgreesql

from Lib.ConfigHandler import ConfigHandler

from Engines import MYSQL_Engine
from Engines import MSSQL_Engine

app = QApplication(sys.argv)
app.processEvents()

_style = str(open(r'assets\css\Style_White.css','r').read())
app.setStyleSheet(_style)

class MainWindow(QMainWindow,Ui_Connector):
    def __init__(self, parent = None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(win_icon))

        self.setWindowFlag(Qt.Window)

        self.dbType.setItemIcon(0,QIcon(b_mysql))
        self.dbType.setItemIcon(1,QIcon(b_mssql))
        self.dbType.setItemIcon(2,QIcon(b_postgreesql))

        self.cf = ConfigHandler(self)
        self.cf.load_config()

        self.connections = {0:'mysql',1:'mssql',2:'postgre'}

        self.show()
        self.connect.clicked.connect(self.pre_connection)

        self.db_changed()
        self.dbType.currentIndexChanged[int].connect(self.db_changed)


    def db_changed(self):
        if self.dbType.currentIndex() == 0: 
            self.port_in.setEnabled(True)
        else: 
            self.port_in.setEnabled(False)


    def pre_connection (self):        
        if self.host_in.text() == "" or self.port_in.text() == "" or self.user_in.text() == "" or self.pass_in.text() == "":
            QMessageBox.warning(self," EMPTY FIELD ALERT!! ","Maybe you left some empty field \nPlease check and try again.",QMessageBox.Ok)
        else:self.Connect()

    def Connect (self):
        self._type      = self.connections.get(self.dbType.currentIndex())
        self._host      = self.host_in.text()
        self._port      = self.port_in.text() 
        self._user      = self.user_in.text()
        self._pass      = self.pass_in.text()
        self.buffered_c = self.buffered.isChecked()

        try:
            if self._type == 'mysql':
                MYSQL_Engine.connect(self._host,self._port,self._user,self._pass,self.buffered_c)
            if self._type == 'mssql':
                MSSQL_Engine.connect(self._host,self._user,self._pass)
            if self._type == 'postgre':
                print("POSTGRE")

            self.manager = ManagerWindow(self._host,self._port,self._user,self._pass,self.buffered_c,self._type)
            self.cf.save_config()
            self.close()
        except Exception as error:
            QMessageBox.critical(self, "CRITICAL ERROR",str(error),QMessageBox.Ok)
            pass

Main_GUI = MainWindow()
sys.exit(app.exec_())
