# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\assets\UI\Layout\ConnectorWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Connector(object):
    def setupUi(self, Connector):
        Connector.setObjectName("Connector")
        Connector.resize(328, 262)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Connector.sizePolicy().hasHeightForWidth())
        Connector.setSizePolicy(sizePolicy)
        Connector.setMinimumSize(QtCore.QSize(328, 262))
        Connector.setMaximumSize(QtCore.QSize(428, 337))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        Connector.setFont(font)
        Connector.setDockNestingEnabled(False)
        Connector.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks|QtWidgets.QMainWindow.VerticalTabs)
        self.centralwidget = QtWidgets.QWidget(Connector)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.user_in = QtWidgets.QLineEdit(self.centralwidget)
        self.user_in.setMinimumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.user_in.setFont(font)
        self.user_in.setClearButtonEnabled(False)
        self.user_in.setObjectName("user_in")
        self.gridLayout.addWidget(self.user_in, 3, 0, 1, 1)
        self.pass_in = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_in.setMinimumSize(QtCore.QSize(88, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pass_in.setFont(font)
        self.pass_in.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.pass_in.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.pass_in.setClearButtonEnabled(False)
        self.pass_in.setObjectName("pass_in")
        self.gridLayout.addWidget(self.pass_in, 3, 1, 1, 1)
        self.trusted = QtWidgets.QCheckBox(self.centralwidget)
        self.trusted.setEnabled(False)
        self.trusted.setMinimumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial,Helvetica,sans-serif")
        font.setPointSize(10)
        font.setItalic(True)
        self.trusted.setFont(font)
        self.trusted.setCheckable(True)
        self.trusted.setChecked(True)
        self.trusted.setAutoRepeat(False)
        self.trusted.setAutoExclusive(False)
        self.trusted.setTristate(False)
        self.trusted.setObjectName("trusted")
        self.gridLayout.addWidget(self.trusted, 3, 2, 1, 1)
        self.buttons = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttons.setMinimumSize(QtCore.QSize(310, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttons.setFont(font)
        self.buttons.setStyleSheet("    min-width: 80px;\n"
" min-height: 20px;")
        self.buttons.setOrientation(QtCore.Qt.Horizontal)
        self.buttons.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Open)
        self.buttons.setCenterButtons(True)
        self.buttons.setObjectName("buttons")
        self.gridLayout.addWidget(self.buttons, 4, 0, 1, 3)
        self.port_in = QtWidgets.QLineEdit(self.centralwidget)
        self.port_in.setMinimumSize(QtCore.QSize(88, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.port_in.setFont(font)
        self.port_in.setFrame(True)
        self.port_in.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.port_in.setClearButtonEnabled(False)
        self.port_in.setObjectName("port_in")
        self.gridLayout.addWidget(self.port_in, 2, 1, 1, 1)
        self.buffered = QtWidgets.QCheckBox(self.centralwidget)
        self.buffered.setEnabled(True)
        self.buffered.setMinimumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial,Helvetica,sans-serif")
        font.setPointSize(10)
        font.setItalic(True)
        self.buffered.setFont(font)
        self.buffered.setCheckable(True)
        self.buffered.setChecked(True)
        self.buffered.setAutoRepeat(False)
        self.buffered.setAutoExclusive(False)
        self.buffered.setTristate(False)
        self.buffered.setObjectName("buffered")
        self.gridLayout.addWidget(self.buffered, 2, 2, 1, 1)
        self.host_in = QtWidgets.QLineEdit(self.centralwidget)
        self.host_in.setMinimumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.host_in.setFont(font)
        self.host_in.setFrame(True)
        self.host_in.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.host_in.setClearButtonEnabled(False)
        self.host_in.setObjectName("host_in")
        self.gridLayout.addWidget(self.host_in, 2, 0, 1, 1)
        self.driver_in = QtWidgets.QLineEdit(self.centralwidget)
        self.driver_in.setEnabled(False)
        self.driver_in.setMinimumSize(QtCore.QSize(210, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.driver_in.setFont(font)
        self.driver_in.setFrame(True)
        self.driver_in.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.driver_in.setClearButtonEnabled(False)
        self.driver_in.setObjectName("driver_in")
        self.gridLayout.addWidget(self.driver_in, 1, 0, 1, 2)
        self.driver = QtWidgets.QCheckBox(self.centralwidget)
        self.driver.setEnabled(False)
        self.driver.setMinimumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial,Helvetica,sans-serif")
        font.setPointSize(10)
        font.setItalic(True)
        self.driver.setFont(font)
        self.driver.setCheckable(True)
        self.driver.setChecked(True)
        self.driver.setAutoRepeat(False)
        self.driver.setAutoExclusive(False)
        self.driver.setTristate(False)
        self.driver.setObjectName("driver")
        self.gridLayout.addWidget(self.driver, 1, 2, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(310, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 3)
        Connector.setCentralWidget(self.centralwidget)

        self.retranslateUi(Connector)
        QtCore.QMetaObject.connectSlotsByName(Connector)
        Connector.setTabOrder(self.comboBox, self.host_in)
        Connector.setTabOrder(self.host_in, self.port_in)
        Connector.setTabOrder(self.port_in, self.user_in)
        Connector.setTabOrder(self.user_in, self.pass_in)
        Connector.setTabOrder(self.pass_in, self.buffered)

    def retranslateUi(self, Connector):
        _translate = QtCore.QCoreApplication.translate
        Connector.setWindowTitle(_translate("Connector", "SQL CONNECTOR"))
        self.user_in.setToolTip(_translate("Connector", "<html><head/><body><p>Username</p></body></html>"))
        self.user_in.setText(_translate("Connector", "root"))
        self.user_in.setPlaceholderText(_translate("Connector", "User:"))
        self.pass_in.setToolTip(_translate("Connector", "<html><head/><body><p>Password</p></body></html>"))
        self.pass_in.setText(_translate("Connector", "123456"))
        self.pass_in.setPlaceholderText(_translate("Connector", "Password:"))
        self.trusted.setToolTip(_translate("Connector", "<html><head/><body><p>Trusted Connection</p></body></html>"))
        self.trusted.setText(_translate("Connector", "Trusted"))
        self.port_in.setToolTip(_translate("Connector", "<html><head/><body><p>Server PORT</p></body></html>"))
        self.port_in.setText(_translate("Connector", "3306"))
        self.port_in.setPlaceholderText(_translate("Connector", "Port:"))
        self.buffered.setToolTip(_translate("Connector", "<html><head/><body><p>Buffered Connection</p></body></html>"))
        self.buffered.setText(_translate("Connector", "Buffered"))
        self.host_in.setToolTip(_translate("Connector", "<html><head/><body><p>Server / IP</p></body></html>"))
        self.host_in.setText(_translate("Connector", "127.0.0.1"))
        self.host_in.setPlaceholderText(_translate("Connector", "Server/IP:"))
        self.driver_in.setToolTip(_translate("Connector", "<html><head/><body><p>Driver</p></body></html>"))
        self.driver_in.setText(_translate("Connector", "SQL Server Native Client 11.0"))
        self.driver_in.setPlaceholderText(_translate("Connector", "Driver:"))
        self.driver.setToolTip(_translate("Connector", "<html><head/><body><p>Use server Driver</p></body></html>"))
        self.driver.setText(_translate("Connector", "Use Driver"))
        self.comboBox.setItemText(0, _translate("Connector", "MYSQL (TCP/IP)"))
        self.comboBox.setItemText(1, _translate("Connector", "Microsoft Server (TCP/IP)"))
        self.comboBox.setItemText(2, _translate("Connector", "Postgre SQL (Experimental)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Connector = QtWidgets.QMainWindow()
    ui = Ui_Connector()
    ui.setupUi(Connector)
    Connector.show()
    sys.exit(app.exec_())
