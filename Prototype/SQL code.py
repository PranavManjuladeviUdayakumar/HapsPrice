if input("Retrieve house information from MySQL? (y/n): ").lower() == 'y':
    mc = m.connect(host= '127.0.0.1', user= 'root', password= 'amaatra', database= 'hapsprice')
    cur = mc.cursor()
    cur.execute(f"select * from data where row = {row} and col = {col}")
    data = cur.fetchall()
    for i in data:
        print(i)
