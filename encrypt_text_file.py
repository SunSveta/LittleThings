#шифрует файлы с текстом симметричным алгоритмом блочного шифрования Aes

import pyAesCrypt

password = input('Введите пароль для шифрования файла:  ')  #password = qwerty123

#encrypt
# pyAesCrypt.encryptFile('text.txt', 'text.txt.aes', password)

#decrypt
pyAesCrypt.decryptFile('text.txt.aes', 'textout.txt', password)
