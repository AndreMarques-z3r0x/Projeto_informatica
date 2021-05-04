#include <unistd.h>
#include <stdio.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <string.h>
#include "open62541.h"
#include <mysql.h>
#include <pthread.h>

#define N_THREADS 100
#define PORT 4455
int server_fd;
struct sockaddr_in address;
int opt = 1;

MYSQL *conn;

const char *server = "192.168.1.86";
const char *user = "andre";
const char *password = "andre199921";
const char *database = "informatica";

UA_Client *client;
UA_StatusCode retval;

pthread_mutex_t mtx_mysql, mtx_opcua;


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
        printf("Conectado com base de dados MySQL\n");
    }
    return 0;
}

int write_unload_values(int param[]){

}

int* write_flag(int *arr){ 

    pthread_mutex_lock(&mtx_mysql);
    database_start_connection();

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
        //printf ("\nValor da base de dados:\n arr[%d] --> %d ", i, arr[i]);
        i++;
    }
    mysql_free_result(res);
    mysql_close(conn);
    pthread_mutex_unlock(&mtx_mysql);

    return arr;
}

int plc_write_values(const char *var_name, int first, int last, int param[]){

    pthread_mutex_lock(&mtx_opcua);
    opcua_connect_to_server();

    UA_Variant value;
    UA_Variant_init(&value);
    char browse_name[150];
    int index = 0;
    int w_data[10];
    UA_Variant *myVariant = UA_Variant_new();
    //printf("\n");

    for (int k=first; k<=last;k++){
        sprintf(browse_name, "|var|CODESYS Control Win V3 x64.Application.GVL.%s[%d]",var_name, k);
        w_data[index] = param[index];
        printf("\n browse_name: %s \n w_data[%d] --> %d \n",browse_name, index, w_data[index]);
        UA_Variant_setScalarCopy(myVariant, &param[index], &UA_TYPES[UA_TYPES_INT16]);
        UA_Client_writeValueAttribute(client, UA_NODEID_STRING(4, browse_name), myVariant);
        index++;
    }
    //printf("\n");
    UA_Variant_delete(myVariant);

    UA_Client_delete(client);
    pthread_mutex_unlock(&mtx_opcua);

    return 0;
}

int* plc_read_values(const char *var_name, int first, int last, int *arr){
    
    pthread_mutex_lock(&mtx_opcua);
    opcua_connect_to_server();

    UA_Variant value;
    UA_Variant_init(&value);
    UA_Int16 temp_val[8];
    char browse_name[150];
    int soma=0,index=0;

    //printf("\n");

    for (int k=first; k<=last;k++){
        sprintf(browse_name, "|var|CODESYS Control Win V3 x64.Application.GVL.%s[%d]",var_name ,k);
        retval = UA_Client_readValueAttribute(client, UA_NODEID_STRING(4, browse_name), &value);
            if(retval == UA_STATUSCODE_GOOD && UA_Variant_hasScalarType(&value, &UA_TYPES[UA_TYPES_INT16])) {
                temp_val[index] = *(UA_Int16 *) value.data;
                arr[index] = temp_val[index];
                //printf("temp_val[%d] --> %d \n",index, temp_val[index]);
                // UA_LOG_INFO(UA_Log_Stdout, UA_LOGCATEGORY_USERLAND,"The state of transf_incremento is %d", temp_val[k-1]);
            }else {
                printf("\n NAO LEU NADA! \n");
            }
            //soma += temp_val[index];
            //printf("\n SOMA = %d \n", soma);
            index++;
    }
    UA_Client_delete(client);
    pthread_mutex_unlock(&mtx_opcua);
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
        for(int i=0; i<8;i++){
            int column[] = {12, 23, 34,45,56,59,67,68};
            char query[150];
            sprintf(query,"UPDATE `informatica`.`orders` SET"
                        "`quantity` = '%d' WHERE `piece`='%d'",param[i],column[i]);
            //printf("%s",query);
            pthread_mutex_lock(&mtx_mysql);
            database_start_connection();
            if(mysql_query(conn, query)){
                fprintf(stderr,"%s\n",mysql_error(conn));
                exit(1);
            }
            // sprintf(query, "UPDATE `informatica`.`orders` SET" 
            //             "`quantity` = '%d' WHERE `piece`= '99'",flag_value);
            // printf("%s",query);
            // if (mysql_query(conn, query)){
            //     fprintf(stderr, "%s\n", mysql_error(conn));
            //     exit(1);
            // }
            mysql_close(conn);
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
    int arr[9];

    data = write_flag(arr);
    // for (int n=0; n<9; n++){
    //     printf("data[%d] --> %d\n", n, data[n]);
    // }
    //printf("\n entrou no primeiro if(write_flag) \n data[2] --> %d", data[2]);
    plc_write_values("receive", 2, 9, data);
    while(1){
        printf("\n");
        int* r_values = plc_read_values("receive", 2, 9, arr);
        // for (int n=0; n<8; n++){
        //     //printf("r_values[%d] --> %d\n", n, r_values[n]);
        // }
        if(check_all_zeros(r_values, 8)){
            break;
        }
    }
    //printf("\n ULTIMOS VALORES LIDOS EM TRANSF FORAM: \n");
    int* r_values = plc_read_values("transf", 2, 9, arr);
    for (int n=0; n<8; n++){
        printf("r_values[%d] --> %d", n, r_values[n]);
    }
    send_values_to_db(4, r_values,sizeof(arr)/sizeof(int),0);
    char query[150];
    sprintf(query, "UPDATE `informatica`.`orders` SET" 
                        "`quantity` = '%d' WHERE `piece`= '99'",0);
    printf("%s",query);
    pthread_mutex_lock(&mtx_mysql);
    database_start_connection();
    if (mysql_query(conn, query)){
        fprintf(stderr, "%s\n", mysql_error(conn));
        exit(1);
    }
    mysql_close(conn);
    pthread_mutex_unlock(&mtx_mysql);

    return 0;
}

void* orders_thread(){
    printf("\n Inicio da thread de orders!\n");
    //database_start_connection();
    //opcua_connect_to_server();
    start_orders();
    //mysql_close(conn);
    //UA_Client_delete(client);
}

int* start_unloads(int zone, int *arr){
    MYSQL_RES *res;
    MYSQL_ROW row;
    char query[150];
    sprintf(query,"Select * from informatica.unload_plc WHERE"
                " destination = '%d';",zone);
    //printf("\n %s \n",query);
    pthread_mutex_lock(&mtx_mysql);
    database_start_connection();
    if(mysql_query(conn, query)){
        fprintf(stderr, "%s\n", mysql_error(conn));
        printf("\n invalid querry!!!\n");
        exit(1);
    }
    res = mysql_use_result(conn);
    if((row = mysql_fetch_row(res)) != NULL){
        for(int i=0; i<4; i++){
            arr[i] = (int)strtol(row[i],(char **)NULL,10);
            printf ("\nValor da base de dados: arr[%d] --> %d \n", i, arr[i]);
        }
    }
    mysql_free_result(res);
    
    mysql_close(conn);
    pthread_mutex_unlock(&mtx_mysql);

    return arr;
}

void* unloads_thread(void *param){
    int zone = *((int *) param);
    free(param);
    //printf("[+]Created new unload thread !\n");
    //printf("[+]thread param received --> %d\n", zone);
    int aux[4];
    //database_start_connection();
    start_unloads(zone, aux);
    int dados_sos[] ={0,0,0,0,0,0,0,0,0,1}; 
    dados_sos[aux[2]-1] = aux[1];
    for (int k=0;k<9;k++)
        printf("\n dados_sos[%d] --> %d\n", k, dados_sos[k]);
    //opcua_connect_to_server();
    if (zone==1){
        plc_write_values("unload_zone_1",1,10,dados_sos);
    }else if (zone==2){
        plc_write_values("unload_zone_2",1,10,dados_sos);
    }else if(zone==3){
        plc_write_values("unload_zone_3",1,10,dados_sos);
    }
    while (1)
    {
        char var_name[150];
        int arr[10];
        sprintf(var_name,"unload_zone_%d",zone);
        int *r_values = plc_read_values(var_name,1,10,arr);
        for(int l=0; l<10; l++)
            printf("r_values[%d] --> %d\n", l, r_values[l]);
        
        if (r_values[9]==0){
            char query[150];
            pthread_mutex_lock(&mtx_mysql);
            database_start_connection();
            sprintf(query, "UPDATE `informatica`.`unload_plc` SET" 
                            "`99` = '%d' WHERE `destination`= '%d'",r_values[9],zone);
            if (mysql_query(conn, query)){
                fprintf(stderr, "%s\n", mysql_error(conn));
                exit(1);
            }
            mysql_close(conn);
            pthread_mutex_unlock(&mtx_mysql);
            break;
        }
    }
       
    //mysql_close(conn);
    //UA_Client_delete(client);
    return NULL;
}

int create_socket(){
    // Creating socket file descriptor
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0)
    {
        perror("socket failed");
        exit(EXIT_FAILURE);
    }
       
    // Forcefully attaching socket to the port 8080
    if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR,
                                                  &opt, sizeof(opt)))
    {
        perror("setsockopt");
        exit(EXIT_FAILURE);
    }
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons( PORT );
       
    // Forcefully attaching socket to the port 8080
    if (bind(server_fd, (struct sockaddr *)&address, 
                                 sizeof(address))<0)
    {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }
    if (listen(server_fd, 100) < 0)
    {
        perror("listen");
        exit(EXIT_FAILURE);
    }
}

int start_stocks_thread(){
    int arr[9];
    while(1){
        int* r_values = plc_read_values("stock", 1,9,arr);
        char query[150];
        int column[] = {1,2,3,4,5,6,7,8,9};
        for(int k= 0; k<9;k++){
            sprintf(query, "UPDATE `informatica`.`stores` SET "
                            "`quantity` = '%d' WHERE `piece`='P%d'",r_values[k],column[k]);
            pthread_mutex_lock(&mtx_mysql);
            database_start_connection();
            if(mysql_query(conn,query)){
                fprintf(stderr, "%s\n", mysql_error(conn));
                exit(1);
            }
            mysql_close(conn);
            pthread_mutex_unlock(&mtx_mysql);
        }
    sleep(1);
    }
}

void* stocks_thread(){
    start_stocks_thread();
}

int main(int argc, char const *argv[])
{   
    //opcua_connect_to_server();
    //database_start_connection();

    int new_socket, valread;
    int addrlen = sizeof(address);
    char buffer[1024] = {0};
    char *hello = "Hello from server";

    pid_t childpid;
    pthread_t th1[N_THREADS],th2[N_THREADS], th_stocks;

    if(pthread_mutex_init(&mtx_mysql, NULL)!=0){
        printf("ERROR CREATING MUTEX!");
        exit(1);
    }
    if(pthread_mutex_init(&mtx_opcua, NULL)!=0){
        printf("ERROR CREATING MUTEX!");
        exit(1);
    }

    pthread_create(&th_stocks, NULL, stocks_thread, NULL);

    create_socket();
   // printf("[+]new socket created\n");

    int i = 0;
    int o_thread=0;

    while(1){
    
        new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t*)&addrlen);
        if (new_socket<0){
            exit(1);
        }
        //printf("[+]connection accepcted!");
        valread = read( new_socket , buffer, 1024);
        //printf("[+]Data received --> %s\n",buffer);
        send(new_socket , hello , strlen(hello) , 0 );
        char *command;
        int zone = (int)strtol(buffer,&command,10);
        if(strcmp(command,"NewUnload") ==0){
            int *arg = malloc(sizeof(*arg));
            *arg = zone;
            pthread_create(&th1[i], NULL, unloads_thread, arg);
            i++;
        }else if(strcmp(command,"NewOrder") ==0){
            printf("\n[+]new thread for NewOrder command!\n");
            start_orders();
            //pthread_create(&th2,NULL,orders_thread,NULL);
            //pthread_join(th2,NULL);
            // o_thread ++;
        }
        memset(buffer, 0, sizeof buffer);
    
    }
    
    for (int k= 0; k<i;k++){
        pthread_join(th1[k], NULL);
    }
    pthread_join(th_stocks,NULL);
    // for (int k= 0; k<o_thread;k++){
    //     pthread_join(th2[k], NULL);
    // }
    printf("\nCODIGO CHEGOU AO FIM!! MERDA!!\n");
    UA_Client_delete(client); /* Disconnects the client internally */
    //mysql_close(conn);
    return EXIT_SUCCESS;
}

//int *arg = malloc(sizeof(*arg));
            //if (arg == NULL){
              //  printf("\n COULDN'T ALLOCATE MEMORY FOR THREAD ARG \n");
                //exit(EXIT_FAILURE);
            //}
            //*arg = zone;
            //pthread_create(&th2, NULL, unloads_thread, arg);
            //printf("main after create thread!");

//pthread_t th1, th2;  //th1 --> orders thread ;;;  th2 --> unload thread ;;;
    /*if(pthread_mutex_init(&mtx_mysql, NULL)!=0){
        printf("ERROR CREATING MUTEX!");
        exit(1);
    } */

/* 
valread = read( new_socket , buffer, 1024);
        char *command;
        int zone = (int)strtol(buffer,&command,10);
        //printf("buffer --> %s\n", buffer);
        printf("[+]Data received: %d  --> %s\n",zone, command);
        //printf("qualquer coisa nice:  %s\n",command);
        if(strcmp(command,"NewUnload") ==0){
            printf("[+]Create new unload thread !\n");
            start_unloads(zone);
        }
        memset(buffer, 0, sizeof buffer);
        //send(new_socket , hello , strlen(hello) , 0 );
*/

// if((childpid = fork()) == 0){
//             printf("[+]connection accepcted!");
//             printf("my pid is --> %u\n",getpid());
//             valread = read( new_socket , buffer, 1024);
//             printf("[+]Data received --> %s\n",buffer);
//             memset(buffer, 0, sizeof buffer);
//             send(new_socket , hello , strlen(hello) , 0 );
//             int aux[4];
//             database_start_connection();
//             start_unloads(1,aux);
//             mysql_close(conn);
//             for(int k=0;k<4;k++)
//                 printf("\n aux[%d] --> %d\n", k, aux[k]);
//             opcua_connect_to_server();
//             int dados_sos[]= {0,0,0,0,0,0,0,0,0};
//             dados_sos[aux[0]-1]=aux[1];
//             plc_write_values("unload_zone_1",1,9,dados_sos);
//             UA_Client_delete(client);
            
//         }