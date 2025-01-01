# -*- coding: utf-8 -*-
"""
Caesar Cipher Implementation
Author: Johana Oktavia Ramadhani

Tugas : Membuat kode enkripsi atau dekripsi menggunakan algoritma Caesar-Chiper dengan bahasa java/Phyton

Contoh plain text :
 Halo, nama saya Johana Oktavia Ramadhani. Saya adalah mahasiswa jurusan Teknik Informatika di Universitas Dian Nuswantoro. Selain belajar di bidang teknologi, saya juga aktif dalam berbagai organisasi seperti HIPMI dan DOSCOM, di mana saya belajar tentang kepemimpinan, manajemen, dan pengembangan bisnis.

##Membuat bilangan
*   string.printable: Mengandung semua karakter yang dapat dicetak, termasuk huruf, angka, spasi, dan karakter khusus.
*   string.ascii_letters: Mengandung semua huruf besar dan kecil, contohnya: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.
*   string.digits: Mengandung semua digit angka, contohnya: '0123456789'
*  string.ascii_uppercase: Mengandung semua huruf besar saja, contohnya: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.
*   string.ascii_lowercase: Mengandung semua huruf kecil saja, contohnya: 'abcdefghijklmnopqrstuvwxyz'
"""

import string
abjad = 'abcdefghijklmnopqrstuvwxyz'
print(abjad)

"""## ENKRIPSI"""

def encode(kalimat, cipher_key):
    kalimat = kalimat.lower()
    hasil_encode = []
    for karakter in kalimat:
        if karakter in abjad:
            index_lama = abjad.index(karakter)
            index_baru = (index_lama + cipher_key) % len(abjad)  # Modulus untuk menangani key besar
            abjad_baru = abjad[index_baru]
            hasil_encode.append(abjad_baru)
        else:
            hasil_encode.append(karakter)
    return ''.join(hasil_encode)

#input plain text
kalimat = input("Masukkan plain text: ")

#input chipher text
key = int(input('Masukkan cipher key yang diinginkan (dalam angka, misal 9): '))

#hasil enkripsi
kalimat_hasil = encode(kalimat, key)
print('Cipher text :', kalimat_hasil)


"""##DEKRIPSI KETIKA SUDAH TAHU KUNCI"""

def decode(kalimat, cipher_key):
    kalimat = kalimat.lower()
    hasil_decode = []
    for karakter in kalimat:
        if karakter in abjad:
            index_lama = abjad.index(karakter)
            index_baru = (index_lama - cipher_key) % len(abjad)  # kuncinya diberi min supaya mundur
            abjad_baru = abjad[index_baru]
            hasil_decode.append(abjad_baru)
        else:
            hasil_decode.append(karakter)
    return ''.join(hasil_decode)

#input cipher text & cipher key
kalimat = input("Masukkan cipher text: ")
key = int(input('Masukkan cipher key yang digunakan saat enkripsi (dalam angka, misal 9): '))

# Dekripsi
kalimat_hasil = decode(kalimat, key)

# Hasil output
print('Hasil dekripsi :', kalimat_hasil)


"""##DEKRIPSI KETIKA BELUM TAHU KUNCI"""

def brute_force_decrypt(kalimat):
    kalimat = kalimat.lower()

    for key in range(len(abjad)):  # Mencoba semua kunci dari 0 sampai 25
        hasil_decode = []

        for karakter in kalimat:
            if karakter in abjad:
                index_lama = abjad.index(karakter)
                index_baru = (index_lama - key) % len(abjad)
                abjad_baru = abjad[index_baru]
                hasil_decode.append(abjad_baru)
            else:
                hasil_decode.append(karakter)

        hasil_dekripsi = ''.join(hasil_decode)
        print(f'Hasil dekripsi dengan key {key}: {hasil_dekripsi}')

# Input dari pengguna
kalimat = input("Masukkan cipher text yang ingin di-decrypt: ")

# Brute force dekripsi
brute_force_decrypt(kalimat)

