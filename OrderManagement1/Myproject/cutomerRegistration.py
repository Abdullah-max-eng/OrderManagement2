# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cutomerRegistration.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegisterWindow(object):
    def setupUi(self, RegisterWindow):
        RegisterWindow.setObjectName("RegisterWindow")
        RegisterWindow.resize(832, 606)
        RegisterWindow.setStyleSheet("background-color: rgb(152, 152, 152)")
        self.centralwidget = QtWidgets.QWidget(RegisterWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.RegistertheUser = QtWidgets.QPushButton(self.centralwidget)
        self.RegistertheUser.setGeometry(QtCore.QRect(590, 180, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        self.RegistertheUser.setFont(font)
        self.RegistertheUser.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.RegistertheUser.setStyleSheet("background-color: rgb(170, 170, 127)")
        self.RegistertheUser.setObjectName("RegistertheUser")
        self.RegNamelineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.RegNamelineEdit.setGeometry(QtCore.QRect(350, 110, 171, 41))
        self.RegNamelineEdit.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"background-color:rgb(255, 255, 255)")
        self.RegNamelineEdit.setObjectName("RegNamelineEdit")
        self.ReglastNamelineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ReglastNamelineEdit.setGeometry(QtCore.QRect(350, 180, 171, 41))
        self.ReglastNamelineEdit.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"background-color:rgb(255, 255, 255)")
        self.ReglastNamelineEdit.setObjectName("ReglastNamelineEdit")
        self.RegUserNamelineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.RegUserNamelineEdit.setGeometry(QtCore.QRect(350, 250, 171, 41))
        self.RegUserNamelineEdit.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"background-color:rgb(255, 255, 255)")
        self.RegUserNamelineEdit.setObjectName("RegUserNamelineEdit")
        self.RegEmailineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.RegEmailineEdit.setGeometry(QtCore.QRect(350, 310, 171, 41))
        self.RegEmailineEdit.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"background-color:rgb(255, 255, 255)")
        self.RegEmailineEdit.setObjectName("RegEmailineEdit")
        self.RegPasslineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.RegPasslineEdit.setGeometry(QtCore.QRect(350, 380, 171, 41))
        self.RegPasslineEdit.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"background-color:rgb(255, 255, 255)")
        self.RegPasslineEdit.setObjectName("RegPasslineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 110, 221, 41))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 180, 221, 41))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(36)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 250, 231, 41))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(36)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 300, 231, 51))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(36)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 370, 231, 51))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(36)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(230, 10, 441, 61))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(36)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_7.setObjectName("label_7")
        self.ClearButton = QtWidgets.QPushButton(self.centralwidget)
        self.ClearButton.setGeometry(QtCore.QRect(590, 270, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        self.ClearButton.setFont(font)
        self.ClearButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ClearButton.setStyleSheet("background-color: rgb(170, 170, 127)")
        self.ClearButton.setObjectName("ClearButton")
        self.BackToLogin = QtWidgets.QPushButton(self.centralwidget)
        self.BackToLogin.setGeometry(QtCore.QRect(590, 360, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        self.BackToLogin.setFont(font)
        self.BackToLogin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BackToLogin.setStyleSheet("background-color: rgb(170, 170, 127)")
        self.BackToLogin.setObjectName("BackToLogin")
        RegisterWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RegisterWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 832, 21))
        self.menubar.setObjectName("menubar")
        RegisterWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RegisterWindow)
        self.statusbar.setObjectName("statusbar")
        RegisterWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RegisterWindow)
        QtCore.QMetaObject.connectSlotsByName(RegisterWindow)

    def retranslateUi(self, RegisterWindow):
        _translate = QtCore.QCoreApplication.translate
        RegisterWindow.setWindowTitle(_translate("RegisterWindow", "MainWindow"))
        self.RegistertheUser.setText(_translate("RegisterWindow", "Register"))
        self.label_2.setText(_translate("RegisterWindow", "Name:"))
        self.label_3.setText(_translate("RegisterWindow", "Last name:"))
        self.label_4.setText(_translate("RegisterWindow", "User Name:"))
        self.label_5.setText(_translate("RegisterWindow", "Email:"))
        self.label_6.setText(_translate("RegisterWindow", "Password:"))
        self.label_7.setText(_translate("RegisterWindow", "Customer Registration"))
        self.ClearButton.setText(_translate("RegisterWindow", "Clear"))
        self.BackToLogin.setText(_translate("RegisterWindow", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegisterWindow = QtWidgets.QMainWindow()
    ui = Ui_RegisterWindow()
    ui.setupUi(RegisterWindow)
    RegisterWindow.show()
    sys.exit(app.exec_())
