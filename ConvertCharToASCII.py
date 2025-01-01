# -*- coding: utf-8 -*-
"""TUGAS Char to ASCII """

def char_to_binary(kata):
  binary_representation = ""
  for char in kata:
    ascii_value = ord(char) #mengambil nilai ascii dr kata
    binary_representation += format(ascii_value, '08b') + " "  # Mengubah ASCII ke biner, Format dengan 08b untuk 8 bit
  return binary_representation.strip()

kata = input("Enter a kata: ")
binary_data = char_to_binary(kata)
print(binary_data)  # Menampilkan string representasi biner

def binary_to_char(binary_data):
  binary_values = binary_data.split()  # Memisahkan biner per 8 bit
  kata = ""
  for binary_value in binary_values:
    ascii_value = int(binary_value, 2)  # Mengubah biner ke ASCII
    kata += chr(ascii_value)  # Mengubah ASCII ke karakter
  return kata

binary_data = input("Masukkan representasi biner: ")
kata = binary_to_char(binary_data)
print(kata)  # Menampilkan kata hasil konversi

