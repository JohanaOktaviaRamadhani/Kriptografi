# -*- coding: utf-8 -*-
"""Implementasi Vigenere Chiper Standar

ENKRIPSI
*   Apabila kunci tidak sepanjang plaintext, maka kunci akan di loop menyesuaikan kunci yang dimasukkan. 
    contoh: plaintext nya "SEPATU SAYA" kunci "AKU", Maka kunci akan di loop menjadi "AKUAKUAKUA" sebanyak 10 huruf sesuai plaintext
*   Mengubah key dan plaintext ke dalam ASCII, dimulai dengan A=0 dan Z=25
*   Kemudian ditambahkan plaintext + kunci, hasilnya diconvert ke dalam huruf lagi dengan A=0 dan Z=25 juga

RUMUS ENKRIPSI
*   A=0 - Z=25
*   Ciphertext = key + Plaintext
"""

#Vigenère Cipher
def enkripsi(plaintext, key):
    if not key:  # Cek jika kunci kosong
        raise ValueError("Kunci tidak boleh kosong")

    ciphertext = ''
    key_index = 0  # Untuk melacak posisi huruf pada kunci

    for char in plaintext:
        if char.isalpha():  # Proses hanya huruf alfabet
            # Tentukan batasan berdasarkan huruf besar atau kecil
            start = ord('a') if char.islower() else ord('A')

            # Hitung jumlah pergeseran berdasarkan karakter kunci
            shift = ord(key[key_index % len(key)].lower()) - ord('a')

            # Mengenkripsi karakter dengan pergeseran (shift)
            encrypted_char = chr(((ord(char) - start + shift) % 26) + start)

            # Menambahkan karakter yang sudah dienkripsi ke hasil
            ciphertext += encrypted_char

            # Pindah ke karakter berikutnya di kunci
            key_index += 1
        else:
            # Jika bukan huruf, tetap tambahkan karakter asli (seperti spasi, angka, simbol)
            ciphertext += char

    return ciphertext

# Meminta input
plaintext = input("Masukkan plain text: ").lower()
key = input('Masukkan cipher key yang diinginkan: ').lower()

# Validasi jika kunci tidak boleh kosong
if not key:
    print("Kunci tidak boleh kosong, silakan masukkan kunci yang valid.")
else:
    # Hasil
    hasil_enkripsi = enkripsi(plaintext, key)

    # Tampilkan hasil
    print('Cipher text adalah', hasil_enkripsi)

print("\n========================**=====================\n")

"""DEKRIPSI"""
def dekripsi(ciphertext, key):
    if not key:  # Cek jika kunci kosong
        raise ValueError("Kunci tidak boleh kosong")

    plaintext = ''
    key_index = 0  # Untuk melacak posisi huruf pada kunci

    for char in ciphertext:
        if char.isalpha():  # Proses hanya huruf alfabet
            # Tentukan batasan berdasarkan huruf besar atau kecil
            start = ord('a') if char.islower() else ord('A')

            # Hitung jumlah pergeseran berdasarkan karakter kunci
            shift = ord(key[key_index % len(key)].lower()) - ord('a')

            # Mendekripsi karakter dengan pergeseran (shift)
            decrypted_char = chr(((ord(char) - start - shift) % 26) + start)

            # Menambahkan karakter yang sudah didekripsi ke hasil
            plaintext += decrypted_char

            # Pindah ke karakter berikutnya di kunci
            key_index += 1
        else:
            # Jika bukan huruf, tetap tambahkan karakter asli (seperti spasi, angka, simbol)
            plaintext += char

    return plaintext

# Meminta input dari pengguna
ciphertext = input("Masukkan cipher text: ").lower()
key = input('Masukkan cipher key yang digunakan: ').lower()

# Validasi jika kunci tidak boleh kosong
if not key:
    print("Kunci tidak boleh kosong, silakan masukkan kunci yang valid.")
else:
    # proses dekripsi
    hasil_dekripsi = dekripsi(ciphertext, key)

    # Tampilkan hasil
    print('Plain text adalah', hasil_dekripsi)

