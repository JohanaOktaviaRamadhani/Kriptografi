# -*- coding: utf-8 -*-
"""
Pengembangan vigenere
disini sy menggunakan string.priable yang terdiri dari 100 jenis, jadi nanti key %100

CONTOH PLAINTEXT
Saat kamu melihat "6789ABCDEFGHIJKLMNOPQRSTUVWXYZ", jangan hanya terpaku pada angka dan huruf.
Simbol-simbol seperti "@[]^_{|}" mungkin saja menunjukkan arah lain.
Cobalah membaca ulang "fghijklmnopqrstuvwxyz" dan temukan pola tersembunyi di baliknya.
Bisa jadi, tanda seperti "$%^&" adalah petunjuk menuju jawaban yang tersembunyi,
sebuah pesan yang hanya bisa dimengerti oleh mereka yang memahami setiap elemen dari "{|}".

"""

import string

# Mengambil semua karakter yang dapat dicetak
abjad = string.printable
print("Karakter yang dapat dicetak:", abjad)
print("Panjang abjad:", len(abjad))

# Fungsi Enkripsi
def enkripsi(plaintext, key):

    ciphertext = ''  # Inisialisasi ciphertext
    key_len = len(key)

    for i, char in enumerate(plaintext):
        if char in abjad:
            # Temukan indeks karakter di abjad
            char_index = abjad.index(char)
            # Temukan indeks karakter kunci di abjad
            key_index = abjad.index(key[i % key_len])
            # Enkripsi dengan menambahkan indeks dan modulo panjang abjad
            encrypted_index = (char_index + key_index) % len(abjad)
            # Tambahkan karakter terenkripsi ke ciphertext
            ciphertext += abjad[encrypted_index]
        else:
            ciphertext += char  # Biarkan karakter tetap jika tidak ada di abjad

    return ciphertext

# Contoh Penggunaan Enkripsi
plaintext = input("Masukkan plain text: ")  # Input plaintext
key = input('Masukkan cipher key yang diinginkan: ')  # Input kunci

# Menghasilkan ciphertext menggunakan fungsi enkripsi
hasil_enkripsi = enkripsi(plaintext, key) #Perbaikan: Menghapus indentasi yang tidak diharapkan
print('Cipher text adalah:', hasil_enkripsi) #Perbaikan: Menghapus indentasi yang tidak diharapkan


print("\n========================**=====================\n")


# Fungsi Dekripsi
def dekripsi(ciphertext, key):
    plaintext = ''  # Inisialisasi plaintext
    key_len = len(key)

    for i, char in enumerate(ciphertext):
        if char in abjad:
            # Temukan indeks karakter di abjad
            char_index = abjad.index(char)
            # Temukan indeks karakter kunci di abjad
            key_index = abjad.index(key[i % key_len])
            # Dekripsi dengan mengurangi indeks dan modulo panjang abjad
            decrypted_index = (char_index - key_index) % len(abjad)
            # Tambahkan karakter terdekripsi ke plaintext
            plaintext += abjad[decrypted_index]
        else:
            plaintext += char  # Biarkan karakter tetap jika tidak ada di abjad

    return plaintext

# Contoh Penggunaan Dekripsi
ciphertext = input("Masukkan ciphertext: ")  # Input ciphertext
key = input('Masukkan cipher key yang diinginkan: ')  # Input kunci

hasil_dekripsi = dekripsi(ciphertext, key)
print('Plain text hasil dekripsi adalah:', hasil_dekripsi)

