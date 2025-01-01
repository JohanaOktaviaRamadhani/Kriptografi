
"""
Enkripsi CBC Modifikasi

- input dan output tipe datanya char
- perblok 8 bit
- rotate kiri 2x
- Padding ditambahkan jika panjang plaintext tidak kelipatan 8


"""

def char_to_binary(char): #Mengubah Char ke Biner
    return format(ord(char), '08b')

def binary_to_char(binary): #Mengubah Biner ke Char
    return chr(int(binary, 2))

def left_rotate(bits, times=1): #melakukan rotasi ke kiri
    for _ in range(times):
        bits = bits[1:] + bits[0]
    return bits

def xor(bits1, bits2): #XOR 2 biner yg panjangnya sama
    return ''.join('1' if b1 != b2 else '0' for b1, b2 in zip(bits1, bits2))

def encrypt_cbc(plaintext, iv, key, rotate_times=2):
    block_size = 8  # Ukuran blok 8 bit
    ciphertext_blocks = []  # Menyimpan hasil setiap blok ciphertext

    # Konversi plaintext, IV, dan key ke biner
    plaintext_binary = ''.join(char_to_binary(char) for char in plaintext)
    iv_binary = char_to_binary(iv)
    key_binary = char_to_binary(key)

    # Memotong plaintext menjadi blok-blok 8 bit
    blocks = [plaintext_binary[i:i + block_size] for i in range(0, len(plaintext_binary), block_size)]

    # ADD padding jika panjang plaintext tidak kelipatan 8
    if len(blocks[-1]) < block_size:
        blocks[-1] += '0' * (block_size - len(blocks[-1]))

    current_iv = iv_binary  # IV pertama
    for block in blocks:
        # XOR plaintext dengan IV
        xor_result = xor(block, current_iv)
        # XOR hasil dengan key (enkripsi)
        cipher_block = xor(xor_result, key_binary)
        # Lakukan rotasi kiri pada cipher block
        rotated_cipher_block = left_rotate(cipher_block, times=rotate_times)
        # Simpan hasil yang sudah dirotasi
        ciphertext_blocks.append(rotated_cipher_block)
        # Update IV untuk blok berikutnya
        current_iv = rotated_cipher_block

    # Konversi blok ciphertext ke karakter
    ciphertext_chars = ''.join(binary_to_char(block) for block in ciphertext_blocks)
    return ciphertext_chars

# Input
plaintext = input("Masukkan plaintext (kalimat): ")
iv = input("Masukkan IV (1 karakter): ")
key = input("Masukkan key (1 karakter): ")

# Jalankan algoritma CBC
ciphertext = encrypt_cbc(plaintext, iv, key)

# Tampilkan hasil
print("\nHasil Ciphertext (sebagai karakter):")
print(ciphertext)


print("\n========================**=====================\n")

"""##Dekripsi CBC Modif kating dengan char"""

def char_to_binary(char): #Mengubah Char ke Biner
    return format(ord(char), '08b')

def binary_to_char(binary): #Mengubah Biner ke Char
    return chr(int(binary, 2))

def left_rotate(bits, times=1): #melakukan rotasi ke kiri
    for _ in range(times):
        bits = bits[1:] + bits[0]
    return bits

def right_rotate(bits, times=1): #melakukan rotasi ke kanan
    for _ in range(times):
        bits = bits[-1] + bits[:-1]
    return bits


def xor(bits1, bits2): #XOR 2 biner yg panjangnya sama
    return ''.join('1' if b1 != b2 else '0' for b1, b2 in zip(bits1, bits2))

def decrypt_cbc(ciphertext, iv, key, rotate_times=2):
    block_size = 8  # Ukuran blok 8 bit
    plaintext_blocks = []  # Menyimpan hasil setiap blok plaintext

    # Konversi ciphertext, IV, dan key ke bentuk biner
    ciphertext_binary = [char_to_binary(char) for char in ciphertext]
    iv_binary = char_to_binary(iv)
    key_binary = char_to_binary(key)

    current_iv = iv_binary  # IV pertama
    for cipher_block in ciphertext_binary:
        # Rotasi kanan pada cipher block
        rotated_cipher_block = right_rotate(cipher_block, times=rotate_times)
        # XOR hasil dengan key (dekripsi)
        xor_result = xor(rotated_cipher_block, key_binary)
        # XOR hasil dengan IV untuk mendapatkan plaintext asli
        plaintext_block = xor(xor_result, current_iv)
        # Simpan hasil plaintext blok
        plaintext_blocks.append(plaintext_block)
        # Update IV untuk blok berikutnya
        current_iv = cipher_block

    # Konversi blok plaintext ke karakter
    plaintext_chars = ''.join(binary_to_char(block) for block in plaintext_blocks)
    return plaintext_chars

# Input dinamis
ciphertext = input("Masukkan ciphertext (string): ")
iv = input("Masukkan IV (1 karakter): ")
key = input("Masukkan key (1 karakter): ")

# Jalankan algoritma Dekripsi CBC
plaintext = decrypt_cbc(ciphertext, iv, key)

# Tampilkan hasil
print("\nHasil Plaintext (setelah dekripsi):")
print(plaintext)
