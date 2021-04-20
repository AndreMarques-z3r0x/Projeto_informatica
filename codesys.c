#include "open62541.h"
#include <mysql.h>
#include <stdlib.h>

int main(void) {

    MYSQL *conn;
	MYSQL_RES *res;
	MYSQL_ROW row;
	
	char *server = "192.168.1.86";
	char *user = "andre";
	char *password = "andre199921";
	char *database = "informatica";
	
	conn = mysql_init(NULL);
	
	/* Connect to database */
	if (!mysql_real_connect(conn, server, user, password, 
                                      database, 0, NULL, 0)) {
		fprintf(stderr, "%s\n", mysql_error(conn));
		exit(1);
	}
	
	/* get data from orders table */
	if (mysql_query(conn, "Select * from informatica.orders")) {
		fprintf(stderr, "%s\n", mysql_error(conn));
		exit(1);
	}
   
	res = mysql_use_result(conn);
	
	/* output the data */
    int data[8];
    int i = 0;
	while ((row = mysql_fetch_row(res)) != NULL){
		data[i] = (int)strtol(row[1], (char **)NULL, 10);
        printf("%d \n", data[i]);
        i++;
    }
	mysql_free_result(res);

    int x= 0; 
    if (x==1){
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

    /* Read the value attribute of the node. UA_Client_readValueAttribute is a
     * wrapper for the raw read service available as UA_Client_Service_read. */
    UA_Variant value; /* Variants can hold scalar values and arrays of any type */
    UA_Variant_init(&value);

    /* NodeId of the variable holding the current time */
    const UA_NodeId nodeId = UA_NODEID_NUMERIC(0, UA_NS0ID_SERVER_SERVERSTATUS_CURRENTTIME);
    retval = UA_Client_readValueAttribute(client, nodeId, &value);

    if(retval == UA_STATUSCODE_GOOD &&
       UA_Variant_hasScalarType(&value, &UA_TYPES[UA_TYPES_DATETIME])) {
        UA_DateTime raw_date = *(UA_DateTime *) value.data;
        UA_DateTimeStruct dts = UA_DateTime_toStruct(raw_date);
        UA_LOG_INFO(UA_Log_Stdout, UA_LOGCATEGORY_USERLAND, "date is: %u-%u-%u %u:%u:%u.%03u\n",
                    dts.day, dts.month, dts.year, dts.hour, dts.min, dts.sec, dts.milliSec);
    }

    // Variables for read access
    UA_Boolean RD22;

    retval = UA_Client_readValueAttribute(client, UA_NODEID_STRING(4, "|var|CODESYS Control Win V3 x64.PLC_PRG.RD22"), &value);
    if(retval == UA_STATUSCODE_GOOD &&
       UA_Variant_hasScalarType(&value, &UA_TYPES[UA_TYPES_BOOLEAN])) {
        RD22 = *(UA_Boolean *) value.data;
        UA_LOG_INFO(UA_Log_Stdout, UA_LOGCATEGORY_USERLAND,"The state of RD22 is %d", RD22);
    }
    else {
        printf("\nNao Leu nada! \n");
    }
    /* Clean up */

    UA_Boolean rdx = UA_TRUE;
    /* Write node attribute (using the highlevel API) */
    UA_Variant *myVariant = UA_Variant_new();
    UA_Variant_setScalarCopy(myVariant, &rdx, &UA_TYPES[UA_TYPES_BOOLEAN]);
    UA_Client_writeValueAttribute(client, UA_NODEID_STRING(4, "|var|CODESYS Control Win V3 x64.PLC_PRG.RD22"), myVariant);
    UA_Variant_delete(myVariant);

    UA_Client_delete(client); /* Disconnects the client internally */
    return EXIT_SUCCESS;
    }
    
    mysql_close(conn);
    return 0;

}