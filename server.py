from socket import *
import xml.etree.ElementTree as ET
import time
from database import DataBase
import random
import threading
import subprocess
import sys

from old_ui import Ui_ERP
#from ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
i=0
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1178, 944)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table_ordens = QtWidgets.QTableWidget(self.centralwidget)

        self.table_ordens.setGeometry(QtCore.QRect(0, 450, 1131, 371))
        self.table_ordens.setObjectName("table_ordens")
        self.table_ordens.setColumnCount(8)
        self.table_ordens.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.table_ordens.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ordens.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ordens.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ordens.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ordens.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ordens.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ordens.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ordens.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ordens.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ordens.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ordens.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ordens.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ordens.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ordens.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ordens.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ordens.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ordens.setHorizontalHeaderItem(7, item)
        self.table_descargas = QtWidgets.QTableWidget(self.centralwidget)
        self.table_descargas.setGeometry(QtCore.QRect(0, 0, 501, 451))
        self.table_descargas.setObjectName("table_descargas")
        self.table_descargas.setColumnCount(3)
        self.table_descargas.setRowCount(11)
        item = QtWidgets.QTableWidgetItem()
        self.table_descargas.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_descargas.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_descargas.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_descargas.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_descargas.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_descargas.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_descargas.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_descargas.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_descargas.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_descargas.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_descargas.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_descargas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_descargas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_descargas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_descargas.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_descargas.setItem(3, 0, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1178, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.table_ordens.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Tempo operação"))
        item = self.table_ordens.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "P1"))
        item = self.table_ordens.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "P2"))
        item = self.table_ordens.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "P3"))
        item = self.table_ordens.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "P4"))
        item = self.table_ordens.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "P5"))
        item = self.table_ordens.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "P6"))
        item = self.table_ordens.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "NÚMERO TOTAL"))
        item = self.table_ordens.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "TEMPO TOTAL"))
        item = self.table_ordens.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "M1"))
        item = self.table_ordens.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "M2"))
        item = self.table_ordens.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "M3"))
        item = self.table_ordens.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "M4"))
        item = self.table_ordens.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "M5"))
        item = self.table_ordens.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "M6"))
        item = self.table_ordens.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "M7"))
        item = self.table_ordens.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "M8"))
        item = self.table_descargas.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "DESCARGA"))
        item = self.table_descargas.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "P1"))
        item = self.table_descargas.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "P2"))
        item = self.table_descargas.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "P3"))
        item = self.table_descargas.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "P4"))
        item = self.table_descargas.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "P5"))
        item = self.table_descargas.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "P6"))
        item = self.table_descargas.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "P7"))
        item = self.table_descargas.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "P8"))
        item = self.table_descargas.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "P9"))
        item = self.table_descargas.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "TOTAL"))
        item = self.table_descargas.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "D1"))
        item = self.table_descargas.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "D2"))
        item = self.table_descargas.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "D3"))
        self.table_descargas.setSortingEnabled(False)
        __sortingEnabled = self.table_descargas.isSortingEnabled()
        '''
        item = self.table_descargas.item(1, 1)
        item.setItem(_translate("MainWindow","1"))


        '''
        print('cona')




        self.table_descargas.setSortingEnabled(__sortingEnabled)

        self.checkThreadTimer = QtCore.QTimer()
        self.checkThreadTimer.setInterval(1000) #.5 seconds
        self.checkThreadTimer.timeout.connect(self.rel)
        self.checkThreadTimer.start(1000)
        '''
        self.at = QtWidgets.QPushButton(self.centralwidget)
        self.at.setGeometry(QtCore.QRect(20+500, 280, 161, 51))
        self.at.setObjectName("ATUALIZAR")

        self.at.setText(_translate("MainWindow", "at"))
        self.at.clicked.connect(lambda: self.rel())
        '''

    def rel(self):
        print('cona')
        for i in range(0,3):
            for j in range(1,10):
                if i==0:

                        self.table_descargas.setItem(j,i,QtWidgets.QTableWidgetItem( str(man.total_tipo_descarga1[j])))


                elif i==1:

                        self.table_descargas.setItem(j,i,QtWidgets.QTableWidgetItem( str(man.total_tipo_descarga2[j])))

                else:
                    try:
                        self.table_descargas.setItem(j,i,QtWidgets.QTableWidgetItem(str( man.total_tipo_descarga3[j])))
                    except:
                        print('f')
        print("[+] man Total str mae do lucas --> ",str(man.total_tipo_descarga1))
        print("[+] man Total --> ", man.total_tipo_descarga1)
        self.table_descargas.setItem(10,0,QtWidgets.QTableWidgetItem(str( sum(man.total_tipo_descarga1))))
        self.table_descargas.setItem(10,1,QtWidgets.QTableWidgetItem(str( sum(man.total_tipo_descarga2))))
        self.table_descargas.setItem(10,2,QtWidgets.QTableWidgetItem(str( sum(man.total_tipo_descarga3))))


class com_erp:
    def __init__(self,host,port):
        self.HOST=host
        self.PORT=port
        self.server = socket(AF_INET, SOCK_DGRAM)
        print("inicio server")
        self.server.bind(("0.0.0.0",self.PORT))

    def read_msg_udp(self):
            msg,addr=self.server.recvfrom(1025)
            print("data= ",str(msg,'utf-8'))
            return str(msg,'utf-8'),addr
    def send_msg_udp(self,msg,addr):
        msg=msg.encode('utf-8')
        self.server.sendto(msg,addr)
    def parse_info(self,msg,addr):
        mensagem=ET.fromstring(msg)

        if mensagem.tag=='ORDERS':
            for ord in mensagem:
                 lista_ordens_pendentes.append(ordem(ord))

        if mensagem.tag=='Order':
            if mensagem.findall('Transform')!=[]:
                lista_ordens_pendentes.append(ordem(mensagem))
            if mensagem.findall('Unload')!=[]:
                lista_descargas_pendentes.append(descarga(mensagem))
        if mensagem.tag=='Request_Stores':
            print("store")
            self.send_stores(addr)
        if mensagem.tag=='Request_Orders':
            print("req_order")
            self.send_orders(addr)
    def send_stores(self,addr):
        mutex.acquire()
        stores=db.request_stores_db()
        mutex.release()
        msg=('<Current_Stores>\n'
            '<WorkPiece type="P1" quantity="{}"/>\n'
            '<WorkPiece type="P2" quantity="{}"/>\n'
            '<WorkPiece type="P3" quantity="{}"/>\n'
            '<WorkPiece type="P4" quantity="{}"/>\n'
            '<WorkPiece type="P5" quantity="{}"/>\n'
            '<WorkPiece type="P6" quantity="{}"/>\n'
            '<WorkPiece type="P7" quantity="{}"/>\n'
            '<WorkPiece type="P8" quantity="{}"/>\n'
            '<WorkPiece type="P9" quantity="{}"/>\n'
            '</Current_Stores>').format(stores[0],stores[1],stores[2],stores[3],stores[4],stores[5],stores[6],stores[7],stores[8])
        self.send_msg_udp(msg,addr)
    def send_orders(self,addr):

        for s in lista_ordens_feitas:
            s.atualizar()
        for s in lista_ordens_pendentes:
            s.atualizar()
        for s in lista_ordens_correntes:
            s.atualizar()

        try:
            mutex.acquire()
            dic=db.request_orders_db()
            mutex.release()
            print(dic)

        except ValueError:
            print('estourou func')

        msg='<Order_Schedule>\n'
        for l in dic:
            msg=('{}'
            '<Order Number="{}">\n'
            '<Transform From="{}" To="{}" Quantity="{}" Quantity1="{}" Quantity2="{}" Quantity3="{}" Time="{}" Time1="{}" MaxDelay="{}" Penalty="{}" Start="{}" End="{}" PenaltyIncurred="{}"/>\n'
            '</Order>\n').format(msg,l["nnn"],l["from"],l["to"],l["quantity"],l["quantity1"],\
            l["quantity2"],l["quantity3"],l["time"],l["time1"],l["max_delay"],l["penalty"],l["start"],l["end"],l["penalty_incurred"])
        msg=msg + '</Order_Schedule>'
        self.send_msg_udp(msg,addr)

class ordem:
    def __init__(self,mensagem):
        self.p=[0,'P1','P2','P3','P4','P5','P6','P7','P8','P9']

        self.estado=0
        self.quantity1=0   #ja produzidas
        self.quantity2=0   # em produção
        self.time_inicio=0 #ST
        self.time_fim=0    #ET
        self.time_mes=int(time.time())
        for info in mensagem:
            self.number=int(mensagem.attrib["Number"])
            self.fro=info.attrib["From"]
            self.to=info.attrib["To"]
            self.quantity=int(info.attrib["Quantity"])
            self.time_erp=int(info.attrib["Time"])
            self.maxdelay=int(info.attrib["MaxDelay"])
            self.penalty=int(info.attrib["Penalty"])

        self.quantity3=self.quantity  #por produzir

        self.actual_penalty=0
        dic={"nnn":self.number,"from":self.fro,"to":self.to,"quantity":self.quantity,"quantity1":self.quantity1,"quantity2": self.quantity2,\
        "quantity3":self.quantity3,"time":self.time_erp,"time1":self.time_mes,"max_delay":self.maxdelay,\
        "penalty":self.penalty,"start":self.time_inicio,"end":self.time_fim,"penalty_incurred":self.actual_penalty,'estado':self.estado}
        self.transforma()
        mutex.acquire()
        db.insert_order_db('transform', dic)
        mutex.release()
        self.calc_penalty()
        self.tempo_atual()

    def print_info(self):
        print('---------------------------------')
        print('number= ',self.number)
        print('fro= ',self.fro)
        print('to= ',self.to)
        print('quantity= ',self.quantity)
        print('maxmelay= ',self.maxdelay)
        print('penalty= ',self.penalty)
        print('---------------------------------')
    def atualizar(self):

        self.quantity1=sum(np.subtract(self.transf,self.falta_mesmo))
        self.quantity2=sum(self.falta_mesmo)
        self.quantity3=sum(self.falta_mesmo)
        if self.estado != 2:
            self.calc_penalty()
        dic={"nnn":self.number,"from":self.fro,"to":self.to,"quantity":self.quantity,"quantity1":self.quantity1,"quantity2": self.quantity2,\
        "quantity3":self.quantity3,"time":self.time_erp,"time1":self.time_mes,"max_delay":self.maxdelay,\
        "penalty":self.penalty,"start":self.time_inicio,"end":self.time_fim,"penalty_incurred":self.actual_penalty,'estado':self.estado}
        mutex.acquire()
        db.update_order_db('transform', dic)
        mutex.release()

    def tempo_atual(self):
        self.tdecorrer=self.maxdelay-(time.time()-self.time_mes)
        print('falta',self.sec)
    def calc_penalty(self):
        self.sec=time.time()-self.time_mes
        if self.sec<self.maxdelay:
            self.actual_penalty=0
        else:
            sec=int((self.sec-self.maxdelay)/50)+1
            self.actual_penalty=sec*self.penalty
        print('---------------------------------')
        print('actual_penalty=',self.actual_penalty)
        print('---------------------------------')
    def transforma(self):
        a=['','P1','P2','P3','P4','P5','P6','P7','P8','P9']

        self.transf=[0]*9

        self.de=a.index(self.fro)
        self.para=a.index(self.to)

        if self.de<=5 and self.para==9:
            self.transf[6]=self.quantity
        if self.de<=5 and self.para==6:
            self.transf[5]=self.quantity
        if self.de<=6 and self.para==7:
            self.transf[7]=self.quantity
        if self.de<=6 and self.para==8:
            self.transf[8]=self.quantity
        if self.de<=5 and self.para>=6 and self.para<=8 :
            self.transf[5]=self.quantity
        for i in range(self.de,self.para):
            if i<5:
                self.transf[i]=self.quantity
            else: break
        self.falta=self.transf.copy()
        self.falta_mesmo=self.transf.copy()

        self.t1=self.transf[1]+self.transf[4]+self.transf[8]
        self.t2=self.transf[2]+self.transf[5]
        self.t3=self.transf[3]+self.transf[6]+self.transf[7]
        print(self.de,self.para)
        print(self.transf)


class descarga:
    def __init__(self,mensagem):
        self.estado=0
        for desc in mensagem:
            self.number=int(mensagem.attrib["Number"])
            self.tipo=desc.attrib["Type"]
            self.destino=desc.attrib["Destination"]
            self.quantity=int(desc.attrib["Quantity"])

        dic={"nnn":self.number,"type":self.tipo,"destination":self.destino,"quantity":self.quantity,'estado':self.estado}
        mutex.acquire()
        db.insert_order_db('unload', dic)
        mutex.release()
        self.print_info()
    def print_info(self):
        print('number= ',self.number)
        print('tipo= ',self.tipo)
        print('destino= ',self.destino)
        print('quantity= ',self.quantity)
    def atualizar_descarga_db(self):
        dic={"nnn":self.number,"type":self.tipo,"destination":self.destino,"quantity":self.quantity,'estado':self.estado}
        mutex.acquire()
        db.update_order_db('unload', dic)
        mutex.release()

class manager:
    def __init__(self) :
        self.tempo_oper=[0,0,0,0,0,0,0]
        self.total_tipo=[0,0,0,0,0,0,0,0,0]
        self.total_peca=0

        self.total_descarga1=0
        self.total_descarga2=0
        self.total_descarga3=0
        self.total_tipo_descarga1=[0,0,0,0,0,0,0,0,0,0]
        self.total_tipo_descarga2=[0,0,0,0,0,0,0,0,0,0]
        self.total_tipo_descarga3=[0,0,0,0,0,0,0,0,0,0]


        self.transf=[0,0,0,0,0,0,0,0,0]
        self.inc=[0,0,0,0,0,0,0,0,0]
        self.b=[0,1,2,3,4,5,5,6,6]
        self.c=[0,2,3,4,5,6,9,7,8]
        self.t1=0
        self.t2=0
        self.t3=0
        self.tool=[1,2,3,1,1,2,3,3]
        self.d1=0
        self.d2=0
        self.d3=0

        self.racio1=0.375
        self.racio2=0.25
        self.racio3=0.375
        self.soma_buff=40
        self.buffer=20
        self.buffer1=5
        self.buffer2=5
        self.buffer3=5
        self.p=[0,'P1','P2','P3','P4','P5','P6','P7','P8','P9']
    def loop_descaargas(self):

        if (self.d1+self.d2+self.d3)<3:
            i=0
            for desc in lista_descargas_pendentes:
                if desc.destino =='P1' and self.d1==0:
                    if desc.quantity<=stock[self.p.index(desc.tipo)]:
                        self.d1=1
                        lista_descargas_correntes.append(desc)
                        self.p1=desc
                        mutex.acquire()
                        db.update_order_db('unload_plc', {'destination':'1','type':desc.tipo[1:],'quantity':desc.quantity,'99':1})
                        mutex.release()
                        lista_descargas_pendentes.pop(i)
                        print('descargas correntes=',len(lista_descargas_correntes))
                elif desc.destino =='P2' and self.d2==0:
                    if desc.quantity<=stock[self.p.index(desc.tipo)]:
                        self.d2=1
                        lista_descargas_correntes.append(desc)
                        self.p2=desc
                        mutex.acquire()
                        db.update_order_db('unload_plc', {'destination':'2','type':desc.tipo[1:],'quantity':desc.quantity,'99':1})
                        mutex.release()
                        lista_descargas_pendentes.pop(i)
                        print('descargas correntes=',len(lista_descargas_correntes))
                elif desc.destino =='P3' and self.d3==0:
                    if desc.quantity<=stock[self.p.index(desc.tipo)]:
                        self.d3=1
                        lista_descargas_correntes.append(desc)
                        self.p3=desc
                        mutex.acquire()
                        db.update_order_db('unload_plc', {'destination':'3','type':desc.tipo[1:],'quantity':desc.quantity,'99':1})
                        mutex.release()
                        lista_descargas_pendentes.pop(i)
                        print('descargas correntes=',len(lista_descargas_correntes))
                i=i+1
        if self.d1==1:
            '''
            mutex.acquire()
            dic=db.read_unload_plc_state()
            mutex.release()
            '''
            dic=self.teste_ler_descargas()
            if dic[0]==0:
                self.p1.estado=1
                self.p1.atualizar_descarga_db()
                self.total_descarga1+=self.p1.quantity
                self.total_tipo_descarga1[int(self.p1.tipo[1:])]+=self.p1.quantity
                print("[+] Total Tipo -->",self.total_tipo_descarga1)
                print("[+] P1 --> ", int(self.p1.tipo[1:]))
                lista_descargas_feitas.append(self.p1)

                print('descargas feitas=',len(lista_descargas_feitas))
                self.d1=0
        if self.d2==1:
            mutex.acquire()
            dic=db.read_unload_plc_state()
            mutex.release()
            if dic[1]==0:
                self.p2.estado=1
                self.p2.atualizar_descarga_db()
                self.total_descarga2+=self.p2.quantity
                self.total_tipo_descarga2[int(self.p2.tipo[1:])]+=self.p2.quantity
                lista_descargas_feitas.append(self.p2)
                print('descargas feitas=',len(lista_descargas_feitas))
                self.d2=0
        if self.d3==1:
            mutex.acquire()
            dic=db.read_unload_plc_state()
            mutex.release()
            if dic[2]==0:
                self.p3.estado=1
                self.p3.atualizar_descarga_db()
                self.total_descarga3+=self.p3.quantity
                self.total_tipo_descarga3[int(self.p3.tipo[1:])]+=self.p3.quantity
                lista_descargas_feitas.append(self.p3)
                print('descargas feitas=',len(lista_descargas_feitas))
                self.d3=0

    def teste_ler_descargas(self):
        return [0,0,0]
    def teste_ler_var(self,valor):
        for i in range(1,9):
            if self.transf[i]>valor+1:
                self.transf[i]=self.transf[i]-random.randrange(valor)
            else:
                self.transf[i]=0
    def sort_order(self,lista):
        for l in lista:
            l.tempo_atual()
        lista.sort(key=lambda x:x.tdecorrer, reverse=True)
        for l in lista:
            print('sort- ',l.number)
        return lista
    def check_order_finish(self,dif):
        for pedido in lista_ordens_correntes:
            for s in range(1,9):
                if dif[s]>0:
                    if pedido.falta_mesmo[s]>0:
                        pedido.falta_mesmo[s]-=dif[s]
                        dif[s]=0
                        if pedido.falta_mesmo[s]<0:
                            dif[s]=pedido.falta_mesmo[s]*(-1)
                            pedido.falta_mesmo[s]=0
    def ver_maquinas(self):
        b1=0
        b2=0
        b3=0
        soma=0
        print('REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
        for ord in lista_ordens_correntes:

            b1=b1+ ord.falta_mesmo[1]*15+ord.falta_mesmo[4]*15+ord.falta_mesmo[8]*15
            b2=b2+ ord.falta_mesmo[2]*15+ord.falta_mesmo[5]*30
            b3=b3+ ord.falta_mesmo[3]*15+ord.falta_mesmo[6]*30+ord.falta_mesmo[7]*30
        soma=b1+b2+b3
        k1=0
        k2=0
        k3=0
        for i in range(0,8):
            k1=k1+1*(self.tool[i]==1)
            k2=k2+1*(self.tool[i]==2)
            k3=k3+1*(self.tool[i]==3)

        self.racio1=k1/8
        self.buffer1=int(self.buffer*self.racio1)
        self.racio2=k2/8
        self.buffer2=int(self.buffer*self.racio2)
        self.racio3=k3/8
        self.buffer3=int(self.buffer*self.racio3)
        print('buffer1={} buffer2={} buffer3={} '.format(self.buffer1,self.buffer2,self.buffer3))
        print('racio1={} racio2={} racio3={} '.format(self.racio1,self.racio2,self.racio3))
        print('k1={} k2={} k3={} '.format(k1,k2,k3))
        #positivo maquinas a mais
        dif=[0,0,0]
        dif[0]=soma*self.racio1-b1
        dif[1]=soma*self.racio2-b2
        dif[2]=soma*self.racio3-b3
        x=dif.index(max(dif))
        x1=dif.index(min(dif))
        print('MAX=' ,x)
        print('MIN=' ,x1)
        if abs(dif[0])>self.soma_buff or abs(dif[1] )>self.soma_buff  or abs(dif[2] )>self.soma_buff :
             for i in range(0,8):

                 if self.tool[i]==x+1:
                     print('IIIIIIIII=',i)
                     self.tool[i]=x1+1
                     print('tooooooooooool=' ,self.tool)
                     db.tools_change(self.tool)
                     #self.atualizar_tool(self.tool)
                     break
    def atualizar_tool(self,tool):
        return 1
    def loop_teste(self):

        self.inc=[0,0,0,0,0,0,0,0,0]
        self.t1=self.transf[1]+self.transf[4]+self.transf[8]
        self.t2=self.transf[2]+self.transf[5]
        self.t3=self.transf[3]+self.transf[6]+self.transf[7]

        #if self.t1!=self.buffer1 or self.buffer2 or self.t3!=self.buffer3:
        f1=self.buffer1-self.t1
        f2=self.buffer2-self.t2
        f3=self.buffer3-self.t3

        for pedido in lista_ordens_correntes:
            if f1>0 :
                for j in [1,4,8]:
                    if f1>0:
                        if pedido.falta[j]>0:
                            if f1>stock[self.b[j]]: dec=stock[self.b[j]]
                            else: dec=f1

                            pedido.falta[j]=pedido.falta[j]-dec
                            self.transf[j]=self.transf[j]+dec
                            self.inc[j]=self.inc[j]+dec
                            dec=0
                            if pedido.falta[j]<0:
                                dec=pedido.falta[j]*(-1)
                                pedido.falta[j]=0
                                self.transf[j]=self.transf[j]-dec
                                self.inc[j]=self.inc[j]-dec

                            if f1>stock[self.b[j]]:
                                f1=f1-stock[self.b[j]]+dec
                                stock[self.b[j]]=stock[self.b[j]] - stock[self.b[j]] + dec

                            else:
                                stock[self.b[j]]=stock[self.b[j]]-f1+dec
                                f1=dec
            if f2>0:
                for j in [2,5]:
                    if pedido.falta[j]>0:
                        if f2>stock[self.b[j]]: dec=stock[self.b[j]]
                        else: dec=f2

                        pedido.falta[j]=pedido.falta[j]-dec
                        self.transf[j]=self.transf[j]+dec
                        self.inc[j]=self.inc[j]+dec
                        dec=0
                        if pedido.falta[j]<0:
                            dec=pedido.falta[j]*(-1)
                            pedido.falta[j]=0
                            self.transf[j]=self.transf[j]-dec
                            self.inc[j]=self.inc[j]-dec

                        if f2>stock[self.b[j]]:
                            f2=f2-stock[self.b[j]]+dec
                            stock[self.b[j]]=stock[self.b[j]] - stock[self.b[j]] + dec

                        else:
                            stock[self.b[j]]=stock[self.b[j]]-f2+dec
                            f2=dec
            if f3>0:
                for j in [3,6,7] :

                    if pedido.falta[j]>0 :
                        if f3>stock[self.b[j]]: dec=stock[self.b[j]]
                        else: dec=f3

                        pedido.falta[j]=pedido.falta[j]-dec
                        self.transf[j]=self.transf[j]+dec
                        self.inc[j]=self.inc[j]+dec
                        dec=0
                        if pedido.falta[j]<0:
                            dec=pedido.falta[j]*(-1)
                            pedido.falta[j]=0
                            self.transf[j]=self.transf[j]-dec
                            self.inc[j]=self.inc[j]-dec
                        if f3>stock[self.b[j]]:
                            f3=f3-stock[self.b[j]]+dec
                            stock[self.b[j]]=stock[self.b[j]] - stock[self.b[j]] + dec

                        else:
                            stock[self.b[j]]=stock[self.b[j]]-f3+dec
                            f3=dec


        if (f1>0 or f2>0 or f3>0)and lista_ordens_pendentes!=[]:
            #stock[self.p.index(lista_ordens_pendentes[0].fro)]-=lista_ordens_pendentes[0].quantity
            lista_ordens_pendentes[0].time_inicio=time.time()
            lista_ordens_pendentes[0].estado=1
            lista_ordens_pendentes[0].atualizar()
            lista_ordens_correntes.append(lista_ordens_pendentes.pop(0))


        print('inc=', self.inc)
        self.temp=[0,0,0,0,0,0,0,0,0,0]
        self.temp=self.transf.copy()
        #self.teste_ler_var(2)

        mutex.acquire()
        x = db.insert_incr(self.inc[1:9])
        self.transf=x.copy()
        mutex.release()

        diference=np.subtract(self.temp,self.transf)

        print('DIFERENCE->',diference)
        for i in range(1,9):
            stock[self.c[i]]+=diference[i]


        self.tempo_oper[1]+=diference[1]*15
        self.tempo_oper[2]+=diference[2]*15
        self.tempo_oper[3]+=diference[3]*15
        self.tempo_oper[4]+=diference[4]*15
        self.tempo_oper[5]+=diference[5]*30+ diference[6]*30
        self.tempo_oper[6]+=diference[7]*30+ diference[8]*15

        self.total_tipo[1]+=diference[1]
        self.total_tipo[2]+=diference[2]
        self.total_tipo[3]+=diference[3]
        self.total_tipo[4]+=diference[4]
        self.total_tipo[5]+=diference[5]
        self.total_tipo[6]+=diference[6]
        self.total_tipo[7]+=diference[7]
        self.total_tipo[8]+=diference[8]

        self.total_peca=sum(self.total_tipo)



        self.check_order_finish(diference)

        j=0
        for i in lista_ordens_correntes:
            print('falta=', i.falta)
            print('falta mesmo=', i.falta_mesmo)
            if sum(i.falta_mesmo)==0:
                print('pop ',i.falta_mesmo)
                #stock[self.p.index(i.to)]+=i.quantity
                lista_ordens_correntes[j].time_fim= time.time()
                lista_ordens_correntes[j].calc_penalty()
                lista_ordens_correntes[j].estado=2
                lista_ordens_correntes[j].atualizar()
                lista_ordens_feitas.append(lista_ordens_correntes.pop(j))
            j=j+1
        print('stock',stock)
        print('----------')


def loop_man():
    while 1:

        if lista_ordens_pendentes!=[] or lista_ordens_correntes!=[] or sum(man.transf)!=0:
            man.sort_order(lista_ordens_pendentes)
            man.ver_maquinas()
            man.loop_teste()

        if lista_descargas_pendentes!=[] or lista_descargas_correntes!=[]:
            man.loop_descaargas()

        try:
            if keyboard.is_pressed('a'):
                erp.server.close()
                print('Abortar')
                break
        except:
            print('reeeeeeer')
            pass


def ui_estat():

    ap = QtWidgets.QApplication(sys.argv)
    print("11111111111111111111111111111111")
    MainWindo = QtWidgets.QMainWindow()
    print("222222222222222222222222222222222")
    ui_estat = Ui_MainWindow()
    print("333333333333333333333333333333333")
    ui_estat.setupUi(MainWindo)
    print("44444444444444444444444444444444")
    MainWindo.show()
    print("555555555555555555555555555555555")
    sys.exit(ap.exec_())
    print("69696969696969696969696969696969")





import keyboard
import numpy as np
mutex = threading.Lock()
erp=com_erp("127.0.0.1",54321)
lista_ordens_pendentes=[]
lista_ordens_correntes=[]
lista_ordens_feitas=[]
lista_descargas_pendentes=[]
lista_descargas_correntes=[]
lista_descargas_feitas=[]

stock=[0,400,40,20,20,20,20,0,0,0]
db = DataBase("dbConfig.txt")
mutex.acquire()
db.clear_db_tables()
mutex.release()
man=manager()

manager_t = threading.Thread(target=loop_man)
manager_t.start()
#subprocess.run(["bash", "insert.sh"])

ui_estat_t = threading.Thread(target=ui_estat)
ui_estat_t.start()


if __name__ == '__main__':
    while 1:
        msg,addr=erp.read_msg_udp()
        erp.parse_info(msg,addr)
        print('desc pend=',len(lista_descargas_pendentes))
