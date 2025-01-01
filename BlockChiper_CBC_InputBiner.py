# -*- coding: utf-8 -*-
"""CBC Standard dengan Blok 4-bit dan Rotasi Kiri

Args:
        plaintext (str): Input plaintext dalam bentuk biner.
        iv (str): Initialization Vector dalam bentuk biner.
        key (str): Kunci enkripsi dalam bentuk biner.

    Returns:
        list: Daftar blok ciphertext hasil enkripsi.
"""

def left_rotate(bits):
    """
    Melakukan rotasi kiri pada string biner.
    Contoh: '1010' -> '0101'
    """
    return bits[1:] + bits[0]

def xor(bits1, bits2):
    return ''.join('1' if b1 != b2 else '0' for b1, b2 in zip(bits1, bits2))

def encrypt_cbc(plaintext, iv, key):
    block_size = len(key)  # Ukuran blok sama dengan panjang kunci
    ciphertext_blocks = []  # Menyimpan hasil setiap blok ciphertext

    # Memotong plaintext menjadi blok-blok
    blocks = [plaintext[i:i + block_size] for i in range(0, len(plaintext), block_size)]

    current_iv = iv  # IV pertama
    for block in blocks:
        # XOR plaintext dengan IV
        xor_result = xor(block, current_iv)
        # XOR hasil dengan key (enkripsi)
        cipher_block = xor(xor_result, key)
        # Lakukan rotasi kiri pada cipher block
        rotated_cipher_block = left_rotate(cipher_block)
        # Simpan hasil yang sudah dirotasi
        ciphertext_blocks.append(rotated_cipher_block)
        # Update IV untuk blok berikutnya
        current_iv = rotated_cipher_block

    return ciphertext_blocks

# Input dinamis dengan validasi
def get_binary_input(prompt, expected_length=None):
    """
    Meminta input biner dari pengguna dengan validasi.
    """
    while True:
        user_input = input(prompt).strip()
        if all(char in '01' for char in user_input):
            if expected_length and len(user_input) != expected_length:
                print(f"Input harus memiliki panjang {expected_length} bit.")
            else:
                return user_input
        else:
            print("Input harus berupa string biner (hanya terdiri dari '0' dan '1').")

# Main program
print("=== Enkripsi CBC Standar dengan Blok 4-bit ===")
key = get_binary_input("Masukkan key (biner): ")
iv = get_binary_input("Masukkan IV (biner, panjang sesuai kunci): ", expected_length=len(key))
plaintext = get_binary_input("Masukkan plaintext (biner): ")

# Pastikan panjang plaintext adalah kelipatan panjang kunci (padding dengan '0' jika perlu)
block_size = len(key)
if len(plaintext) % block_size != 0:
    padding = block_size - (len(plaintext) % block_size)
    plaintext += '0' * padding  # Padding dengan '0'

# Jalankan algoritma CBC
ciphertext = encrypt_cbc(plaintext, iv, key)

# Menampilkan hasil
print("\nHasil Ciphertext (blok per blok):")
for i, block in enumerate(ciphertext, start=1):
    print(f"Blok {i}: {block}")

print("\nCiphertext Akhir (digabung):")
print(''.join(ciphertext))
