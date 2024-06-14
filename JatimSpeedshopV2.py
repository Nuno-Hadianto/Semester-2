import os
from prettytable import PrettyTable
from pwinput import pwinput
from datetime import datetime

multiuser = {}
suku_cadang = {}
diskon_minimal = 100000
tingkat_diskon = 0.15
diskon_minimal2 = 350000
tingkat_diskon2 = 0.25
biaya_pelayanan = 2000

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
    return waktu_saat_ini >= datetime.strptime("08:30", "%H:%M").time() and waktu_saat_ini <= datetime.strptime("16:00", "%H:%M").time()

def cek_jam_kerja():
    if not jam_kerja():
        print("+===================================================================================+")
        print("| Maaf toko kami tutup🙏😔, toko dibuka kembali pada jam kerja (08.30 - 16.00)😄🥰  |")
        print("|                                                                                   |")
        print("|                              Jatim SpeedShop Teams👨🧑👩                          |")
        print("+===================================================================================+")
        return False
    return True

def hari_kerja():
    return datetime.now().strftime("%A")

def daftar_akun():
    os.system('cls')
    try:
        username = input("Masukkan nama akun baru🎫 : ")
        while any(char in '|/?+=_-)(*&^$#!' for char in username):
                    print("🚫tidak boleh berisi karakter khusus seperti |/?+=_-)(*&^$#!")
                    username = input("Masukkan nama akun baru🎫 : ")
        if username in multiuser:
            print("Nama akun sudah ada.☹️  Silahkan masukkan nama akun lain.😄")
            return
        usia = int(input("Masukkan usia anda🔍 :"))
        while usia < 12:
            print("Usia minimal 12 tahun.🧐")
            usia = int(input("Masukkan usia anda🔍 :"))
        gender = input("Masukkan jenis kelamin (laki-laki/perempuan)👫 :")
        while gender not in ['laki-laki', 'perempuan']:
            print("Jenis kelamin tidak valid❌. Harus laki-laki atau perempuan.😑")
            gender = input("Masukkan jenis kelamin (laki-laki/perempuan)👫 :")
        password = int(pwinput("Masukkan pin akun baru🔐  : "))
        privilage = input("Masukkan privilage (admin/pembeli)⚖️  : ")
        if privilage not in ['admin', 'pembeli']:
            print("Privilage tidak valid.☹️  Harus atau admin atau pembeli.😄")
            return
        else:
            multiuser[username] = {'password': password, 'saldo e-money': 0, 'suku_cadang': [], 'privilage': privilage, 'usia' : usia, 'gender' : gender}
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
    except ValueError:
        os.system('cls')
        print("==========================")
        print("| INPUT TIDAK VALID🤨🧐 |")
        print("==========================")

def masuk_akun():
    os.system('cls')
    try:
        username = input("Masukkan nama akun🎫 : ")
        password = int(pwinput("Masukkan pin akun🔐 : "))
        if username in multiuser and multiuser[username]['password'] == password:
            usia = multiuser[username]['usia']
            gender = multiuser[username]['gender']
            if usia < 15:
                print("Selamat Datang👏 Dek",username," 🤩")
                return username
            elif 15 <= usia <= 29:
                print("Selamat Datang👏 Kak",username," 🤩")
                return username
            elif usia >= 30 and usia <= 70 and gender == 'laki-laki':
                print(f"Selamat Datang👏 Bapak {username} 🤩")
                return username
            elif usia >= 30 and usia <= 70 and gender == 'perempuan':
                print(f"Selamat Datang👏 Ibu {username} 🤩")
                return username
            else:
                print("Selamat Datang👏",username," 🤩")
                return username
        else:
            print("Nama akun atau pin akun salah atau takde.☹️")
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
    print('\n' * 1000)
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
        print('\n' * 1000)
        print(f"Saldo E-Money saat ini💰 : {multiuser[username]['saldo e-money']}")
    

def tambah_suku_cadang():
    os.system('cls')
    try:
        nama_suku_cadang = input("Masukkan nama suku cadang🔩 : ").lower().strip()
        while any(char in '|/?+=_-)(*&^$#!' for char in nama_suku_cadang):
                    print("🚫tidak boleh berisi karakter khusus seperti |/?+=_-)(*&^$#!")
                    nama_suku_cadang = input("Masukkan nama suku cadang🔩 : ").lower().strip()
        if nama_suku_cadang in suku_cadang:
            print("Nama suku cadang sudah ada.✅  Tidak bisa ditambahkan lagi.❌")
            return

        jumlah_part = int(input("Masukkan jumlah suku cadang🔧 :").strip())
        harga_part = int(input("Masukkan harga suku cadang💵 : ").strip())
        jenis_part = input("Masukkan jenis suku cadang⚙️ : ").lower().strip()
        while any(char in '|/?+=_-)(*&^$#!' for char in jenis_part):
                    print("🚫tidak boleh berisi karakter khusus seperti |/?+=_-)(*&^$#!")
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
        if suku_cadang:
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
        else:
            print("Tidak ada suku cadang yang tersedia.☹️")
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
        if suku_cadang:
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
        else:
            print("Tidak ada suku cadang yang tersedia.☹️")
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
    print('\n' * 1000)
    try:
        total_belanja = 0
        parts_bought = []

        while True:
            if suku_cadang:
                table = PrettyTable(['Nama Suku Cadang', 'Jumlah', 'Harga', 'Jenis'])
                for part, data in suku_cadang.items():
                    table.add_row([part, data['jumlah'], data['harga'], data['jenis']])
                print(table)
                nama_suku_cadang = input("Masukkan nama suku cadang yang ingin dibeli🔩 (atau ketik 'selesai' untuk mengakhiri)❌ : ").strip()
                if nama_suku_cadang.lower() == 'selesai':
                    break
                if nama_suku_cadang in suku_cadang:
                    jumlah_part = int(input("Masukkan jumlah yang ingin dibeli⚙️ : "))
                    harga_part = suku_cadang[nama_suku_cadang]['harga'] * jumlah_part  
                    harga_part += biaya_pelayanan  
                    if multiuser[username]['saldo e-money'] >= total_belanja + harga_part:
                        total_belanja += harga_part
                        if suku_cadang[nama_suku_cadang]['jumlah'] >= jumlah_part:
                            parts_bought.append((nama_suku_cadang, jumlah_part, harga_part, suku_cadang[nama_suku_cadang]['jenis']))
                            suku_cadang[nama_suku_cadang]['jumlah'] -= jumlah_part
                            print(f"Suku cadang {nama_suku_cadang} sebanyak {jumlah_part} berhasil ditambahkan ke keranjang.✅")
                        else:
                            print("Jumlah suku cadang yang tersedia tidak mencukupi.☹️")
                    else:
                        print("Saldo E-Money tidak cukup💰❌. Pembelian dibatalkan.☹️")
                else:
                    print("Suku cadang tidak ditemukan atau salah ketik.☹️")
            else:
                print("Tidak ada suku cadang yang tersedia.☹️")
                break

        if total_belanja == 0:
            print("Tidak ada item yang dibeli.❌")
            return

        if total_belanja >= diskon_minimal2:
            diskon = total_belanja * tingkat_diskon2
            total_belanja -= diskon
            print(f"Selamat!🥳 Anda mendapatkan diskon sebesar 25% (Rp {diskon}).😱")
        elif total_belanja >= diskon_minimal:
            diskon = total_belanja * tingkat_diskon
            total_belanja -= diskon
            print(f"Selamat!🥳 Anda mendapatkan diskon sebesar 15% (Rp {diskon}).😱")

        multiuser[username]['saldo e-money'] -= total_belanja
        multiuser[username]['suku_cadang'].extend(parts_bought)
        print(f"Total pembelian setelah biaya pelayanan🙏, dan diskon🔖(S&K Berlaku untuk diskon) adalah Rp {total_belanja}. Pembayaran berhasil.✅")

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
    if suku_cadang:
        table = PrettyTable(['Nama Suku Cadang', 'Jumlah', 'Harga', 'Jenis'])
        for part, data in suku_cadang.items():
            table.add_row([part, data['jumlah'], data['harga'], data['jenis']])
        print(table)
    else:
        print("Tidak ada suku cadang yang tersedia.☹️")

def struk_pesanan(username):
    os.system('cls')
    print('\n' * 1000)
    if multiuser[username]['suku_cadang']:
        print("=============== Struk Pesanan ===============")
        total_belanja = 0
        table = PrettyTable(['Nama Suku Cadang', 'Jumlah', 'Harga', 'Jenis'])
        for part in multiuser[username]['suku_cadang']:
            table.add_row([part[0], part[1], part[2], part[3]])
            total_belanja += part[2]
        print(table)
        print("=============================================")
        pajak = total_belanja * 0.02
        total_belanja += pajak
        print(f"Total Biaya     : Rp {total_belanja:.2f}")
        diskon = 0
        if total_belanja >= 350000:
            diskon = total_belanja * 0.25
            total_belanja -= diskon
            print(f"Diskon 25%      : Rp {diskon:.2f}")
        elif total_belanja >= 100000:
            diskon = total_belanja * 0.15
            total_belanja -= diskon
            print(f"Diskon 15%      : Rp {diskon:.2f}")
        print(f"Pajak (2%)      : Rp {pajak:.2f}")
        print(f"Biaya Pelayanan : Rp 2000")
        print("=============================================")
        print(f"Total Bayar     : Rp {total_belanja:.2f}")
        print(f"Terimakasih telah membeli suku cadang di toko kami😉, silahkan beli disini kapan saja.👋")
        print("")
    else:
        print("Belum ada pesanan.☹️")

def tutup():
    print("+================================================================================================================+")
    print("| Maaf😔, hari ini hari minggu.📅 Toko kami tutup.🏪🔒 Silakan datang kembali hari senin.😁 Terima kasih.🙏      |")
    print("|                                                                                                                |")
    print("|                                          Jatim SpeedShop Teams👨🧑👩                                           |")
    print("+================================================================================================================+")
    exit()

while True:
    try:
        if not cek_jam_kerja():
            break
        if hari_kerja() in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']:
            print("")
        else:
            tutup()
        print("                Menu Utama")    
        print("+-----------------------------------------+")
        print("|                                         |")
        print("|          Jatim SpeedShop v2🔥           |")
        print("|                                         |")
        print("|    TOKO SPAREPART MOTOR SAMARINDA       |")
        print("|    Melayani partai & eceran             |")
        print("|    NO DM🚫 WA ONLY👍🏻                  |")
        print("|    Senin-Sabtu (08:30-17:00)            |")
        print("|    📍Jl Biawan (samping rumbia)         |")
        print("|    📍Jl Kehewanan (dpn kantor camat)    |")
        print("|    📞WA - 0813-9999-8825                |")
        print("|    linktr.ee/jatimspeedshop             |")
        print("|                                         |")
        print("|                                         |")
        print("|   [1]. Daftar Akun Admin/Pembeli🖊️       |")
        print("|                                         |")
        print("|   [2]. Masuk Akun Admin/Pembeli📲       |")
        print("|                                         |")
        print("|   [3]. Keluar dari aplikasi🚪           |")
        print("|                                         |")
        print("+-----------------------------------------+")
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
                            print("+------------------------------+")
                            print("|          Menu Admin          |")
                            print("|                              |")
                            print("| [1]. Tambah Suku Cadang🔩    |")
                            print("|                              |")
                            print("| [2]. Perbarui Suku Cadang🔧  |")
                            print("|                              |")
                            print("| [3]. Hapus Suku Cadang❌     |")
                            print("|                              |")
                            print("| [4]. Lihat Suku Cadang👀     |")
                            print("|                              |")
                            print("| [5]. Logout Akun🚪           |")
                            print("|                              |")
                            print("+------------------------------+")
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
                            print("+------------------------------+")
                            print("|        Menu Pembeli          |")
                            print("|                              |")
                            print("| [1]. Tambah Saldo E-Money💸  |")
                            print("|                              |")
                            print("| [2]. Beli Suku Cadang🔩      |")
                            print("|                              |")
                            print("| [3]. Struk Pesanan🧾         |")
                            print("|                              |")
                            print("| [4]. Lihat Saldo💰           |")
                            print("|                              |")
                            print("| [5]. Logout Akun🚪           |")
                            print("|                              |")
                            print("+------------------------------+")
                            user_choice = input("Pilihlah opsi bossque😎 : ")
                            if user_choice == '1':
                                os.system('cls')
                                isi_e_money(user)
                            elif user_choice == '2':
                                os.system('cls')
                                beli_suku_cadang(user)
                            elif user_choice == '3':
                                os.system('cls')
                                struk_pesanan(user)
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