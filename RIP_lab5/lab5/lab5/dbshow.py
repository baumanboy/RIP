import pymysql
pymysql.install_as_MySQLdb()


db = pymysql.connect (
     host="localhost",
     user="dbuser",
     passwd="123",
     db="first_db"
)

# курсор
c = db.cursor()

c.execute('SELECT * FROM products;')
entries = c.fetchall()
for e in entries:
    print(e)
c.close()
db.close()