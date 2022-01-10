import tkinter as tk
from tkinter import ttk, messagebox
from ConnectionOracle import *


class GUI:
    tabel = ""
    SetConnection()
    cursor = ConnectionDB.connection.cursor()
    dictionar = {}

    def __init__(self, name):
        self.interfata = tk.Tk(className=name)

    def DictionarMedicSectie(self):
        sql = "select * from Medic"
        GUI.cursor.execute(sql)
        for index in GUI.cursor:
            # Creez dictionar k=cod_medic, v=id_sectie
            GUI.dictionar[index[0]] = index[4]

    def Vizualizare(self):
        self.CuratareFereastra()
        # Alegere tabela pentru afisare
        self.l1 = tk.Label(self.interfata, text="Alegeti tabela pe care doriti sa o afisati:")
        self.l1.place(x=50, y=60)
        self.comboBox1 = ttk.Combobox(self.interfata,
                                      values=["Pacient", "Detalii_pacient", "Internari", "Diagnostic", "Sectie",
                                              "Medic"], width=23)
        self.comboBox1.place(x=300, y=60)
        self.comboBox1.current(0)

        # Buton de afisare
        self.afisare_btt = tk.Button(self.interfata, text="Afisare", command=self.ShowTable)
        self.afisare_btt.place(x=470, y=57)

        # Caseta in care afisez
        self.t1 = tk.Text(self.interfata, height=20, width=145)
        self.t1.place(x=50, y=100)

    def ShowTable(self):
        GUI.tabel = self.comboBox1.get()
        print(GUI.tabel)

        # Golesc fereastra de afisare
        self.t1.delete("1.0", "end")
        self.afisare()

    def afisare(self):
        if GUI.tabel == "Pacient":
            sql_afisare = "select * from Pacient order by cod_pacient"
            GUI.cursor.execute(sql_afisare)
            self.t1.insert(tk.END, "cod_pacient\t\t nume\t\t         nr_card_sanatate\n")
            self.t1.insert(tk.END, "-------------------------------------------------------\n")
            for index in GUI.cursor:
                print(index)
                self.t1.insert(tk.END, index[0])
                self.t1.insert(tk.END, "\t\t")
                self.t1.insert(tk.END, index[1])
                self.t1.insert(tk.END, "\t\t\t\t")
                self.t1.insert(tk.END, index[2])
                self.t1.insert(tk.END, "\n")

        if GUI.tabel == "Detalii_pacient":
            sql_afisare = "select * from Detalii_pacient order by pacient_cod_pacient"
            GUI.cursor.execute(sql_afisare)
            self.t1.insert(tk.END, "cod_pacient\t\tCNP\t\t adresa\t\t\t      greutate\t\t     inaltime\n")
            self.t1.insert(tk.END,
                           "---------------------------------------------------------------------------------------\n")
            for index in GUI.cursor:
                print(index)
                self.t1.insert(tk.END, index[0])
                self.t1.insert(tk.END, "\t\t")
                self.t1.insert(tk.END, index[1])
                self.t1.insert(tk.END, "\t\t")
                self.t1.insert(tk.END, index[2])
                self.t1.insert(tk.END, "\t\t\t\t")
                self.t1.insert(tk.END, index[3])
                self.t1.insert(tk.END, "\t\t")
                self.t1.insert(tk.END, index[4])
                self.t1.insert(tk.END, "\n")

        if GUI.tabel == "Internari":
            sql_afisare = "select * from Internari order by id_internari"
            GUI.cursor.execute(sql_afisare)
            self.t1.insert(tk.END,
                           "id_internari\t\tdata_internare\t\t data_externare\t\t\t   gravitate_afectiune\t\t\tdenumire_diagnostic\t\t\t\tcod_pacient\t\t    cod_medic\n")
            self.t1.insert(tk.END,
                           "-----------------------------------------------------------------------------------------------------------------------------------------\n")
            for index in GUI.cursor:
                print(index)
                self.t1.insert(tk.END, index[0])
                self.t1.insert(tk.END, "\t\t")
                self.t1.insert(tk.END, index[1])
                self.t1.insert(tk.END, "\t\t")
                if index[2] is not None:
                    self.t1.insert(tk.END, index[2])
                else:
                    self.t1.insert(tk.END, "Null")
                self.t1.insert(tk.END, "\t\t\t\t")
                self.t1.insert(tk.END, index[3])
                self.t1.insert(tk.END, "\t\t")
                self.t1.insert(tk.END, index[4])
                self.t1.insert(tk.END, "\t\t\t\t\t")
                self.t1.insert(tk.END, index[5])
                self.t1.insert(tk.END, "\t\t")
                self.t1.insert(tk.END, index[6])
                self.t1.insert(tk.END, "\n")

        if GUI.tabel == "Diagnostic":
            sql_afisare = "select * from Diagnostic order by den_diagnostic"
            GUI.cursor.execute(sql_afisare)
            self.t1.insert(tk.END, "den_diagnostic\t\t\torgan_principal_afectat\t\t tip_afectiune\n")
            self.t1.insert(tk.END, "----------------------------------------------------------------------\n")
            for index in GUI.cursor:
                print(index)
                self.t1.insert(tk.END, index[0])
                self.t1.insert(tk.END, "\t\t\t\t")
                self.t1.insert(tk.END, index[1])
                self.t1.insert(tk.END, "\t\t\t")
                if index[2] is not None:
                    self.t1.insert(tk.END, index[2])
                else:
                    self.t1.insert(tk.END, "Null")
                self.t1.insert(tk.END, "\n")

        if GUI.tabel == "Sectie":
            sql_afisare = "select * from Sectie order by id_sectie"
            GUI.cursor.execute(sql_afisare)
            self.t1.insert(tk.END, "id_sectie\t\ttip\t\tnr_paturi\t\tnr_locuri_disponibile\n")
            self.t1.insert(tk.END, "--------------------------------------------------------------------\n")

            for index in GUI.cursor:
                print(index)
                self.t1.insert(tk.END, index[0])
                self.t1.insert(tk.END, "\t\t")
                self.t1.insert(tk.END, index[1])
                self.t1.insert(tk.END, "\t\t")
                self.t1.insert(tk.END, index[2])
                self.t1.insert(tk.END, "\t\t")
                self.t1.insert(tk.END, index[3])
                self.t1.insert(tk.END, "\n")

        if GUI.tabel == "Medic":
            sql_afisare = "select * from Medic order by cod_medic"
            GUI.cursor.execute(sql_afisare)
            self.t1.insert(tk.END, "cod_medic\t\tnume\t\t\tspecializare\t\t\t\tnr_telefon\t\t    id_sectie\n")
            self.t1.insert(tk.END,
                           "------------------------------------------------------------------------------------------------------\n")
            for index in GUI.cursor:
                print(index)
                self.t1.insert(tk.END, index[0])
                self.t1.insert(tk.END, "\t\t")
                self.t1.insert(tk.END, index[1])
                self.t1.insert(tk.END, "\t\t\t")
                self.t1.insert(tk.END, index[2])
                self.t1.insert(tk.END, "\t\t\t\t")
                if index[3] is not None:
                    self.t1.insert(tk.END, index[3])
                else:
                    self.t1.insert(tk.END, "Null")
                self.t1.insert(tk.END, "\t\t\t")
                self.t1.insert(tk.END, index[4])
                self.t1.insert(tk.END, "\n")

    def Adaugare(self):
        self.CuratareFereastra()
        self.l2 = tk.Label(self.interfata, text="Alegeti tabela in care doriti sa inserati:")
        self.l2.place(x=50, y=60)
        self.comboBox2 = ttk.Combobox(self.interfata,
                                      values=["Pacient / Detalii_pacient", "Internari", "Diagnostic", "Sectie",
                                              "Medic"], width=23)
        self.comboBox2.place(x=300, y=60)
        self.comboBox2.current(0)

        self.ok_btt = tk.Button(self.interfata, text="OK", command=self.TabelSelectetPtInserare)
        self.ok_btt.place(x=470, y=57)

    def TabelSelectetPtInserare(self):
        GUI.tabel = self.comboBox2.get()
        print("Ati selectat tabelul " + GUI.tabel)

        if GUI.tabel == "Pacient / Detalii_pacient":
            self.CuratareFereastra()

            # Introducere nume pacient
            self.l3 = tk.Label(self.interfata, text="Introduceti numele pacientului:")
            self.l3.place(x=50, y=150)
            self.e1 = tk.Entry(self.interfata, width="40")
            self.e1.place(x=280, y=150)

            # Introducere numar card sanatate
            self.l4 = tk.Label(self.interfata, text="Introduceti numarul cardului de sanatate:")
            self.l4.place(x=50, y=180)
            self.e2 = tk.Entry(self.interfata, width="15")
            self.e2.place(x=280, y=180)

            # Introducere CNP
            self.l5 = tk.Label(self.interfata, text="Introduceti CNP-ul pacientului:")
            self.l5.place(x=50, y=210)
            self.e3 = tk.Entry(self.interfata, width="30")
            self.e3.place(x=280, y=210)

            # Introducere adresa
            self.l6 = tk.Label(self.interfata, text="Introduceti adresa pacientului:")
            self.l6.place(x=50, y=240)
            self.e4 = tk.Entry(self.interfata, width="40")
            self.e4.place(x=280, y=240)

            # Introducere greutate
            self.l7 = tk.Label(self.interfata, text="Introduceti greutatea pacientului (in kg):")
            self.l7.place(x=50, y=270)
            self.e5 = tk.Entry(self.interfata, width="10")
            self.e5.place(x=280, y=270)

            # Introducere inaltime
            self.l8 = tk.Label(self.interfata, text="Introduceti inaltimea pacientului (in m):")
            self.l8.place(x=50, y=300)
            self.e6 = tk.Entry(self.interfata, width="10")
            self.e6.place(x=280, y=300)

            # Buton InserarePacient
            self.inserare_btt1 = tk.Button(self.interfata, text="INSERARE IN TABELA PACIENT",
                                           command=self.ComandaInserareP)
            self.inserare_btt1.place(x=50, y=350)

            # Buton InserareDetalii_Pacient
            self.inserare_btt2 = tk.Button(self.interfata, text="INSERARE IN TABELA DETALII_PACIENT",
                                           command=self.ComandaInserareD)
            self.inserare_btt2.place(x=50, y=390)

        if GUI.tabel == "Internari":
            self.CuratareFereastra()

            # Introducere Data_internare
            self.l3 = tk.Label(self.interfata, text="Introduceti data internarii:")
            self.l3.place(x=50, y=150)
            self.e1 = tk.Entry(self.interfata, width="30")
            self.e1.place(x=230, y=150)

            # Introducere Gravitate_afectiune
            self.l5 = tk.Label(self.interfata, text="Introduceti gravitatea afectiunii:")
            self.l5.place(x=50, y=210)
            self.e3 = tk.Entry(self.interfata, width="5")
            self.e3.place(x=230, y=210)

            # Introducere Den_Diagnostic
            self.l6 = tk.Label(self.interfata, text="Introduceti denumirea diagnosticului:")
            self.l6.place(x=50, y=240)
            self.e4 = tk.Entry(self.interfata, width="30")
            self.e4.place(x=230, y=240)

            # Introducere Cod_Pacient
            self.l7 = tk.Label(self.interfata, text="Introduceti codul pacientului:")
            self.l7.place(x=50, y=270)
            self.e5 = tk.Entry(self.interfata, width="5")
            self.e5.place(x=230, y=270)

            # Introducere Cod_Medic
            self.l8 = tk.Label(self.interfata, text="Introduceti codul medicului:")
            self.l8.place(x=50, y=300)
            self.e6 = tk.Entry(self.interfata, width="5")
            self.e6.place(x=230, y=300)

            # Buton inserare internari
            self.inserare_btt2 = tk.Button(self.interfata, text="INSERARE IN TABELA INTERNARI",
                                           command=self.ComandaInserareI)
            self.inserare_btt2.place(x=50, y=350)

        if GUI.tabel == "Diagnostic":
            self.CuratareFereastra()

            # Introducere denumire diagnostic
            self.l3 = tk.Label(self.interfata, text="Introduceti denumirea diagnosticului:")
            self.l3.place(x=50, y=150)
            self.e1 = tk.Entry(self.interfata, width="40")
            self.e1.place(x=255, y=150)

            # Introducere organ principal afectat
            self.l4 = tk.Label(self.interfata, text="Introduceti organul principal afectat:")
            self.l4.place(x=50, y=180)
            self.e2 = tk.Entry(self.interfata, width="20")
            self.e2.place(x=255, y=180)

            # Introducere tip afectiune
            self.l5 = tk.Label(self.interfata, text="Introduceti tipul afectiunii:")
            self.l5.place(x=50, y=210)
            self.e3 = tk.Entry(self.interfata, width="20")
            self.e3.place(x=255, y=210)

            # Buton inserare diagnostic
            self.inserare_btt2 = tk.Button(self.interfata, text="INSERARE IN TABELA DIAGNOSTIC",
                                           command=self.ComandaInserareDiag)
            self.inserare_btt2.place(x=50, y=250)

        if GUI.tabel == "Sectie":
            self.CuratareFereastra()

            # Introducere tip sectie
            self.l3 = tk.Label(self.interfata, text="Introduceti tipul sectiei:")
            self.l3.place(x=50, y=150)
            self.e1 = tk.Entry(self.interfata, width="40")
            self.e1.place(x=280, y=150)

            # Introducere numar total paturi
            self.l4 = tk.Label(self.interfata, text="Introduceti numarul de paturi:")
            self.l4.place(x=50, y=180)
            self.e2 = tk.Entry(self.interfata, width="10")
            self.e2.place(x=280, y=180)

            # Introducere numar locuri disponibile
            self.l5 = tk.Label(self.interfata, text="Introduceti numarul de locuri disponibile:")
            self.l5.place(x=50, y=210)
            self.e3 = tk.Entry(self.interfata, width="10")
            self.e3.place(x=280, y=210)

            # Buton inserare sectie
            self.inserare_btt2 = tk.Button(self.interfata, text="INSERARE IN TABELA SECTIE",
                                           command=self.ComandaInserareS)
            self.inserare_btt2.place(x=50, y=250)

        if GUI.tabel == "Medic":
            self.CuratareFereastra()

            # Introducere nume doctor
            self.l3 = tk.Label(self.interfata, text="Introduceti numele:")
            self.l3.place(x=50, y=150)
            self.e1 = tk.Entry(self.interfata, width="40")
            self.e1.place(x=250, y=150)

            # Introducere specializare
            self.l4 = tk.Label(self.interfata, text="Introduceti specializarea:")
            self.l4.place(x=50, y=180)
            self.e2 = tk.Entry(self.interfata, width="30")
            self.e2.place(x=250, y=180)

            # Introducere numar telefon
            self.l5 = tk.Label(self.interfata, text="Introduceti numarul de telefon:")
            self.l5.place(x=50, y=210)
            self.e3 = tk.Entry(self.interfata, width="30")
            self.e3.place(x=250, y=210)

            # Introducere id_sectie
            self.l6 = tk.Label(self.interfata, text="Introduceti id-ul sectiei:")
            self.l6.place(x=50, y=240)
            self.e4 = tk.Entry(self.interfata, width="10")
            self.e4.place(x=250, y=240)

            # Buton inserare medic
            self.inserare_btt2 = tk.Button(self.interfata, text="INSERARE IN TABELA MEDIC",
                                           command=self.ComandaInserareM)
            self.inserare_btt2.place(x=50, y=280)

    # Inserare in tabela PACIENT
    def ComandaInserareP(self):
        nume_pacient = self.e1.get()
        print(nume_pacient)
        nr_card_sanatate = self.e2.get()
        print(nr_card_sanatate)

        # Determin prin program valoarea primary key-ului cod_pacient

        sql_cod_pacient = "select max(cod_pacient) from Pacient"
        GUI.cursor.execute(sql_cod_pacient)
        result = GUI.cursor.fetchall()
        result = result.pop(0)
        if result[0] is not None:
            cod_pacient = result[0] + 1
        else:
            cod_pacient = 1
        print(cod_pacient)

        # Verificam daca nu exista deja un pacient cu acelasi nume
        sql_verificare_nume = "select * from Pacient where upper(nume)=upper(:n)"
        GUI.cursor.execute(sql_verificare_nume, n=nume_pacient)
        result = GUI.cursor.fetchall()
        if len(result):
            messagebox.showinfo('Eroare', 'Exista deja acest nume')

        # Inserare in tabela PACIENT
        sql_inserare1 = "INSERT INTO Pacient VALUES (:c_p, :n_p, :nr_c)"
        mesaj_eroare = 'Date eronate! Introduceti alte date.\n - Asigurati-va ca numele nu contine cifre.\n - Numarul cardului de sanatate trebuie sa fie de tip numeric'
        try:
            GUI.cursor.execute(sql_inserare1, c_p=cod_pacient, n_p=nume_pacient, nr_c=nr_card_sanatate)
        except cx_Oracle.Error:
            messagebox.showinfo('Eroare', mesaj_eroare)

        # ConnectionDB.connection.commit()

    # Inserare in tabela DETALII_PACIENT
    def ComandaInserareD(self):
        CNP = self.e3.get()
        print(CNP)
        adresa = self.e4.get()
        print(adresa)
        greutate = self.e5.get()
        print(greutate)
        inaltime = self.e6.get()
        print(inaltime)

        # Determin prin program valoarea primary key-ului cod_pacient
        sql_cod_pacient = "select max(pacient_cod_pacient) from Detalii_pacient"
        GUI.cursor.execute(sql_cod_pacient)
        result = GUI.cursor.fetchall()
        result = result.pop(0)
        if result[0] is not None:
            cod_pacient = result[0] + 1
        else:
            cod_pacient = 1
        print(cod_pacient)

        sql_inserare2 = "INSERT INTO Detalii_pacient VALUES (:c_p, :cnp, :addr, :g, :i)"
        mesaj_eroare = 'Date eronate! Introduceti alte date.\n - CNP-ul sa nu contina mai mult de 13 caractere si sa fie unic\n - Greutatea sa fie in kg(>2)\n - Inaltimea sa fie in m(>0)'
        try:
            GUI.cursor.execute(sql_inserare2, c_p=cod_pacient, cnp=CNP, addr=adresa, g=greutate, i=inaltime)
        except cx_Oracle.Error:
            messagebox.showinfo('Eroare', mesaj_eroare)

        # ConnectionDB.connection.commit()

    # Inserare in tabela INTERNARI
    def ComandaInserareI(self):
        data_internare = self.e1.get()
        print(data_internare)
        gravitate_afectiune = self.e3.get()
        print(gravitate_afectiune)
        den_diagnostic = self.e4.get()
        print(den_diagnostic)
        cod_pacient = self.e5.get()
        print(cod_pacient)
        cod_medic = self.e6.get()
        print(cod_medic)

        # Determin prin program valoarea primary key-ului internarii
        sql_id_internare = "select max(id_internari) from Internari"
        GUI.cursor.execute(sql_id_internare)
        result = GUI.cursor.fetchall()
        result = result.pop(0)
        if result[0] is not None:
            id_internari = result[0] + 1
        else:
            id_internari = 1
        print(id_internari)

        # Verificam daca pacientul nu este deja internat(data_externare=None)
        sql_pacient = "select data_externare from Internari where pacient_cod_pacient=:cp"
        GUI.cursor.execute(sql_pacient, cp=cod_pacient)
        a = 0
        for i in GUI.cursor:
            if i[0] is None:
                a = 1
        if a == 1:
            messagebox.showinfo('Eroare', "Pacientul pe care doriti sa il internati nu a fost externat inca.")
        else:
            # Update nr_docuri_disponibile din sectii
            sql_verificare_locuri = "select nr_locuri_disponibile from Sectie where id_sectie = (select sectie_id_sectie " \
                                    "from Medic where cod_medic=:id) "
            GUI.cursor.execute(sql_verificare_locuri, id=cod_medic)  # id=GUI.dictionar[int(cod_medic)]
            locuri_disp = 0
            for i in GUI.cursor:
                locuri_disp = i

            print(locuri_disp[0])

            if locuri_disp[0] == 0:
                messagebox.showinfo('Eroare', "Nu mai sunt locuri disponibile pentru sectia acestui medic.")
            else:
                sql_inserare = "INSERT INTO Internari VALUES (:id, :di, :de, :ga, :dd, " \
                               ":cp, :cm) "
                mesaj_eroare = 'Date eronate! Introduceti alte date cu atentie.\n'
                try:
                    GUI.cursor.execute(sql_inserare, id=id_internari, di=data_internare, de=None, ga=gravitate_afectiune,
                                       dd=den_diagnostic, cp=cod_pacient, cm=cod_medic)
                except cx_Oracle.Error:
                    messagebox.showinfo('Eroare', mesaj_eroare)

                print(GUI.dictionar[int(cod_medic)])
                sql_update_s = "UPDATE sectie SET nr_locuri_disponibile = nr_locuri_disponibile - 1 where id_sectie = (" \
                               "select sectie_id_sectie from Medic where cod_medic=:id) "
                GUI.cursor.execute(sql_update_s, id=cod_medic)  # id=GUI.dictionar[int(cod_medic)]

        # ConnectionDB.connection.commit()

    # Inserare in tabela DIAGNOSTIC
    def ComandaInserareDiag(self):
        den_diagnostic = self.e1.get()
        print(den_diagnostic)
        organ_principal_afectat = self.e2.get()
        print(organ_principal_afectat)
        tip_afectiune = self.e3.get()
        print(tip_afectiune)

        # Verificam daca nu exista deja denumirea diagnosticului
        sql_verificare_den = "select * from Diagnostic where upper(den_diagnostic)=upper(:den)"
        GUI.cursor.execute(sql_verificare_den, den=den_diagnostic)
        result = GUI.cursor.fetchall()
        if len(result):
            messagebox.showinfo('Eroare', 'Exista deja un diagnostic cu acelasi nume')

        sql_inserare = "INSERT INTO Diagnostic VALUES (:den, :opa, :tip)"
        mesaj_eroare = 'Date eronate! Introduceti alte date cu atentie.\n'
        try:
            GUI.cursor.execute(sql_inserare, den=den_diagnostic, opa=organ_principal_afectat, tip=tip_afectiune)
        except cx_Oracle.Error:
            messagebox.showinfo('Eroare', mesaj_eroare)

        # ConnectionDB.connection.commit()

    # Inserare in tabela SECTIE
    def ComandaInserareS(self):
        tip = self.e1.get()
        print(tip)
        nr_paturi = self.e2.get()
        print(nr_paturi)
        nr_locuri_disponibile = self.e3.get()
        print(nr_locuri_disponibile)

        # Verificam daca nu exista deja o sectie cu acelasi nume
        sql_verificare_sectie = "select * from Sectie where upper(tip)=upper(:t)"
        GUI.cursor.execute(sql_verificare_sectie, t=tip)
        result = GUI.cursor.fetchall()
        if len(result):
            messagebox.showinfo('Eroare', 'Exista deja aceasta sectie')

        # Determin prin program valoarea primary key-ului sectiei
        sql_id_sectie = "select max(id_sectie) from Sectie"
        GUI.cursor.execute(sql_id_sectie)
        result = GUI.cursor.fetchall()
        result = result.pop(0)
        if result[0] is not None:
            id_sectie = result[0] + 1
        else:
            id_sectie = 1
        print(id_sectie)

        sql_inserare = "INSERT INTO Sectie VALUES (:id, :t, :np, :nld)"
        mesaj_eroare = 'Date eronate! Introduceti alte date cu atentie.\n'
        try:
            GUI.cursor.execute(sql_inserare, id=id_sectie, t=tip, np=nr_paturi, nld=nr_locuri_disponibile)
        except cx_Oracle.Error:
            messagebox.showinfo('Eroare', mesaj_eroare)

        # ConnectionDB.connection.commit()

    # Inserare in tabela MEDIC
    def ComandaInserareM(self):
        nume = self.e1.get()
        print(nume)
        specializare = self.e2.get()
        print(specializare)
        nr_telefon = self.e3.get()
        print(nr_telefon)
        id_sectie = self.e4.get()
        print(id_sectie)

        # Determin prin program valoarea primary key-ului medicului
        sql_id_medic = "select max(cod_medic) from Medic"
        GUI.cursor.execute(sql_id_medic)
        result = GUI.cursor.fetchall()
        result = result.pop(0)
        if result[0] is not None:
            cod_medic = result[0] + 1
        else:
            cod_medic = 1
        print(cod_medic)

        sql_inserare = "INSERT INTO Medic VALUES (:cod, :n, :s, :nt, :i_s)"
        mesaj_eroare = 'Date eronate! Introduceti alte date cu atentie.\n'
        try:
            GUI.cursor.execute(sql_inserare, cod=cod_medic, n=nume, s=specializare, nt=nr_telefon, i_s=id_sectie)
        except cx_Oracle.Error:
            messagebox.showinfo('Eroare', mesaj_eroare)

        # actualizare dictionar
        GUI.dictionar[cod_medic] = int(id_sectie)
        print(GUI.dictionar)
        # ConnectionDB.connection.commit()

    def Actualizeaza(self):
        self.CuratareFereastra()

        self.l3 = tk.Label(self.interfata, text="Actualizare data de externare din tabela Internari",
                           font=("Helvetica", 20))
        self.l3.place(x=50, y=55)
        self.l4 = tk.Label(self.interfata,
                           text="Introduceti id-ul de internare al pacientului caruia doriti sa ii setati data de externare: ")
        self.l4.place(x=50, y=130)
        self.e1 = tk.Entry(self.interfata, width="10")
        self.e1.place(x=500, y=130)
        self.l5 = tk.Label(self.interfata, text="Inserati data de externare: ")
        self.l5.place(x=50, y=160)
        self.e2 = tk.Entry(self.interfata, width="30")
        self.e2.place(x=230, y=160)
        self.update_btt = tk.Button(self.interfata, text="ACTUALIZARE", command=self.ActualizareInternari)
        self.update_btt.place(x=50, y=200)

    def ActualizareInternari(self):
        id_internari = self.e1.get()
        data_externare = self.e2.get()

        sql_internari = "select medic_cod_medic from internari where id_internari= :id_i"
        GUI.cursor.execute(sql_internari, id_i=id_internari)
        doctor = 0
        for i in GUI.cursor:
            doctor = i[0]

        # Verificam daca exista pacientul cu id_internari specificat
        sql_verif1 = "select id_internari from Internari"
        GUI.cursor.execute(sql_verif1)
        ok = 0
        for i in GUI.cursor:
            if int(id_internari) == i[0]:
                ok = 1
                break

        if ok == 0:
            messagebox.showinfo('Atentie!', 'Nu exista acest id.')
        else:
            sql_verif = "select data_externare from Internari where id_internari=:id"
            GUI.cursor.execute(sql_verif, id=id_internari)
            ok = 0
            for i in GUI.cursor:
                print(i[0])
                if i[0] is not None:
                    ok = 1
            if ok == 1:
                messagebox.showinfo('Atentie!', 'Pacientul a fost deja externat.')
            else:
                sql_update = "UPDATE internari SET data_externare = :de where id_internari = :id"
                mesaj_eroare = 'Date eronate! Introduceti alte date cu atentie.\n'
                try:
                    GUI.cursor.execute(sql_update, de=data_externare, id=id_internari)
                except cx_Oracle.Error:
                    messagebox.showinfo('Eroare', mesaj_eroare)

                sql_update_locuri = "UPDATE sectie SET nr_locuri_disponibile = nr_locuri_disponibile + 1 where id_sectie = :id_s"
                GUI.cursor.execute(sql_update_locuri, id_s=GUI.dictionar[int(doctor)])

        # ConnectionDB.connection.commit()

    def Stergere(self):
        self.CuratareFereastra()

        self.l3 = tk.Label(self.interfata, text="Optiuni de stergere a datelor din tabele:", font=("Helvetica", 20))
        self.l3.place(x=50, y=55)

        self.l4 = tk.Label(self.interfata, text=" ----> Stergerea unei internari: ")
        self.l4.place(x=50, y=100)
        self.l5 = tk.Label(self.interfata, text=" Introduceti id-ul de internare: ")
        self.l5.place(x=80, y=130)
        self.e2 = tk.Entry(self.interfata, width="15")
        self.e2.place(x=250, y=130)
        self.delete_btt1 = tk.Button(self.interfata, text="STERGERE", command=self.ComandaStergereInternare)
        self.delete_btt1.place(x=350, y=125)

        self.l6 = tk.Label(self.interfata, text=" ----> Stergerea tuturor medicilor dintr-o anumita sectie: ")
        self.l6.place(x=50, y=250)
        self.l7 = tk.Label(self.interfata, text=" Introduceti id-ul sectiei: ")
        self.l7.place(x=80, y=280)
        self.e3 = tk.Entry(self.interfata, width="15")
        self.e3.place(x=250, y=280)
        self.delete_btt2 = tk.Button(self.interfata, text="STERGERE", command=self.ComandaStergereMedici)
        self.delete_btt2.place(x=350, y=275)

    def ComandaStergereInternare(self):
        id_internari = self.e2.get()

        sql_verif_id = "select id_internari from Internari"
        GUI.cursor.execute(sql_verif_id)
        ok = 0
        for i in GUI.cursor:
            if int(id_internari) == i[0]:
                ok = 1
                break
        if ok == 0:
            messagebox.showinfo('Atentie!', 'Nu exista acest id in tabela Internari.')
        else:
            sql_deleteInternare = "delete from Internari where id_internari=:id"
            GUI.cursor.execute(sql_deleteInternare, id=id_internari)
            print("deleted...")

        # ConnectionDB.connection.commit()

    def ComandaStergereMedici(self):
        id_sectie = self.e3.get()

        sql_verif_id = "select sectie_id_sectie from Medic"
        GUI.cursor.execute(sql_verif_id)
        ok = 0
        for i in GUI.cursor:
            if int(id_sectie) == i[0]:
                ok = 1
                break
        if ok == 0:
            messagebox.showinfo('Atentie!', 'Nu exista acest id in tabela Medic.')
        else:
            sql_deleteInternare = "delete from Medic where sectie_id_sectie=:id"
            try:
                GUI.cursor.execute(sql_deleteInternare, id=id_sectie)
                print("deleted...")
            except cx_Oracle.Error:
                messagebox.showinfo('Eroare',
                                    'Pentru a putea sterge date din tabela Medic trebuie golita tabele Internari')

        # ConnectionDB.connection.commit()

    def Verificare(self):

        self.CuratareFereastra()

        self.l3 = tk.Label(self.interfata, text="Statistica pe ani a pacientilor cu insuficienta cardiaca: ",
                           font=("Helvetica", 20))
        self.l3.place(x=50, y=55)

        sql_statistica1 = "select to_number(to_char(i.data_internare, 'YYYY')), count(*) " \
                          "from pacient p, internari i, diagnostic d where p.cod_pacient = i.pacient_cod_pacient " \
                          "and i.diagnostic_den_diagnostic = d.den_diagnostic and d.den_diagnostic = 'Insuficienta cardiaca' " \
                          "group by to_number(to_char(i.data_internare, 'YYYY'))"
        GUI.cursor.execute(sql_statistica1)

        self.t1 = tk.Text(self.interfata, height=4, width=60)
        self.t1.place(x=50, y=100)

        self.t1.insert(tk.END, "AN\t\t Numar pacienti cu insuficienta cardiaca\n")
        self.t1.insert(tk.END, "-----------------------------------------------------------\n")
        for index in GUI.cursor:
            print(index)
            self.t1.insert(tk.END, index[0])
            self.t1.insert(tk.END, "\t\t\t\t")
            self.t1.insert(tk.END, index[1])
            self.t1.insert(tk.END, "\n")

        self.l4 = tk.Label(self.interfata, text="Cea mai lunga durata de spitalizre pe sectii: ",
                           font=("Helvetica", 20))
        self.l4.place(x=50, y=190)

        sql_statistica2 = "select s.tip, max(i.data_externare-i.data_internare) from sectie s, internari i, medic m " \
                          "where s.id_sectie=m.sectie_id_sectie and m.cod_medic=i.medic_cod_medic group by s.tip"
        GUI.cursor.execute(sql_statistica2)

        self.t2 = tk.Text(self.interfata, height=8, width=40)
        self.t2.place(x=50, y=230)

        self.t2.insert(tk.END, "Tip\t\t Zile de spitalizare\n")
        self.t2.insert(tk.END, "-----------------------------------\n")
        for index in GUI.cursor:
            print(index)
            self.t2.insert(tk.END, index[0])
            self.t2.insert(tk.END, "\t\t\t\t")
            self.t2.insert(tk.END, index[1])
            self.t2.insert(tk.END, "\n")

        self.l5 = tk.Label(self.interfata,
                           text="Pacientii cu grad ridicat de severitate a bolii(>=7) din sectia de ATI si Cardiologie",
                           font=("Helvetica", 20))
        self.l5.place(x=50, y=390)

        sql_statistica3 = "select p.nume, i.gravitate_afectiune, s.tip from pacient p, sectie s, internari i, medic m where " \
                          "p.cod_pacient=i.pacient_cod_pacient and i.medic_cod_medic = m.cod_medic and " \
                          "m.sectie_id_sectie=s.id_sectie and i.gravitate_afectiune>=7 and s.tip in ('ATI', " \
                          "'Cardiologie') "
        GUI.cursor.execute(sql_statistica3)

        self.t3 = tk.Text(self.interfata, height=8, width=80)
        self.t3.place(x=50, y=430)

        self.t3.insert(tk.END, "Nume\t\t\t Gravitate afectiune\t\t\t\t\tSectie\n")
        self.t3.insert(tk.END, "----------------------------------------------------------------------\n")
        for index in GUI.cursor:
            print(index)
            self.t3.insert(tk.END, index[0])
            self.t3.insert(tk.END, "\t\t\t\t")
            self.t3.insert(tk.END, index[1])
            self.t3.insert(tk.END, "\t\t\t")
            self.t3.insert(tk.END, index[2])
            self.t3.insert(tk.END, "\n")

    def CuratareFereastra(self):
        try:
            self.l3.destroy()
        except AttributeError:
            pass
        try:
            self.l4.destroy()
        except AttributeError:
            pass
        try:
            self.l5.destroy()
        except AttributeError:
            pass
        try:
            self.l6.destroy()
        except AttributeError:
            pass
        try:
            self.l7.destroy()
        except AttributeError:
            pass
        try:
            self.l8.destroy()
        except AttributeError:
            pass
        try:
            self.e1.destroy()
        except AttributeError:
            pass
        try:
            self.l4.destroy()
        except AttributeError:
            pass
        try:
            self.e2.destroy()
        except AttributeError:
            pass
        try:
            self.e3.destroy()
        except AttributeError:
            pass
        try:
            self.e4.destroy()
        except AttributeError:
            pass
        try:
            self.e5.destroy()
        except AttributeError:
            pass
        try:
            self.e6.destroy()
        except AttributeError:
            pass
        try:
            self.inserare_btt1.destroy()
        except AttributeError:
            pass
        try:
            self.inserare_btt2.destroy()
        except AttributeError:
            pass
        try:
            self.l1.destroy()
        except AttributeError:
            pass
        try:
            self.t1.destroy()
        except AttributeError:
            pass
        try:
            self.afisare_btt.destroy()
        except AttributeError:
            pass
        try:
            self.comboBox1.destroy()
        except AttributeError:
            pass
        try:
            self.update_btt.destroy()
        except AttributeError:
            pass
        try:
            self.delete_btt1.destroy()
        except AttributeError:
            pass
        try:
            self.delete_btt2.destroy()
        except AttributeError:
            pass
        try:
            self.t1.destroy()
        except AttributeError:
            pass
        try:
            self.t2.destroy()
        except AttributeError:
            pass
        try:
            self.t3.destroy()
        except AttributeError:
            pass

    def EditareFereastra(self):
        self.interfata.geometry("1250x700")

        self.vizualizare_btt = tk.Button(self.interfata, text="Vizualizare date", command=self.Vizualizare)
        self.vizualizare_btt.place(x=50, y=20)

        self.adaugare_btt = tk.Button(self.interfata, text="Adaugare date", command=self.Adaugare)
        self.adaugare_btt.place(x=200, y=20)

        self.actualizare_btt = tk.Button(self.interfata, text="Actualizare date", command=self.Actualizeaza)
        self.actualizare_btt.place(x=350, y=20)

        self.actualizare_btt = tk.Button(self.interfata, text="Stergere date", command=self.Stergere)
        self.actualizare_btt.place(x=500, y=20)

        self.verificari_btt = tk.Button(self.interfata, text="Verificare date", command=self.Verificare)
        self.verificari_btt.place(x=650, y=20)

        self.DictionarMedicSectie()

        self.interfata.mainloop()
