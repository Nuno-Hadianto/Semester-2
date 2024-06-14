data_mahasiswa = [
  {"nama": "Fatur", "nilai": 75},
  {"nama": "Danil", "nilai": 80},
  {"nama": "Andika", "nilai": 85},
  {"nama": "Ilyas", "nilai": 90},
  {"nama": "Rizal", "nilai": 95},
  {"nama": "Ikmal", "nilai": 70},
  {"nama": "Fachi", "nilai": 65},
  {"nama": "Asnan", "nilai": 60},
  {"nama": "Nuno", "nilai": 55},
  {"nama": "Fahrezi", "nilai": 50}
]

def pengurutan_ascending(data_mahasiswa):
  for i in range(len(data_mahasiswa) - 1):
    min_index = i
    for j in range(i + 1, len(data_mahasiswa)):
      if data_mahasiswa[j]["nilai"] < data_mahasiswa[min_index]["nilai"]:
        min_index = j
    data_mahasiswa[i], data_mahasiswa[min_index] = data_mahasiswa[min_index], data_mahasiswa[i]

def pengurutan_descending(data_mahasiswa):
  for i in range(len(data_mahasiswa) - 1):
    max_index = i
    for j in range(i + 1, len(data_mahasiswa)):
      if data_mahasiswa[j]["nilai"] > data_mahasiswa[max_index]["nilai"]:
        max_index = j
    data_mahasiswa[i], data_mahasiswa[max_index] = data_mahasiswa[max_index], data_mahasiswa[i]

pengurutan_ascending(data_mahasiswa)
print("======================================")
print("Hasil data mahasiswa secara ascending:")
print("======================================")
for item in data_mahasiswa:
  print(item["nama"], item["nilai"])

pengurutan_descending(data_mahasiswa)
print("=======================================")
print("Hasil data mahasiswa secara descending:")
print("=======================================")
for item in data_mahasiswa:
  print(item["nama"], item["nilai"])
