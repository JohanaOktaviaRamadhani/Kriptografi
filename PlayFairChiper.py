# -*- coding: utf-8 -*-
"""Implementation PlayFair Chiper

##ATURAN PLAYFAIR CHIPER
1.   huruf dibagi menjadi beberapa bagian , yang dimana setiap bagian terdiri dari 2 huruf.
Contoh : Sekolah, menjadi : SE KO LA H
2.   Jika kedua huruf sama/ tersisa 1 huruf maka tambahkan huruf "Z" setelah huruf pertama.
Contoh :
Belanja Abu, maka menjadi BE LA NJ AZ AB UZ
3. Membuat matrik 5x5 dari kunci, kemudian di lengkapi dengan alpabet yang belum ada
4. Jika 2 huruf di dalam kolom yang sama maka hasilnya adalah bawahnya
5. Jika 2 huruf di dalam baris yang sama maka hasilnya adalah sebelah kanannya
6. Jika berbeda kolom maupun baris, maka hasilnya adalah perpotongannya (yg berada di sudut yang berlawanan/ yg sekolom)
"""

# PLAYFAIR CIPHERTEXT
def prepare_text(text):
    text = text.replace(" ", "").upper().replace("J", "I")  # Mengganti J menjadi I dalam plaintext
    new_text = ""
    for i in range(0, len(text), 2):  # memasangkan 2 huruf
        if i + 1 < len(text):
            if text[i] == text[i+1]:  # mengecek kalau ada 2 huruf yang sama + Z
                new_text += text[i] + 'Z'
            else:
                new_text += text[i] + text[i+1]
        else:
            new_text += text[i] + 'Z'  # huruf ganjil ditambah Z
    return new_text

# Fungsi untuk menghasilkan matriks 5x5 berdasarkan kunci yang diberikan
def generate_matrix(key):
    key = key.replace(" ", "").upper().replace("J", "I")  # Mengganti J menjadi I dalam key
    matrix = []
    for char in key:  # Memasukkan karakter dari key ke dalam matriks,
        if char not in matrix and 'A' <= char <= 'Z':  # huruf yang masuk harus alfabet
            matrix.append(char)
    for char in range(ord('A'), ord('Z') + 1):
        char_str = chr(char)
        if char_str not in matrix and char_str != 'J':  # Tanpa huruf 'J'
            matrix.append(char_str)

    matrix_grid = [matrix[i:i+5] for i in range(0, 25, 5)]
    return matrix_grid  # membuat grid 5x5

# Fungsi untuk menemukan posisi karakter dalam matriks
def find_char_position(matrix, char):
    for row_index, row in enumerate(matrix):
        if char in row:
            col_index = row.index(char)
            return row_index, col_index
    return None

# Fungsi enkripsi Playfair
def encrypt(plaintext, key):
    matrix = generate_matrix(key)  # Membuat matriks berdasarkan kunci
    plaintext = prepare_text(plaintext)  # Menyiapkan plaintext
    ciphertext = ""

    for i in range(0, len(plaintext), 2):
        char1 = plaintext[i]
        char2 = plaintext[i + 1]

        row1, col1 = find_char_position(matrix, char1)
        row2, col2 = find_char_position(matrix, char2)

        if row1 == row2:  # Jika dalam baris yang sama
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Jika dalam kolom yang sama
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:  # Jika berbeda baris dan kolom (membentuk persegi)
            ciphertext += matrix[row1][col2] + matrix[row2][col1]

    return ciphertext

# Masukkan kata kunci & plaintext
key = input("Masukkan Key: ")
plaintext = input("Masukkan Plaintext: ")

# Tampilkan hasil enkripsi
ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)


"""#DEKRIPSI"""
# Fungsi untuk menghasilkan matriks 5x5 berdasarkan kunci yang diberikan
def generate_matrix(key):
    key = key.replace(" ", "").upper().replace("J", "I")  # Mengganti J menjadi I dalam key
    matrix = []
    for char in key:  # Memasukkan karakter dari key ke dalam matriks
        if char not in matrix and 'A' <= char <= 'Z':  # huruf yang masuk harus alfabet
            matrix.append(char)
    for char in range(ord('A'), ord('Z') + 1):
        char_str = chr(char)
        if char_str not in matrix and char_str != 'J':  # Tanpa huruf 'J'
            matrix.append(char_str)

    matrix_grid = [matrix[i:i+5] for i in range(0, 25, 5)]
    return matrix_grid  # membuat grid 5x5

# Fungsi untuk menemukan posisi karakter dalam matriks
def find_char_position(matrix, char):
    for row_index, row in enumerate(matrix):
        if char in row:
            col_index = row.index(char)
            return row_index, col_index
    return None

# Fungsi dekripsi Playfair
def decrypt(ciphertext, key):
    matrix = generate_matrix(key)  # Membuat matriks berdasarkan kunci
    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        char1 = ciphertext[i]
        char2 = ciphertext[i + 1]

        row1, col1 = find_char_position(matrix, char1)
        row2, col2 = find_char_position(matrix, char2)

        if row1 == row2:  # Jika dalam baris yang sama
            plaintext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Jika dalam kolom yang sama
            plaintext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:  # Jika berbeda baris dan kolom (membentuk persegi)
            plaintext += matrix[row1][col2] + matrix[row2][col1]

    return plaintext

# Masukkan kata kunci & ciphertext
key = input("Masukkan Key: ")
ciphertext = input("Masukkan Ciphertext: ")

# Tampilkan hasil dekripsi
plaintext = decrypt(ciphertext, key)
print("Plaintext:", plaintext)


""" 
Kekurangan code dekrispi di atas :
*   belum bisa memperkirakan kata yang sesuai sehingga huruf masi menyatu
*   huruf z di kata ganjil/ di huruf yang sama masi ada
*   belum bisa memastikan apakah itu benar huruf i atau seharusnya huruf j

"""

