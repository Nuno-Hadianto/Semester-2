import mysql.connector
import pwinput
import os
from prettytable import PrettyTable

RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
CYAN = "\033[96m"

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pemkot"
)
mycursor = mydb.cursor() 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display_admin(self): 
        os.system("cls")
        print('\n' * 1000)
        current = self.head
        x = PrettyTable()
        x.field_names = ["id_orang", "username", "password", "email"]
        while current:
            x.add_row(current.data)
            current = current.next
        print(x)
    
    def display_samarinda(self):
        os.system("cls")
        print('\n' * 1000)
        current = self.head
        x = PrettyTable()
        x.field_names = ["id_samarinda", "kecamatan", "kelurahan", "kode_pos"]
        while current:
            x.add_row(current.data)
            current = current.next
        print(x)
    
    def display_pemerintah(self):
        os.system("cls")
        print('\n' * 1000)
        current = self.head
        x = PrettyTable()
        x.field_names = ["id_pemerintah", "pejabat", "jabatan", "partai"]
        while current:
            x.add_row(current.data)
            current = current.next
        print(x)

    def display_program(self):
        os.system("cls")
        print('\n' * 1000)
        current = self.head
        x = PrettyTable()
        x.field_names = ["id_program", "nama_program", "bidang_program", "status_program"]
        while current:
            x.add_row(current.data)
            current = current.next
        print(x)

def quick_sort(arr, ascending=True):
    
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2][0]
    left = [x for x in arr if x[0] < pivot]
    middle = [x for x in arr if x[0] == pivot]
    right = [x for x in arr if x[0] > pivot]
    if ascending:
        return quick_sort(left, ascending) + middle + quick_sort(right, ascending)
    else:
        return quick_sort(right, ascending) + middle + quick_sort(left, ascending)

def jump_search(arr, x):
    n = len(arr)
    step = int(n ** 0.5)
    prev = 0
    while arr[min(step, n)-1][0] < x:
        prev = step
        step += int(n ** 0.5)
        if prev >= n:
            return -1
    while arr[prev][0] < x:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[prev][0] == x:
        return prev
    return -1

while True:
    try:
        print(BOLD + GREEN + "")
        def read_admin():
            mycursor.execute("SELECT * FROM admin")
            myresult = mycursor.fetchall()
            ll = LinkedList()
            for data in myresult:
                ll.append(data)
            ll.display_admin()

        def read_samarinda1():
            mycursor.execute("SELECT * FROM samarinda")
            myresult = mycursor.fetchall()
            ll = LinkedList()
            for data in myresult:
                ll.append(data)
            ll.display_samarinda()

        def read_pemerintah1():
            mycursor.execute("SELECT * FROM pemerintah")
            myresult = mycursor.fetchall()
            ll = LinkedList()
            for data in myresult:
                ll.append(data)
            ll.display_pemerintah()

        def read_program1():
            mycursor.execute("SELECT * FROM program")
            myresult = mycursor.fetchall()
            ll = LinkedList()
            for data in myresult:
                ll.append(data)
            ll.display_program()

        def tambah_data_admin():
            try:
                read_admin()
                id_orang = int(input("MASUKKAN ID BARU ORANG : ").strip())
                username = input("MASUKKAN USERNAME ADMIN : ").strip()
                while any(char in '|/?+=_-)(*&^$#!' for char in username):
                    print("cannot contain special characters like |/?+=_-)(*&^$#!")
                    username = input("MASUKKAN USERNAME ADMIN : ").strip()
                password = input("MASUKKANT PASSWORD ADMIN : ").strip()
                while any(char in '|/?+=_-)(*&^$#!' for char in password):
                    print("cannot contain special characters like |/?+=_-)(*&^$#!")
                    password = input("MASUKKANT PASSWORD ADMIN : ").strip()
                email = input("MASUKKAN EMAIL ADMIN : ").strip()
                while any(char in '|/?+=_-)(*&^$#!' for char in email):
                    print("cannot contain special characters like |/?+=_-)(*&^$#!")
                    email = input("MASUKKAN EMAIL ADMIN : ").strip()
                query = f"""
                INSERT INTO admin (id_orang, username, password, email)
                VALUES ({id_orang}, '{username}', '{password}', '{email}')
                """

                mycursor.execute(query)
                mydb.commit()
                print("+-------------------------------+")
                print("|DATA ADMIN BERHASIL DITAMBAHKAN|")
                print("+-------------------------------+")
            except KeyboardInterrupt:
                print("\n+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except ValueError:
                print("+-----------+")
                print("|SALAH INPUT|")
                print("+-----------+")
            except EOFError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except mysql.connector.IntegrityError:
                print("+------------+")
                print("|ID SUDAH ADA|")
                print("+------------+")
            except mysql.connector.errors.ProgrammingError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except UnboundLocalError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except AttributeError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except TypeError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")

        def hapus_data_admin():
            try:
                read_admin()
                id_orang = int(input("MASUKKAN ID ORANG YANG INGIN DIHAPUS : ").strip())

                query = f"DELETE FROM admin WHERE id_orang = {id_orang}"

                mycursor.execute(query)
                mydb.commit()
                
                if mycursor.rowcount > 0:  
                    print("+---------------------------+")
                    print("|DATA ADMIN BERHASIL DIHAPUS|")
                    print("+---------------------------+")
                else:
                    print("+------------------+")
                    print("|ID TIDAK DITEMUKAN|")
                    print("+------------------+")
            except KeyboardInterrupt:
                print("\n+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except EOFError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except ValueError:
                print("+-----------+")
                print("|SALAH INPUT|")
                print("+-----------+")
            except mysql.connector.errors.ProgrammingError:
                print("+------------+")
                print("|ID SUDAH ADA|")
                print("+------------+")
            except mysql.connector.errors.IntegrityError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except UnboundLocalError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except AttributeError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except TypeError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")

        def perbarui_data_admin():
            try:
                read_admin()
                id_orang = int(input("MASUKKAN ID ADMIN YANG INGIN DIPERBARUI : ").strip())
                username = input("MASUKKAN USERNAME ADMIN BARU : ").strip()
                while any(char in '|/?+=_-)(*&^$#!' for char in username):
                    print("cannot contain special characters like |/?+=_-)(*&^$#!")
                    username = input("MASUKKAN USERNAME ADMIN BARU : ").strip()
                password = input("MASUKKAN PASSWORD ADMIN BARU : ").strip()
                while any(char in '|/?+=_-)(*&^$#!' for char in password):
                    print("cannot contain special characters like |/?+=_-)(*&^$#!")
                    password = input("MASUKKAN PASSWORD ADMIN BARU : ").strip()
                email = input("MASUKKAN EMAIL ADMIN BARU : ").strip()
                while any(char in '|/?+=_-)(*&^$#!' for char in email):
                    print("cannot contain special characters like |/?+=_-)(*&^$#!")
                    email = input("MASUKKAN EMAIL ADMIN BARU : ").strip()

                query = f"""
                UPDATE admin
                SET username = '{username}',
                password = '{password}',
                email = '{email}'
                WHERE id_orang = {id_orang}
                """

                mycursor.execute(query)
                if mycursor.rowcount > 0:
                    mydb.commit()
                    print("+----------------------------+")
                    print("|DATABASE BERHASIL DIPERBARUI|")
                    print("+----------------------------+")
                else:
                    print("+------------------------+")
                    print("|ID ADMIN TIDAK DITEMUKAN|")
                    print("+------------------------+")
            except EOFError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except ValueError:
                print("+-----------+")
                print("|SALAH INPUT|")
                print("+-----------+")
            except KeyboardInterrupt:
                print("\n+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except mysql.connector.IntegrityError:
                print("+------------+")
                print("|ID SUDAH ADA|")
                print("+------------+")
            except mysql.connector.errors.ProgrammingError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except UnboundLocalError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except AttributeError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except TypeError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")


        def read_samarinda():
            mycursor.execute("SELECT * FROM samarinda")
            myresult = mycursor.fetchall()
            data_list = []
            for data in myresult:
                data_list.append(data)

            while True:
                try:
                    print("------------------------------------------------------------")
                    print("|                  TAMPILKAN DATA SAMARINDA                |")
                    print("------------------------------------------------------------")
                    print("|   [1]. URUTKAN DATA BERDASARKAN ID - ASCENDING           |")
                    print("|   [2]. URUTKAN DATA BERDASARKAN ID - DESCENDING          |")
                    print("|   [3]. CARI DATA BERDASARKAN NAMA                        |")
                    print("|   [4]. CARI DATA BERDASARKAN ID                          |")
                    print("|   [5]. KEMBALI KE MENU DATABASE SAMARINDA                |")
                    print("------------------------------------------------------------")
                    
                    pilihan = input("MASUKKAN PILIHAN ANDA : ")

                    if pilihan == "1":
                        os.system("cls")
                        sorted_data = quick_sort(data_list, ascending=True)
                        ll = LinkedList()
                        for data in sorted_data:
                            ll.append(data)
                        ll.display_samarinda()
                    elif pilihan == "2":
                        os.system("cls")
                        sorted_data = quick_sort(data_list, ascending=False)
                        ll = LinkedList()
                        for data in sorted_data:
                            ll.append(data)
                        ll.display_samarinda()
                    elif pilihan == "3":
                        nama = input("MASUKKAN NAMA KECAMATAN YANG DICARI: ")
                        mycursor.execute(f"SELECT * FROM samarinda WHERE kecamatan LIKE '%{nama}%'")
                        myresult = mycursor.fetchall()
                        if myresult:
                            ll = LinkedList()
                            for data in myresult:
                                ll.append(data)
                            ll.display_samarinda()
                        else:
                            print("+-----------------------------------------------+")
                            print("|TIDAK ADA DATA YANG COCOK DENGAN PENCARIAN ANDA|")
                            print("+-----------------------------------------------+")
                    elif pilihan == "4":
                        id_to_search = int(input("MASUKKAN ID YANG INGIN DICARI : "))
                        result_index = jump_search(data_list, id_to_search)
                        if result_index != -1:
                            print("+--------------+")
                            print("|DATA DITEMUKAN|")
                            print("+--------------+")
                            x = PrettyTable()
                            x.field_names = ["id_samarinda", "kecamatan", "kelurahan", "kode_pos"]
                            x.add_row(data_list[result_index])
                            print(x)
                        else:
                            print("+--------------------+")
                            print("|DATA TIDAK DITEMUKAN|")
                            print("+--------------------+")
                    elif pilihan == "5":
                        os.system("cls")
                        break
                    else:
                        print("+-------------------+")
                        print("|PILIHAN TIDAK VALID|")
                        print("+-------------------+")
                except KeyboardInterrupt:
                    print("\n+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except ValueError:
                    print("+-----------+")
                    print("|SALAH INPUT|")
                    print("+-----------+")
                except EOFError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except mysql.connector.IntegrityError:
                    print("+------------+")
                    print("|ID SUDAH ADA|")
                    print("+------------+")
                except mysql.connector.errors.ProgrammingError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except UnboundLocalError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except AttributeError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except TypeError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                    
        def tambah_data_samarinda():
            try:
                read_samarinda1()
                id_samarinda = int(input("MASUKKAN ID BARU SAMARINDA : ").strip())
                kecamatan = input("MASUKKAN NAMA KECAMATAN : ").strip()
                while any(char in '|/?+=_-)(*&^$#!' for char in kecamatan):
                    print("cannot contain special characters like |/?+=_-)(*&^$#!")
                    kecamatan = input("MASUKKAN NAMA KECAMATAN : ").strip()
                kelurahan = input("MASUKKAN NAMA KELURAHAN : ").strip()
                while any(char in '|/?+=_-)(*&^$#!' for char in kelurahan):
                    print("cannot contain special characters like |/?+=_-)(*&^$#!")
                    kelurahan = input("MASUKKAN NAMA KELURAHAN : ").strip()
                kode_pos = int(input("MASUKKAN KODE POS : ").strip())
                query = f"""
                INSERT INTO samarinda (id_samarinda, kecamatan, kelurahan, kode_pos)
                VALUES ({id_samarinda}, '{kecamatan}', '{kelurahan}', {kode_pos})
                """

                mycursor.execute(query)
                mydb.commit()
                print("+-------------------------+")
                print("|DATA BERHASIL DITAMBAHKAN|")
                print("+-------------------------+")
            except KeyboardInterrupt:
                print("\n+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except ValueError:
                print("+-----------+")
                print("|SALAH INPUT|")
                print("+-----------+")
            except EOFError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except mysql.connector.IntegrityError:
                print("+------------+")
                print("|ID SUDAH ADA|")
                print("+------------+")
            except mysql.connector.errors.ProgrammingError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except UnboundLocalError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except AttributeError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except TypeError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")

        def hapus_data_samarinda():
            try:
                mycursor.execute("SELECT * FROM samarinda")
                myresult = mycursor.fetchall()
                x = PrettyTable()
                x.field_names = ["id_samarinda", "kecamatan", "kelurahan", "kode_pos"]
                for data in myresult:
                    x.add_row(data)
                print(x)

                id_samarinda = int(input("MASUKKAN ID SAMARINDA YANG INGIN DIHAPUS : ").strip())

                query = f"DELETE FROM samarinda WHERE id_samarinda = {id_samarinda}"

                mycursor.execute(query)
                mydb.commit()
                
                if mycursor.rowcount > 0:  
                    print("+-------------------------------+")
                    print("|DATA SAMARINDA BERHASIL DIHAPUS|")
                    print("+-------------------------------+")
                else:
                    print("+------------------+")
                    print("|ID TIDAK DITEMUKAN|")
                    print("+------------------+")
            except EOFError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except KeyboardInterrupt:
                print("\n+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except ValueError:
                print("+-----------+")
                print("|SALAH INPUT|")
                print("+-----------+")
            except mysql.connector.IntegrityError:
                print("+------------+")
                print("|ID SUDAH ADA|")
                print("+------------+")
            except mysql.connector.errors.ProgrammingError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except UnboundLocalError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except AttributeError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except TypeError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")

        def perbarui_data_samarinda():
            try:
                mycursor.execute("SELECT * FROM samarinda")
                myresult = mycursor.fetchall()
                x = PrettyTable()
                x.field_names = ["id_samarinda", "kecamatan", "kelurahan", "kode_pos"]
                for data in myresult:
                    x.add_row(data)
                print(x)

                id_samarinda = int(input("MASUKKAN ID SAMARINDA YANG INGIN DIPERBARUI : ").strip())
                kecamatan = input("MASUKKAN NAMA KECAMATAN BARU : ").strip()
                while any(char in '|/?+=_-)(*&^$#!' for char in kecamatan):
                    print("cannot contain special characters like |/?+=_-)(*&^$#!")
                    kecamatan = input("MASUKKAN NAMA KECAMATAN BARU : ").strip()
                kelurahan = input("MASUKKAN NAMA KELURAHAN BARU : ").strip()
                while any(char in '|/?+=_-)(*&^$#!' for char in kelurahan):
                    print("cannot contain special characters like |/?+=_-)(*&^$#!")
                    kelurahan = input("MASUKKAN NAMA KELURAHAN BARU : ").strip()
                kode_pos = int(input("MASUKKAN KODE POS BARU : ").strip())

                query = f"""
                UPDATE samarinda
                SET kecamatan = '{kecamatan}',
                kelurahan = '{kelurahan}',
                kode_pos = {kode_pos}
                WHERE id_samarinda = {id_samarinda}
                """

                mycursor.execute(query)
                if mycursor.rowcount > 0:
                    mydb.commit()
                    print("+----------------------------+")
                    print("|DATABASE BERHASIL DIPERBARUI|")
                    print("+----------------------------+")
                else:
                    print("+----------------------------+")
                    print("|ID SAMARINDA TIDAK DITEMUKAN|")
                    print("+----------------------------+")
            except KeyboardInterrupt:
                print("\n+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except EOFError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except ValueError:
                print("+-----------+")
                print("|SALAH INPUT|")
                print("+-----------+")
            except mysql.connector.IntegrityError:
                print("+------------+")
                print("|ID SUDAH ADA|")
                print("+------------+")
            except mysql.connector.errors.ProgrammingError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except UnboundLocalError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except AttributeError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except TypeError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")

        def read_pemerintah():
            mycursor.execute("SELECT * FROM pemerintah")
            myresult = mycursor.fetchall()
            data_list = []
            for data in myresult:
                data_list.append(data)

            while True:
                try:
                    print("------------------------------------------------------------")
                    print("|                  TAMPILKAN DATA PEMERINTAH               |")
                    print("------------------------------------------------------------")
                    print("|   [1]. URUTKAN DATA BERDASARKAN ID - ASCENDING           |")
                    print("|   [2]. URUTKAN DATA BERDASARKAN ID - DESCENDING          |")
                    print("|   [3]. CARI DATA BERDASARKAN NAMA                        |")
                    print("|   [4]. CARI DATA BERDASARKAN ID                          |")
                    print("|   [5]. KEMBALI KE MENU DATABASE PEMERINTAH               |")
                    print("------------------------------------------------------------")

                    pilihan = input("MASUKKAN PILIHAN ANDA : ")

                    if pilihan == "1":
                        os.system("cls")
                        sorted_data = quick_sort(data_list, ascending=True)
                        ll = LinkedList()
                        for data in sorted_data:
                            ll.append(data)
                        ll.display_pemerintah()
                    elif pilihan == "2":
                        os.system("cls")
                        sorted_data = quick_sort(data_list, ascending=False)
                        ll = LinkedList()
                        for data in sorted_data:
                            ll.append(data)
                        ll.display_pemerintah()
                    elif pilihan == "3":
                        nama = input("MASUKKAN NAMA PEJABAT YANG DICARI : ")
                        mycursor.execute(f"SELECT * FROM pemerintah WHERE nama_pejabat LIKE '%{nama}%'")
                        myresult = mycursor.fetchall()
                        if myresult:
                            ll = LinkedList()
                            for data in myresult:
                                ll.append(data)
                            ll.display_pemerintah()
                        else:
                            print("+-----------------------------------------------+")
                            print("|TIDAK ADA DATA YANG COCOK DENGAN PENCARIAN ANDA|")
                            print("+-----------------------------------------------+")
                    elif pilihan == "4":
                        id_to_search = int(input("MASUKKAN ID YANG INGIN DICARI : "))
                        result_index = jump_search(data_list, id_to_search)
                        if result_index != -1:
                            print("+--------------+")
                            print("|DATA DITEMUKAN|")
                            print("+--------------+")
                            x = PrettyTable()
                            x.field_names = ["id_pemerintah", "nama_pejabat", "jabatan", "partai"]
                            x.add_row(data_list[result_index])
                            print(x)
                        else:
                            print("+--------------------+")
                            print("|DATA TIDAK DITEMUKAN|")
                            print("+--------------------+")
                    elif pilihan == "5":
                        os.system("cls")
                        break
                    else:
                        print("+-------------------+")
                        print("|PILIHAN TIDAK VALID|")
                        print("+-------------------+")
                except KeyboardInterrupt:
                    print("\n+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except EOFError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except ValueError:
                    print("+-----------+")
                    print("|SALAH INPUT|")
                    print("+-----------+")
                except mysql.connector.IntegrityError:
                    print("+------------+")
                    print("|ID SUDAH ADA|")
                    print("+------------+")
                except mysql.connector.errors.ProgrammingError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except UnboundLocalError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except AttributeError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except TypeError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")

        def tambah_data_pemerintah():
            try:
                read_pemerintah1()
                id_pemerintah = int(input("MASUKKAN ID BARU PEMERINTAH : ").strip())
                nama_pejabat = input("MASUKKAN NAMA PEJABAT BARU : ").strip()
                while any(char in '|/?+=_-)(*&^$#!' for char in nama_pejabat):
                    print("cannot contain special characters like |/?+=_-)(*&^$#!")
                    nama_pejabat = input("MASUKKAN NAMA PEMERINTAH BARU : ").strip()
                jabatan = input("MASUKKAN JABATAN BARU : ").strip()
                while any(char in '|/?+=_-)(*&^$#!' for char in jabatan):
                    print("cannot contain special characters like |/?+=_-)(*&^$#!")
                    jabatan = input("MASUKKAN JABATAN BARU : ").strip()
                partai = input("MASUKKAN PARTAI BARU : ").strip()
                while any(char in '|/?+=_-)(*&^$#!' for char in partai):
                    print("cannot contain special characters like |/?+=_-)(*&^$#!")
                    partai = input("MASUKKAN PARTAI BARU : ").strip()

                query = f"""
                INSERT INTO pemerintah (id_pemerintah, nama_pejabat, jabatan, partai)
                VALUES ({id_pemerintah}, '{nama_pejabat}', '{jabatan}', '{partai}')
                """

                mycursor.execute(query)
                mydb.commit()
                print("+----------------------------------+")
                print("|DATA DATABASE BERHASIL DITAMBAHKAN|")
                print("+----------------------------------+")
            except EOFError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except ValueError:
                print("+-----------+")
                print("|SALAH INPUT|")
                print("+-----------+")
            except KeyboardInterrupt:
                print("\n+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except mysql.connector.IntegrityError:
                print("+------------+")
                print("|ID SUDAH ADA|")
                print("+------------+")
            except mysql.connector.errors.ProgrammingError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except UnboundLocalError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except AttributeError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except TypeError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")

        def hapus_data_pemerintah():
            try:
                mycursor.execute("SELECT * FROM pemerintah")
                myresult = mycursor.fetchall()
                x = PrettyTable()
                x.field_names = ["id_pemerintah", "nama_pejabat", "jabatan", "partai"]
                for data in myresult:
                    x.add_row(data)
                print(x)

                id_pemerintah = int(input("MASUKKAN ID PEMERINTAH YANG INGIN DIHAPUS : ").strip())

                query = f"DELETE FROM pemerintah WHERE id_pemerintah = {id_pemerintah}"

                mycursor.execute(query)
                mydb.commit()
                
                if mycursor.rowcount > 0:  
                    print("+--------------------------------+")
                    print("|DATA PEMERINTAH BERHASIL DIHAPUS|")
                    print("+--------------------------------+")
                else:
                    print("+------------------+")
                    print("|ID TIDAK DITEMUKAN|")
                    print("+------------------+")
            except EOFError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except ValueError:
                print("+-----------+")
                print("|SALAH INPUT|")
                print("+-----------+")
            except KeyboardInterrupt:
                print("\n+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except mysql.connector.IntegrityError:
                print("+------------+")
                print("|ID SUDAH ADA|")
                print("+------------+")
            except mysql.connector.errors.ProgrammingError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except UnboundLocalError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except AttributeError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except TypeError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")

        def perbarui_data_pemerintah():
            try:
                mycursor.execute("SELECT * FROM pemerintah")
                myresult = mycursor.fetchall()
                x = PrettyTable()
                x.field_names = ["id_pemerintah", "nama_pejabat", "jabatan", "partai"]
                for data in myresult:
                    x.add_row(data)
                print(x)

                id_pemerintah = int(input("MASUKKAN ID PEMERINTAH YANG INGIN DIPERBARUI : ").strip())
                nama_pejabat = input("MASUKKAN NAMA PEJABAT BARU : ").strip()
                while any(char in '|/?+=_-)(*&^$#!' for char in nama_pejabat):
                    print("cannot contain special characters like |/?+=_-)(*&^$#!")
                    nama_pejabat = input("MASUKKAN NAMA PEJABAT BARU : ").strip()
                jabatan = input("MASUKKAN JABATAN BARU : ").strip()
                while any(char in '|/?+=_-)(*&^$#!' for char in jabatan):
                    print("cannot contain special characters like |/?+=_-)(*&^$#!")
                    jabatan = input("MASUKKAN JABATAN BARU : ").strip()
                partai = input("MASUKKAN PARTAI BARU : ").strip()
                while any(char in '|/?+=_-)(*&^$#!' for char in partai):
                    print("cannot contain special characters like |/?+=_-)(*&^$#!")
                    partai = input("MASUKKAN PARTAI BARU : ").strip()

                query = f"""
                UPDATE pemerintah
                SET nama_pejabat = '{nama_pejabat}',
                jabatan = '{jabatan}',
                partai = '{partai}',
                WHERE id_pemerintah = {id_pemerintah}
                """

                mycursor.execute(query)
                if mycursor.rowcount > 0:
                    mydb.commit()
                    print("+----------------------------+")
                    print("|DATABASE BERHASIL DIPERBARUI|")
                    print("+----------------------------+")
                else:
                    print("+-----------------------------+")
                    print("|ID PEMERINTAH TIDAK DITEMUKAN|")
                    print("+-----------------------------+")
            except EOFError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except ValueError:
                print("+-----------+")
                print("|SALAH INPUT|")
                print("+-----------+")
            except KeyboardInterrupt:
                print("\n+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except mysql.connector.IntegrityError:
                print("+------------+")
                print("|ID SUDAH ADA|")
                print("+------------+")
            except mysql.connector.errors.ProgrammingError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except UnboundLocalError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except AttributeError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except TypeError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")

        def read_program():
            mycursor.execute("SELECT * FROM program")
            myresult = mycursor.fetchall()
            data_list = []
            for data in myresult:
                data_list.append(data)

            while True:
                try:
                    print("------------------------------------------------------------")
                    print("|                  TAMPILKAN DATA PROGRAM                  |")
                    print("------------------------------------------------------------")
                    print("|   [1]. URUTKAN DATA BERDASARKAN ID - ASCENDING           |")
                    print("|   [2]. URUTKAN DATA BERDASARKAN ID - DESCENDING          |")
                    print("|   [3]. CARI DATA BERDASARKAN NAMA                        |")
                    print("|   [4]. CARI DATA BERDASARKAN ID                          |")
                    print("|   [5]. KEMBALI KE MENU DATABASE PROGRAM                  |")
                    print("------------------------------------------------------------")
                    pilihan = input("MASUKKAN PILIHAN ANDA : ")

                    if pilihan == "1":
                        os.system("cls")
                        sorted_data = quick_sort(data_list, ascending=True)
                        ll = LinkedList()
                        for data in sorted_data:
                            ll.append(data)
                        ll.display_program()
                    elif pilihan == "2":
                        os.system("cls")
                        sorted_data = quick_sort(data_list, ascending=False)
                        ll = LinkedList()
                        for data in sorted_data:
                            ll.append(data)
                        ll.display_program()
                    elif pilihan == "3":
                        nama = input("MASUKKAN NAMA PROGRAM YANG DICARI : ")
                        mycursor.execute(f"SELECT * FROM program WHERE nama_program LIKE '%{nama}%'")
                        myresult = mycursor.fetchall()
                        if myresult:
                            ll = LinkedList()
                            for data in myresult:
                                ll.append(data)
                            ll.display_program()
                        else:
                            print("+-----------------------------------------------+")
                            print("|TIDAK ADA DATA YANG COCOK DENGAN PENCARIAN ANDA|")
                            print("+-----------------------------------------------+")
                    elif pilihan == "4":
                        id_to_search = int(input("MASUKKAN ID YANG DICARI : "))
                        result_index = jump_search(data_list, id_to_search)
                        if result_index != -1:
                            print("+-----------------------+")
                            print("|DATA DATABASE DITEMUKAN|")
                            print("+-----------------------+")
                            x = PrettyTable()
                            x.field_names = ["id_program", "nama_program", "bidang_program", "status_program"]
                            x.add_row(data_list[result_index])
                            print(x)
                        else:
                            print("+-----------------------------+")
                            print("|DATA DATABASE TIDAK DITEMUKAN|")
                            print("+-----------------------------+")
                    elif pilihan == "5":
                        os.system("cls")
                        break
                    else:
                        print("+-------------------+")
                        print("|PILIHAN TIDAK VALID|")
                        print("+-------------------+")
                except EOFError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except ValueError:
                    print("+-----------+")
                    print("|SALAH INPUT|")
                    print("+-----------+")
                except KeyboardInterrupt:
                    print("\n+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except mysql.connector.IntegrityError:
                    print("+------------+")
                    print("|ID SUDAH ADA|")
                    print("+------------+")
                except mysql.connector.errors.ProgrammingError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except UnboundLocalError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except AttributeError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except TypeError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")

        def tambah_data_program():
            try:
                read_program1()
                id_program = int(input("MASUKKAN ID BARU PROGRAM : ").strip())
                nama_program = input("MASUKKAN NAMA PROYEK : ").strip()
                while any(char in '|/?+=_-)(*&^$#!' for char in nama_program):
                    print("cannot contain special characters like |/?+=_-)(*&^$#!")
                    nama_program = input("MASUKKAN NAMA PROYEK : ").strip()
                bidang_program = input("MASUKKAN BIDANG PROGRAM : ").strip()
                while any(char in '|/?+=_-)(*&^$#!' for char in bidang_program):
                    print("cannot contain special characters like |/?+=_-)(*&^$#!")
                    bidang_program = input("MASUKKAN BIDANG PROGRAM : ").strip()
                status_program = input("MASUKKAN STATUS PROGRAM : ").strip()
                while any(char in '|/?+=_-)(*&^$#!' for char in status_program):
                    print("cannot contain special characters like |/?+=_-)(*&^$#!")
                    status_program = input("MASUKKAN STATUS PROGRAM : ").strip()
                query = f"""
                INSERT INTO program (id_program, nama_program, bidang_program, status_program)
                VALUES ({id_program}, '{nama_program}', '{bidang_program}', '{status_program}')
                """

                mycursor.execute(query)
                mydb.commit()
                print("+---------------------------------------------+")
                print("|DATA PROGRAM BERHASIL DITAMBAHKAN KE DATABASE|")
                print("+---------------------------------------------+") 
            except EOFError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except ValueError:
                print("+-----------+")
                print("|SALAH INPUT|")
                print("+-----------+")
            except KeyboardInterrupt:
                print("\n+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except mysql.connector.IntegrityError:
                print("+------------+")
                print("|ID SUDAH ADA|")
                print("+------------+")
            except mysql.connector.errors.ProgrammingError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except UnboundLocalError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except AttributeError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except TypeError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")

        def hapus_data_program():
            try:
                mycursor.execute("SELECT * FROM program")
                myresult = mycursor.fetchall()
                x = PrettyTable()
                x.field_names = ["id_program", "nama_program", "bidang_program", "status_program"]
                for data in myresult:
                    x.add_row(data)
                print(x)

                id_program = int(input("MASUKKAN ID PROGRAM YANG INGIN DIHAPUS : ").strip())

                query = f"DELETE FROM program WHERE id_program = {id_program}"

                mycursor.execute(query)
                mydb.commit()
                
                if mycursor.rowcount > 0:  
                    print("+-----------------------------+")
                    print("|DATA PROGRAM BERHASIL DIHAPUS|")
                    print("+-----------------------------+")
                else:
                    print("+------------------+")
                    print("|ID TIDAK DITEMUKAN|")
                    print("+------------------+")
            except EOFError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except ValueError:
                print("+-----------+")
                print("|SALAH INPUT|")
                print("+-----------+")
            except KeyboardInterrupt:
                print("\n+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except mysql.connector.IntegrityError:
                print("+------------+")
                print("|ID SUDAH ADA|")
                print("+------------+")
            except mysql.connector.errors.ProgrammingError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except UnboundLocalError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except AttributeError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except TypeError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")

        def perbarui_data_program():
            try:
                mycursor.execute("SELECT * FROM program")
                myresult = mycursor.fetchall()
                x = PrettyTable()
                x.field_names = ["id_program", "nama_program", "bidang_program", "status_program"]
                for data in myresult:
                    x.add_row(data)
                print(x)

                id_program = int(input("MASUKKAN ID PROGRAM YANG INGIN DIPERBARUI : ").strip())
                nama_program = input("MASUKKAN NAMA PROGRAM BARU : ").strip()
                while any(char in '|/?+=_-)(*&^$#!' for char in nama_program):
                    print("cannot contain special characters like |/?+=_-)(*&^$#!")
                    nama_program = input("MASUKKAN NAMA PROGRAM BARU : ").strip()
                bidang_program = input("MASUKKAN BIDANG PROGRAM BARU : ").strip()
                while any(char in '|/?+=_-)(*&^$#!' for char in bidang_program):
                    print("cannot contain special characters like |/?+=_-)(*&^$#!")
                    bidang_program = input("MASUKKAN BIDANG PROGRAM BARU : ").strip()
                status_program = input("MASUKKAN STATUS PROGRAM BARU : ").strip()
                while any(char in '|/?+=_-)(*&^$#!' for char in status_program):
                    print("cannot contain special characters like |/?+=_-)(*&^$#!")
                    status_program = input("MASUKKAN STATUS PROGRAM BARU : ").strip()

                query = f"""
                UPDATE program
                SET nama_program = '{nama_program}',
                bidang_program = '{bidang_program}',
                status_program = '{status_program}'
                WHERE id_program = {id_program}
                """

                mycursor.execute(query)
                if mycursor.rowcount > 0:
                    mydb.commit()
                    print("+----------------------------+")
                    print("|DATABASE BERHASIL DIPERBARUI|")
                    print("+----------------------------+")
                else:
                    print("+--------------------------+")
                    print("|ID PROGRAM TIDAK DITEMUKAN|")
                    print("+--------------------------+")
            except EOFError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except ValueError:
                print("+-----------+")
                print("|SALAH INPUT|")
                print("+-----------+")
            except KeyboardInterrupt:
                print("\n+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except mysql.connector.IntegrityError:
                print("+------------+")
                print("|ID SUDAH ADA|")
                print("+------------+")
            except mysql.connector.errors.ProgrammingError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except UnboundLocalError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except AttributeError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except TypeError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")

        def menu_utama_admin():
            while True:
                try:
                    print("------------------------------------------------------------")
                    print("|                   DATABASE ADMIN                         |")
                    print("------------------------------------------------------------")
                    print("|                [1]. TAMBAH DATA ADMIN                    |")
                    print("|                [2]. HAPUS DATA ADMIN                     |")
                    print("|                [3]. PERBARUI DATA ADMIN                  |")
                    print("|                [4]. TAMPILKAN DATA ADMIN                 |")
                    print("|                [5]. KELUAR DARI DATABASE ADMIN           |")
                    print("------------------------------------------------------------")
                    pilihan = input("MASUKKAN PILIHAN ANDA : ")

                    if pilihan == "1":
                        os.system("cls")
                        tambah_data_admin()
                    elif pilihan == "2":
                        os.system("cls")
                        hapus_data_admin()
                    elif pilihan == "3":
                        os.system("cls")
                        perbarui_data_admin()
                    elif pilihan == "4":
                        os.system("cls")
                        read_admin()
                    elif pilihan == "5":
                        os.system("cls")
                        print("+---------------+")
                        print("|BERHASIL KELUAR|")
                        print("+---------------+")
                        break
                    else:
                        print("+-------------------+")
                        print("|PILIHAN TIDAK VALID|")
                        print("+-------------------+")
                except EOFError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except ValueError:
                    print("+-----------+")
                    print("|SALAH INPUT|")
                    print("+-----------+")
                except KeyboardInterrupt:
                    print("\n+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except mysql.connector.IntegrityError:
                    print("+------------+")
                    print("|ID SUDAH ADA|")
                    print("+------------+")
                except mysql.connector.errors.ProgrammingError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except UnboundLocalError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except AttributeError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except TypeError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")

        def menu_utama_samarinda():
            while True:
                try:
                    print("------------------------------------------------------------")
                    print("|                   DATABASE SAMARINDA                     |")
                    print("------------------------------------------------------------")
                    print("|                [1]. TAMBAH DATA SAMARINDA                |")
                    print("|                [2]. HAPUS DATA SAMARINDA                 |")
                    print("|                [3]. PERBARUI DATA SAMARINDA              |")
                    print("|                [4]. TAMPILKAN DATA SAMARINDA             |")
                    print("|                [5]. KELUAR DARI DATABASE SAMARINDA       |")
                    print("------------------------------------------------------------")
                    pilihan = input("MASUKKAN PILIHAN ANDA : ")

                    if pilihan == "1":
                        os.system("cls")
                        tambah_data_samarinda()
                    elif pilihan == "2":
                        os.system("cls")
                        hapus_data_samarinda()
                    elif pilihan == "3":
                        os.system("cls")
                        perbarui_data_samarinda()
                    elif pilihan == "4":
                        os.system("cls")
                        read_samarinda()
                    elif pilihan == "5":
                        os.system("cls")
                        print("+---------------+")
                        print("|BERHASIL KELUAR|")
                        print("+---------------+")
                        break
                    else:
                        print("+-------------------+")
                        print("|PILIHAN TIDAK VALID|")
                        print("+-------------------+")
                except EOFError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except ValueError:
                    print("+-----------+")
                    print("|SALAH INPUT|")
                    print("+-----------+")
                except KeyboardInterrupt:
                    print("\n+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except mysql.connector.IntegrityError:
                    print("+------------+")
                    print("|ID SUDAH ADA|")
                    print("+------------+")
                except mysql.connector.errors.ProgrammingError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except UnboundLocalError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except AttributeError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except TypeError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")

        def menu_utama_pemerintah():
            while True:
                try:
                    print("------------------------------------------------------------")
                    print("|                   DATABASE PEMERINTAH                    |")
                    print("------------------------------------------------------------")
                    print("|                [1]. TAMBAH DATA PEMERINTAH               |")
                    print("|                [2]. HAPUS DATA PEMERINTAH                |")
                    print("|                [3]. PERBARUI DATA PEMERINTAH             |")
                    print("|                [4]. TAMPILKAN DATA PEMERINTAH            |")
                    print("|                [5]. KELUAR DARI DATABASE PEMERINTAH      |")
                    print("------------------------------------------------------------")
                    pilihan = input("MASUKKAN PILIHAN ANDA : ")

                    if pilihan == "1":
                        os.system("cls")
                        tambah_data_pemerintah()
                    elif pilihan == "2":
                        os.system("cls")
                        hapus_data_pemerintah()
                    elif pilihan == "3":
                        os.system("cls")
                        perbarui_data_pemerintah()
                    elif pilihan == "4":
                        os.system("cls")
                        read_pemerintah()
                    elif pilihan == "5":
                        os.system("cls")
                        print("+---------------+")
                        print("|BERHASIL KELUAR|")
                        print("+---------------+")
                        break
                    else:
                        print("+-------------------+")
                        print("|PILIHAN TIDAK VALID|")
                        print("+-------------------+")
                except EOFError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except ValueError:
                    print("+-----------+")
                    print("|SALAH INPUT|")
                    print("+-----------+")
                except KeyboardInterrupt:
                    print("\n+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except mysql.connector.IntegrityError:
                    print("+------------+")
                    print("|ID SUDAH ADA|")
                    print("+------------+")
                except mysql.connector.errors.ProgrammingError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except UnboundLocalError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except AttributeError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except TypeError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")

        def menu_utama_program():
            while True:
                try:
                    print("------------------------------------------------------------")
                    print("|                   DATABASE PROGRAM                       |")
                    print("------------------------------------------------------------")
                    print("|                [1]. TAMBAH DATA PROGRAM                  |")
                    print("|                [2]. HAPUS DATA PROGRAM                   |")
                    print("|                [3]. PERBARUI DATA PROGRAM                |")
                    print("|                [4]. TAMPILKAN DATA PROGRAM               |")
                    print("|                [5]. KELUAR DARI DATABASE PROGRAM         |")
                    print("------------------------------------------------------------")
                    pilihan = input("MASUKKAN PILIHAN ANDA : ")

                    if pilihan == "1":
                        os.system("cls")
                        tambah_data_program()
                    elif pilihan == "2":
                        os.system("cls")
                        hapus_data_program()
                    elif pilihan == "3":
                        os.system("cls")
                        perbarui_data_program()
                    elif pilihan == "4":
                        os.system("cls")
                        read_program()
                    elif pilihan == "5":
                        os.system("cls")
                        print("+---------------+")
                        print("|BERHASIL KELUAR|")
                        print("+---------------+")
                        print
                        break
                    else:
                        print("+-------------------+")
                        print("|PILIHAN TIDAK VALID|")
                        print("+-------------------+")
                except EOFError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except ValueError:
                    print("+-----------+")
                    print("|SALAH INPUT|")
                    print("+-----------+")
                except KeyboardInterrupt:
                    print("\n+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except mysql.connector.IntegrityError:
                    print("+------------+")
                    print("|ID SUDAH ADA|")
                    print("+------------+")
                except mysql.connector.errors.ProgrammingError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except UnboundLocalError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except AttributeError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except TypeError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
            

        def menu_utama_superuser():
            while True:
                try:
                    print("------------------------------------------------------------")
                    print("|           USERNAME :",username, "BERHASIL MASUK                 |")
                    print("------------------------------------------------------------")
                    print("|                [1]. DATABASE ADMIN                       |")
                    print("|                [2]. DATABASE SAMARINDA                   |")
                    print("|                [3]. DATABASE PEMERINTAH                  |")
                    print("|                [4]. DATABASE PROGRAM                     |")
                    print("|                [5]. KELUAR DARI DATABASE PEMKOT          |")
                    print("------------------------------------------------------------")
                    pilihan = input("MASUKKAN PILIHAN ANDA : ")

                    if pilihan == "1":
                        os.system("cls")
                        menu_utama_admin()
                    elif pilihan == "2":
                        os.system("cls")
                        menu_utama_samarinda()
                    elif pilihan == "3":
                        os.system("cls")
                        menu_utama_pemerintah()
                    elif pilihan == "4":
                        os.system("cls")
                        menu_utama_program()
                    elif pilihan == "5":
                        os.system("cls")
                        print("+-----------------+")
                        print("|BERHASIL KELUAR !|")
                        print("+-----------------+")
                        break
                    else:
                        print("+-------------------+")
                        print("|PILIHAN TIDAK VALID|")
                        print("+-------------------+")
                except EOFError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except ValueError:
                    print("+-----------+")
                    print("|SALAH INPUT|")
                    print("+-----------+")
                except KeyboardInterrupt:
                    print("\n+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except mysql.connector.IntegrityError:
                    print("+------------+")
                    print("|ID SUDAH ADA|")
                    print("+------------+")
                except mysql.connector.errors.ProgrammingError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except UnboundLocalError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except AttributeError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except TypeError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
            

        def menu_tamu():
            while True:
                try:
                    print("==============================================================")
                    print("|                   SELAMAT DATANG : TAMU                    |")
                    print("==============================================================")
                    print("|                [1]. LIHAT DATA SAMARINDA                   |")
                    print("|                [2]. LIHAT DATA PEMERINTAH                  |")
                    print("|                [3]. LIHAT DATA PROGRAM                     |")
                    print("|                [4]. KELUAR DARI MENU TAMU                  |")
                    print("==============================================================")
                    pilihan = input("MASUKKAN PILIHAN ANDA : ")

                    if pilihan == "1":
                        os.system("cls")
                        read_samarinda()
                    elif pilihan == "2":
                        os.system("cls")
                        read_pemerintah()
                    elif pilihan == "3":
                        os.system("cls")
                        read_program()
                    elif pilihan == "4":
                        os.system("cls")
                        print("+------------+")
                        print("|TERIMA KASIH|")
                        print("+------------+")
                        break
                    else:
                        print("+-------------------+")
                        print("|PILIHAN TIDAK VALID|")
                        print("+-------------------+")
                except EOFError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except ValueError:
                    print("+-----------+")
                    print("|SALAH INPUT|")
                    print("+-----------+")
                except KeyboardInterrupt:
                    print("\n+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except mysql.connector.IntegrityError:
                    print("+------------+")
                    print("|ID SUDAH ADA|")
                    print("+------------+")
                except mysql.connector.errors.ProgrammingError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except UnboundLocalError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except AttributeError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
                except TypeError:
                    print("+-----------+")
                    print("|SALAH KETIK|")
                    print("+-----------+")
            

        class LoginSystem:
            def __init__(self, db_connection):
                self.db_connection = db_connection
                self.db_cursor = db_connection.cursor()

            def get_user_info(self, username):
                query = f"SELECT * FROM admin WHERE username = '{username}'"
                self.db_cursor.execute(query)
                user_data = self.db_cursor.fetchone()
                return user_data

            def login(self, username, password):
                user_data = self.get_user_info(username)
                if user_data:
                    if user_data[2] == password:  
                        menu_utama_superuser()
                    else:
                        print("+---------------------------+")
                        print("|PASSWORD SALAH , COBA LAGI|") 
                        print("+---------------------------+")
                else:
                    print("+------------------------+")
                    print("|USERNAME TIDAK DITEMUKAN|")
                    print("+------------------------+")

        login_system = LoginSystem(mydb)

        while True:
            try:
                print("------------------------------------------------------------")
                print("|                       WEBSITE KAMI                       |")
                print("|               https://www.kaltimprov.go.id/              |")
                print("|                                                          |")
                print("|               https://samarindakota.go.id/               |")
                print("|----------------------------------------------------------|")
                print("| SISTEM INFORMASI SAMARINDA DAN PEMERINTAH BERKELANJUTAN  |")
                print("|                                                          |")
                print("|                      [1]. LOGIN                          |")
                print("|                      [2]. MASUK SEBAGAI TAMU             |")
                print("|                      [3]. KELUAR DARI PROGRAM            |")
                print("|                                                          |")
                print("|                       KELOMPOK 9                         |")
                print("------------------------------------------------------------")
                choice = input("PILIH MENU : ")
                if choice == "1":
                    os.system("cls")
                    username = input("MASUKKAN USERNAME : ")
                    password = pwinput.pwinput("MASUKKAN PASSWORD : ", mask="*")
                    login_system.login(username, password)
                elif choice == "2":
                    os.system("cls")
                    menu_tamu()
                elif choice == "3":
                    os.system("cls")
                    print("+-------------------------------------------+")
                    print("|TERIMA KASIH TELAH MENGGUNAKAN PROGRAM KAMI|")
                    print("+-------------------------------------------+")
                    raise SystemExit
                else:
                    print("+-------------------+")
                    print("|PILIHAN TIDAK VALID|")
                    print("+-------------------+")
            except EOFError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except ValueError:
                print("+-----------+")
                print("|SALAH INPUT|")
                print("+-----------+")
            except KeyboardInterrupt:
                print("\n+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except mysql.connector.IntegrityError:
                print("+------------+")
                print("|ID SUDAH ADA|")
                print("+------------+")
            except mysql.connector.errors.ProgrammingError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except UnboundLocalError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except AttributeError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")
            except TypeError:
                print("+-----------+")
                print("|SALAH KETIK|")
                print("+-----------+")

    except KeyboardInterrupt:
        print("\n+-----------+")
        print("|SALAH KETIK|")
        print("+-----------+")
        continue
    except EOFError:
        print("+-----------+")
        print("|SALAH KETIK|")
        print("+-----------+")
        continue
    except ValueError:
        print("+-----------+")
        print("|SALAH INPUT|")
        print("+-----------+")
        continue
    except mysql.connector.IntegrityError:
        print("+------------+")
        print("|ID SUDAH ADA|")
        print("+------------+")
        continue
    except mysql.connector.errors.ProgrammingError:
        print("+-----------+")
        print("|SALAH KETIK|")
        print("+-----------+")
        continue
    except UnboundLocalError:
        print("+-----------+")
        print("|SALAH KETIK|")
        print("+-----------+")
        continue
    except AttributeError:
        print("+-----------+")
        print("|SALAH KETIK|")
        print("+-----------+")
        continue
    except TypeError:
        print("+-----------+")
        print("|SALAH KETIK|")
        print("+-----------+")
        continue
