import csv

import tkinter as tk
from tkinter import ttk, StringVar
from tkinter import LEFT, NO, DISABLED, NORMAL
import tkinter.messagebox


class exekuce:

    def __init__(self):
        self.zaznamy = []
        self.nazev_soubor = "D:/Python/Projekty_Python/Exekuce/exekuce.csv"
        self.hledam_RC = ""
        self.nalezeno = []

    
    def pridej_zaznam(self, RC, Datum_prijeti, Nabyti_pravni_moci, cislo_exekuce, prednostni, celkovy_dluh, cislo_uctu, datovka, email, doplatit, poznamka):
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
        self.zaznamy.append((RC, Datum_prijeti, Nabyti_pravni_moci, cislo_exekuce, prednostni, celkovy_dluh, cislo_uctu, datovka, email, doplatit, poznamka))
        self.uloz(self.nazev_soubor)
    

    def uloz(self, nazev_soubor):
        """
        funguje, už bych do toho nesahal
        """
        with open(self.nazev_soubor, "w", encoding="utf-8") as soubor:
            for RC, Datum_prijeti, Nabyti_pravni_moci, cislo_exekuce, prednostni, celkovy_dluh, cislo_uctu, datovka, email, doplatit, poznamka in self.zaznamy:
                print(RC + ";"
                     + Datum_prijeti + ";"
                     + Nabyti_pravni_moci + ";" 
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
            tk.messagebox.showwarning("Error", "Soubor, nebo cesta k souboru nenalezena.")
            return


    def smaz(self, index):
        self.zaznamy.pop(index)

    def vyhledat(self, hledam_RC):
        self.opraveny_RC = ""

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
            tk.messagebox.showwarning("Error", "RČ nenalezeno, žádná data k zobrazení.")
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


        # Pridavani zaznamu
        self.frame_zaznam = tk.Frame()
        self.frame_zaznam.pack()

        self.RC = StringVar()
        self.entry_RC = ttk.Entry(self.frame_zaznam, width=20, textvariable=self.RC)
        self.entry_RC.pack(side=LEFT)


        self.Datum_prijeti = StringVar()
        self.entry_Datum_prijeti = ttk.Entry(self.frame_zaznam, width=20, textvariable=self.Datum_prijeti)
        self.entry_Datum_prijeti.pack(side=LEFT)


        self.Nabyti_pravni_moci = StringVar()
        self.entry_Nabyti_pravni_moci = ttk.Entry(self.frame_zaznam, width=20, textvariable=self.Nabyti_pravni_moci)
        self.entry_Nabyti_pravni_moci.pack(side=LEFT)


        self.cislo_exekuce = StringVar()
        self.entry_cislo_exekuce = ttk.Entry(self.frame_zaznam, width=20, textvariable=self.cislo_exekuce)
        self.entry_cislo_exekuce.pack(side=LEFT)

        self.prednostni = StringVar()
        self.entry_prednostni = ttk.Entry(self.frame_zaznam, width=12, textvariable=self.prednostni)
        self.entry_prednostni.pack(side=LEFT)


        self.celkovy_dluh = StringVar()
        self.entry_celkovy_dluh = ttk.Entry(self.frame_zaznam, width=20, textvariable=self.celkovy_dluh)
        self.entry_celkovy_dluh.pack(side=LEFT)


        self.cislo_uctu = StringVar()
        self.entry_cislo_uctu = ttk.Entry(self.frame_zaznam, width=20, textvariable=self.cislo_uctu)
        self.entry_cislo_uctu.pack(side=LEFT)

        self.datovka = StringVar()
        self.entry_datovka = ttk.Entry(self.frame_zaznam, width=20, textvariable=self.datovka)
        self.entry_datovka.pack(side=LEFT)

        self.email = StringVar()
        self.entry_email = ttk.Entry(self.frame_zaznam, width=20, textvariable=self.email)
        self.entry_email.pack(side=LEFT)

        self.doplatit = StringVar()
        self.entry_doplatit = ttk.Entry(self.frame_zaznam, width=20, textvariable=self.doplatit)
        self.entry_doplatit.pack(side=LEFT)


        self.poznamka = StringVar()
        self.entry_poznamka = ttk.Entry(self.frame_zaznam, width=40, textvariable=self.poznamka)
        self.entry_poznamka.pack(side=LEFT)


        # tlačítko přidat novou exekuci
        self.pridej_button = ttk.Button(self.frame_zaznam, text="Přidat novou exekuci", state=NORMAL, width=20, command=self.on_pridej)
        self.pridej_button.pack(side=LEFT)

        # Seznam zaznamu
        self.frame_seznam = tk.Frame()
        self.frame_seznam.pack()
        self.tree_zaznamy = ttk.Treeview(self.frame_seznam, columns=("RC", "Datum přijetí", "Nabytí právní moci", "Číslo exekuce", "Přednostní", "Celkový dluh", "Číslo účtu", "Datovka", "Email", "Doplatit", "poznamka"), height=20)

        self.tree_zaznamy.heading("#0", text="#")
        self.tree_zaznamy.column("#0", width=35)

        self.tree_zaznamy.heading("RC", text="RČ")
        self.tree_zaznamy.column("RC", width=88)

        self.tree_zaznamy.heading("Datum přijetí", text="Datum přijetí")
        self.tree_zaznamy.column("Datum přijetí", width=126)
        self.tree_zaznamy.pack()

        self.tree_zaznamy.heading("Nabytí právní moci", text="Nabytí právní moci")
        self.tree_zaznamy.column("Nabytí právní moci", width=126)
        self.tree_zaznamy.pack()

        self.tree_zaznamy.heading("Číslo exekuce", text="Číslo exekuce")
        self.tree_zaznamy.column("Číslo exekuce", width=126)
        self.tree_zaznamy.pack()

        self.tree_zaznamy.heading("Přednostní", text="Přednostní")
        self.tree_zaznamy.column("Přednostní", width=78)
        self.tree_zaznamy.pack()

        self.tree_zaznamy.heading("Celkový dluh", text="Celkový dluh")
        self.tree_zaznamy.column("Celkový dluh", width=126)
        self.tree_zaznamy.pack()

        self.tree_zaznamy.heading("Číslo účtu", text="Číslo účtu")
        self.tree_zaznamy.column("Číslo účtu", width=126)
        self.tree_zaznamy.pack()

        self.tree_zaznamy.heading("Datovka", text="Datovka")
        self.tree_zaznamy.column("Datovka", width=126)
        self.tree_zaznamy.pack()

        self.tree_zaznamy.heading("Email", text="Email")
        self.tree_zaznamy.column("Email", width=126)
        self.tree_zaznamy.pack()

        self.tree_zaznamy.heading("Doplatit", text="Doplatit")
        self.tree_zaznamy.column("Doplatit", width=126)
        self.tree_zaznamy.pack()

        self.tree_zaznamy.heading("poznamka", text="Poznámka")
        self.tree_zaznamy.column("poznamka", width=374)
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



    def nacti(self):
        if self.exekuce.zaznamy == []:
            self.exekuce.nacti_soubor()
            self.zobraz()


    def vyhledej(self):
        self.exekuce.zaznamy = []
        exekuce.nacti_soubor()
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
        for zaznam in self.exekuce.nalezeno:
            self.tree_zaznamy.insert("", "end",
                                 text=f"{len(self.tree_zaznamy.get_children())}",
                                 values=zaznam)
    
if __name__ == '__main__':
    root = tk.Tk()
    exekuce = exekuce()
    app = exekuceGUI(root, exekuce)
    app.mainloop()