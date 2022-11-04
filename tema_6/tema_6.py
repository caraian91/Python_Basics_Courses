# 1.Clasa Cerc
# Atribute: raza, culoare
# Constructor pentru ambele atribute
# Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()

class Cerc:
    # ATRIBUTE
    PI = 3.14

    # CONSTRUCTOR
    def __init__(self,raza,culoare):
        self.raza = raza
        self.culoare = culoare
    # METODE
    def descrie_cerc(self):
        print(f"Cercul este de culoarea {self.culoare} si are raza de {self.raza}")

    def aria(self):
        aria_cercului = self.PI * self.raza ** 2
        return aria_cercului

    def diametru(self):
        diam_cerc = 2 * self.raza
        return diam_cerc

    def circumferinta(self):
        circumf_cerc = self.PI * self.diametru()
        return circumf_cerc

cerc1 = Cerc(3,"negru")
cerc1.descrie_cerc()
print("Aria cercului este:",cerc1.aria())
print("Diametrul cercului este:",cerc1.diametru())
print("Circumferinta cercului este:",cerc1.circumferinta())
print('-' * 100)
# --------------------------------------------------------------------------------------------------------
# 2. Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare.
# Puteti verifica schimbarea culorii prin apelarea metodei descrie().
class Dreptunghi:
    # CONSTRUCTOR
    def __init__(self,lungime,latime,culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    # METODE
    def descriere(self):
        print(f"Dreptunghiul are L={self.lungime} si l={self.latime}, iar culoarea este {self.culoare}")

    def aria(self):
        aria_dreptunghi = self.lungime * self.latime
        return aria_dreptunghi

    def perimetrul(self):
        peri_dreptunghi = 2 * (self.lungime + self.latime)
        return peri_dreptunghi

    def schimba_culoarea(self,culoare):
        self.culoare = culoare

drept1 = Dreptunghi(3,4,"verde")
drept1.descriere()
print("Arie:",drept1.aria())
print("Perimetru:",drept1.perimetrul())
drept1.schimba_culoarea("rosu")
drept1.descriere()
print('-' * 100)
# --------------------------------------------------------------------------------------------------------
# 3. Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# ● descrie()
# ● nume_complet()
# ● salariu_lunar()
# ● salariu_anual()
# ● marire_salariu(procent)
class Angajat:
    # CONSTRUCTOR
    def __init__(self,nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salar = salariu
    # METODE
    def descriere(self):
        print(f"Angajat {self.nume} {self.prenume} are salar de {self.salar} lei")

    def nume_complet(self):
        print(f"Numele complet: {self.nume} {self.prenume}")

    def salariu_lunar(self):
        print(f"Salariu lunar este {self.salar} lei")

    def salariu_anual(self):
        salar_anual = self.salar * 12
        return salar_anual

    def marire_salariu(self,procente):
        self.salar = (self.salar * (procente/100)) + self.salar
        print(f"Noul salar este: {self.salar} lei dupa marirea de {procente}% ")

angajat1 = Angajat("Cristian","Popescu",5000)
angajat1.descriere()
angajat1.nume_complet()
angajat1.salariu_lunar()
print("Salariu anual este",angajat1.salariu_anual(),"lei")
angajat1.marire_salariu(10)
print('-' * 100)
# --------------------------------------------------------------------------------------------------------
# 4.Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma)
# ● creditare_cont(suma)
class Cont:
    # CONSTRUCTOR
    def __init__(self,iban,titular_cont,sold):
        self.iban = iban
        self.titular = titular_cont
        self.sold = sold
    # METODE
    def afisare_sold(self):
        print(f"Titularul {self.titular} are in contul {self.iban} suma de {self.sold} lei")

    def debitare_cont(self,suma):
        if self.sold > 0:
            if self.sold >= suma > 0:
                self.sold -= suma
                print(f"Au fost retrasi din contul dvs suma de {suma} lei.Sold disponibil {self.sold} lei")
            elif suma <= 0:
                print("Introduceti un sold de retragere pozitiv sau mai mare ca 0!")
            else:
                print(f"Sold indisponibil! Tranzactie nereusita!")
        else:
            print("Debitati contul cu o suma (mai mare ca 0)")
    def creditare_cont(self,suma):
        self.sold += suma
        print(f"Contul dvs a fost alimentat cu suma de {suma} lei.Sold disponibil {self.sold} lei")

cont1 = Cont("RO60BTRL001","Cristian Popescu", 500)
cont1.afisare_sold()
cont1.debitare_cont(500)
cont1.creditare_cont(100)
cont1.debitare_cont(50)
print('-' * 100)
# --------------------------------------------------------------------------------------------------------
# 5. Clasa Factura
# Factura seria x numar y
# Data: generați automat data de azi
# Produs | cantitate | preț bucată | Total
# Telefon | 7 | 700 | 49000
# Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/
from datetime import date
from tabulate import tabulate
class Factura():
    # ATRIBUTE
    seria = "PRD"

    # CONSTRUCTOR
    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    # METODE
    # ● schimbă_cantitatea(cantitate)
    def schimba_cantitatea(self,cantitatea):
        if cantitatea > 0:
            self.cantitate = cantitatea
        else:
            print("Introduceti un numar pozitiv de cantitate")

    # ● schimbă_prețul(pret)
    def schima_pret(self,pret):
        if pret > 0:
            self.pret_buc = pret
        else:
            print("Pretul trebuie sa fie pozitiv")

    # ● schimbă_nume_produs(nume)
    def schimba_nume_produs(self,nume):
        self.nume_produs = nume

    # ● generează_factura() - va printa tabelar dacă reușiți
    def genereaza_factura(self):
        total = self.cantitate * self.pret_buc
        print(f"Factura seria {self.seria} numar {self.numar}")
        today = date.today()
        print("Data:",today)
        # generam un model de tabel simplu cu functia Tabulate si declaram antetul(sus) si tabel pentru populare
        antet = ["Produs", "Cantitate", "Pret bucata", "Total"]
        tabel = [[self.nume_produs, self.cantitate, self.pret_buc, total]]
        print(tabulate(tabel, antet, tablefmt='simple'))

produs1 = Factura(1001,"Iphone",1,2000)
produs1.schimba_cantitatea(20)
produs1.schima_pret(1000)
produs1.schimba_nume_produs("Telefon")

produs1.genereaza_factura()
print('-' * 100)
# --------------------------------------------------------------------------------------------------------
# 6.Clasa Masina
# Atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)
# Culoare = gri - toate mașinile cand ies din fabrica sunt gri
# Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
# Culori disponibile = alegeți voi 5-7 culori
# Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
# Inmatriculata = False
# Constructor: model, viteza_maxima

class Masina:
    # ATRIBUTE
    marca = "Audi"
    viteza_actuala = 0
    culoare = "gri"
    culori_disponibile = ("rosu","galben","negru","verde","alb","albastru")
    inmatriculata = False

    # CONSTRUCTOR
    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_max = viteza_maxima

    # METODE
    # printam toate atributele, in afara de culori_disponibile
    def descriere(self):
        print(f"Masina {self.marca} {self.model} - culoare {self.culoare}. Viteaza actuala {self.viteza_actuala},viteza maxima {self.viteza_max } km/h. Inmatriculata: {self.inmatriculata}")
    # schimbam atributul înmatriculată în True
    def inmatriculare(self):
        self.inmatriculata = True
    # vopsim in noua culoare doar daca noua culoare este in optiunile din setul culori_disponibile
    def vopseste(self,culoare):
        if culoare.lower() in self.culori_disponibile:
            self.culoare = culoare.lower()
            print(f"Culoarea schimbata: {self.culoare}")
        elif self.culoare == culoare:
            print("Masina este vopsita deja in aceasta culoare")
        else:
            print("Nu avem culoarea aceasta pe stoc!")
    # accelereaza pana la o anumita viteaza, dc viteaza negativa Eroare
    def accelereaza(self,viteaza):
        if viteaza > 0:
            if viteaza > self.viteza_max:                   # dc viteza este mai mare ca viteza max, masina va accelera pana la viteza maxima doar
                self.viteza_actuala = self.viteza_max
            else:
                self.viteza_actuala = viteaza
        else:
            print("Eroare Viteaza negativa! (-)")
        print(f"Viteza actuala {self.viteza_actuala}")
    # fct va avea viteaza actuala 0 se va opri
    def franeaza(self):
        self.viteza_actuala = 0
        print(f"Viteaza acutuala {self.viteza_actuala}")


masina1 = Masina("A4",250)
masina1.descriere()
masina1.inmatriculare()
masina1.vopseste("rosu")
masina1.accelereaza(200)
masina1.franeaza()
masina1.descriere()
print('-' * 100)
# --------------------------------------------------------------------------------------------------------
# 7.Clasa TodoList
# Atribute: todoList(dict, cheia e numele taskului, valoarea e descrierea)
# La început nu avem taskuri, dict e gol și nu avem nevoie de constructor

class TodoList:
    # ATRIBUTE
    dict_task = {}
    # METODE
    # ● adauga_task(nume, descriere) - se va adauga in dict
    def adauga_task(self,nume,descriere):
        self.dict_task[nume] = descriere

    # ● finalizează_task(nume) - se va sterge din dict
    def finalizeaza_task(self,nume):
        self.dict_task.pop(nume)

    # ● afișează_todo_list() - doar cheile
    def afiseaza_todo_list(self):
        print(self.dict_task.keys())

    # ● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,printăm detalii suplimentare.
    def afiseaza_detalii_suplimentare(self,nume_task):
        for cheia,valoarea in self.dict_task.items():
            if nume_task in cheia:
                print(f"Descrierea task-ului: {valoarea}")
        if nume_task not in cheia:                                                              # Dacă taskul nu e în todolist
            text_tastura1 = input("Doriti sa adaugati noul task[Da/Nu]: ").capitalize()         # întrebam utilizatorul dacă vrea să-l adauge
            if text_tastura1 == "Da":                                                           # Daca DA il intrebam detalii task si salvam detalile+nume in dict
                text_tastura2 = input("Detalii task: ")
                self.adauga_task(nume_task,text_tastura2)
                print(self.dict_task)
            else:
                print("La reveredere!")                                                         # Daca NU printam La reverdere !


taskuri = TodoList()
taskuri.adauga_task("Baze de date","citeste si vizioneaza cursurile pe Youtube")
taskuri.adauga_task("Python","vizualizeazea cursul programare intro in programare")
taskuri.adauga_task("Java","citeste cartea x de programare")
print(taskuri.dict_task)

taskuri.finalizeaza_task("Python")
print(taskuri.dict_task)

taskuri.afiseaza_todo_list()

keyboard_text = input("Numele task-ului: ").capitalize()
taskuri.afiseaza_detalii_suplimentare(keyboard_text)
