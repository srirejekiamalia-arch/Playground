import os

def cari_folder(root, nama):
    hasil = []
    
    for root, dirs, files in os.walk(root):
        if nama in dirs:
            path_ditemukan = os.path.join(root, nama)
            hasil.append(path_ditemukan)
    
    return hasil


# ==== PEMAKAIAN ====
root = "C://"  # ganti sesuai kebutuhan
nama = "Downloads"  # nama folder yang dicari

ditemukan = cari_folder(root, nama)

if ditemukan:
    print("Folder ditemukan:")
    for d in ditemukan:
        print(d)
else:
    print("Folder tidak ditemukan")