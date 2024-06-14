import numpy as np
import scipy.stats as stats

# Data
curah_hujan = [0.5 ,15.5 ,20.1 ,12 ,1 ,11.1 ,10.5 ,84 ,3.3 ,3.6 ,19.6 ,12 ,1.4 ,0.4 ,29.7 ,0 ,8 ,1 ,0.8 ,1.5 ,1.9]
kelembapan_udara = [85 ,89 ,83 ,82 ,86 ,82 ,83 ,94 ,89 ,97 ,88 ,83 ,82 ,88 ,84 ,83 ,87 ,84 ,84 ,84 ,85 ,82 ,94 ,83 ,84 ,90 ,86 ,83 ,87 ,84 ,84]

# Remove invalid data points (8888)
valid_indices = [i for i, x in enumerate(curah_hujan) if x != 8888]
curah_hujan_valid = [curah_hujan[i] for i in valid_indices]
kelembapan_udara_valid = [kelembapan_udara[i] for i in valid_indices]

# Calculate Pearson correlation
correlation, p_value = stats.pearsonr(curah_hujan_valid, kelembapan_udara_valid)

print("Koefisien Korelasi Pearson:", correlation)
print("Nilai p:", p_value)
