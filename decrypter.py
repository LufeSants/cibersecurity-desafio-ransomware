import os
import pyaes

## Solicitar a chave de criptografia ao usuário
key = input("Insira a chave de criptografia: ").encode()

## Abrir o arquivo criptografado
file_name = "personal_data.txt.encrypted"
with open(file_name, "rb") as file:
    file_data = file.read()

## Chave para descriptografia
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## Remover o arquivo criptografado
os.remove(file_name)

## Criar o arquivo descriptografado
new_file_name  = "personal_data.txt"
with open(new_file_name, "wb") as new_file:
    new_file.write(decrypt_data)

print(f"Arquivo descriptografado e salvo como '{new_file_name}'")