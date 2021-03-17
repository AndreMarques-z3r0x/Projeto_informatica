from socket import *
import xml.etree.ElementTree as ET
import time
from main import DataBase
lista_ordens_pendentes=[]
lista_descargas_pendentes=[]

def request_stores_db():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]
def request_orders_db():
    dic=[0,0,0]
    for i in range(3):
        dic[i]= {"Number": i,
                "From": i,
                "To":i,
                "Quantity":i,
                "Quantity1":i,
                "Quantity2":i,
                "MaxDelay":i,
                "TT":i,
                "T1":i,
                "DD":i,
                "PP":i,
                "ST":i,
                "ET":i,
                "P1":i
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
        stores=request_stores_db()
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
        dic=request_orders_db()
        msg='<Order_Schedule>\n'
        for l in dic:
            msg=('{}'
            '<Order Number="{}">\n'
            '<Transform From="{}" To="{}" Quantity="{}" Quantity1="{}" Quantity2="{}" Quantity3="{}" Time="{}" Time1="{}" MaxDelay="{}" Penalty="{}" Start="{}" End="{}" PenaltyIncurred="{}"/>\n'
            '</Order>\n').format(msg,l["Number"],l["From"],l["To"],l["Quantity"],l["Quantity1"],l["Quantity2"],l["MaxDelay"],l["TT"],l["T1"],l["DD"],l["PP"],l["ST"],l["ET"],l["P1"])
        msg=msg + '</Order_Schedule>'
        self.send_msg_udp(msg,addr)

class ordem:
    def __init__(self,mensagem):
        self.estado=0
        self.quantity1=0
        self.time_inicio=0
        self.time_fim=0
        self.time_mes=time.time()
        for info in mensagem.findall('Transform'):
            self.number=int(mensagem.attrib["Number"])
            self.fro=int(info.attrib["From"])
            self.to=int(info.attrib["To"])
            self.quantity=int(info.attrib["Quantity"])
            self.time_erp=int(info.attrib["Time"])
            self.maxdelay=int(info.attrib["MaxDelay"])
            self.penalty=int(info.attrib["Penalty"])
        self.quantity2=self.quantity
        self.actual_penalty=0
        self.print_info()
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

class descarga:
    def __init__(self,mensagem):
        self.estado=0
        for desc in mensagem.findall('Unload'):
            self.number=int(mensagem.attrib["Number"])
            self.tipo=int(desc.attrib["Type"])
            self.destino=int(desc.attrib["Destination"])
            self.quantity=int(desc.attrib["Quantity"])
        self.print_info()
    def print_info(self):
        print('number= ',self.number)
        print('tipo= ',self.tipo)
        print('destino= ',self.destino)
        print('quantity= ',self.quantity)

erp=com_erp("127.0.0.1",54321)

while 1:
    msg,addr=erp.read_msg_udp()
    erp.parse_info(msg,addr)
    print('ordens pententes=',len(lista_ordens_pendentes))
    print('descargas pententes=',len(lista_descargas_pendentes))
