import os

# Fungsi untuk menambahkan 'http://' ke setiap proxy
def convert_proxy(proxy):
    return f"http://{proxy}"

# Menentukan lokasi file output
output_directory = "/storage/emulated/0/HTTP PROXY"
output_file = os.path.join(output_directory, "converted_proxies.txt")

# Memastikan direktori output ada
os.makedirs(output_directory, exist_ok=True)

# Input proxy dari pengguna
proxy_input = input("Masukkan proxy (misalnya 120.18.018.18:8080): ")

# Mengkonversi proxy
converted_proxy = convert_proxy(proxy_input)

# Menyimpan hasilnya ke file
with open(output_file, "a") as file:
    file.write(converted_proxy + "\n")

print(f"Proxy telah dikonversi dan disimpan di {output_file}")