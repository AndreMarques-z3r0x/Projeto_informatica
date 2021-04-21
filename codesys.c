#include "open62541.h"
#include <mysql.h>
#include <stdlib.h>
#include <unistd.h>

int main(void) {

    MYSQL *conn;
	MYSQL_RES *res;
	MYSQL_ROW row;
	
	char *server = "192.168.1.86";
	char *user = "andre";
	char *password = "andre199921";
	char *database = "informatica";

    int columns[8] = {12, 23, 34,45,56,59,67,68};
    char query[150];
	
	UA_Client *client = UA_Client_new();
    UA_ClientConfig_setDefault(UA_Client_getConfig(client));
    UA_StatusCode retval = UA_Client_connect(client, "opc.tcp://localhost:4840");
    if(retval != UA_STATUSCODE_GOOD) {
        UA_Client_delete(client);
        printf("Nao conectou! Temos Pena!");
        return (int)retval;
        }
    
    else{
        printf("Conectou!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n");
    }
    
    conn = mysql_init(NULL);
	
	/* Connect to database */
	if (!mysql_real_connect(conn, server, user, password, 
                                      database, 0, NULL, 0)) {
		fprintf(stderr, "%s\n", mysql_error(conn));
		exit(1);
	}

	while(1){
	    /* get data from orders table */
	    if (mysql_query(conn, "Select * from informatica.orders")) {
		    fprintf(stderr, "%s\n", mysql_error(conn));
		    exit(1);
	    }
   
	    res = mysql_use_result(conn);
	
	    /* output the data */
        int data[9];
        int i = 0;
        while ((row = mysql_fetch_row(res)) != NULL){
            data[i] = (int)strtol(row[1], (char **)NULL, 10);
            //printf("%d \n", data[i]);
            i++;
        }
        mysql_free_result(res);

        if (data[8] == 1){

            UA_Variant value;
            UA_Variant_init(&value);

            char browse_name[150];
            UA_Variant *myVariant = UA_Variant_new();
            for (int k=1; k<=8;k++){
                sprintf(browse_name, "|var|CODESYS Control Win V3 x64.Application.GVL.receive[%d]", k);
                UA_Variant_setScalarCopy(myVariant, &data[k-1], &UA_TYPES[UA_TYPES_INT16]);
                UA_Client_writeValueAttribute(client, UA_NODEID_STRING(4, browse_name), myVariant);
            }

            UA_Variant_delete(myVariant);

            while (true){
                sleep(5);
                UA_Int16 temp_val[8];
                int soma=0;
                for (int k=1; k<=8;k++){
                    sprintf(browse_name, "|var|CODESYS Control Win V3 x64.Application.GVL.receive[%d]", k);
                    retval = UA_Client_readValueAttribute(client, UA_NODEID_STRING(4, browse_name), &value);
                        if(retval == UA_STATUSCODE_GOOD && UA_Variant_hasScalarType(&value, &UA_TYPES[UA_TYPES_INT16])) {
                            temp_val[k-1] = *(UA_Int16 *) value.data;
                           // UA_LOG_INFO(UA_Log_Stdout, UA_LOGCATEGORY_USERLAND,"The state of transf_incremento is %d", temp_val[k-1]);
                        }
                        else {
                            printf("\nNao Leu nada! \n");
                        }
                        soma += temp_val[k-1];
                }
                if (soma == 0 ){
                    for (int k=1; k<=8;k++){
                    sprintf(browse_name, "|var|CODESYS Control Win V3 x64.Application.GVL.transf[%d]", k);
                    retval = UA_Client_readValueAttribute(client, UA_NODEID_STRING(4, browse_name), &value);
                        if(retval == UA_STATUSCODE_GOOD && UA_Variant_hasScalarType(&value, &UA_TYPES[UA_TYPES_INT16])) {
                            temp_val[k-1] = *(UA_Int16 *) value.data;
                            UA_LOG_INFO(UA_Log_Stdout, UA_LOGCATEGORY_USERLAND,"The state of tranf is %d", temp_val[k-1]);
                            sprintf(query, "UPDATE `informatica`.`orders` SET `quantity` = '%d' WHERE `piece`= '%d'",temp_val[k-1], columns[k]);
                            printf("%s",query);
                            if (mysql_query(conn, query)){
                                fprintf(stderr, "%s\n", mysql_error(conn));
                                exit(1);
                            }
                        }
                        else {
                            printf("\nNao Leu nada! \n");
                        }  
                    }
                    sprintf(query, "UPDATE `informatica`.`orders` SET `quantity` = '0' WHERE `piece`= '99'");
                    if (mysql_query(conn, query)){
                        fprintf(stderr, "%s\n", mysql_error(conn));
                        exit(1);
                    }
                    break;
                }
            }
  }
}
UA_Client_delete(client); /* Disconnects the client internally */
mysql_close(conn);
return EXIT_SUCCESS;
}

//gcc -o clt codesys.c `mysql_config --cflags --libs` -std=c99 open62541.c