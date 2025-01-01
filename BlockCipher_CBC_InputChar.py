def char_to_binary(char):  # Mengubah Char ke Biner
    return format(ord(char), '08b')

def binary_to_char(binary):  # Mengubah Biner ke Char
    return chr(int(binary, 2))

def left_rotate(bits):  # Melakukan rotasi ke kiri (2 kali)
    times = 2
    times %= len(bits)
    return bits[times:] + bits[:times]

def right_rotate(bits):  # Melakukan rotasi ke kanan (2 kali)
    times = 2
    times %= len(bits)
    return bits[-times:] + bits[:-times]


def xor(bits1, bits2):  # XOR 2 biner yang panjangnya sama
    return ''.join('1' if b1 != b2 else '0' for b1, b2 in zip(bits1, bits2))

def encrypt_cbc(plaintext, iv, key):
    block_size = 8
    ciphertext_blocks = []

    plaintext_binary = ''.join(char_to_binary(char) for char in plaintext)
    iv_binary = char_to_binary(iv)
    key_binary = char_to_binary(key)

    # Padding eksplisit
    padding_length = block_size - (len(plaintext_binary) % block_size)
    plaintext_binary += char_to_binary(chr(padding_length)) * padding_length

    blocks = [plaintext_binary[i:i + block_size] for i in range(0, len(plaintext_binary), block_size)]

    current_iv = iv_binary
    for block in blocks:
        xor_result = xor(block, current_iv)
        cipher_block = xor(xor_result, key_binary)
        rotated_cipher_block = left_rotate(cipher_block)
        ciphertext_blocks.append(rotated_cipher_block)
        current_iv = rotated_cipher_block

    return ''.join(binary_to_char(block) for block in ciphertext_blocks)

# Input dan eksekusi
plaintext = input("Masukkan plaintext (kalimat): ")
iv = input("Masukkan IV (1 karakter): ")
key = input("Masukkan key (1 karakter): ")

ciphertext = encrypt_cbc(plaintext, iv, key)
print("\nHasil Ciphertext:"+ ciphertext)

def decrypt_cbc(ciphertext, iv, key):
    block_size = 8
    plaintext_blocks = []

    ciphertext_binary = [char_to_binary(char) for char in ciphertext]
    iv_binary = char_to_binary(iv)
    key_binary = char_to_binary(key)

    current_iv = iv_binary
    for cipher_block in ciphertext_binary:
        rotated_cipher_block = right_rotate(cipher_block)
        xor_result = xor(rotated_cipher_block, key_binary)
        plaintext_block = xor(xor_result, current_iv)
        plaintext_blocks.append(plaintext_block)
        current_iv = cipher_block

    plaintext_binary = ''.join(plaintext_blocks)

    # Menghapus padding
    padding_length = int(plaintext_binary[-8:], 2)
    plaintext_binary = plaintext_binary[:-padding_length * 8]

    return ''.join(binary_to_char(plaintext_binary[i:i + block_size]) for i in range(0, len(plaintext_binary), block_size))

# Input dan eksekusi
ciphertext = input("Masukkan ciphertext (kalimat): ")
iv = input("Masukkan IV (1 karakter): ")
key = input("Masukkan key (1 karakter): ")

plaintext_decrypted = decrypt_cbc(ciphertext, iv, key)
print("\nHasil Plaintext (setelah dekripsi):")
print(plaintext_decrypted)
