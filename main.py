import mysql.connector
from mysql.connector import errorcode
#luca gay

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

    def request_orders_db(self, table):
        __query = "SELECT * FROM %s;"
        cursor = self.mysqldb.cursor()
        cursor.execute(__query % table)
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
                }
            except ValueError:
                print("error while fetching data")
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
                    if __columns[i] == 'from' or __columns[i] == 'to' or __columns[i] == 'piece':
                        __query_values += ("'" + data[__columns[i]] + "'")
                    else:
                        __query_values += (str(data[__columns[i]]))
                else:
                    __query_columns += ('`' + __columns[i] + '`, ')
                    if __columns[i] == 'from' or __columns[i] == 'to' or __columns[i] == 'piece':
                        __query_values += ("'" + data[__columns[i]] + "', ")
                    else:
                        __query_values += (str(data[__columns[i]]) + ", ")
            __query = __query % (__query_columns, __query_values)
            try:
                cursor.execute(__query)
                self.mysqldb.commit()
            except mysql.connector.Error as err:
                print("Something went wrong: {}".format(err))
            finally:
                print("Order was successfully inserted on table")
                return 1
        except ValueError:
            print('Error passing table name')
            return 1
        finally:
            cursor.close()
            return 0

    def update_order_db(self, table, data):
        __columns = []
        #cursor = self.mysqldb.cursor()
        __query = "UPDATE " + table + " SET "
        try:
            for (name, value) in data.items():
                __columns.append(name)
        except ValueError:
            print('Error while passing data')
            return 1
        if table == 'transform' or table == 'unload':
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
            print(__query)


def main():
    db = DataBase("dbConfig.txt")
    q = db.request_stores_db()
    info = {
        'nnn': 8,
        'from': 'P2',
        'to': 'P3',
        'quantity': 69,
        'time': 0,
        'max_delay': 6969,
        'penalty': 0,
        'quantity1': 0,
        'quantity2': 0,
        'quantity3': 0,
    }
    #ret = db.insert_order_db('transform', info)
    information = {
        'piece': 'P12',
        'quantity': 86,
    }
    #db.insert_order_db('stores', information)
    #orders = db.request_orders_db('transform')
    db.update_order_db("transform", info)

if __name__ == '__main__':
    main()
