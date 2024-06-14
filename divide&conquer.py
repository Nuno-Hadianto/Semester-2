def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

mahasiswa1 = {'nama': 'Udin', 'angka': [5, 2, 8, 3, 1, 7, 6, 10, 4, 9]}
mahasiswa2 = {'nama': 'Ucok', 'angka': [9, 3, 1, 5, 7, 4, 10, 2, 6, 8]}

semua_angka = mahasiswa1['angka'] + mahasiswa2['angka']

merge_sort(semua_angka)

print("==================================================")
print("Nama Mahasiswa 1:", mahasiswa1['nama'])
print("Angka Mahasiswa 1:", mahasiswa1['angka'])
print("==================================================")
print("Nama Mahasiswa 2:", mahasiswa2['nama'])
print("Angka Mahasiswa 2:", mahasiswa2['angka'])
print("==================================================")
print("===================================================================================================")
print("Angka setelah diurutkan (ascending):", semua_angka)
print("===================================================================================================")
