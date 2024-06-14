import numpy as np
from scipy import stats
from scipy.stats import levene

data_samarinda = [2 ,2 ,2 ,3 ,3 ,2 ,3 ,3 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,1 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,1 ,1 ,2 ,2]
data_balikpapan = [1 ,2 ,2 ,2 ,3 ,2 ,2 ,2 ,1 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,1 ,1 ,2 ,1 ,1 ,2 ,1 ,2 ,2 ,2 ,1 ,1 ,1]

mean_samarinda = np.mean(data_samarinda)
mean_balikpapan = np.mean(data_balikpapan)
print("Rata-rata kecepatan angin di Samarinda:", mean_samarinda)
print("Rata-rata kecepatan angin di Balikpapan:", mean_balikpapan)
print("")

# Melakukan uji t (asumsi: data terdistribusi normal dan memiliki varians yang homogen)
t_stat, p_value = stats.ttest_ind(data_samarinda, data_balikpapan)
alpha = 0.05

print("Nilai p-value dari uji t:", p_value)
if p_value < alpha:
    print("Terdapat perbedaan yang signifikan antara rata-rata kecepatan angin di Samarinda dan Balikpapan.")
else:
    print("Tidak terdapat perbedaan yang signifikan antara rata-rata kecepatan angin di Samarinda dan Balikpapan.")
print("")

# Melakukan uji Mann-Whitney U (tidak memerlukan asumsi tentang distribusi data atau homogenitas varians)
u_stat, p_value_mannwhitney = stats.mannwhitneyu(data_samarinda, data_balikpapan)

print("Nilai p-value dari uji Mann-Whitney U:", p_value_mannwhitney)
if p_value_mannwhitney < alpha:
    print("Terdapat perbedaan yang signifikan antara rata-rata kecepatan angin di Samarinda dan Balikpapan.")
else:
    print("Tidak terdapat perbedaan yang signifikan antara rata-rata kecepatan angin di Samarinda dan Balikpapan.")
print("")


# Melakukan uji Levene untuk menguji homogenitas varians
statistic, p_value_levene = levene(data_samarinda, data_balikpapan)
print("Nilai p-value dari uji Levene:", p_value_levene)

if p_value_levene < alpha:
    print("Varians kecepatan angin di kedua kota tidak homogen.")
else:
    print("Varians kecepatan angin di kedua kota homogen.")
