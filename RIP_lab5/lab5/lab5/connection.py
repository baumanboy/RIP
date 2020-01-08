""""import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='dbuser',
                             password='123',
                             db='first_db',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        # Вставка записи
        sql_request = "INSERT INTO products (name, description) VALUES (%s, %s)"
        cursor.execute(sql_request, ('Computer', 'Electronic desktop device for working with files and programming'))

        # Зафиксировать изменения
        connection.commit()
        with connection.cursor() as cursor:
            # Выполним выборку
            sql_request = "SELECT * FROM products"
            cursor.execute(sql_request)
            result = cursor.fetchall()

        print(result)
finally:
    connection.close()

"""""

import pymysql

pymysql.install_as_MySQLdb()


class Connection:

    def __init__(self, user, password, db, host='localhost'):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.charset = "utf8"
        self._connection = None

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        if not self._connection:
            self._connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                db=self.db,
                charset=self.charset
            )

    def disconnect(self):
        if self._connection:
            self._connection.close()


class Product:
    def __init__(self, db_connection, name, description):
        self.db_connection = db_connection.connection
        self.name = name
        self.description = description

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO products (name, description) VALUES (%s, %s);", (self.name, self.description))

        self.db_connection.commit()
        c.close()


connection = Connection('dbuser', '123', 'first_db', 'localhost')
with connection:
    product = Product(connection, 'Computer', 'Electronic desktop device for working with files and programming')
    product.save()

