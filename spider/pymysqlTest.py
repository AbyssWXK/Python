import pymysql
db = pymysql.connect(host='47.101.62.125',user='root',password='Abyss,578',port=3306,db='spiders')
cursor = db.cursor()
id = '2012001'
user = 'Bob'
age = 20
sql = 'INSERT INTO students(id,name,age) values(%s,%s,%s)'
try:
    cursor.execute(sql,(id,user,age))
    db.commit()
except:
    db.rollback()
db.close()
