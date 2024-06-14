import numpy as np
from scipy import stats
import statsmodels.api as sm
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Data suhu dari ketiga kota
samarinda = [29, 29.4, 25.3, 28.4, 26.9, 27.9, 28.1, 26.8, 26.8, 29, 27.8, 27.1, 28.3, 27.6, 28, 28.2, 27.7, 27.8, 28.1, 27.9, 27.8, 28, 27.6, 29, 28, 27, 28, 28.4, 30.4]
balikpapan = [29.9, 28.7, 26, 29, 27.5, 28.7, 29.8, 28.6, 27.6, 29.3, 28.7, 26.9, 29.5, 29.5, 29.7, 29.4, 27.9, 29.2, 29.1, 27.6, 28.9, 28.7, 28.1, 29.4, 29.6, 26.6, 26.6, 28.4, 29.9]
jayapura = [30.1, 27.3, 29.5, 30.2, 29.1, 29.8, 30.2, 26.7, 27.9, 25.4, 28.8, 29.9, 30.1, 28.9, 30.3, 30.1, 28.9, 29.5, 30.2, 29.8, 29.5, 30.7, 27.1, 30, 30.2, 28.2, 29.2, 30, 28.7]

# Melakukan uji ANOVA satu arah
f_stat, p_value = stats.f_oneway(samarinda, balikpapan, jayapura)

print("Nilai F-statistik:", f_stat)
print("Nilai p-value:", p_value)

alpha = 0.05
if p_value < alpha:
    print("Terdapat perbedaan yang signifikan antara rata-rata suhu di ketiga kota.")
else:
    print("Tidak terdapat perbedaan yang signifikan antara rata-rata suhu di ketiga kota.")
print("")

# Menggabungkan data dan membuat array untuk kota
data = samarinda + balikpapan + jayapura
kota = ['Samarinda'] * len(samarinda) + ['Balikpapan'] * len(balikpapan) + ['Jayapura'] * len(jayapura)

# Melakukan uji Tukey's HSD
tukey = pairwise_tukeyhsd(endog=data, groups=kota, alpha=0.05)

print(tukey)

