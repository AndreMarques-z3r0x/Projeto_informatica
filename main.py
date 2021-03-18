
import multiprocessing
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from socket import *
import time
import xml.etree.ElementTree as ET
from ui import Ui_ERP
from server import com_erp,ordem,descarga
from database import DataBase
def spawn():
    print('Spawned')
    app = QtWidgets.QApplication(sys.argv)
    ERP = QtWidgets.QMainWindow()
    ui = Ui_ERP()
    ui.setupUi(ERP)
    ERP.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    p = multiprocessing.Process(target=spawn)
    p.start()
    lista_ordens_pendentes=[]
    lista_descargas_pendentes=[]
    db = DataBase("dbConfig.txt")
    db.clear_db_tables()
    erp=com_erp("127.0.0.1",54321,db)
    while(1):
        msg,addr=erp.read_msg_udp()
        erp.parse_info(msg,addr)
        print('ordens pententes=',len(lista_ordens_pendentes))
        print('descargas pententes=',len(lista_descargas_pendentes))
