from time import sleep
import random
from opcua import Server

server = Server()
server.set_endpoint("opc.tcp://127.0.0.1:12345")
server.register_namespace("Room1")
objects = server.get_objects_node()
print(objects)
tempsens = objects.add_object('ns=2;s="TS1"', "Temperature Sensor 1")
print(tempsens)
tempsens.add_variable('ns=2;s="TS1_vendor_name"', "TS1 Vendor Name", "Sensor King")
tempsens.add_variable('ns=2;s="TS1_serial_number"', "TS1 Serial Nunber", 12345678)
temp = tempsens.add_variable('ns=2;s="TS1_Temperature"',"TS1 Temperature",20)
bulb = objects.add_object(2, "Light Bulb")
print(bulb)
state= bulb.add_variable(2, "state of Light Bulb", False)
print(state)
state.set_writable()
temperature = 20.0
try:
    print("start server")
    server.start()
    print("server online")
    while True:
        temperature += random.uniform(-1,1)
        temp.set_value(temperature)
        print("New temperature: " + str(temp.get_value()))
        print("Bulb State: " + str(state.get_value()))
        sleep(2)
finally:
    server.stop()
    print('Server offfline')
