# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from socket import *
import time

class Ui_ERP(object):
    def setupUi(self, ERP):
        ERP.setObjectName("ERP")
        ERP.resize(1546/3, 808) #1546 808
        self.centralwidget = QtWidgets.QWidget(ERP)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 1521, 761))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.pordem = QtWidgets.QPushButton(self.groupBox)
        self.pordem.setGeometry(QtCore.QRect(20, 280, 161, 51))
        self.pordem.setObjectName("pordem")
        self.pdescarga = QtWidgets.QPushButton(self.groupBox)
        self.pdescarga.setGeometry(QtCore.QRect(310, 280, 161, 51))
        self.pdescarga.setObjectName("pdescarga")
        self.parmazem = QtWidgets.QPushButton(self.groupBox)
        self.parmazem.setGeometry(QtCore.QRect(570, 280, 161, 51))
        self.parmazem.setObjectName("parmazem")
        self.prordens = QtWidgets.QPushButton(self.groupBox)
        self.prordens.setGeometry(QtCore.QRect(810, 280, 161, 51))
        self.prordens.setObjectName("prordens")
        self.lmsgdescarga = QtWidgets.QLabel(self.groupBox)
        self.lmsgdescarga.setGeometry(QtCore.QRect(310, 340, 181, 31))
        self.lmsgdescarga.setObjectName("lmsgdescarga")
        self.sfrom = QtWidgets.QSpinBox(self.groupBox)
        self.sfrom.setGeometry(QtCore.QRect(130, 50, 51, 31))
        self.sfrom.setMinimum(1)
        self.sfrom.setMaximum(8)
        self.sfrom.setProperty("value", 1)
        self.sfrom.setObjectName("sfrom")
        self.sto = QtWidgets.QSpinBox(self.groupBox)
        self.sto.setGeometry(QtCore.QRect(130, 90, 51, 31))
        self.sto.setMinimum(2)
        self.sto.setMaximum(9)
        self.sto.setProperty("value", 2)
        self.sto.setObjectName("sto")
        self.spenalty = QtWidgets.QSpinBox(self.groupBox)
        self.spenalty.setGeometry(QtCore.QRect(130, 210, 51, 31))
        self.spenalty.setMaximum(1000)
        self.spenalty.setProperty("value", 10)
        self.spenalty.setObjectName("spenalty")
        self.smaxdelay = QtWidgets.QSpinBox(self.groupBox)
        self.smaxdelay.setGeometry(QtCore.QRect(130, 170, 51, 31))
        self.smaxdelay.setMaximum(500)
        self.smaxdelay.setProperty("value", 50)
        self.smaxdelay.setDisplayIntegerBase(10)
        self.smaxdelay.setObjectName("smaxdelay")
        self.lfrom = QtWidgets.QLabel(self.groupBox)
        self.lfrom.setGeometry(QtCore.QRect(10, 60, 91, 21))
        self.lfrom.setObjectName("lfrom")
        self.lto = QtWidgets.QLabel(self.groupBox)
        self.lto.setGeometry(QtCore.QRect(10, 100, 55, 16))
        self.lto.setObjectName("lto")
        self.lmaxdelay = QtWidgets.QLabel(self.groupBox)
        self.lmaxdelay.setGeometry(QtCore.QRect(10, 170, 101, 31))
        self.lmaxdelay.setObjectName("lmaxdelay")
        self.lpenalty = QtWidgets.QLabel(self.groupBox)
        self.lpenalty.setGeometry(QtCore.QRect(10, 210, 91, 21))
        self.lpenalty.setObjectName("lpenalty")
        self.lquantity2 = QtWidgets.QLabel(self.groupBox)
        self.lquantity2.setGeometry(QtCore.QRect(300, 170, 101, 31))
        self.lquantity2.setObjectName("lquantity2")
        self.ltype = QtWidgets.QLabel(self.groupBox)
        self.ltype.setGeometry(QtCore.QRect(300, 100, 91, 21))
        self.ltype.setObjectName("ltype")
        self.ldestination = QtWidgets.QLabel(self.groupBox)
        self.ldestination.setGeometry(QtCore.QRect(300, 140, 101, 21))
        self.ldestination.setObjectName("ldestination")
        self.sdestination = QtWidgets.QSpinBox(self.groupBox)
        self.sdestination.setGeometry(QtCore.QRect(420, 140, 51, 31))
        self.sdestination.setMinimum(1)
        self.sdestination.setMaximum(3)
        self.sdestination.setProperty("value", 1)
        self.sdestination.setObjectName("sdestination")
        self.squantity2 = QtWidgets.QSpinBox(self.groupBox)
        self.squantity2.setGeometry(QtCore.QRect(420, 180, 51, 31))
        self.squantity2.setMinimum(1)
        self.squantity2.setProperty("value", 1)
        self.squantity2.setObjectName("squantity2")
        self.stype = QtWidgets.QSpinBox(self.groupBox)
        self.stype.setGeometry(QtCore.QRect(420, 100, 51, 31))
        self.stype.setMinimum(1)
        self.stype.setMaximum(9)
        self.stype.setProperty("value", 1)
        self.stype.setObjectName("stype")
        self.lrarmazem = QtWidgets.QLabel(self.groupBox)
        self.lrarmazem.setGeometry(QtCore.QRect(500, 20, 261, 251))
        self.lrarmazem.setObjectName("lrarmazem")
        self.lrordens = QtWidgets.QLabel(self.groupBox)
        self.lrordens.setGeometry(QtCore.QRect(520, 340, 991, 391))
        self.lrordens.setObjectName("lrordens")
        self.squantity1 = QtWidgets.QSpinBox(self.groupBox)
        self.squantity1.setGeometry(QtCore.QRect(130, 130, 51, 31))
        self.squantity1.setMinimum(1)
        self.squantity1.setProperty("value", 1)
        self.squantity1.setObjectName("squantity1")
        self.lquantity1 = QtWidgets.QLabel(self.groupBox)
        self.lquantity1.setGeometry(QtCore.QRect(10, 130, 101, 31))
        self.lquantity1.setObjectName("lquantity1")
        self.lmsgordem = QtWidgets.QLabel(self.groupBox)
        self.lmsgordem.setGeometry(QtCore.QRect(0, 340, 281, 31))
        self.lmsgordem.setObjectName("lmsgordem")
        self.ltype_2 = QtWidgets.QLabel(self.groupBox)
        self.ltype_2.setGeometry(QtCore.QRect(300, 60, 91, 21))
        self.ltype_2.setObjectName("ltype_2")
        self.stype_2 = QtWidgets.QSpinBox(self.groupBox)
        self.stype_2.setGeometry(QtCore.QRect(420, 60, 51, 31))
        self.stype_2.setMinimum(1)
        self.stype_2.setMaximum(9)
        self.stype_2.setProperty("value", 1)
        self.stype_2.setObjectName("stype_2")
        ERP.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ERP)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1546, 26))
        self.menubar.setObjectName("menubar")
        self.menuordens = QtWidgets.QMenu(self.menubar)
        self.menuordens.setObjectName("menuordens")
        self.menuestatisticas = QtWidgets.QMenu(self.menubar)
        self.menuestatisticas.setObjectName("menuestatisticas")
        ERP.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ERP)
        self.statusbar.setObjectName("statusbar")
        ERP.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuordens.menuAction())
        self.menubar.addAction(self.menuestatisticas.menuAction())

        self.metodos()
        self.retranslateUi(ERP)
        QtCore.QMetaObject.connectSlotsByName(ERP)

    def retranslateUi(self, ERP):
        _translate = QtCore.QCoreApplication.translate
        ERP.setWindowTitle(_translate("ERP", "MainWindow"))
        self.groupBox.setTitle(_translate("ERP", "GroupBox"))
        self.pordem.setText(_translate("ERP", "Enviar Ordem"))
        self.pdescarga.setText(_translate("ERP", "Enviar Descarga"))
        self.parmazem.setText(_translate("ERP", "Request Armazem"))
        self.prordens.setText(_translate("ERP", "Request Ordens"))
        self.lmsgdescarga.setText(_translate("ERP", "TextLabel"))
        self.lfrom.setText(_translate("ERP", "From"))
        self.lto.setText(_translate("ERP", "To"))
        self.lmaxdelay.setText(_translate("ERP", "MaxDelay"))
        self.lpenalty.setText(_translate("ERP", "Penalty"))
        self.lquantity2.setText(_translate("ERP", "Quantity"))
        self.ltype.setText(_translate("ERP", "Type"))
        self.ldestination.setText(_translate("ERP", "Destination"))
        self.lrarmazem.setText(_translate("ERP", "TextLabel"))
        self.lrordens.setText(_translate("ERP", "TextLabel"))
        self.lquantity1.setText(_translate("ERP", "Quantity"))
        self.lmsgordem.setText(_translate("ERP", "TextLabel"))
        self.ltype_2.setText(_translate("ERP", "Id"))
        self.menuordens.setTitle(_translate("ERP", "ordens"))
        self.menuestatisticas.setTitle(_translate("ERP", "estatisticas"))

    def metodos(self):
        self.p=['','P1','P2','P3','P4','P5','P6','P7','P8','P9']
        self.id=0
        self.idd=0
        self.HOST='localhost'
        self.PORT=54321
        self.clt = socket(AF_INET,SOCK_DGRAM)
        self.pordem.clicked.connect(lambda: self.send_order())
        self.pdescarga.clicked.connect(lambda: self.send_descarga())
        self.parmazem.clicked.connect(lambda: self.send_stores())
        self.prordens.clicked.connect(lambda: self.send_req_orders())

    def send_order(self):
        msg='<Order Number="{}"><Transform From="{}" To="{}" Quantity="{}" Time="{}" MaxDelay="{}" Penalty="{}"/></Order>'.format(self.id,self.p[self.sfrom.value()],self.p[self.sto.value()],self.squantity1.value(),int(time.time()),self.smaxdelay.value(),self.spenalty.value())
        self.id=self.id+1
        #msg='<ORDERS><Order Number="001"><Transform From="P1" To="P2" Quantity="10" Time="500" MaxDelay="420" Penalty="69"/></Order><Order Number="002"><Transform From="P2" To="P8" Quantity="10" Time="500" MaxDelay="420" Penalty="69"/></Order></ORDERS>'
        self.clt.sendto(msg.encode('utf-8'),(self.HOST,self.PORT))
        text='id={} \nfrom={} \nTo={} \nQuantity={} \nMaxDelay={}\npenalty={}'.format(self.id,self.p[self.sfrom.value()],self.p[self.sto.value()],self.squantity1.value(),self.smaxdelay.value(),self.spenalty.value())
        self.lmsgordem.setText(text)
        self.lmsgordem.adjustSize()

    def send_descarga(self):
        self.idd=self.idd+1
        #msg='<Order Number="{}"><Unload Type="{}" Destination="{}" Quantity="{}"/></Order>'.format(self.stype_2.value(),self.p[self.stype.value()],self.p[self.sdestination.value()],self.squantity2.value())
        msg='<Order Number="{}"><Unload Type="{}" Destination="{}" Quantity="{}"/></Order>'.format(self.idd,self.p[self.stype.value()],self.p[self.sdestination.value()],self.squantity2.value())
        self.clt.sendto(msg.encode('utf-8'),(self.HOST,self.PORT))

        #text='id={} \nType={} \nDestination={} \nQuantity={}'.format(self.stype_2.value(),self.p[self.stype.value()],self.p[self.sdestination.value()],self.squantity2.value())
        text='id={} \nType={} \nDestination={} \nQuantity={}'.format(self.idd,self.p[self.stype.value()],self.p[self.sdestination.value()],self.squantity2.value())
        self.lmsgdescarga.setText(text)
        self.lmsgdescarga.adjustSize()

    def send_stores(self):
        msg='<Request_Stores/>'
        self.clt.sendto(msg.encode('utf-8'),(self.HOST,self.PORT))
        data,addr=self.clt.recvfrom(1025)
        text=str(data,'utf-8')
        self.lrarmazem.setText(text)
        self.lrarmazem.adjustSize()

    def send_req_orders(self):
        msg='<Request_Orders/>'
        self.clt.sendto(msg.encode('utf-8'),(self.HOST,self.PORT))
        data,addr=self.clt.recvfrom(100000)
        text=str(data,'utf-8')
        self.lrordens.setText(text)
        self.lrordens.adjustSize()
l=0
if __name__ == "__main__":
    print(l)
    l+=1
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ERP = QtWidgets.QMainWindow()
    ui = Ui_ERP()
    ui.setupUi(ERP)
    ERP.show()
    sys.exit(app.exec_())