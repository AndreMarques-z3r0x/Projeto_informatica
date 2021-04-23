#include "open62541.h"
#include <mysql.h>
#include <stdlib.h>
#include <unistd.h>

MYSQL *conn;

const char *server = "192.168.1.86";
const char *user = "andre";
const char *password = "andre199921";
const char *database = "informatica";

UA_Client *client;
UA_StatusCode retval;


int* write_flag(int *arr){
    MYSQL_RES *res;
    MYSQL_ROW row;

    if(mysql_query(conn, "Select * from informatica.orders")){
        fprintf(stderr, "%s\n", mysql_error(conn));
        exit(1);
    }
    res = mysql_use_result(conn);
    int i = 0;
    while((row = mysql_fetch_row(res)) != NULL){
        arr[i] = (int)strtol(row[1],(char **)NULL,10);
        printf ("\nValor da base de dados:\n arr[%d] --> %d ", i, arr[i]);
        i++;
    }
    mysql_free_result(res);

    return arr;
}

int plc_write_values(const char *var_name, int first, int last, int param[]){

    UA_Variant value;
    UA_Variant_init(&value);
    char browse_name[150];
    int index = 0;
    int w_data[8];
    UA_Variant *myVariant = UA_Variant_new();
    printf("\n");

    for (int k=first; k<=last;k++){
        sprintf(browse_name, "|var|CODESYS Control Win V3 x64.Application.GVL.%s[%d]",var_name, k);
        w_data[index] = param[index];
        printf("\n browse_name: \r %s \n w_data[%d] --> %d \n",browse_name, index, w_data[index]);
        UA_Variant_setScalarCopy(myVariant, &param[index], &UA_TYPES[UA_TYPES_INT16]);
        UA_Client_writeValueAttribute(client, UA_NODEID_STRING(4, browse_name), myVariant);
        index++;
    }
    printf("\n");
    UA_Variant_delete(myVariant);
    return 0;
}

int* plc_read_values(const char *var_name, int first, int last, int *arr){
    
    UA_Variant value;
    UA_Variant_init(&value);
    UA_Int16 temp_val[8];
    char browse_name[150];
    int soma=0,index=0;

    printf("\n");

    for (int k=first; k<=last;k++){
        sprintf(browse_name, "|var|CODESYS Control Win V3 x64.Application.GVL.%s[%d]",var_name ,k);
        retval = UA_Client_readValueAttribute(client, UA_NODEID_STRING(4, browse_name), &value);
            if(retval == UA_STATUSCODE_GOOD && UA_Variant_hasScalarType(&value, &UA_TYPES[UA_TYPES_INT16])) {
                temp_val[index] = *(UA_Int16 *) value.data;
                arr[index] = temp_val[index];
                printf("temp_val[%d] --> %d \n",index, temp_val[index]);
                // UA_LOG_INFO(UA_Log_Stdout, UA_LOGCATEGORY_USERLAND,"The state of transf_incremento is %d", temp_val[k-1]);
            }else {
                printf("\n NAO LEU NADA! \n");
            }
            //soma += temp_val[index];
            //printf("\n SOMA = %d \n", soma);
            index++;
    } 
    return arr;
}

int check_all_zeros(int param[], int size){
    int sum=0;
    for(int n=0; n < size; n++){
        sum += param[n];
    }
    if(sum==0)
        return 1;
        else
            return 0;
}

int main(){

    /* OPCUA Connect */
    client = UA_Client_new();
    UA_ClientConfig_setDefault(UA_Client_getConfig(client));
    retval = UA_Client_connect(client, "opc.tcp://localhost:4840");
    if(retval != UA_STATUSCODE_GOOD) {
        UA_Client_delete(client);
        printf("\n NAO CONECTOU! TEMOS PENA!\n");
        return (int)retval;
        } else{
        printf("\n CONECTOU!!!!!!!!!!!!! \n");
    }

    conn = mysql_init(NULL);

    /* Connect to database */
    if (!mysql_real_connect(conn, server, user, password, database, 0, NULL, 0)) {
        fprintf(stderr, "%s\n", mysql_error(conn));
        exit(1);
    } else {
        printf("Conectado com base de dados MySQL");
    }
    
    int* data;
    int soma = 0;
    int arr[8];

    while(1){
        data = write_flag(arr);
        for (int n=0; n<8; n++){
            printf("data[%d] --> %d\n", n, data[n]);
        }
        if(data[8] == 1){
            printf("\n entrou no primeiro if(write_flag) \n data[2] --> %d", data[2]);
            plc_write_values("receive", 2, 9, data);
            while(1){
                printf("\n");
                int* r_values = plc_read_values("receive", 2, 9, arr);
                for (int n=0; n<8; n++){
                    printf("r_values[%d] --> %d\n", n, r_values[n]);
                }
                if(check_all_zeros(r_values, sizeof(arr)/sizeof(int))){
                    break;
                }
            }
            printf("\n ULTIMOS VALORES LIDOS EM TRANSF FORAM: \n");
            int* r_values = plc_read_values("transf", 2, 9, arr);
            for (int n=0; n<8; n++){
                printf("r_values[%d] --> %d\n", n, r_values[n]);
            }
            break;
        }
    }
    UA_Client_delete(client); /* Disconnects the client internally */
    mysql_close(conn);
    return EXIT_SUCCESS;
}