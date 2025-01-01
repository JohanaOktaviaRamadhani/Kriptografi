# -*- coding: utf-8 -*-
"""Enkripsi dan Dekripsi CBC Standar dengan Input dan Output Karakter"""

import base64

def char_to_binary(char):
    """Mengonversi karakter ke representasi biner 8-bit."""
    return format(ord(char), '08b')

def binary_to_char(binary):
    """Mengonversi string biner 8-bit ke karakter."""
    return chr(int(binary, 2))

def left_rotate(bits):
    """Melakukan rotasi kiri pada string biner."""
    return bits[1:] + bits[0]

def right_rotate(bits):
    """Melakukan rotasi kanan pada string biner."""
    return bits[-1] + bits[:-1]

def xor(bits1, bits2):
    """Melakukan operasi XOR pada dua string biner dengan panjang yang sama."""
    return ''.join('1' if b1 != b2 else '0' for b1, b2 in zip(bits1, bits2))

# ENKRIPSI
def encrypt_cbc(plaintext, iv, key):
    block_size = 4  # Ukuran blok 4 bit
    ciphertext_blocks = []

    # Tambahkan padding menggunakan '\x80' diikuti '\x00'
    padding_length = block_size - (len(plaintext) % block_size)
    plaintext += chr(0x80) + '\x00' * (padding_length - 1)

    # Konversi plaintext menjadi biner
    plaintext_binary = ''.join(char_to_binary(char) for char in plaintext)
    blocks = [plaintext_binary[i:i + block_size] for i in range(0, len(plaintext_binary), block_size)]

    # Konversi IV dan Key ke biner
    iv_binary = char_to_binary(iv)[-block_size:]
    key_binary = char_to_binary(key)[-block_size:]

    current_iv = iv_binary
    for block in blocks:
        xor_result = xor(block, current_iv)
        cipher_block = xor(xor_result, key_binary)
        rotated_cipher_block = left_rotate(cipher_block)
        ciphertext_blocks.append(rotated_cipher_block)
        current_iv = rotated_cipher_block

    ciphertext_binary = ''.join(ciphertext_blocks)
    ciphertext_encoded = base64.b64encode(''.join(binary_to_char(ciphertext_binary[i:i + 8]) for i in range(0, len(ciphertext_binary), 8)).encode()).decode()

    return ciphertext_encoded

# DEKRIPSI
def decrypt_cbc(ciphertext, iv, key):
    block_size = 4  # Ukuran blok 4 bit
    plaintext_blocks = []

    # Decode ciphertext dari Base64
    ciphertext_decoded = base64.b64decode(ciphertext).decode()
    ciphertext_binary = ''.join(char_to_binary(char) for char in ciphertext_decoded)
    blocks = [ciphertext_binary[i:i + block_size] for i in range(0, len(ciphertext_binary), block_size)]

    # Konversi IV dan Key ke biner
    iv_binary = char_to_binary(iv)[-block_size:]
    key_binary = char_to_binary(key)[-block_size:]

    current_iv = iv_binary
    for block in blocks:
        rotated_cipher_block = right_rotate(block)
        xor_result = xor(rotated_cipher_block, key_binary)
        plaintext_block = xor(xor_result, current_iv)
        plaintext_blocks.append(plaintext_block)
        current_iv = block

    plaintext_binary = ''.join(plaintext_blocks)
    plaintext_chars = ''.join(binary_to_char(plaintext_binary[i:i + 8]) for i in range(0, len(plaintext_binary), 8))

    # Hapus padding
    return plaintext_chars.rstrip('\x80').rstrip('\x00')

# Program utama
print("=== Enkripsi dan Dekripsi CBC ===")
mode = input("Pilih mode (enkripsi/dekripsi): ").strip().lower()

if mode == "enkripsi":
    plaintext = input("Masukkan plaintext (string): ")
    iv = input("Masukkan IV (1 karakter): ")
    key = input("Masukkan key (1 karakter): ")

    if len(iv) != 1 or len(key) != 1:
        print("IV dan key harus tepat 1 karakter.")
    else:
        ciphertext = encrypt_cbc(plaintext, iv, key)
        print("\nHasil Ciphertext (string):")
        print(ciphertext)

elif mode == "dekripsi":
    ciphertext = input("Masukkan ciphertext (string): ")
    iv = input("Masukkan IV (1 karakter): ")
    key = input("Masukkan key (1 karakter): ")

    if len(iv) != 1 or len(key) != 1:
        print("IV dan key harus tepat 1 karakter.")
    else:
        decrypted_plaintext = decrypt_cbc(ciphertext, iv, key)
        print("\nHasil Plaintext (setelah dekripsi):")
        print(decrypted_plaintext)

else:
    print("Mode tidak dikenali. Silakan pilih 'enkripsi' atau 'dekripsi'.")
