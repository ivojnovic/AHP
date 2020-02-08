import tkinter as tk
from tkinter import ttk
import numpy as np
from PIL import ImageTk, Image

class ERP:
    def __init__(self, ime):
        self.ime = ime

lista_svih_sustava = []
lista_svih_kriterija = []
lista_odabranih_sustava = []
odabrani_sustavi = {}
odabrani_kriteriji = {}

odabrani_sustavi_po_kriterijima = {}

filepath = 'popis_sustava.txt'
with open(filepath) as fp:
    line = fp.readline()
    line = line[:-1]
    while line:
        _erp = ERP(line)
        lista_svih_sustava.append(_erp)
        line = fp.readline()
        line = line[:-1]
fp.close()

filepath = 'popis_kriterija.txt'
with open(filepath) as fp:
    line = fp.readline()
    line = line[:-1]
    while line:
        lista_svih_kriterija.append(line)
        line = fp.readline()
        line = line[:-1]
fp.close()

scale_dictionary = {
1: 9,
2: 8,
3: 7,
4: 6,
5: 5,
6: 4,
7: 3,
8: 2,
9: 1,
10: 1/2,
11: 1/3,
12: 1/4,
13: 1/5,
14: 1/6,
15: 1/7,
16: 1/8,
17: 1/9
}
