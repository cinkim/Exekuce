import csv
import tkinter as tk
from tkinter import ttk, StringVar, NORMAL, CENTER
from tkinter import LEFT, NO, DISABLED, NORMAL
import tkinter.messagebox


class exekuce:

    def __init__(self):
        self.zaznamy = []
        self.nazev_soubor = "D:/Python/Projekty_Python/Exekuce/exekuce.csv"
        self.cesta_k_textu = "D:/Python/Projekty_Python/Exekuce/velikost_textu.txt"
        self.velikost_textu = exekuce.velikost_textu(self, self.cesta_k_textu)
        self.hledam_RC = ""
        self.nalezeno = []
        self.odepsat_castku = ""
        self.exekuce_k_odepsani = []
        self.novy_seznam = []

        """
        0       1               2            3           4           5              6           7        8         9        10          11 
        RČ  Datum přijetí   Nabytí moci     ŘSD     č. jednací    Přednostní   Celkový dluh   Č. účtu  Datovka   Email   Doplatit     Poznámka  
        """


    def velikost_textu(self, cesta_k_textu):
        with open(self.cesta_k_textu, mode="r", encoding="utf-8") as velikost:
            self.velikost_textu = velikost.read()
            return self.velikost_textu

            


    def odepis_castku(self, nazev_soubor, odepis_castku, exekuce_k_odepsani):
        chyba = False
        self.zaznamy = []
        with open(self.nazev_soubor, "r", encoding="utf-8") as soubor:
            soubor = csv.reader(soubor, delimiter=";")
            for radka in soubor:
                self.zaznamy.append(radka)
        # print(self.zaznamy)
        k_odepsani_nova = []
        for ii in self.exekuce_k_odepsani:
                a = str(ii)
                k_odepsani_nova.append(a)
        # print(k_odepsani_nova)
        nova_radka = ""
        self.novy_seznam = []
        cislo_prvku = 0
        for seznam in self.zaznamy:
            # print(seznam)
            if seznam == k_odepsani_nova:
                try:
                    castka = float(seznam[10])
                    odepsat = float(self.odepsat_castku)
                    zustatek = str(castka - odepsat)
                    for prvek in seznam:
                        if cislo_prvku < 10:
                            nova_radka = nova_radka + prvek + ";"
                            cislo_prvku += 1
                        elif cislo_prvku == 10:
                            nova_radka = nova_radka + zustatek + ";"
                            cislo_prvku += 1
                        else:
                            nova_radka = nova_radka + prvek
                except ValueError:
                    tk.messagebox.showwarning("Error", "Jako oddělovač pro desetinná čísla použij tečku")
                    chyba = True
                # print(nova_radka)
                self.novy_seznam.append(nova_radka)
                nova_radka = ""
                cislo_prvku = 0
            elif seznam != k_odepsani_nova:
                for prvek in seznam:
                    if cislo_prvku < 10:
                        nova_radka = nova_radka + prvek + ";"
                        cislo_prvku += 1
                    elif cislo_prvku == 10:
                        nova_radka = nova_radka + prvek + ";"
                        cislo_prvku += 1
                    else:
                        nova_radka = nova_radka + prvek
                # print(nova_radka)
                self.novy_seznam.append(nova_radka)
                nova_radka = ""
                cislo_prvku = 0

        # print(self.novy_seznam)
        if chyba == True:
            pass
        else:
            with open(nazev_soubor, "w", encoding="utf-8") as soubor:
                for radka in self.novy_seznam:
                    radka2 = str(radka)
                    radka2 = radka2.replace("[", "").replace("]", "").replace("'","")
                    radka2 = radka2.replace(" ", "")
                    print(radka2, file=soubor)
            self.novy_seznam = []
        

    
    def pridej_zaznam(self, RC, Datum_prijeti, Nabyti_pravni_moci, RSD, cislo_exekuce, prednostni, celkovy_dluh, cislo_uctu, datovka, email, doplatit, poznamka):
        """
        funguje, už bych do toho nesahal
        """
        self.test = ""
        try:
            a = int(RC)
        except ValueError:
            pass
        else:
            tk.messagebox.showwarning("Error", "RČ musí obsahovat oddělovač.")
            return

        for ii in RC:
            try:
                if int(ii):
                    self.test = self.test + ii
                elif ii == "0":
                    self.test = self.test + ii
            except ValueError:
                self.test = self.test + "/"
        RC = self.test
        if poznamka == "":
            poznamka = " "
        self.zaznamy.append((RC, Datum_prijeti, Nabyti_pravni_moci, RSD, cislo_exekuce, prednostni, celkovy_dluh, cislo_uctu, datovka, email, doplatit, poznamka))
        self.uloz(self.nazev_soubor)
    

    def uloz(self, nazev_soubor):
        """
        funguje, už bych do toho nesahal
        """
        with open(self.nazev_soubor, "w", encoding="utf-8") as soubor:
            for RC, Datum_prijeti, Nabyti_pravni_moci, RSD, cislo_exekuce, prednostni, celkovy_dluh, cislo_uctu, datovka, email, doplatit, poznamka in self.zaznamy:
                print(RC + ";"
                     + Datum_prijeti + ";"
                     + Nabyti_pravni_moci + ";" 
                     + RSD + ";"
                     + cislo_exekuce + ";" 
                     + prednostni + ";" 
                     + celkovy_dluh + ";" 
                     + cislo_uctu + ";" 
                     + datovka + ";" 
                     + email + ";" 
                     + doplatit + ";" 
                     + poznamka, file=soubor)

    
    def nacti_soubor(self):
        """
        funguje, už bych do toho nesahal
        """
        try:
            with open(self.nazev_soubor, "r", encoding="utf-8") as soubor:
                soubor = csv.reader(soubor, delimiter=";")
                for radka in soubor:
                    self.zaznamy.append(radka)
        except FileNotFoundError:
            tk.messagebox.showwarning("Error", "Soubor, nebo cesta k souboru nenalezena.\n Nebo se jedná o prvotní použití programu.")
            return


    def smaz(self, index):
        self.zaznamy.pop(index)

    def vyhledat(self, hledam_RC):
        self.opraveny_RC = ""

        try:
            a = int(hledam_RC)
        except ValueError:
            pass
        else:
            tk.messagebox.showwarning("Error", " RČ musí obsahovat oddělovač.\n Načti znovu exekuce a opakuj hledání.")
            return

        for ii in self.hledam_RC:
            try:
                if int(ii):
                    self.opraveny_RC = self.opraveny_RC + ii
                elif ii == "0":
                    self.opraveny_RC = self.opraveny_RC + ii
            except ValueError:
                self.opraveny_RC = self.opraveny_RC + "/"

        for radek in self.zaznamy:
            if self.opraveny_RC == radek[0]:
                self.nalezeno.append(radek)
            else:
                pass
        
        if self.nalezeno == []:
            tk.messagebox.showwarning("Error", "RČ nenalezeno, žádná data k zobrazení.\n Načti znovu exekuce a opakuj hledání.")
        else:
            pass


class exekuceGUI(tk.Frame):

    def __init__(self, parent, exekuce):
        super().__init__(parent)
        self.parent = parent
        self.exekuce = exekuce
        self.parent.title("Správa Exekucí")
        self.entry_width = 30

        self.parent.protocol("WM_DELETE_WINDOW", self.on_close)
        self.create_widgets()


    def create_widgets(self):

        self.frame_nacti = tk.Frame()
        self.frame_nacti.pack()

        self.button_nacti = tk.Button(self.frame_nacti, width=100, text="Načti všechny exekuce", command=self.nacti)
        self.button_nacti.pack(side=LEFT)

        self.frame_mezera = tk.Frame()
        self.frame_mezera.pack()

        self.label_mez = tk.Label(self.frame_mezera, text="   ")
        self.label_mez.pack(side=LEFT)

        # Vyhledat
        self.frame_vyhledat = tk.Frame()
        self.frame_vyhledat.pack()

        self.hledej_RC = StringVar()
        self.entry_hledej_RC = ttk.Entry(self.frame_vyhledat, width=20, textvariable=self.hledej_RC)
        self.entry_hledej_RC.pack(side=LEFT)


        self.button_vyhledat = tk.Button(self.frame_vyhledat, width=30, text="Vyhledat RČ", command=self.vyhledej)
        self.button_vyhledat.pack(side=LEFT)

        self.frame_mezera = tk.Frame()
        self.frame_mezera.pack()

        self.label_mez = tk.Label(self.frame_mezera, text="   ")
        self.label_mez.pack(side=LEFT)

         # Zaplaceno
        self.frame_zaplaceno = tk.Frame()
        self.frame_zaplaceno.pack()

        self.zaplatit = StringVar()
        self.entry_zaplatit = ttk.Entry(self.frame_zaplaceno, width=20, textvariable=self.zaplatit)
        self.entry_zaplatit.pack(side=LEFT)


        self.button_zaplaceno = tk.Button(self.frame_zaplaceno, width=30, text="Odepsat částku", command=self.odepsat)
        self.button_zaplaceno.pack(side=LEFT)

        self.frame_mezera = tk.Frame()
        self.frame_mezera.pack()

        self.label_mez = tk.Label(self.frame_mezera, text="   ")
        self.label_mez.pack(side=LEFT)


        # Pridavani zaznamu
        self.frame_zaznam = tk.Frame()
        self.frame_zaznam.pack()

        self.RC = StringVar()
        self.entry_RC = ttk.Entry(self.frame_zaznam, width=18, textvariable=self.RC)
        self.entry_RC.pack(side=LEFT)


        self.Datum_prijeti = StringVar()
        self.entry_Datum_prijeti = ttk.Entry(self.frame_zaznam, width=13, textvariable=self.Datum_prijeti)
        self.entry_Datum_prijeti.pack(side=LEFT)


        self.Nabyti_pravni_moci = StringVar()
        self.entry_Nabyti_pravni_moci = ttk.Entry(self.frame_zaznam, width=11, textvariable=self.Nabyti_pravni_moci)
        self.entry_Nabyti_pravni_moci.pack(side=LEFT)

        self.RSD = StringVar()
        self.entry_RSD = ttk.Entry(self.frame_zaznam, width=10, textvariable=self.RSD)
        self.entry_RSD.pack(side=LEFT)


        self.cislo_exekuce = StringVar()
        self.entry_cislo_exekuce = ttk.Entry(self.frame_zaznam, width=23, textvariable=self.cislo_exekuce)
        self.entry_cislo_exekuce.pack(side=LEFT)

        self.prednostni = StringVar()
        self.entry_prednostni = ttk.Entry(self.frame_zaznam, width=10, textvariable=self.prednostni)
        self.entry_prednostni.pack(side=LEFT)


        self.celkovy_dluh = StringVar()
        self.entry_celkovy_dluh = ttk.Entry(self.frame_zaznam, width=12, textvariable=self.celkovy_dluh)
        self.entry_celkovy_dluh.pack(side=LEFT)


        self.cislo_uctu = StringVar()
        self.entry_cislo_uctu = ttk.Entry(self.frame_zaznam, width=22, textvariable=self.cislo_uctu)
        self.entry_cislo_uctu.pack(side=LEFT)

        self.datovka = StringVar()
        self.entry_datovka = ttk.Entry(self.frame_zaznam, width=20, textvariable=self.datovka)
        self.entry_datovka.pack(side=LEFT)

        self.email = StringVar()
        self.entry_email = ttk.Entry(self.frame_zaznam, width=25, textvariable=self.email)
        self.entry_email.pack(side=LEFT)

        self.doplatit = StringVar()
        self.entry_doplatit = ttk.Entry(self.frame_zaznam, width=12, textvariable=self.doplatit)
        self.entry_doplatit.pack(side=LEFT)


        self.poznamka = StringVar()
        self.entry_poznamka = ttk.Entry(self.frame_zaznam, width=59, textvariable=self.poznamka)
        self.entry_poznamka.pack(side=LEFT)


        # tlačítko přidat novou exekuci
        self.pridej_button = ttk.Button(self.frame_zaznam, text="Přidat novou exekuci", state=NORMAL, width=19, command=self.on_pridej)
        self.pridej_button.pack(side=LEFT)

        # Seznam zaznamu
        self.frame_seznam = tk.Frame()
        self.frame_seznam.pack()
        style = ttk.Style(self.frame_seznam)
        style.configure("Treeview", rowheight=23, font=(None, exekuce.velikost_textu))
        self.tree_zaznamy = ttk.Treeview(self.frame_seznam, columns=("RC", "Datum přijetí", "Nabytí moci", "ŘSD", "č. jednací", "Přednostní", "Celkový dluh", "Číslo účtu", "Datovka", "Email", "Doplatit", "poznamka"), height=20)

        self.tree_zaznamy.heading("#0", text="#")
        self.tree_zaznamy.column("#0", minwidth=0, width=35, stretch=NO, anchor='w')

        self.tree_zaznamy.heading("RC", text="RČ")
        self.tree_zaznamy.column("RC", minwidth=0, width=77, stretch=NO, anchor='center')

        self.tree_zaznamy.heading("Datum přijetí", text="Datum přijetí")
        self.tree_zaznamy.column("Datum přijetí", minwidth=0, width=83, anchor='center')
        self.tree_zaznamy.pack()

        self.tree_zaznamy.heading("Nabytí moci", text="Nabytí moci")
        self.tree_zaznamy.column("Nabytí moci", minwidth=0, width=74, anchor='center')
        self.tree_zaznamy.pack()

        self.tree_zaznamy.heading("ŘSD", text="ŘSD")
        self.tree_zaznamy.column("ŘSD", minwidth=0, width=65, anchor='center')
        self.tree_zaznamy.pack()

        self.tree_zaznamy.heading("č. jednací", text="č. jednací")
        self.tree_zaznamy.column("č. jednací", minwidth=0, width=145, anchor='center')
        self.tree_zaznamy.pack()

        self.tree_zaznamy.heading("Přednostní", text="Přednostní")
        self.tree_zaznamy.column("Přednostní", minwidth=0, width=66, anchor='center')
        self.tree_zaznamy.pack()

        self.tree_zaznamy.heading("Celkový dluh", text="Celkový dluh")        
        self.tree_zaznamy.column("Celkový dluh", minwidth=0, width=78, anchor='center')
        self.tree_zaznamy.pack()

        self.tree_zaznamy.heading("Číslo účtu", text="Číslo účtu")
        self.tree_zaznamy.column("Číslo účtu", minwidth=0, width=138, anchor='center')
        self.tree_zaznamy.pack()

        self.tree_zaznamy.heading("Datovka", text="Datovka")
        self.tree_zaznamy.column("Datovka", minwidth=0, width=124, anchor='center')
        self.tree_zaznamy.pack()

        self.tree_zaznamy.heading("Email", text="Email")
        self.tree_zaznamy.column("Email", minwidth=0, width=158, anchor='center')
        self.tree_zaznamy.pack()

        self.tree_zaznamy.heading("Doplatit", text="Doplatit")
        self.tree_zaznamy.column("Doplatit", minwidth=0, width=78, anchor='center')
        self.tree_zaznamy.pack()

        self.tree_zaznamy.heading("poznamka", text="Poznámka")
        self.tree_zaznamy.column("poznamka", minwidth=0, width=482, anchor='center')
        self.tree_zaznamy.pack()

        # Tlačítka operací
        self.frame_operace = tk.Frame()
        self.frame_operace.pack()

        self.smaz_button = ttk.Button(self.frame_operace, text="Smazat exekuce", state=NORMAL, command=self.on_smaz)
        self.smaz_button.pack()


    def on_smaz(self):
        if self.tree_zaznamy.focus():
            index = int(self.tree_zaznamy.item(self.tree_zaznamy.focus())["text"])
            self.exekuce.smaz(index)
            self.exekuce.uloz(self.exekuce.nazev_soubor)
            self.zobraz()


    def odepsat(self):
        index = self.tree_zaznamy.item(self.tree_zaznamy.focus())
        self.exekuce.exekuce_k_odepsani = index["values"]
        self.exekuce.odepsat_castku = self.zaplatit.get()
        self.exekuce.odepis_castku(self.exekuce.nazev_soubor, self.exekuce.odepis_castku, self.exekuce.exekuce_k_odepsani) 
        self.exekuce.zaznamy = []
        self.exekuce.nacti_soubor()
        self.zobraz()
        self.zaplatit.set("")
        self.exekuce.exekuce_k_odepsani = []



    def nacti(self):
        if self.exekuce.zaznamy == []:
            self.exekuce.nacti_soubor()
            self.zobraz()
            # print(self.exekuce.zaznamy)



    def vyhledej(self):
        self.exekuce.zaznamy = []
        self.exekuce.nacti_soubor()
        self.exekuce.nalezeno = []
        self.exekuce.hledam_RC = self.hledej_RC.get()
        self.exekuce.vyhledat(self.exekuce.hledam_RC)
        self.zobraz_nalezene()
        self.hledej_RC.set("")

    def on_pridej(self):
        self.exekuce.zaznamy == [] # test
        self.nacti()          
        self.exekuce.pridej_zaznam(
                            self.RC.get(),
                            self.Datum_prijeti.get(),
                            self.Nabyti_pravni_moci.get(),
                            self.RSD.get(),
                            self.cislo_exekuce.get(),
                            self.prednostni.get(),
                            self.celkovy_dluh.get(),
                            self.cislo_uctu.get(),
                            self.datovka.get(),
                            self.email.get(),
                            self.doplatit.get(),
                            self.poznamka.get())

        self.zobraz()
        self.RC.set("")
        self.Datum_prijeti.set("")
        self.Nabyti_pravni_moci.set("")
        self.RSD.set("")
        self.cislo_exekuce.set("")
        self.prednostni.set("")
        self.celkovy_dluh.set("")
        self.cislo_uctu.set("")
        self.datovka.set("")
        self.email.set("")
        self.doplatit.set("")
        self.poznamka.set("")
        self.exekuce.zaznamy = []
        self.exekuce.nacti_soubor()
        self.zobraz()


    
    def on_close(self):
       self.parent.destroy()

    def zobraz(self):

        for ii in self.tree_zaznamy.get_children():
            self.tree_zaznamy.delete(ii)

        pozice = 0
        for zaznam in self.exekuce.zaznamy:
            self.tree_zaznamy.insert("", "end", text=pozice, values=zaznam)
            pozice += 1


    def zobraz_nalezene(self):
        # for ii in self.tree_nalezeno.get_children():
            # self.tree_nalezeno.delete(ii)
        self.exekuce.zaznamy = []
        self.zobraz()
        """
        tady se musí záznamy setřídit podle sloupce ŘSD od nejstaršího
        """
        for zaznam in self.exekuce.nalezeno:
            self.tree_zaznamy.insert("", "end",
                                 text=f"{len(self.tree_zaznamy.get_children())}",
                                 values=zaznam)
    
if __name__ == '__main__':
    root = tk.Tk()
    exekuce = exekuce()
    app = exekuceGUI(root, exekuce)
    app.mainloop()