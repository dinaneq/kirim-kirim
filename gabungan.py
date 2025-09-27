import os
from typing import List

def gabungkan_file_teks(
    file_input: List[str], 
    nama_file_gabungan: str = "gabungan_akhir.txt",
    tambahkan_baris_baru: bool = True
) -> None:
    """
    Menggabungkan beberapa file plain teks menjadi satu file keluaran.

    Args:
        file_input: Daftar nama file teks (.txt) yang akan digabungkan.
        nama_file_gabungan: Nama file keluaran (default: "gabungan_akhir.txt").
        tambahkan_baris_baru: Jika True, akan menambahkan baris baru setelah konten 
                              setiap file input (default: True).
    """
    
    print(f"⚙️ Memulai proses penggabungan menjadi: {nama_file_gabungan}")
    
    # Menggunakan 'w' untuk membuat/menimpa file keluaran
    with open(nama_file_gabungan, 'w', encoding='utf-8') as output_file:
        
        file_berhasil = 0
        file_gagal = 0
        
        # Loop melalui setiap nama file yang ada dalam daftar
        for input_file_name in file_input:
            
            # Memeriksa apakah file ada sebelum mencoba membukanya
            if not os.path.exists(input_file_name):
                print(f"❌ Peringatan: File '{input_file_name}' tidak ditemukan dan dilewati.")
                file_gagal += 1
                continue

            try:
                # Membuka file input dalam mode baca ('r')
                # Menggunakan encoding='utf-8' untuk kompatibilitas karakter
                with open(input_file_name, 'r', encoding='utf-8') as input_file:
                    
                    # Membaca seluruh konten file
                    konten = input_file.read()
                    
                    # Menulis konten ke file output
                    output_file.write(konten)
                    
                    # Menambahkan baris baru jika diminta
                    if tambahkan_baris_baru:
                        # Menambahkan dua baris baru untuk pemisah yang lebih jelas
                        output_file.write("\n\n") 
                    
                print(f"✅ Berhasil menggabungkan: {input_file_name}")
                file_berhasil += 1
                
            except Exception as e:
                print(f"⚠️ Terjadi kesalahan saat memproses '{input_file_name}': {e}")
                file_gagal += 1

    print("-" * 30)
    print(f"🎉 Proses Selesai.")
    print(f"  - Total file berhasil digabungkan: {file_berhasil}")
    print(f"  - Total file gagal (tidak ditemukan/error): {file_gagal}")
    print(f"  - File gabungan tersimpan sebagai: {nama_file_gabungan}")

# --- Bagian Utama Skrip ---
if __name__ == "__main__":
    
    # --- Konfigurasi Anda ---
    
    # 1. Daftar file yang akan digabungkan
    daftar_file_saya = [
        "01.txt", 
        "02.txt", 
        "03.txt",       
        "04.txt",
        "05.txt",
        "06.txt", 
        "07.txt", 
        "08.txt",
        "09.txt",
        "10.txt",
        "11.txt", 
        "12.txt", 
        "13.txt",       
        "14.txt",
        "15.txt",
        "16.txt", 
        "17.txt",      
    ]
    
    # 2. Nama untuk file hasil gabungan
    file_output_saya = "database.txt"
    
    # 3. Panggil fungsi untuk memulai penggabungan
    gabungkan_file_teks(
        file_input=daftar_file_saya,
        nama_file_gabungan=file_output_saya,
        tambahkan_baris_baru=True 
    )
