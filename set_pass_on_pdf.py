# Создает копию pdf файла защищенную паролем.
#TODO разобраться, почему не работает

from PyPDF2 import PdfFileReader, PdfFileWriter
from getpass import getpass


pdf = PdfFileReader('dict.pdf')
pdf_writer = PdfFileWriter()

for page in range(pdf.numPages):
    pdf_writer.add_page(pdf.pages[page])

password = getpass(prompt='Введите пароль: ')
pdf_writer.encrypt(password)

with open('protected.pdf', 'wb') as file:
    pdf_writer.write(file)



