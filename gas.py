import os
import multiprocessing

# Fungsi untuk menambahkan 'http://' ke setiap proxy
def convert_proxy(proxy):
    return f"http://{proxy.strip()}"

# Fungsi untuk memproses proxy secara paralel menggunakan multiprocessing
def process_proxies(proxy_chunk):
    return [convert_proxy(proxy) for proxy in proxy_chunk]

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
    # Tentukan ukuran chunk (misalnya, memproses dalam batch 500 proxy per proses)
    chunk_size = 500
    chunks = list(chunkify(proxy_list, chunk_size))

    # Menentukan jumlah worker untuk multiprocessing
    num_workers = multiprocessing.cpu_count()

    # Memulai multiprocessing untuk mengonversi proxy secara paralel
    with multiprocessing.Pool(num_workers) as pool:
        # Memproses chunks proxy secara paralel
        result = pool.map(process_proxies, chunks)

    # Menggabungkan hasil konversi menjadi satu list
    converted_proxies = [proxy for sublist in result for proxy in sublist]

    # Menulis hasil konversi ke file dalam batch besar untuk efisiensi
    with open(output_file, "w") as file:
        file.writelines(f"{proxy}\n" for proxy in converted_proxies)

    print(f"{len(converted_proxies)} proxy telah dikonversi dan disimpan di {output_file}")
