import os
from concurrent.futures import ThreadPoolExecutor

# Fungsi untuk menambahkan 'http://' ke setiap proxy
def convert_proxy(proxy):
    return f"http://{proxy.strip()}"

# Menentukan lokasi file output
output_directory = "/storage/emulated/0/HTTP PROXY"
output_file = os.path.join(output_directory, "converted_proxies.txt")

# Memastikan direktori output ada
os.makedirs(output_directory, exist_ok=True)

# Fungsi untuk membagi input menjadi bagian-bagian lebih kecil
def chunkify(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

# Input proxy dari pengguna (dalam satu string yang dipisahkan oleh baris baru)
proxy_input = input("Masukkan proxy (maksimum 10.000 proxy, pisahkan dengan newline): ")

# Memecah input berdasarkan baris baru untuk mendapatkan daftar proxy
proxy_list = proxy_input.splitlines()

# Pastikan tidak lebih dari 10.000 proxy
if len(proxy_list) > 10000:
    print("Jumlah proxy terlalu banyak! Batasi hingga 10.000 proxy.")
else:
    # Tentukan ukuran chunk (misalnya, memproses dalam batch 200 proxy per proses)
    chunk_size = 200
    chunks = list(chunkify(proxy_list, chunk_size))

    # Menulis hasil konversi ke file dalam buffer besar untuk efisiensi
    with open(output_file, "w") as file:
        with ThreadPoolExecutor() as executor:
            # Memproses chunk secara paralel
            for converted_chunk in executor.map(lambda chunk: [convert_proxy(proxy) for proxy in chunk], chunks):
                # Menulis setiap chunk yang sudah dikonversi
                file.writelines(f"{proxy}\n" for proxy in converted_chunk)

    print(f"{len(proxy_list)} proxy telah dikonversi dan disimpan di {output_file}")
