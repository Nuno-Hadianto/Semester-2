import os
from prettytable import PrettyTable
from pwinput import pwinput
from datetime import datetime
import tkinter as tk

multiuser = {}
parts_recink = {}
discount_threshold = 100000
discount_rate = 0.1

def get_current_time():
    return datetime.now().time()

def is_working_hours():
    current_time = get_current_time()
    return current_time >= datetime.strptime("08:00", "%H:%M").time() and current_time <= datetime.strptime("16:00", "%H:%M").time()

def SignUp():
    root = tk.Tk()
    root.title("Sign Up")

    tk.Label(root, text="Username:").pack()
    username = tk.Entry(root)
    username.pack()

    tk.Label(root, text="Password:").pack()
    password = tk.Entry(root, show="*")
    password.pack()

    tk.Label(root, text="Privilege (admin/pembeli):").pack()
    privilege = tk.Entry(root)
    privilege.pack()

    def submit():
        try:
            multiuser[username.get()] = {'password': password.get(), 'saldo e-money': 0, 'parts_recink': [], 'privilage': privilege.get()}
            print(f"User akun baru {username.get()} berhasil didaftarkan.")\

            root = tk.Tk()
            root.title("Confirmation")

            tk.Label(root, text="User akun baru berhasil didaftarkan.").pack()

            root.mainloop()

        except KeyboardInterrupt:
            print("error")
        except EOFError:
            print("error")

    tk.Button(root, text="Submit", command=submit).pack()

    root.mainloop()

def SignIn():
    root = tk.Tk()
    root.title("Sign In")

    tk.Label(root, text="Username:").pack()
    username = tk.Entry(root)
    username.pack()

    tk.Label(root, text="Password:").pack()
    password = tk.Entry(root, show="*")
    password.pack()

    def submit():
        try:
            if username.get() in multiuser and multiuser[username.get()]['password'] == password.get():
                if multiuser[username.get()]['privilage'] == 'admin':
                    admin_menu()
                elif multiuser[username.get()]['privilage'] == 'pembeli':
                    pembeli_menu()
                else:
                    print("Anda bukan admin atau pembeli.")
            else:
                print("Username atau password salah atau takde.")
                return None
        except KeyboardInterrupt:
            print("error")
        except EOFError:
            print("error")

    tk.Button(root, text="Submit", command=submit).pack()

    root.mainloop()

def admin_menu():
    root = tk.Tk()
    root.title("Admin Menu")

    tk.Label(root, text="Admin Menu").pack()

    tk.Button(root, text="Menu 1", command=lambda: print("Tambah Part")).pack()
    tk.Button(root, text="Menu 2", command=lambda: print("Perbarui Part")).pack()
    tk.Button(root, text="Menu 3", command=lambda: print("Hapus Part")).pack()
    tk.Button(root, text="Menu 3", command=lambda: print("Melihat Part")).pack()

    root.mainloop()

def pembeli_menu():
    root = tk.Tk()
    root.title("Pembeli Menu")

    tk.Label(root, text="Pembeli Menu").pack()

    tk.Button(root, text="Tambah Saldo E-Money", command=recharge_e_money).pack()
    tk.Button(root, text="Masuk Akun Admin/Pembeli", command=beli_part).pack()
    tk.Button(root, text="Melihat Invoice", command=melihat_invoice).pack()

    root.mainloop()

def recharge_e_money(username):
    try:
        print(f"Saldo E-Money saat ini: {multiuser[username]['saldo e-money']}")
        jumlah = int(input("Masukkan jumlah saldo E-Money yang ingin ditambahi: "))
        multiuser[username]['saldo e-money'] += jumlah
        print(f"Saldo E-Money berhasil ditambahkan. Saldo E-Money saat ini: {multiuser[username]['saldo e-money']}")
    except KeyboardInterrupt:
        print("error")
    except EOFError:
        print("error")
    except ValueError:
        print("error")

def tambah_part():
    try:
        nama_part = input("Masukkan nama part racing: ")
        harga_part = int(input("Masukkan harga part racing: "))
        parts_recink[nama_part] = harga_part
        print(f"Part Racing {nama_part} berhasil ditambahkan.")
    except KeyboardInterrupt:
        print("error")
    except EOFError:
        print("error")
    except ValueError:
        print("error")

def perbarui_part():
    try:
        table = PrettyTable(['Nama Part Racing', 'Harga'])
        for part, harga in parts_recink.items():
            table.add_row([part, harga])
        print(table)
        nama_part = input("Masukkan nama part racing yang ingin diperbarui harga nya : ")
        if nama_part in parts_recink:
            harga_baru = int(input("Masukkan harga baru : "))
            parts_recink[nama_part] = harga_baru
            print(f"Harga part racing {nama_part} berhasil diperbarui.")
        else:
            print("Part racing tidak ditemukan atau salah ketik.")
    except KeyboardInterrupt:
        print("error")
    except EOFError:
        print("error")
    except ValueError:
        print("error")

def hapus_part():
    try:
        table = PrettyTable(['Nama Part Racing', 'Harga'])
        for part, harga in parts_recink.items():
            table.add_row([part, harga])
        print(table)
        nama_part = input("Masukkan nama part racing yang ingin dihapus: ")
        if nama_part in parts_recink:
            del parts_recink[nama_part]
            print(f"Part racing {nama_part} berhasil dihapus.")
        else:
            print("Part racing tidak ditemukan atau salah ketik.")
    except KeyboardInterrupt:
        print("error")
    except EOFError:
        print("error")

def beli_part(username):
    try:
        if not is_working_hours():  
            print("Maaf, fitur ini hanya tersedia pada jam kerja (08.00 - 16.00).")
            return

        total_belanja = 0  
        while True:
            table = PrettyTable(['Nama Part Racing', 'Harga'])
            for part, harga in parts_recink.items():
                table.add_row([part, harga])
            print(table)
            nama_part = input("Masukkan nama part racing yang ingin dibeli (atau ketik 'selesai' untuk mengakhiri): ")
            if nama_part.lower() == 'selesai':
                break
            if nama_part in parts_recink:
                harga_part = parts_recink[nama_part]
                total_belanja += harga_part  
                if total_belanja >= discount_threshold:  
                    diskon = total_belanja * discount_rate
                    total_belanja -= diskon
                    print(f"Selamat! Anda mendapatkan diskon sebesar {discount_rate*100}% (Rp {diskon}).")
                if multiuser[username]['saldo e-money'] >= harga_part:
                    multiuser[username]['saldo e-money'] -= harga_part
                    multiuser[username]['parts_recink'].append(nama_part)
                    print(f"Part racing {nama_part} berhasil dibeli.")
                else:
                    print("Saldo E-Money tidak cukup.")
            else:
                print("Part racing tidak ditemukan atau salah ketik.")
    except KeyboardInterrupt:
        print("error")
    except EOFError:
        print("error")

def melihat_part():
    table = PrettyTable(['Nama Part Racing', 'Harga'])
    for part, harga in parts_recink.items():
        table.add_row([part, harga])
    print(table)

def melihat_invoice(username):
    try:
        if not is_working_hours():  
            print("Maaf, fitur ini hanya tersedia pada jam kerja (08.00 - 16.00).")
            return

        total_belanja = 0  
        table = PrettyTable(['Nama Part Racing', 'Harga'])
        for part in multiuser[username]['parts_recink']:
            harga_part = parts_recink[part]
            table.add_row([part, harga_part])
            total_belanja += harga_part  
        print(table)
        print(f"Total Belanja: Rp {total_belanja}")
        if total_belanja >= discount_threshold:  
            diskon = total_belanja * discount_rate
            total_belanja -= diskon
            print(f"Selamat! Anda mendapatkan diskon sebesar {discount_rate*100}% (Rp {diskon}).")
        print("Bonus Pembelian keduanya kalinya klo motormu beat mberrr")
    except KeyboardInterrupt:
        print("error")
    except EOFError:
        print("error")

while True:
    def main_menu():
        root = tk.Tk()
        root.title("Jatim SpeedShop")

        tk.Label(root, text="Jatim SpeedShop", font=("Arial", 20)).pack()

        tk.Button(root, text="Daftar Akun Admin/Pembeli", command=SignUp).pack()
        tk.Button(root, text="Masuk Akun Admin/Pembeli", command=SignIn).pack()
        tk.Button(root, text="Keluar dari aplikasi", command=exit).pack()

        root.mainloop()

    main_menu()