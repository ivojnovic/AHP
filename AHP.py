from init import *

def Dodaj_ERP():
    mtext = ment.get()
    filepath = 'popis_sustava.txt'
    fp = open(filepath, 'a')
    fp.write(mtext + '\n')
    lista_svih_sustava.append(ERP(mtext))
    fp.close()
    napuni_checkbox_listu_ERP()
    return

def Dodaj_kriterij():
    mtext = ment1.get()
    filepath = 'popis_kriterija.txt'
    fp = open(filepath, 'a')
    fp.write(mtext + '\n')
    lista_svih_kriterija.append(mtext)
    fp.close()
    napuni_checkbox_listu_kriterija()
    return
def napuni_checkbox_listu_ERP():
    try:
        erp_odabir_frame.destroy()
    except:
        erp_odabir_frame = tk.Frame(tab1)
        # erp_odabir_frame.place(x=10, y=10)
        erp_odabir_frame.grid(row=0,column=0)
        mylabel = tk.Label(erp_odabir_frame, text = 'Odaberite ERP sustave '+ '\n' + 'za metodu (max. 4)', fg='black').pack(anchor=tk.W) #ili se može napraviti labela, i iudća linija mylabel.pak()
        # mybutton = tk.Button(window, text = "Dodaj", command = Dodaj_ERP_U_Listu, bg = 'antiquewhite2', fg='black').place(x=10, y=35)
        i = 0
        for erp in lista_svih_sustava:
            odabrani_sustavi['x' + str(i)] = [tk.IntVar(),i]
            #print(odabrani_sustavi['x' + str(i)][0].get())
            tk.Checkbutton(erp_odabir_frame, text = erp.ime, variable = odabrani_sustavi['x' + str(i)][0]).pack(anchor=tk.W)
            i+=1
    return
def napuni_checkbox_listu_kriterija():
    try:
        kriterij_odabir_frame.destroy()
    except:
        kriterij_odabir_frame = tk.Frame(tab1)
        # erp_odabir_frame.place(x=10, y=10)
        kriterij_odabir_frame.grid(row=0,column=1)
        mylabel1 = tk.Label(kriterij_odabir_frame, text = 'Odaberite kriterije sustava'+ '\n' + 'za metodu (max. 4)').pack(anchor=tk.N)
        i = 0
        for kriterij in lista_svih_kriterija:
            odabrani_kriteriji['y' + str(i)] = [tk.IntVar(),i]
            tk.Checkbutton(kriterij_odabir_frame, text = kriterij, variable = odabrani_kriteriji['y' + str(i)][0]).pack(anchor=tk.NW)
            i+=1
    return
def Dalje_na_izracun():
    l = []
    for k in odabrani_sustavi:
        if(odabrani_sustavi[k][0].get() == 0):
            l.append(odabrani_sustavi[k][1])
    for i in sorted(l, reverse=True):
        del lista_svih_sustava[i]

    l = []
    for k in odabrani_kriteriji:
        if(odabrani_kriteriji[k][0].get() == 0):
            l.append(odabrani_kriteriji[k][1])
    for i in sorted(l, reverse=True):
        del lista_svih_kriterija[i]

    prozor_za_izracun()

def prozor_za_izracun():
    top = tk.Toplevel()
    top.title("Odabir preferenci")
    top.geometry('800x800')
    n = len(lista_svih_sustava)
    m = len(lista_svih_kriterija)
    odabrani_sustavi.clear() #Spremanje najznacajnijeg kriterija
    odabrani_kriteriji.clear()

    # Kriteriji
    tk.Label(top, text='Odabir najznačajnijeg' + '\n' +'kriterija', fg='darkorchid4', anchor=tk.W).grid(row=1, column=0)
    row = 2
    for i in range (m):
        for j in range(i+1, m):
            tk.Label(top, text=lista_svih_kriterija[i]).grid(row=row, column=0)
            s = tk.Scale(top, orient=tk.HORIZONTAL, from_=1, to=17, showvalue=0)
            s.grid(row=row,column=1)
            odabrani_sustavi[str(i) + str(j)] = s
            tk.Label(top, text=lista_svih_kriterija[j]).grid(row=row, column=2)
            row+=1

    # ERP po Kriterijima
    row+=1
    tk.Label(top, text='Odabir ERP po kriterijima', fg='darkorchid4', anchor=tk.W).grid(row=row, column=0)
    row+=1
    for b in range(len(lista_svih_kriterija)):
        te = 'Odabir ERP po \n' + lista_svih_kriterija[b] + '\n kriteriju'
        tk.Label(top, text=te, fg='red', anchor=tk.E).grid(row=row, column=0)
        row+=1
        for i in range (n):
            for j in range(i+1, n):
                tk.Label(top, text=lista_svih_sustava[i].ime, anchor=tk.W).grid(row=row, column=0)
                s = tk.Scale(top, orient=tk.HORIZONTAL, from_=1, to=17, showvalue=0)
                s.grid(row=row,column=1)
                if (lista_svih_kriterija[b] in odabrani_sustavi_po_kriterijima):
                    odabrani_sustavi_po_kriterijima[lista_svih_kriterija[b]].append((s, str(i) + str(j)))
                else:
                    odabrani_sustavi_po_kriterijima[lista_svih_kriterija[b]] = []
                    odabrani_sustavi_po_kriterijima[lista_svih_kriterija[b]].append((s, str(i) + str(j)))
                tk.Label(top, text=lista_svih_sustava[j].ime, anchor=tk.W).grid(row=row, column=2)
                row+=1


    tk.Button(top, text="izračunaj", command=Konacni_izracun).grid(row=row, column=5, pady=20)
    global labelarezultat
    labelarezultat = tk.StringVar()
    row+=1
    rez_labela = tk.Label(top, textvariable=labelarezultat, fg='red', anchor=tk.E, font=("Courier", 18))
    rez_labela.grid(row=row, column=5)

def Konacni_izracun():

    n = len(lista_svih_sustava)
    m = len(lista_svih_kriterija)
    matrica_kriterija = np.zeros( (m,m))
    matrica_ERP = np.zeros( (n,n) )
    for i in range(n):
        for j in range(n):
            if i==j:
                matrica_ERP[i][j] = 1
    for i in range(m):
        for j in range(m):
            if i==j:
                matrica_kriterija[i][j] = 1
# Po kriterijima
    for key, value in odabrani_sustavi_po_kriterijima.items():
        odabrani_kriteriji[key] = matrica_ERP
        for a in value:
            x = int(a[1][0])
            y = int(a[1][1])
            z = (scale_dictionary[a[0].get()])
            odabrani_kriteriji[key][x][y] = z
            odabrani_kriteriji[key][y][x] = 1/z
        eigenvector = izracun_vektora_prioriteta (odabrani_kriteriji[key])
        odabrani_kriteriji[key] = eigenvector
    print(odabrani_kriteriji)
    vektor_prioriteta_alternativa = []
    for _, alternative in odabrani_kriteriji.items():
        if (len(vektor_prioriteta_alternativa)==0):
            vektor_prioriteta_alternativa = alternative
        else:
            vektor_prioriteta_alternativa = np.vstack((vektor_prioriteta_alternativa, alternative))
    vektor_prioriteta_alternativa = np.transpose(vektor_prioriteta_alternativa)
# Izracun najznacajnijeg kriterija
    for key, value in odabrani_sustavi:
        b = scale_dictionary[odabrani_sustavi[key+value].get()]
        matrica_kriterija[int(key)][int(value)] = b
        matrica_kriterija[int(value)][int(key)] = 1/b
    eigenvector = izracun_vektora_prioriteta(matrica_kriterija)
    # max_krit_index = np.argmax(eigenvector)
    # najznacajniji_kriterij = lista_svih_kriterija[max_krit_index]
    # for alternative in najznacajniji_kriterij.items():
    #     print(alternative)

    konacan_vektor = np.dot(vektor_prioriteta_alternativa, eigenvector)
    print (konacan_vektor)
    max_index = np.argmax(konacan_vektor)
    rezultat = lista_svih_sustava[max_index].ime
    labelarezultat.set("Najbolja alternativa je: \n" + rezultat)

def izracun_vektora_prioriteta(matrica_ERP):
    korak2_ERP = np.dot(matrica_ERP, matrica_ERP)
    zbroj_redova_matrice_ERP = korak2_ERP.sum(axis=1)
    total_zbroj_redova_matrice_ERP = zbroj_redova_matrice_ERP.sum()
    eigenvector1 = np.divide(zbroj_redova_matrice_ERP, total_zbroj_redova_matrice_ERP)
    korak3_ERP = np.dot(korak2_ERP, korak2_ERP)
    zbroj_redova_matrice_ERP_3_korak = korak3_ERP.sum(axis=1)
    total_zbroj_redova_matrice_ERP_2 = zbroj_redova_matrice_ERP_3_korak.sum()
    eigenvector2 = np. divide(zbroj_redova_matrice_ERP_3_korak, total_zbroj_redova_matrice_ERP_2)
    return (eigenvector2)

window = tk.Tk() #Instanca, full prozor
window.title("AHP metoda za biranje ERP sustava")
tabControl = ttk.Notebook(window) #Kreiramo tabkontrole
window.geometry('450x450')
window.configure(background="black")

tab1 = tk.Frame(tabControl) # Kreiramo tab i stavimo ga u tabkontrole
tab2 = tk.Frame(tabControl, bg = 'antiquewhite2') # Kreiramo tab i stavimo ga u tabkontrole

tabControl.add(tab1, text="Konfiguracija")
tabControl.pack(expand=1, fill="both")
tabControl.add(tab2, text="Određivanje najznačajnijeg kriterija", state="hidden")
tabControl.pack(expand=1, fill="both")

#####################################################Tab 1##################################

#############Lijevo ####################
napuni_checkbox_listu_ERP()
erp_dodaj_novi = tk.Frame(tab1)
erp_dodaj_novi.grid(row=1,column=0, padx=5)
ment = tk.StringVar()
mylabel = tk.Label(erp_dodaj_novi, text = "Dodaj novi sustav",fg='black').pack(anchor=tk.W)
dodaj_novi_erp = tk.Entry(erp_dodaj_novi,textvariable = ment, bg = 'antiquewhite2').pack(anchor=tk.W)
botun_dodaj_novi_sustav = tk.Button(erp_dodaj_novi, text="Dodaj", command=Dodaj_ERP).pack(anchor=tk.W)

############Desno #####################
napuni_checkbox_listu_kriterija()
kriterij_dodaj_novi = tk.Frame(tab1)
kriterij_dodaj_novi.grid(row=1,column=1, padx=5)
ment1 = tk.StringVar()
mylabel = tk.Label(kriterij_dodaj_novi, text = "Dodaj novi kriterij",fg='black').pack(anchor=tk.E)
dodaj_novi_kriterij = tk.Entry(kriterij_dodaj_novi,textvariable = ment1, bg = 'antiquewhite2').pack(anchor=tk.E)
botun_dodaj_novi_kriterij = tk.Button(kriterij_dodaj_novi, text="Dodaj", command=Dodaj_kriterij).pack(anchor=tk.E)

#########Botun za izračun#########
frame_za_izracun = tk.Frame(tab1)
frame_za_izracun.grid(row=2,column=3)

botun_za_izracun = tk.Button(frame_za_izracun, text="Spremi postavke-->", bg="RoyalBlue", height=2, width=15, command=Dalje_na_izracun).pack()

##############################################################Tab2##############################################################


###########Novi prozor################



window.mainloop()
