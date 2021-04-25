import mysql.connector
from mysql.connector import errorcode


class DataBase:
    def __init__(self, filename):
        __db_config = []
        with open(filename, "r") as f:
            for line in f:
                a = line.split(":")
                __db_config.append(a[-1].rstrip("\n"))
            __config = {
                'host': __db_config[0],
                'user': __db_config[1],
                'password': __db_config[2],
                'database': __db_config[3],
                'raise_on_warnings': True
            }
            print(__db_config)
        try:
            self.mysqldb = mysql.connector.connect(**__config)
            if self.mysqldb.is_connected():
                db_info = self.mysqldb.get_server_info()
                print("Connected to MySQL Server version ", db_info)
                cursor = self.mysqldb.cursor()
                cursor.execute("Select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong wth username or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist!")
            else:
                print(err)

    def request_stores_db(self):
        __query = "SELECT * FROM stores;"
        cursor = self.mysqldb.cursor()
        cursor.execute(__query)
        __quantity_pieces = []
        for(Piece, quantity) in cursor:
            __quantity_pieces.append(quantity)
        cursor.close()
        return __quantity_pieces

    def request_orders_db(self):
        __query = "SELECT * FROM transform;"
        cursor = self.mysqldb.cursor()
        cursor.execute(__query)
        __orders = []
        __order = {}
        for row in cursor.fetchall():
            try:
                __order = {
                    'nnn': row[0],
                    'from': row[1],
                    'to': row[2],
                    'quantity': row[3],
                    'time': row[4],
                    'max_delay': row[5],
                    'penalty': row[6],
                    'quantity1': row[7],
                    'quantity2': row[8],
                    'quantity3': row[9],
                    'time1': row[10],
                    'start': row[11],
                    'end': row[12],
                    'penalty_incurred': row[13],
                    'estado': row[14]
                }
            except ValueError:
                print("error while fetching data")
                return 1
            finally:
                __orders.append(__order)
        return __orders

    def insert_order_db(self, table, data):
        __columns = []
        cursor = self.mysqldb.cursor()
        __query = ""
        try:
            for (name, value) in data.items():
                __columns.append(name)
        except ValueError:
            print('Error passing data dictionary')
            return 1
        try:
            __query = ("INSERT INTO `" + table + "` ( %s ) VALUES ( %s )")
            __query_columns = ""
            __query_values = ""
            for i in range(__columns.__len__()):
                if i == __columns.__len__()-1:
                    __query_columns += ('`' + __columns[i] + '`')
                    if __columns[i] in ('from', 'to', 'piece', 'type', 'destination'):
                        __query_values += ("'" + data[__columns[i]] + "'")
                    else:
                        __query_values += (str(data[__columns[i]]))
                else:
                    __query_columns += ('`' + __columns[i] + '`, ')
                    if __columns[i] in ('from', 'to', 'piece', 'type', 'destination'):
                        __query_values += ("'" + data[__columns[i]] + "', ")
                    else:
                        __query_values += (str(data[__columns[i]]) + ", ")
            __query = __query % (__query_columns, __query_values)
            print(__query)
            try:
                cursor.execute(__query)
                self.mysqldb.commit()
            except mysql.connector.Error as err:
                print("Something went wrong: {}".format(err))
                return 1
        except ValueError:
            print('Error passing table name')
            return 1
        finally:
            cursor.close()
            print('Order sucessfully inserted')
            return 0

    def update_order_db(self, table, data):
        __columns = []
        __cursor = self.mysqldb.cursor()
        __query = "UPDATE " + table + " SET "
        try:
            for (name, value) in data.items():
                __columns.append(name)
        except ValueError:
            print('Error while passing data')
            return 1
        if table == 'transform' or table == 'unload' or table == 'unload_plc':
            for i in range(__columns.__len__()):
                if __columns[i] != 'nnn' and __columns[i] != 'piece':
                    if __columns[i] in ('from', 'to', 'type', 'destination'):
                        __query += "`" + __columns[i] + "` = '" + data[__columns[i]] + "'"
                    else:
                        __query += "`" + __columns[i] + "` = " + str(data[__columns[i]])
                    if i < __columns.__len__()-1:
                        __query += ", "
            if __columns[0] == 'nnn':
                __query += " WHERE (`nnn` = " + str(data['nnn']) + ");"
            elif __columns[0] == 'piece':
                __query += " WHERE (`piece` = " + str(data['piece']) + ");"
            elif __columns[0] == 'destination':
                __query += " WHERE (`destination` = " + str(data['destination']) + ");"
            print(__query)
            __cursor.execute(__query)
            self.mysqldb.commit()
        return 0

    def read_unload_plc_state(self):
        __cursor = self.mysqldb.cursor()
        __query = 'Select `99` from `informatica`.`unload_plc`;'
        __state = []
        try:
            __cursor.execute(__query)
            for __row in __cursor.fetchall():
                __state.append(__row[0])
            __cursor.close()
            self.mysqldb.commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return 1
        return __state


    def clear_db_tables(self):
        __query = "DELETE FROM transform;"
        __cursor = self.mysqldb.cursor()
        __cursor.execute(__query)
        __query = "DELETE FROM unload;"
        __cursor.execute(__query)
        self.mysqldb.commit()
        __cursor.close()
        return 0


    def insert_incr(self, data):
        __columns = [12, 23, 34, 45, 56, 59, 67, 68, 99]
        __cursor = self.mysqldb.cursor()
        __pointer = 0
        data.append(1)
        for x in data:
            __query = "UPDATE `informatica`.`orders` SET `quantity` = '" + str(x) + "' WHERE (`piece` = '" + str(__columns[__pointer]) + "');"
            print(__query)
            try:
                __cursor.execute(__query)
                self.mysqldb.commit()
            except mysql.connector.Error as err:
                print("Something went wrong: {}".format(err))
                return 1
            __pointer += 1
        __cursor.close()
        print("A Espera que fique zero!  ")
        while True:
            __cursor = self.mysqldb.cursor()
            __query = "Select * from informatica.orders;"
            __cursor.execute(__query)
            __teste = []
            for __row in __cursor.fetchall():
                #print (__row[1])
                __teste.append(__row[1])
            if __teste[8] == 0:
                print("Ficou zero!!!!")
                self.mysqldb.commit()
                __cursor.close()
                break
            self.mysqldb.commit()
            __cursor.close()
        return [0]+__teste[:-1]

def main():
    db = DataBase("dbConfig.txt")
    #q = db.request_stores_db()
    info = {
        'nnn': 5,
        'from': 'P2',
        'to': 'P3',
        'quantity': 69,
        'time': 0,
        'max_delay': 6969,
        'penalty': 0,
        'quantity1': 0,
        'quantity2': 0,
        'quantity3': 0,
        'time1': 0,
        'start': 0,
        'end': 0,
        'penalty_incurred': 0,
        'estado': 0,
    }
    #print(info)
    info2 = {
        'nnn': 2,
        'type': 'P1',
        'destination': 'P3',
        'quantity': 5,
        'estado': 0,
        '99': 1,
    }
    #ret = db.insert_order_db('transform', info)
    information = {
        'piece': 'P12',
        'quantity': 90,
    }
    while(1):
        print(db.read_unload_plc_state())
    #dt = [5,0,0,0,0,0,0,0]
    #print(db.insert_incr(dt))
    #dt = [2,0,0,0,0,0,0,0]
    #print(db.insert_incr(dt))
    #db.insert_order_db('unload', info2)
    #orders = db.request_orders_db('transform')
    #db.update_order_db("transform", information)
    #db.clear_db_tables()

if __name__ == '__main__':
    main()
