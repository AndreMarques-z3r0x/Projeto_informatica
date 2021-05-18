#include<iostream>
#include <mysql.h>
#include "open62541.h"


struct connection_details{
    const char *server, *user, *password, *database;
};

MYSQL* mysql_connection_setup(struct connection_details mysql_details){
    MYSQL *connection = mysql_init(NULL);

    if(!mysql_real_connect(connection, mysql_details.server, mysql_details.user, mysql_details.password, mysql_details.database, 0, NULL,0)){
        std::cout << "Connection Error: " << mysql_error(connection) << std::endl;
        exit(1);
    }

    return connection;
}

MYSQL_RES* mysql_execute_query(MYSQL *connection, const char *sql_query){
    if(mysql_query(connection, sql_query)){
        std::cout << "MySQL Query Error: " << mysql_error(connection) << std::endl;
        exit(1);
    }

    return mysql_use_result(connection);
}

int opcua_connect_to_server(){
    UA_Client *client;
    UA_StatusCode retval;
    /* OPCUA Connect */
    client = UA_Client_new();
    UA_ClientConfig_setDefault(UA_Client_getConfig(client));
    retval = UA_Client_connect(client, "opc.tcp://localhost:4840");
    if(retval != UA_STATUSCODE_GOOD) {
        UA_Client_delete(client);
        std::cout << "NAO CONECTOU! TEMOS PENA!\n" << std::endl;
        return (int)retval;
        } else{
        std::cout << "CONECTOU!!!!!!!!!!!!! " << std::endl;
    }
    return 0;
}

int main(int argc, char const *argv[]){
    
    MYSQL *con;
    MYSQL_RES *res;
    MYSQL_ROW row;

    struct  connection_details mysqlDB;
    mysqlDB.user = "andre";
    mysqlDB.server = "192.168.1.86";
    mysqlDB.password = "andre199921";
    mysqlDB.database = "informatica";

    con = mysql_connection_setup(mysqlDB);
    res = mysql_execute_query(con, "select * from orders;");

    std::cout << "Displayng database output:\n" << std::endl;

    while ((row = mysql_fetch_row(res)) != NULL )
    {
        std::cout << row[0] << std::endl;
        std::cout << "Bye bitches!!" << std::endl;
    }
    
    opcua_connect_to_server();
    std::cout << "Bye bitches!!" << std::endl;

    return 0;
}