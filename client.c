#include "open62541.h"
#include <mysql.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

MYSQL *conn;

const char *server = "192.168.1.86";
const char *user = "andre";
const char *password = "andre199921";
const char *database = "informatica";

UA_Client *client;
UA_StatusCode retval;

pthread_mutex_t mtx_mysql;


int opcua_connect_to_server(){
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
    return 0;
}

int database_start_connection(){
    conn = mysql_init(NULL);
    /* Connect to database */
    if (!mysql_real_connect(conn, server, user, password, database, 0, NULL, 0)) {
        fprintf(stderr, "%s\n", mysql_error(conn));
        exit(1);
    } else {
        printf("Conectado com base de dados MySQL");
    }
    return 0;
}

int write_unload_values(int param[]){

}

int* write_flag(int *arr, int act){          //act=0 --> orders           act=1 --> unloads
    MYSQL_RES *res;
    MYSQL_ROW row;

    switch (act)
    {
    case 0:
        pthread_mutex_lock(&mtx_mysql);
        if(mysql_query(conn, "Select * from informatica.orders")){
            fprintf(stderr, "%s\n", mysql_error(conn));
            exit(1);
        }
        pthread_mutex_unlock(&mtx_mysql);
        res = mysql_use_result(conn);
        int i = 0;
        while((row = mysql_fetch_row(res)) != NULL){
            arr[i] = (int)strtol(row[1],(char **)NULL,10);
            printf ("\nValor da base de dados:\n arr[%d] --> %d ", i, arr[i]);
            i++;
        }
        mysql_free_result(res);
        break;
    
    case 1:
        pthread_mutex_lock(&mtx_mysql);
        if(mysql_query(conn, "Select * from informatica.unload_plc")){
            fprintf(stderr, "%s\n", mysql_error(conn));
            exit(1);
        }
        pthread_mutex_unlock(&mtx_mysql);
        res = mysql_use_result(conn);
        int i = 0;
        while((row = mysql_fetch_row(res)) != NULL){
            int flag_state = (int)strtol(row[3],(char **)NULL,10);
            printf ("\nValor da flag na base de dados:\n flag_state --> %d ", flag_state);
            if (flag_state)
            {
                int aux[4];
                for(int n=0; n<4; n++){
                    aux[n] = (int)strtol(row[n],(char **)NULL,10);
                    printf("Valores da ordem unload na db: \n aux[%d] --> %d \n", n , aux[n]);
                }
                write_unload_values(aux);
            }
            
            i++;
        }
        mysql_free_result(res);
        break;

    default:
        printf("404: Action not recognized!");
        break;
    }
    /*pthread_mutex_lock(&mtx_mysql);
    if(mysql_query(conn, "Select * from informatica.orders")){
        fprintf(stderr, "%s\n", mysql_error(conn));
        exit(1);
    }
    pthread_mutex_unlock(&mtx_mysql);
    res = mysql_use_result(conn);
    int i = 0;
    while((row = mysql_fetch_row(res)) != NULL){
        arr[i] = (int)strtol(row[1],(char **)NULL,10);
        printf ("\nValor da base de dados:\n arr[%d] --> %d ", i, arr[i]);
        i++;
    }
    mysql_free_result(res); */

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

int send_values_to_db(int table_id, int param[],int size, int flag_value){
    switch (table_id)
    {
    case 4:
        for(int i=0; i<size;i++){
            int column[] = {12, 23, 34,45,56,59,67,68};
            char query[150];
            sprintf(query,"UPDATE `informatica`.`orders` SET"
                        "`quantity` = '%d' WHERE `piece`='%d'",param[i],column[i]);
            pthread_mutex_lock(&mtx_mysql);
            if(mysql_query(conn, query)){
                fprintf(stderr,"%s\n",mysql_error(conn));
                exit(1);
            }
            sprintf(query, "UPDATE `informatica`.`orders` SET" 
                        "`quantity` = '%d' WHERE `piece`= '99'",flag_value);
            if (mysql_query(conn, query)){
                fprintf(stderr, "%s\n", mysql_error(conn));
                exit(1);
            }
            pthread_mutex_unlock(&mtx_mysql);
        }
        break;
    
    default:
        printf("table '%d' not found", table_id);
        break;
    }
}

int start_orders(){
    int* data;
    int soma = 0;
    int arr[8];

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
            send_values_to_db(4, r_values,sizeof(arr)/sizeof(int),0);
            return 1;
        }
    return 0;
}

void* orders_thread(){
    while(1){
        start_orders();
    } 
}

void* unloads_thread(){
    while(1){
        start_unloads();
    }
}

int main(){
    opcua_connect_to_server();
    database_start_connection();
    
    pthread_t th1, th2;  //th1 --> orders thread ;;;  th2 --> unload thread ;;;
    if(pthread_mutex_init(&mtx_mysql, NULL)!=0){
        printf("ERROR CREATING MUTEX!");
        exit(1);
    }

    pthread_create(&th1, NULL, orders_thread, NULL);
    pthread_create(&th2, NULL, unloads_thread, NULL);

    pthread_join(th1,NULL);
    pthread_join(th2,NULL);

    UA_Client_delete(client); /* Disconnects the client internally */
    mysql_close(conn);
    return EXIT_SUCCESS;
}