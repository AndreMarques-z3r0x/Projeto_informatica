sck_server: sck_server.c open62541.c
	gcc -o sck_server sck_server.c `mysql_config --cflags --libs` -std=c99 open62541.c -lpthread