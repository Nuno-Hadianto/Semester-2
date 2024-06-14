#biar bewarna
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
CYAN = "\033[96m"

print(RED + "" + RESET)
print(BOLD + "" + RESET)
print(BOLD + "" + RESET)
print(BOLD + "" + RESET)
print(BOLD + "" + RESET)

#kelas buat nyimpan data scooter
class Scooter_Matic:#
    def __init__(self, nama_scooter, pulley_depan, pulley_belakang, slider_pulley, roller, kampas_ganda, 
                 per_kampas_ganda, per_cvt, injector, ecu, noken, tb, tps, oli, filter_udara, knalpot, mesin):
        self.nama_motor = nama_scooter
        self.pulley_depan = pulley_depan
        self.pulley_belakang = pulley_belakang
        self.slider_pulley = slider_pulley
        self.roller = roller
        self.kampas_ganda = kampas_ganda
        self.per_kampas_ganda = per_kampas_ganda
        self.per_cvt = per_cvt
        self.injector = injector
        self.ecu = ecu
        self.noken = noken
        self.tb = tb
        self.tps = tps
        self.oli = oli
        self.filter_udara = filter_udara
        self.knalpot = knalpot
        self.mesin = mesin

    def __str__(self):
        return f"""{self.nama_scooter} - {self.pulley_depan} - {self.pulley_belakang} - {self.slider_pulley} - 
        {self.roller} - {self.kampas_ganda} - {self.per_kampas_ganda} - {self.injector} - {self.ecu} - {self.noken} - 
        {self.tb} - {self.tps} - {self.oli} - {self.filter_udara} - {self.knalpot} - {self.mesin}""" 

#membuat list untuk menyimpan data scooter
data_scooter = []

#gasan menambahkan data scooter baru
def create():
    try:
        print(BOLD + YELLOW + "==========================================================" + RESET)
        print(BOLD + YELLOW + "Masukkan data scooter matic anda yang ingin dimodifikasi :" + RESET)
        print(BOLD + YELLOW + "==========================================================" + RESET)
        nama_scooter = input(BOLD + BLUE + "Nama Scooter Matic: " + RESET)
        pulley_depan = input(BOLD + BLUE + "Pulley depan: " + RESET)
        pulley_belakang = input(BOLD + BLUE + "Pulley belakang/Sliding Shave: " + RESET)
        slider_pulley = input(BOLD + BLUE + "Slider Pulley: " + RESET)
        roller = input(BOLD + BLUE + "Roller beserta gram/berat: " + RESET)
        kampas_ganda = input(BOLD + BLUE + "Kampas Ganda: " + RESET)
        per_kampas_ganda = input(BOLD + BLUE + "Per Kampas Ganda: " + RESET)
        per_cvt = input(BOLD + BLUE + "Per cvt: " + RESET)
        injector = input(BOLD + BLUE + "Injector: " + RESET)
        ecu = input(BOLD + BLUE + "ECU: " + RESET)
        noken = input(BOLD + BLUE + "Noken: " + RESET)
        tb = input(BOLD + BLUE + "TB(Throttle Body): " + RESET)
        tps = input(BOLD + BLUE + "TPS Sensor: " + RESET)
        oli = input(BOLD + BLUE + "Oli Mesin + Gardan: " + RESET)
        filter_udara = input(BOLD + BLUE + "Filter Udara: " + RESET)
        knalpot = input(BOLD + BLUE + "Knalpot: " + RESET)
        mesin = input(BOLD + BLUE + "Isi Silinder/CC: " + RESET)
        #membuat objek scooter dari data yang dimasukkan
        scooter = Scooter_Matic(nama_scooter, pulley_depan, pulley_belakang, slider_pulley, roller, 
                                kampas_ganda, per_kampas_ganda, per_cvt, injector, ecu, noken, tb, 
                                tps, oli, filter_udara, knalpot, mesin) 
        #menambahkan objek scooter ke list
        data_scooter.append(scooter)
        print(BOLD + YELLOW + "==========================================================" + RESET)
        print(BOLD + YELLOW + "Data scooter yang ingin dimodifikasi berhasil ditambahkan." + RESET)
        print(BOLD + YELLOW + "==========================================================" + RESET)
    except KeyboardInterrupt:
        print(BOLD + RED + "============" + RESET)
        print(BOLD + RED + "Salah Pencet" + RESET)
        print(BOLD + RED + "============" + RESET)
    except EOFError:
        print(BOLD + RED + "============" + RESET)
        print(BOLD + RED + "Salah Pencet" + RESET)
        print(BOLD + RED + "============" + RESET)
    except ValueError:
        print(BOLD + RED + "============" + RESET)
        print(BOLD + RED + "Salah Pencet" + RESET)
        print(BOLD + RED + "============" + RESET)

#gasan menampilkan data scooter yang ada
def read():
    print(BOLD + YELLOW + "Data scooter yang ada:" + RESET)
    #menggunakan perulangan for untuk mengakses setiap elemen di list
    for scooter in data_scooter:
        #menampilkan data scooter dengan memanggil metode __str__ dari objek scooter
        print(scooter)

#gasan mengubah data scooter yang ada
def update():
    print(BOLD + YELLOW + "Masukkan nama scooter yang ingin diubah datanya:" + RESET)
    nama_scooter = input(BOLD + YELLOW + "Nama: " + RESET)
    #mengecek apakah scooter ada di list
    ada = False
    for scooter in data_scooter:
        if scooter.nama_scooter == nama_scooter:
            ada = True
            break
    if ada:
        print(BOLD + GREEN + "Data scooter sebelum diubah:" + RESET)
        print(scooter)
        print(BOLD + YELLOW + "Masukkan data scooter yang baru:" + RESET)
        pulley_depan = input(BOLD + BLUE + "Pulley depan: " + RESET)
        pulley_belakang = input(BOLD + BLUE + "Pulley belakang: " + RESET)
        slider_pulley = input(BOLD + BLUE + "Slider Pulley: " + RESET)
        roller = input(BOLD + BLUE + "Roller beserta gr/berat: " + RESET)
        kampas_ganda = input(BOLD + BLUE + "Kampas Ganda: " + RESET)
        per_kampas_ganda = input(BOLD + BLUE + "Per Kampas Ganda: " + RESET)
        per_cvt = input(BOLD + BLUE + "Per cvt: " + RESET)
        injector = input(BOLD + BLUE + "Injector: " + RESET)
        ecu = input(BOLD + BLUE + "ECU:" + RESET)
        noken = input(BOLD + BLUE + "Noken: " + RESET)
        tb = input(BOLD + BLUE + "Throttle Body: " + RESET)
        tps = input(BOLD + BLUE + "TPS Sensor: " + RESET)
        oli = input(BOLD + BLUE + "Oli Mesin + Gardan: " + RESET)
        filter_udara = input(BOLD + BLUE + "Filter Udara: " + RESET)
        knalpot = input(BOLD + BLUE + "Knalpot: " + RESET)
        mesin = input(BOLD + BLUE + "Isi Silinder/CC + BRT PERFORMANCE PACKAGE: " + RESET)
        #mengubah atribut objek scooter dengan data yang baru
        scooter.pulley_depan = pulley_depan
        scooter.pulley_belakang = pulley_belakang
        scooter.slider_pulley = slider_pulley
        scooter.roller = roller
        scooter.kampas_ganda = kampas_ganda
        scooter.per_kampas_ganda = per_kampas_ganda
        scooter.per_cvt = per_cvt
        scooter.injector = injector
        scooter.ecu = ecu
        scooter.noken = noken
        scooter.tb = tb
        scooter.tps = tps
        scooter.oli = oli
        scooter.filter_udara = filter_udara
        scooter.knalpot = knalpot
        scooter.mesin = mesin
        print(BOLD + GREEN + "Data scooter berhasil diubah." + RESET)
    else:
        print("==================================")
        print(BOLD + RED + "Nama tidak ditemukan.")

#gasan menghapus data scooter yang ada
def delete():
    print(BOLD + RED + "Masukkan nama scooter yang ingin dihapus datanya:")
    nama_scooter = input("Nama: ")
    #mengecek apakah scooter ada di list
    ada = False
    for scooter in data_scooter:
        if scooter.nama_scooter == nama_scooter:
            ada = True
            break
    if ada:
        #menghapus objek scooter dari list dengan remove
        data_scooter.remove(scooter)
        print(BOLD + RED + "Data scooter berhasil dihapus.")
    else:
        print( BOLD + RED + "Nama tidak ditemukan.")

#gasan mencari data scooter yang ada
def search():
    try:
        print(BOLD + YELLOW + "Masukkan kata kunci untuk mencari data scooter:")
        keyword = input(BOLD + YELLOW + "Kata kunci: ")
        #list kosong gasan menyimpan data scooter yang valdi
        hasil = []
        #perulangan for gasan mencari data scooter yang ada kata kuncinya
        for scooter in data_scooter:
            if keyword.lower() in scooter.__str__().lower():
                hasil.append(scooter)
        #nampilkan data scooter yang ditemukan
        if len(hasil) > 0:
            print(BOLD + RED + "Data scooter yang ditemukan:")
            for scooter in hasil:
                print(scooter)
        else:
            print(BOLD + RED + "Data scooter tidak ditemukan.")
    except KeyboardInterrupt:
        print(BOLD + RED + "Salah Pencet")
    except EOFError:
        print(BOLD + RED + "Salah Pencet")
    except ValueError:
        print()
        print(BOLD + RED + "Salah Pencet")

#menu pilihan CRUD
def menu():
    try:     
        print(BOLD + CYAN + """ 
              NoLimitz MaticShop
              ============================================================= 
              = The Largest Scooter Parts & Accessories Shop In Indonesia =
              = - Jalan Cijagra 14 B-C Bandung                            =
              = - Senin - Sabtu : 08.30 s/d 17.00                         =
              = - Phone: +6285860901990                                   =
              = * linktr.ee/nolimitz.id                                   =  
              =============================================================

              """)
        
        print("+++++++++++++++")
        print("+ 1. Create   +")
        print("+ 2. Read     +")
        print("+ 3. Update   +")
        print("+ 4. Delete   +")
        print("+ 5. Search   +")
        print("+ 0. Exit     +")
        print("+++++++++++++++")
        pilihan = int(input("Masukkan pilihan Anda: "))
        return pilihan
    except KeyboardInterrupt:
        print("============")
        print("Salah Pencet")
        print("============")
    except EOFError:
        print("============")
        print("Salah Pencet")
        print("============")
    except ValueError:
        print("============")
        print("Salah Pencet")
        print("============")

#buat isian yang diatas
try:
    pilihan = menu()
    while pilihan != 0:
        if pilihan == 1:
            create()
        elif pilihan == 2:
            read()
        elif pilihan == 3:
            update()
        elif pilihan == 4:
            delete()
        elif pilihan == 5:
            search()
        else:
            print("====================")
            print("Pilihan tidak valid.")
            print("====================")
        pilihan = menu()
    print("===========================================")
    print("Terima kasih telah berkunjung di toko kami.")
    print("===========================================")
except KeyboardInterrupt:
    print("Salah Pencet")
except EOFError:
    print("============")
    print("Salah Pencet")
    print("============")
except ValueError:
    print("============")
    print("Salah Pencet")
    print("============")
