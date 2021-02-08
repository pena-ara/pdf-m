#!/usr/bin/env python

from os import popen as po
from os import chdir as cd
from PyPDF2 import PdfFileMerger as pdfm
print('''
 /$$$$$$$  /$$$$$$$  /$$$$$$$$ /$$      /$$
 | $$__  $$| $$__  $$| $$_____/| $$$    /$$$
 | $$  \ $$| $$  \ $$| $$      | $$$$  /$$$$
 | $$$$$$$/| $$  | $$| $$$$$   | $$ $$/$$ $$
 | $$____/ | $$  | $$| $$__/   | $$  $$$| $$
 | $$      | $$  | $$| $$      | $$\  $ | $$
 | $$      | $$$$$$$/| $$      | $$ \/  | $$
 |__/      |_______/ |__/      |__/     |__/ by Nestero
 Tool sederhana untuk menyatukan file PDF
        ''')
f = input("Dimana File PDF : ")
hm = input("Nama File untuk hasil merge : ")
cd(f)

lpdf = po("ls").read().strip().split("\n")
m = pdfm()

for pdf in lpdf:
    m.append(pdf)

m.write(f"{hm}.pdf")
print(f"Pdf berhasil disatukan, dengan nama {hm}.pdf di folder {f}")
m.close()
