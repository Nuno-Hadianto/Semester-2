import mysql.connector

mydb = mysql.connector.connect(
    host = "192.168.1.2",
    user = "kelompok9",
    password = "kelompok9",
    database = "pemkot" # ganti dengan nama_staff database kalian
)

mycursor = mydb.cursor()

def read():
    query = "SELECT * FROM admin"
    mycursor.execute(query)
    result = mycursor.fetchall()
    for data in result:
        print(data)

read()
nama_staff = input("Masukkan nama_staff : ")
id_staff = input("Masukkan id_staff : ")
query = "INSERT INTO staff VALUES ('',%s,%s)"
val = (nama_staff,id_staff)
mycursor.execute(query,val)
mydb.commit()
read()
        
read()
id_staff = int(input("Masukkan id_staff yang ingin dihapus : "))
query = "DELETE FROM staff WHERE id_staff = %s"
val = [id_staff]
mycursor.execute(query,val)
mydb.commit()
read()
        
read()
id_staff = int(input("Masukkan id_staff yang ingin diubah : "))
nama_staff = input("Masukkan nama_staff : ")
id_staff = input("Masukkan id_staff : ")
query = "UPDATE staff SET nama_staff = %s, id_staff = %s WHERE id_staff = %s"
val = (nama_staff,id_staff,id_staff)
mycursor.execute(query,val)
mydb.commit()
read()