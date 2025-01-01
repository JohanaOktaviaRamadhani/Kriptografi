# -*- coding: utf-8 -*-
"""
Stream Cipher

- Menggunakan keystream generator = XOR kan bilangan ke-1 dan ke-4 dari belakang

"""

# Fungsi untuk membuat keystream
def generate_keystream(initial_key, length):
    # Mulai dengan kunci awal
    keystream = initial_key

    # Tambahkan bit hingga keystream sepanjang plaintext
    while len(keystream) < length:
        # Ambil bit terakhir dan bit ke-4 dari belakang
        bit1 = keystream[-1]
        bit4 = keystream[-4]

        # XOR kedua bit
        xor_result = str(int(bit1) ^ int(bit4))

        # Tambahkan hasil XOR ke keystream
        keystream += xor_result

    # Kembalikan keystream sepanjang plaintext
    return keystream[:length]

# Fungsi untuk mengenkripsi plaintext menggunakan keystream
def encrypt(plaintext, keystream):
    ciphertext = ""  # Inisialisasi ciphertext kosong

    # Lakukan XOR untuk setiap bit plaintext dan keystream
    for p_bit, k_bit in zip(plaintext, keystream):
        ciphertext += str(int(p_bit) ^ int(k_bit))

    return ciphertext  # Kembalikan hasil ciphertext

def main():
    plaintext = input("Masukkan plaintext (Bilangan biner): ")
    initial_key = input("Masukkan kunci awal (harus minimal 4 bit): ")

    # Validasi panjang kunci awal
    if len(initial_key) < 4:
        print("Error: Kunci awal harus memiliki setidaknya 4 bit.")
        return

    # Pastikan input hanya mengandung 0 dan 1
    if not (all(bit in '01' for bit in plaintext) and all(bit in '01' for bit in initial_key)):
        print("Error: Input hanya boleh berisi angka 0 dan 1.")
        return

    # Hasilkan keystream
    keystream = generate_keystream(initial_key, len(plaintext))

    # Lakukan enkripsi
    ciphertext = encrypt(plaintext, keystream)

    # hasil
    print("\n=== Hasil Enkripsi ===")
    print(f"Plaintext : {plaintext}")
    print(f"Keystream : {keystream}")
    print(f"Ciphertext: {ciphertext}")

# Jalankan program
if __name__ == "__main__":
    main()

"""#MODIFIKASI 

Dengan cara :
XOR KAN DENGAN ANGKA 1 PADA BILANGAN KE 8 DARI DEPAN & KELIAPATANNYA

contoh:

hasil chipertext : 11110010 01011100
maka di xor kan  :        1        1
----------------------------------------XOR
Chipertext akhir : 11110011 01011101

"""

print("\n==========STREAM MODIFIKASI XOR 1 DENGAN BILANGAN KE-8 & KELIPATANNYA==========\n")

# Fungsi untuk membuat keystream
def generate_keystream(initial_key, length):
    # Mulai dengan kunci awal
    keystream = initial_key

    # Tambahkan bit hingga keystream sepanjang plaintext
    while len(keystream) < length:
        # Ambil bit terakhir dan bit ke-4 dari belakang
        bit1 = keystream[-1]
        bit4 = keystream[-4]

        # XOR kedua bit
        xor_result = str(int(bit1) ^ int(bit4))

        # Tambahkan hasil XOR ke keystream
        keystream += xor_result

    # Kembalikan keystream sepanjang plaintext
    return keystream[:length]

# Fungsi untuk mengenkripsi plaintext menggunakan keystream
def encrypt(plaintext, keystream):
    ciphertext = ""  # Inisialisasi ciphertext kosong

    # Lakukan XOR untuk setiap bit plaintext dan keystream
    for p_bit, k_bit in zip(plaintext, keystream):
        ciphertext += str(int(p_bit) ^ int(k_bit))

    return ciphertext  # hasil ciphertext

# Fungsi untuk memodifikasi ciphertext dengan XOR pada posisi ke-8 atau kelipatannya
def modify_ciphertext(ciphertext):
    modified_ciphertext = list(ciphertext)  # Ubah ciphertext menjadi list untuk mempermudah modifikasi

    for i in range(7, len(modified_ciphertext), 8):  # Posisi ke-8 atau kelipatannya (indeks mulai dari 0)
        # XOR bit dengan angka 1
        modified_ciphertext[i] = str(int(modified_ciphertext[i]) ^ 1)

    return ''.join(modified_ciphertext)  # Kembalikan ciphertext yang sudah dimodifikasi

def main():
    plaintext = input("Masukkan plaintext (Bilangan biner): ")
    initial_key = input("Masukkan kunci awal (harus minimal 4 bit): ")

    # Validasi panjang kunci awal
    if len(initial_key) < 4:
        print("Error: Kunci awal harus memiliki setidaknya 4 bit.")
        return

    # Pastikan input hanya mengandung 0 dan 1
    if not (all(bit in '01' for bit in plaintext) and all(bit in '01' for bit in initial_key)):
        print("Error: Input hanya boleh berisi angka 0 dan 1.")
        return

    # Hasilkan keystream
    keystream = generate_keystream(initial_key, len(plaintext))

    # Lakukan enkripsi
    ciphertext = encrypt(plaintext, keystream)

    # Modifikasi ciphertext
    modified_ciphertext = modify_ciphertext(ciphertext)

    # Tampilkan hasil
    print("\n=== Hasil Enkripsi ===")
    print(f"Plaintext              : {plaintext}")
    print(f"Keystream             : {keystream}")
    print(f"Ciphertext Awal       : {ciphertext}")
    print(f"Ciphertext Setelah Modif: {modified_ciphertext}")

# Jalankan program
if __name__ == "__main__":
    main()