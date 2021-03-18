from socket import *
import xml.etree.ElementTree as ET
import time
from database import DataBase

def request_stores_db():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]
def request_orders_db():
    dic=[0,0,0]
    for i in range(3):
        dic[i]= {"nnn": i,
                "from": i,
                "to":i,
                "quantity":i,
                "quantity1":i,
                "quantity2":i,
                "quantity3":i,
                "maxdelay":i,
                "time":i,
                "time1":i,
                "max_delay":i,
                "penalty":i,
                "start":i,
                "end":i,
                "penalty_incurred":i,
                "estado":i
                }
    return dic



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
        self.transorma()
        db.insert_order_db('transform', dic)
        self.calc_penalty()
        
    def print_info(self):
        print('---------------------------------')
        print('number= ',self.number)
        print('fro= ',self.fro)
        print('to= ',self.to)
        print('quantity= ',self.quantity)
        print('maxmelay= ',self.maxdelay)
        print('penalty= ',self.penalty)
        print('---------------------------------')

    def calc_penalty(self):
        sec=time.time()-self.time_erp
        if sec<self.maxdelay:
            self.actual_penalty=0
        else:
            sec=int((sec-self.maxdelay)/50)+1
            self.actual_penalty=sec*self.penalty
        print('---------------------------------')
        print('actual_penalty=',self.actual_penalty)
        print('---------------------------------')
    def transforma(self):
        a=['','P1','P2','P3','P4','P5','P6','P7','P8','P9']
        self.transf=[0]*9

        de=a.index(self.fro)
        para=a.index(self.to)

        if de<=5 and para==9:
            self.transf[6]=self.quantity
        if de<=5 and para==6:
            self.transf[5]=self.quantity
        if de<=6 and para==7:
            self.transf[7]=self.quantity
        if de<=6 and para==8:
            self.transf[8]=self.quantity
        for i in range(de,5):
            self.transf[i]=self.quantity

        self.t1=self.transf[1]+self.transf[4]+self.transf[8]
        self.t2=self.transf[2]+self.transf[5]
        self.t3=self.transf[3]+self.transf[6]+self.transf[7]
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
        db.insert_order_db('unload', dic)

        self.print_info()
    def print_info(self):
        print('number= ',self.number)
        print('tipo= ',self.tipo)
        print('destino= ',self.destino)
        print('quantity= ',self.quantity)


erp=com_erp("127.0.0.1",54321)
lista_ordens_pendentes=[]
lista_descargas_pendentes=[]
db = DataBase("dbConfig.txt")
db.clear_db_tables()

if __name__ == '__main__':

    while 1:
        msg,addr=erp.read_msg_udp()
        erp.parse_info(msg,addr)
        print('ordens pententes=',len(lista_ordens_pendentes))
        print('descargas pententes=',len(lista_descargas_pendentes))
