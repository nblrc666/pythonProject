from pyhive import hive

conn = hive.Connection(host="192.168.137.10", port=10000, username="root", database="default")
cursor = conn.cursor()
cursor.execute("select * from business ")
for i in cursor.fetchall():
    print(i)