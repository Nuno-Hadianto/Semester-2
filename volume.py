import math

def volume_balok(p, l, t):
    return p * l * t

def volume_prisma(a, t, L):
    return 0.5 * a * t * L

def volume_bola(r):
    return 4/3 * math.pi * r**3

pilihan = 0

while pilihan != 4:
    print("Menu:")
    print("1. Menghitung volume balok")
    print("2. Menghitung volume prisma")
    print("3. Menghitung volume bola")
    print("4. Keluar")
    pilihan = int(input("Masukkan pilihan Anda: "))

    if pilihan == 1:
        p = float(input("Masukkan panjang balok: "))
        l = float(input("Masukkan lebar balok: "))
        t = float(input("Masukkan tinggi balok: "))
        print("Volume balok adalah", volume_balok(p, l, t))
        
    elif pilihan == 2:
        a = float(input("Masukkan alas prisma: "))
        t = float(input("Masukkan tinggi prisma: "))
        L = float(input("Masukkan panjang prisma: "))
        print("Volume prisma adalah", volume_prisma(a, t, L))

    elif pilihan == 3:
        r = float(input("Masukkan jari-jari bola: "))
        print("Volume bola adalah", volume_bola(r))

    elif pilihan == 4:
        print("Terima kasih telah menggunakan program ini.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        print("-" * 20)
