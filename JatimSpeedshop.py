import os
from prettytable import PrettyTable
from pwinput import pwinput
from datetime import datetime

multiuser = {}
suku_cadang = {}
diskon_minimal = 100000
tingkat_diskon = 0.1

RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
CYAN = "\033[96m"

print(BOLD + CYAN + "   ")
def ambil_waktu_sekarang():
    return datetime.now().time()

def jam_kerja():
    waktu_saat_ini = ambil_waktu_sekarang()
    return waktu_saat_ini >= datetime.strptime("08:00", "%H:%M").time() and waktu_saat_ini <= datetime.strptime("16:00", "%H:%M").time()

def cek_jam_kerja():
    if not jam_kerja():
        print("+===================================================================================+")
        print("| Maaf toko kami tutup🙏😔, toko dibuka kembali pada jam kerja (08.00 - 16.00)😄🥰  |")
        print("|                                                                                   |")
        print("|                              Jatim SpeedShop Teams👨🧑👩                          |")
        print("+===================================================================================+")
        return False
    return True

def daftar_akun():
    os.system('cls')
    try:
        username = input("Masukkan username akun baru😃 : ")
        while any(char in '|/?+=_-)(*&^$#!' for char in username):
                    print("tidak boleh berisi karakter khusus seperti |/?+=_-)(*&^$#!")
                    username = input("Masukkan username akun baru😃 : ")
        if username in multiuser:
            print("Username sudah ada.☹️  Silakan masukkan username lain.😄")
            return

        password = pwinput("Masukkan password akun baru⌨️  : ")
        privilage = input("Masukkan privilage (admin/pembeli)⚖️  : ")
        if privilage not in ['admin', 'pembeli']:
            print("Privilage tidak valid.☹️  Harus atau admin atau pembeli.😄")
            return
        else:
            multiuser[username] = {'password': password, 'saldo e-money': 0, 'suku_cadang': [], 'privilage': privilage}
            print(f"User akun baru {username} berhasil didaftarkan.✅")
    except KeyboardInterrupt:
        os.system('cls')
        print("\n========================")
        print("| INPUT TIDAK VALID🤨🧐 |")
        print("==========================")
    except EOFError:
        os.system('cls')
        print("==========================")
        print("| INPUT TIDAK VALID🤨🧐 |")
        print("==========================")

def masuk_akun():
    os.system('cls')
    try:
        username = input("Masukkan username akun😃 : ")
        password = pwinput("Masukkan password akun⌨️ : ")
        if username in multiuser and multiuser[username]['password'] == password:
            return username
        else:
            print("Username atau password salah atau takde.☹️")
            return None
    except KeyboardInterrupt:
        os.system('cls')
        print("\n========================")
        print("| INPUT TIDAK VALID🤨🧐 |")
        print("==========================")
    except EOFError:
        os.system('cls')
        print("==========================")
        print("| INPUT TIDAK VALID🤨🧐 |")
        print("==========================")
    except ValueError:
        os.system('cls')
        print("==========================")
        print("| INPUT TIDAK VALID🤨🧐 |")
        print("==========================")

def isi_e_money(username):
    os.system('cls')
    try:
        print(f"Saldo E-Money saat ini💰 : {multiuser[username]['saldo e-money']}")
        jumlah = int(input("Masukkan jumlah saldo E-Money yang ingin ditambahi💵 : "))
        multiuser[username]['saldo e-money'] += jumlah
        print(f"Saldo E-Money berhasil ditambahkan.💸  Saldo E-Money saat ini💰 : {multiuser[username]['saldo e-money']}")
    except KeyboardInterrupt:
        os.system('cls')
        print("\n========================")
        print("| INPUT TIDAK VALID🤨🧐 |")
        print("==========================")
    except EOFError:
        os.system('cls')
        print("==========================")
        print("| INPUT TIDAK VALID🤨🧐 |")
        print("==========================")
    except ValueError:
        os.system('cls')
        print("==========================")
        print("| INPUT TIDAK VALID🤨🧐 |")
        print("==========================")

def lihat_saldo(username):
        os.system('cls')
        print(f"Saldo E-Money saat ini💰 : {multiuser[username]['saldo e-money']}")
    

def tambah_suku_cadang():
    os.system('cls')
    try:
        nama_suku_cadang = input("Masukkan nama suku cadang🔩 : ").lower().strip()
        while any(char in '|/?+=_-)(*&^$#!' for char in nama_suku_cadang):
                    print("tidak boleh berisi karakter khusus seperti |/?+=_-)(*&^$#!")
                    nama_suku_cadang = input("Masukkan nama suku cadang🔩 : ").lower().strip()
        if nama_suku_cadang in suku_cadang:
            print("Nama suku cadang sudah ada.✅  Tidak bisa ditambahkan lagi.❌")
            return

        jumlah_part = int(input("Masukkan jumlah suku cadang🔧 :").strip())
        harga_part = int(input("Masukkan harga suku cadang💵 : ").strip())
        jenis_part = input("Masukkan jenis suku cadang⚙️ : ").lower().strip()
        while any(char in '|/?+=_-)(*&^$#!' for char in jenis_part):
                    print("tidak boleh berisi karakter khusus seperti |/?+=_-)(*&^$#!")
                    jenis_part = input("Masukkan jenis suku cadang⚙️ : ").lower().strip()
        suku_cadang[nama_suku_cadang] = {'jumlah': jumlah_part, 'harga': harga_part, 'jenis': jenis_part}
        print(f"Suku cadang {nama_suku_cadang} berhasil ditambahkan.✅")
    except KeyboardInterrupt:
        os.system('cls')
        print("\n========================")
        print("| INPUT TIDAK VALID🤨🧐 |")
        print("==========================")
    except EOFError:
        os.system('cls')
        print("==========================")
        print("| INPUT TIDAK VALID🤨🧐 |")
        print("==========================")
    except ValueError:
        os.system('cls')
        print("==========================")
        print("| INPUT TIDAK VALID🤨🧐 |")
        print("==========================")

def perbarui_suku_cadang():
    os.system('cls')
    try:
        table = PrettyTable(['Nama Suku Cadang', 'Jumlah', 'Harga', 'Jenis'])
        for part, data in suku_cadang.items():
            table.add_row([part, data['jumlah'], data['harga'], data['jenis']])
        print(table)
        nama_suku_cadang = input("Masukkan nama suku cadang yang ingin diperbarui harga nya🔩 : ").strip()
        if nama_suku_cadang in suku_cadang:
            harga_baru = int(input("Masukkan harga baru💴 : ").strip())
            suku_cadang[nama_suku_cadang]['harga'] = harga_baru
            print(f"Harga suku cadang {nama_suku_cadang} berhasil diperbarui.✅")
            jumlah_baru = int(input("Masukkan jumlah baru⚙️ : "))
            suku_cadang[nama_suku_cadang]['jumlah'] = jumlah_baru
            print(f"Jumlah suku cadang {nama_suku_cadang} berhasil diperbarui.✅")
        else:
            print("Suku cadang tidak ditemukan atau salah ketik.☹️")
    except KeyboardInterrupt:
        os.system('cls')
        print("\n========================")
        print("| INPUT TIDAK VALID🤨🧐 |")
        print("==========================")
    except EOFError:
        os.system('cls')
        print("==========================")
        print("| INPUT TIDAK VALID🤨🧐 |")
        print("==========================")
    except ValueError:
        os.system('cls')
        print("==========================")
        print("| INPUT TIDAK VALID🤨🧐 |")
        print("==========================")

def hapus_suku_cadang():
    os.system('cls')
    try:
        table = PrettyTable(['Nama Suku Cadang', 'Jumlah', 'Harga', 'Jenis'])
        for part, data in suku_cadang.items():
            table.add_row([part, data['jumlah'], data['harga'], data['jenis']])
        print(table)
        nama_suku_cadang = input("Masukkan nama suku cadang yang ingin dihapus🔩 : ")
        if nama_suku_cadang in suku_cadang:
            del suku_cadang[nama_suku_cadang]
            print(f"Suku cadang {nama_suku_cadang} berhasil dihapus.✅")
        else:
            print("Suku cadang tidak ditemukan atau salah ketik.☹️")
    except KeyboardInterrupt:
        os.system('cls')
        print("\n========================")
        print("| INPUT TIDAK VALID🤨🧐 |")
        print("==========================")
    except EOFError:
        os.system('cls')
        print("==========================")
        print("| INPUT TIDAK VALID🤨🧐 |")
        print("==========================")

def beli_suku_cadang(username):
    os.system('cls')
    try:
        total_belanja = 0
        parts_bought = []

        while True:
            table = PrettyTable(['Nama Suku Cadang', 'Jumlah', 'Harga', 'Jenis'])
            for part, data in suku_cadang.items():
                table.add_row([part, data['jumlah'], data['harga'], data['jenis']])
            print(table)
            nama_suku_cadang = input("Masukkan nama suku cadang yang ingin dibeli🔩 (atau ketik 'selesai' untuk mengakhiri)❌ : ")
            if nama_suku_cadang.lower() == 'selesai':
                break
            if nama_suku_cadang in suku_cadang:
                jumlah_part = int(input("Masukkan jumlah yang ingin dibeli⚙️ : "))
                harga_part = suku_cadang[nama_suku_cadang]['harga'] * jumlah_part
                if multiuser[username]['saldo e-money'] >= total_belanja + harga_part:
                    total_belanja += harga_part
                    if suku_cadang[nama_suku_cadang]['jumlah'] >= jumlah_part:
                        parts_bought.append((nama_suku_cadang, jumlah_part, harga_part, suku_cadang[nama_suku_cadang]['jenis']))
                        suku_cadang[nama_suku_cadang]['jumlah'] -= jumlah_part
                        print(f"Suku cadang {nama_suku_cadang} sebanyak {jumlah_part} berhasil ditambahkan ke keranjang.✅")
                    else:
                        os.system('cls')
                        print("Jumlah suku cadang yang tersedia tidak mencukupi.☹️")
                else:
                    os.system('cls')
                    print("Saldo E-Money tidak cukup. Pembelian dibatalkan.☹️")
            else:
                os.system('cls')
                print("Part racing tidak ditemukan atau salah ketik.☹️")

        if total_belanja == 0:
            print("Tidak ada item yang dibeli.❌")
            return

        if total_belanja >= diskon_minimal:
            diskon = total_belanja * tingkat_diskon
            total_belanja -= diskon
            print(f"Selamat!🥳 Anda mendapatkan diskon sebesar {tingkat_diskon*100}% (Rp {diskon}).😱")

        multiuser[username]['saldo e-money'] -= total_belanja
        multiuser[username]['suku_cadang'].extend(parts_bought)
        print(f"Total pembelian setelah diskon adalah Rp {total_belanja}. Pembayaran berhasil.✅")

    except KeyboardInterrupt:
        os.system('cls')
        print("\n========================")
        print("| INPUT TIDAK VALID🤨🧐 |")
        print("==========================")
    except EOFError:
        os.system('cls')
        print("==========================")
        print("| INPUT TIDAK VALID🤨🧐 |")
        print("==========================")
    except ValueError:
        os.system('cls')
        print("==========================")
        print("| INPUT TIDAK VALID🤨🧐 |")
        print("==========================")


def liat_suku_cadang():
    os.system('cls')
    table = PrettyTable(['Nama Suku Cadang', 'Jumlah', 'Harga', 'Jenis'])
    for part, data in suku_cadang.items():
        table.add_row([part, data['jumlah'], data['harga'], data['jenis']])
    print(table)

def liat_invoice(username):
    os.system('cls')
    try:
        total_belanja = 0
        table = PrettyTable(['Nama Suku Cadang', 'Jumlah', 'Harga', 'Jenis'])
        for part in multiuser[username]['suku_cadang']:
            table.add_row([part[0], part[1], part[2], part[3]])
            total_belanja += part[2]
        print(table)
        print(f"Total Belanja: Rp {total_belanja} 💵")
        if total_belanja >= diskon_minimal:
            diskon = total_belanja * tingkat_diskon
            total_belanja -= diskon
            print(f"Selamat!🥳 Anda mendapatkan diskon sebesar {tingkat_diskon*100}% (Rp {diskon}).😱")
        print(f"Total Belanja Setelah Diskon: Rp {total_belanja} 💵")
    except KeyboardInterrupt:
        os.system('cls')
        print("\n========================")
        print("| INPUT TIDAK VALID🤨🧐 |")
        print("==========================")
    except EOFError:
        os.system('cls')
        print("==========================")
        print("| INPUT TIDAK VALID🤨🧐 |")
        print("==========================")


while True:
    try:
        if not cek_jam_kerja():
            break
        print("")
        print("              Jatim SpeedShop                                                                    ")
        print("                                                                                                 ")
        print("              TOKO SPAREPART MOTOR SAMARINDA                                                     ")
        print("              Melayani partai & eceran                                                           ")
        print("              NO DM🚫 WA ONLY👍🏻                                                                 ")
        print("              Senin-Sabtu (08:30-17:00)                                                          ")
        print("              📍Jl Biawan (samping rumbia)                                                       ")
        print("              📍Jl Kehewanan (dpn kantor camat)                                                  ")
        print("              📞WA - 0813-9999-8825                                                             ")
        print("              linktr.ee/jatimspeedshop                                                           ")
        print("")
        print(" [1]. Daftar Akun Admin/Pembeli🖊️")
        print(" [2]. Masuk Akun Admin/Pembeli📲")
        print(" [3]. Keluar dari aplikasi🚪 ")
        print("")
        choice = input("Pilihlah opsi bossque😎 : ")
        os.system('cls')
        if choice == '1':
            os.system("cls")
            daftar_akun()
        elif choice == '2':
            os.system("cls")
            user = masuk_akun()
            if user is not None:
                while True:
                    try:
                        if multiuser[user]['privilage'] == 'admin':
                            print("\n[1]. Tambah Suku Cadang🔩\n[2]. Perbarui Suku Cadang🔧\n[3]. Hapus Suku Cadang❌\n[4]. Lihat Suku Cadang👀\n[5]. Logout Akun🚪")
                            user_choice = input("Pilihlah opsi bossque😎 : ")
                            if user_choice == '1':
                                os.system('cls')
                                tambah_suku_cadang()
                            elif user_choice == '2':
                                os.system('cls')
                                perbarui_suku_cadang()
                            elif user_choice == '3':
                                os.system('cls')
                                hapus_suku_cadang()
                            elif user_choice == '4':
                                os.system('cls')
                                liat_suku_cadang()
                            elif user_choice == '5':
                                os.system('cls')
                                break
                            else:
                                os.system('cls')
                                print("===========================")
                                print("| PILIHAN TIDAK VALID🤨🧐 |")
                                print("===========================")
                        elif multiuser[user]['privilage'] == 'pembeli':
                            print("\n[1]. Tambah Saldo E-Money💸\n[2]. Beli Suku Cadang🔩\n[3]. Lihat Invoice👜\n[4]. Lihat Saldo💰\n[5]. Logout Akun🚪")
                            user_choice = input("Pilihlah opsi bossque😎 : ")
                            if user_choice == '1':
                                os.system('cls')
                                isi_e_money(user)
                            elif user_choice == '2':
                                os.system('cls')
                                beli_suku_cadang(user)
                            elif user_choice == '3':
                                os.system('cls')
                                liat_invoice(user)
                            elif user_choice == '4':
                                os.system('cls')
                                lihat_saldo(user)
                            elif user_choice == '5':
                                os.system('cls')
                                break
                            else:
                                os.system('cls')
                                print("===========================")
                                print("| PILIHAN TIDAK VALID🤨🧐 |")
                                print("===========================")
                        else:
                            os.system('cls')
                            print("==========================")
                            print("| INPUT TIDAK VALID🤨🧐 |")
                            print("==========================")
                            break
                    except KeyboardInterrupt:
                        os.system('cls')
                        print("\n=========================")
                        print("| INPUT TIDAK VALID🤨🧐 |")
                        print("=========================")
                    except EOFError:
                        os.system('cls')
                        print("=========================")
                        print("| INPUT TIDAK VALID🤨🧐 |")
                        print("=========================")
        elif choice == '3':
            print("+===============================================================================================+")
            print("| Terimakasih Telah Mengunjungi Toko Kami😄, Semoga Puas Dengan Pelayanan Yang Kami Berikan🥰   |")
            print("|                                                                                               |")
            print("|                                Jatim SpeedShop Teams👨🧑👩                                    |")
            print("+===============================================================================================+")
            break
        else:
            os.system('cls')
            print("=========================")
            print("| PILIHAN TIDAK ADA🤨🧐 |")
            print("=========================")
    except KeyboardInterrupt:
        os.system('cls')
        print("\n=========================")
        print("| INPUT TIDAK VALID🤨🧐 |")
        print("=========================")
    except EOFError:
        os.system('cls')
        print("=========================")
        print("| INPUT TIDAK VALID🤨🧐 |")
        print("=========================")