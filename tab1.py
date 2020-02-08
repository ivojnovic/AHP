tab1 = tk.Frame(tabControl) # Kreiramo tab i stavimo ga u tabkontrole
tabControl.add(tab1, text="Konfiguracija")
tabControl.pack(expand=1, fill="both")

erp_odabir_frame = tk.Frame(tab1)
erp_odabir_frame.place(x=10, y=10)

mylabel = tk.Label(erp_odabir_frame, text = 'Odaberite ERP sustave za metodu (max. 4)', fg='black').pack(anchor=tk.NW) #ili se može napraviti labela, i iudća linija mylabel.pak()
# mybutton = tk.Button(window, text = "Dodaj", command = Dodaj_ERP_U_Listu, bg = 'antiquewhite2', fg='black').place(x=10, y=35)
for a in lista_svih_sustava:
    mycheckbutton = tk.Checkbutton(erp_odabir_frame, text = a.ime, variable = a.ime).pack(anchor=tk.NW)


erp_dodaj_novi = tk.Frame(tab1)
erp_dodaj_novi.place(x=225, y=10)


mylabel = tk.Label(erp_dodaj_novi, text = "Dodaj novi sustav").pack()
