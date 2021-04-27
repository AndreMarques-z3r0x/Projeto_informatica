from socket import *
import xml.etree.ElementTree as ET
import time
from database import DataBase
import random
import threading
import subprocess


class com_erp:
    def __init__(self,host,port):
        self.HOST=host
        self.PORT=port
        self.server = socket(AF_INET, SOCK_DGRAM)
        print("inicio server")
        self.server.bind((self.HOST,self.PORT))

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
        stores=db.request_stores_db()
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
        try:
            dic=db.request_orders_db()
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
        self.estado=0
        self.quantity1=0
        self.time_inicio=0
        self.time_fim=0
        self.time_mes=int(time.time())
        for info in mensagem:
            self.number=int(mensagem.attrib["Number"])
            self.fro=info.attrib["From"]
            self.to=info.attrib["To"]
            self.quantity=int(info.attrib["Quantity"])
            self.time_erp=int(info.attrib["Time"])
            self.maxdelay=int(info.attrib["MaxDelay"])
            self.penalty=int(info.attrib["Penalty"])
        self.quantity2=0
        self.quantity3=self.quantity
        self.actual_penalty=0
        self.print_info()
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
    def tempo_atual(self):
        self.tdecorrer=self.maxdelay-(time.time()-self.time_erp)
        print('falta',self.sec)
    def calc_penalty(self):
        self.sec=time.time()-self.time_erp
        if self.sec<self.maxdelay:
            self.actual_penalty=0
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
        self.falta=self.transf
        self.t1=self.transf[1]+self.transf[4]+self.transf[8]
        self.t2=self.transf[2]+self.transf[5]
        self.t3=self.transf[3]+self.transf[6]+self.transf[7]
        print(self.de,self.para)
        print(self.transf)
        print('t1= ',self.t1)
        print('t2= ',self.t2)
        print('t3= ',self.t3)

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
        self.transf=[0,0,0,0,0,0,0,0,0]
        self.inc=[0,0,0,0,0,0,0,0,0]
        self.t1=0
        self.t2=0
        self.t3=0

        self.d1=0;
        self.d2=0;
        self.d3=0;

        self.p=[0,'P1','P2','P3','P4','P5','P6','P7','P8','P9']


    def loop_descaargas(self):

        if (self.d1+self.d2+self.d3)<3:
            i=0
            for desc in lista_descargas_pendentes:
                if desc.destino =='P1' and self.d1==0:
                    if desc.quantity<stock[self.p.index(desc.tipo)]:
                        self.d1=1
                        lista_descargas_correntes.append(desc)
                        self.p1=desc
                        mutex.acquire()
                        db.update_order_db('unload_plc', {'destination':'1','type':desc.tipo[1:],'quantity':desc.quantity,'99':1})
                        mutex.release()
                        lista_descargas_pendentes.pop(i)
                        print('descargas correntes=',len(lista_descargas_correntes))
                elif desc.destino =='P2' and self.d2==0:
                    if desc.quantity<stock[self.p.index(desc.tipo)]:
                        self.d2=1
                        lista_descargas_correntes.append(desc)
                        self.p2=desc
                        mutex.acquire()
                        db.update_order_db('unload_plc', {'destination':'2','type':desc.tipo[1:],'quantity':desc.quantity,'99':1})
                        mutex.release()
                        lista_descargas_pendentes.pop(i)
                        print('descargas correntes=',len(lista_descargas_correntes))
                elif desc.destino =='P3' and self.d3==0:
                    if desc.quantity<stock[self.p.index(desc.tipo)]:
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
            mutex.acquire()
            dic=db.read_unload_plc_state()
            mutex.release()
            if dic[0]==0:
                self.p1.estado=1
                self.p1.atualizar_descarga_db()
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
    def loop(self):

        #self.teste_ler_var(2)
        self.inc=[0,0,0,0,0,0,0,0,0]
        self.t1=self.transf[1]+self.transf[4]+self.transf[8]
        self.t2=self.transf[2]+self.transf[5]
        self.t3=self.transf[3]+self.transf[6]+self.transf[7]
        print('f1= {},f2= {},f3 == {}'.format(self.t1,self.t2,self.t3))
        if self.t1!=5 or self.t2!=5 or self.t3!=55:

             f1=5-self.t1
             f2=5-self.t2
             f3=5-self.t3
             print('calc-f1= {},f2= {},f3 == {}'.format(f1,f2,f3))
             for pedido in lista_ordens_correntes:
                if f1>0:
                    for j in [1,4,8]:
                        if f1>0:
                            if pedido.falta[j]>0:
                                pedido.falta[j]=pedido.falta[j]-f1
                                self.transf[j]=self.transf[j]+f1
                                self.inc[j]=self.inc[j]+f1
                                f1=0
                                if pedido.falta[j]<0:
                                    f1=pedido.falta[j]*(-1)
                                    pedido.falta[j]=0
                                    self.transf[j]=self.transf[j]-f1
                                    self.inc[j]=self.inc[j]-f1
                                if pedido.falta[j]>0:
                                    f1=0
                if f2>0:
                    for j in [2,5]:
                        if pedido.falta[j]>0:
                            pedido.falta[j]=pedido.falta[j]-f2
                            self.transf[j]=self.transf[j]+f2
                            self.inc[j]=self.inc[j]+f2
                            f2=0
                            if pedido.falta[j]<0:
                                f2=pedido.falta[j]*(-1)
                                pedido.falta[j]=0
                                self.transf[j]=self.transf[j]-f2
                                self.inc[j]=self.inc[j]-f2
                            if pedido.falta[j]>0:
                                f2=0
                if f3>0:
                    for j in [3,6,7]:
                        if pedido.falta[j]>0:
                            pedido.falta[j]=pedido.falta[j]-f3
                            self.transf[j]=self.transf[j]+f3
                            self.inc[j]=self.inc[j]+f3
                            f3=0
                            if pedido.falta[j]<0:
                                f3=pedido.falta[j]*(-1)
                                pedido.falta[j]=0
                                self.transf[j]=self.transf[j]-f3
                                self.inc[j]=self.inc[j]-f3
                            if pedido.falta[j]>0:
                                f3=0

             if (f1>0 or f2>0 or f3>0)and lista_ordens_pendentes!=[]:
                lista_ordens_correntes.append(lista_ordens_pendentes.pop(0))
        print('fim-f1= {},f2= {},f3 == {}'.format(f1,f2,f3))
        j=0
        for i in lista_ordens_correntes:
            if sum(i.falta)==0:
                print('pop ',i.falta)
                lista_ordens_feitas.append(lista_ordens_correntes.pop(j))
            j=j+1

            print('lista',i.falta)

        print('self=',self.transf)
        print('inc=', self.inc)
        print('soma',sum(self.transf))
        print('----------')
        mutex.acquire()
        self.transf = db.insert_incr(self.inc[1:9])
        mutex.release()
        print('QUALQUER COISA EM CAPS LOCK: !! ' , self.transf)

def loop_man():
    while 1:
        if lista_ordens_pendentes!=[] or lista_ordens_correntes!=[] or sum(man.transf)!=0:
            man.sort_order()
            man.loop()

        if lista_descargas_pendentes!=[] or lista_descargas_correntes!=[]:
            man.loop_descaargas()


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
db.clear_db_tables()
man=manager()

manager_t = threading.Thread(target=loop_man)
manager_t.start()
#subprocess.run(["bash", "insert.sh"])

if __name__ == '__main__':
    while 1:
        msg,addr=erp.read_msg_udp()
        erp.parse_info(msg,addr)
        print('desc pend=',len(lista_descargas_pendentes))
