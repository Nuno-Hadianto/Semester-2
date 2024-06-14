import mysql.connector

mydb = mysql.connector.connect(
    host="192.168.1.2",
    user="kelompok9",
    password="kelompok9",
    database = "pemkot" #ganti dengan nama database kalian
)

mycursor = mydb.cursor()

# read data
def read() :
    mycursor.execute("show tables;")
    myresult = mycursor.fetchall()
    print(myresult)


# # tambah data
# read()
# nama = input("Masukkan Nama : ")
# nim = input("Masukkan NIM : ")
# query = f"INSERT INTO mahasiswa VALUES ('','{nama}','{nim}')"
# mycursor.execute(query)         
# mydb.commit()
# read()

# # hapus data
# read()
# id = int(input("Masukkan id yang ingin di hapus : "))
# query = f"DELETE FROM mahasiswa WHERE id = {id}"
# mycursor.execute(query)
# mydb.commit()
# read()

# # update data
# read()
# id = int(input("Masukkan id yang ingin di update : "))
# nama = input("Masukkan Nama : ")
# nim = input("Masukkan NIM : ")
# query = f"UPDATE mahasiswa SET nama = '{nama}', nim = '{nim}' WHERE id = {id}"
# mycursor.execute(query)
# mydb.commit()
# read()