import mysql.connector as m


mc = m.connect(host='127.0.0.1', user='root', password='amaatra', database='hapsprice')
cur = mc.cursor()
cur.execute("create table data(row int(3), col int(3), ownername varchar(20), contactno int(10), forsale int(2))")
mc.commit()

cur.execute("insert into data values()")
