# 1.Avem lista:
# folosim un for ca sa iteream prin lista si sa afisam
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
for i in masini:
    print(i)

# for each
print("*" * 50)
for i in masini:
    print(f"Masina mea preferata este {i}")     # afisam mesajul cu for ptr fiecare iteratie

# while
print("*" * 50)
i = 0
while i < len(masini):
    print(f"Masina mea preferata este {masini[i]}")
    i += 1
# --------------------------------------------------------------------------------------------------------
# 2. Aceeași listă: Folosește un for else
# În for: - Modifică elementele din listă astfel încât să fie scrie cu majuscule, exceptând primul și ultimul.
# În else: - Printează lista.

print("*" * 50)
print(f"Lista este:              {masini}")
for i in range(1,len(masini)-1):
    masini[i] = masini[i].upper()
else:
    print(f"Lista dupa capitalizare: {masini}")
# --------------------------------------------------------------------------------------------------------
# 3. Aceeași listă:
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Itereaza prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
# Printează ‘am găsit mașina dorită de dvs’
# Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
# Printează ‘Am găsit mașina X. Mai căutam‘

# Metoda 1 cu for
print("*" * 50)
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
for i in masini:
    if i == "Mercedes":
        print(f"Am gasit masina dorita de dvs: {i}")
        break
    else:
        print(f"Am gasit masina {i}.Mai cautam")

# Metoda 2 cu while
i=0
while i < len(masini):
    if masini[i] == 'Mercedes':
        print(f"Am gasit masina dorita de dvs {masini[i]}")
        break
    else:
        print(f"Am gasit masina {masini[i]} mai cautam")
    i += 1
# --------------------------------------------------------------------------------------------------------


print("*" * 50)
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
for i in masini:
    if i == "Trabant" or i =="Lăstun":
        continue
    print(f"S-ar putea sa va placa masina: {i}")
# --------------------------------------------------------------------------------------------------------
# 5. Modernizează parcul de mașini:
# Crează o listă goală, masini_vechi.
# Itereaza prin mașini.
# Când găsesti Lăstun sau Trabant:
# Salvează aceste mașini în masini_vechi.
# Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
# Printează Modele vechi: x.
# Modele noi: x.

print("*" * 50)
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
masini_vechi = []
for i in masini:
    if  i == "Trabant" or i == "Lăstun":
        masini_vechi.append(i)
masini[masini.index('Lăstun')] = "Tesla"
masini[masini.index('Trabant')] = "Tesla"# 4. Aceași listă;
# Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun.
# Dacă mașina e Trabant sau Lăstun:
# Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
# Printează S-ar putea să vă placă mașina x.
print(f"Modele vechi: {masini_vechi}")
print(f"Modele noi: {masini}")
# --------------------------------------------------------------------------------------------------------
# 6. Având dict:
# Vine un client cu un buget de 15000 euro.
# Prezintă doar mașinile care se încadrează în acest buget.
# Itereaza prin dict.items() și accesează mașina și prețul.
# Printează Pentru un buget de sub 15000 euro puteți alege mașină
# xLastun
# Iterează prin listă.

print("*" * 50)
pret_masini = { 'Dacia': 6800,'Lăstun': 500,'Opel': 1100,'Audi': 19000,'BMW': 23000 }
CLIENT_BUGET = 15000

for marca,pret in pret_masini.items():
    print(f"Marca: {marca}, la pret de {pret}")
for marca,pret in pret_masini.items():
    if pret <= CLIENT_BUGET:
        print(f"Masinilie pentru bugetul dvs sunt: {marca}, avand pretul de {pret} Euro")
# --------------------------------------------------------------------------------------------------------
# 7. Având lista:
# Iterează prin ea.
# Afișează de câte ori apare 3 (nu ai voie să folosești count).

print("*" * 50)
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
total = 0
for i in numere:
    if i == 3:
        total += 1
print(f"Numarul 3 apare de: {total}")
# --------------------------------------------------------------------------------------------------------
# 8. Aceeași listă:
# Iterează prin ea
# Calculează și afișează suma numerelor (nu ai voie să folosești sum).

print("*" * 50)
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0
for nr in numere:
    suma += nr
print(f"Suma numerelor: {suma}")
# --------------------------------------------------------------------------------------------------------
# 9. Aceeași listă:
# Iterează prin ea.
# Afișază cel mai mare număr (nu ai voie să folosești max).

print("*" * 50)
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
maxim = numere[0]
for nr in numere:
    if nr > maxim:
        maxim = nr
print(f"Cel mai mare nr: {maxim}")
# --------------------------------------------------------------------------------------------------------
# 10. Aceeași listă:
# Iterează prin ea.
# Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# Ex: dacă e 3, să devină -3
# Afișază noua listă.

print("*" * 50)
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for nr in range(len(numere)):
    if numere[nr] > 0:
        numere[nr] = -numere[nr]
print(f"negativ: {numere}")

# Metoda cu ForEach
alta_lista = []
for i in numere:
    if i>=0:
        i = i * (-1)
        alta_lista.append(i)
print(f"negativ: {alta_lista}")
# --------------------------------------------------------------------------------------------------------
# 11.
# Itereaza prin listă alte_numere
# Populează corect celelalte liste
# Afișeaza cele 4 liste la final

print("*" * 50)
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for i in alte_numere:
    if i % 2 == 0:
        numere_pare.append(i)
    else:
        numere_impare.append(i)
    if i > 0:
        numere_pozitive.append(i)
    else:
        numere_negative.append(i)
alte_numere.clear()
print(f"Numerele pare: {numere_pare}")
print(f"Numerele impare: {numere_impare}")
print(f"Numerele pozitive: {numere_pozitive}")
print(f"Numerele negative: {numere_negative}")
print(alte_numere)
# --------------------------------------------------------------------------------------------------------
# 12. Aceeași listă:
# Ordonează crescător lista fară să folosești sort.
# Te poți inspira vizual de aici: https://www.youtube.com/watch?v=lyZQPjUT5B4

print("*" * 50)
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
i=0
while i < len(alte_numere):                         # parcugem lista
    for j in range(len(alte_numere)-1):
        if alte_numere[j]>alte_numere[j+1]:
            temp = alte_numere[j]                   # salvam intro variabila temporala daca j este mai mare decat urmatorul
            alte_numere[j] = alte_numere[j+1]
            alte_numere[j+1] = temp
    i += 1
print(alte_numere)

# Metoda 2
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
for i in range(len(alte_numere)):
    for j in range(len(alte_numere) - 1):
        if alte_numere[j] > alte_numere [j + 1]:
            tmp = alte_numere[j]
            alte_numere[j] = alte_numere[j+1]
            alte_numere[j+1] = tmp
print(alte_numere)

# --------------------------------------------------------------------------------------------------------
# 13. Ghicitoare de număr:
# numar_secret = Generați un număr random între 1 și 30
# Numar_ghicit = None
# Folosind un while
# User alege un număr
# Programul îi spune:
# Nr secret e mai mare
# Nr secret e mai mic
# Felicitări! Ai ghicit!
import random

print("*" * 50)
numar_secret = random.randrange(1,31)
numar_ghicit = None
print(numar_secret)
while numar_ghicit == None:
    tastatura_nr = int(input("Introduceti numarul: "))
    if 0 <= tastatura_nr <= 30:
        if numar_secret > tastatura_nr:
            print("Nr secret e mai mare")
        elif numar_secret < tastatura_nr:
            print("Nr secret e mai mic")
        else:
            numar_ghicit = False
            print("Felicitari! Ai ghicit!")
    else:
        print("Dati un numar intre 0 si 30")
# --------------------------------------------------------------------------------------------------------
# 14. Alege un număr de la tastatură
# Scrie un program care să genereze în consolă următoarea piramidă
# Ex:3
# 1
# 22
# 333

print("*" * 50)
numar = int(input("Alegeti un numar: "))
for i in range(numar+1):        # bucla exterioara pentru numar ales
    for j in range(i):          # bucla nested(imbricata) pt a repeta pana la numarul ales (ex: 3-> 1,22,333)
        print(i, end="")        # afisare numar
    print("")                   # linie noua dupa fiecare rand
# --------------------------------------------------------------------------------------------------------
# 15.
# tastatura_telefon
# Iterează prin listă 2d
# Printează ‘Cifra curentă este x’
# (hint: nested for - adică for în for)

print("*" * 50)
tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
for i in range(len(tastatura_telefon)):
    print(tastatura_telefon[i], end="")
print("\n")

for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
        print(f"Cifra curenta este {tastatura_telefon[i][j]}")

"""
Exercitiu:
Scrie un program care citeste de la tastatura 3 numere: a, b, c
Verifica cate numere intre a si b sunt divizibile cu c
"""
a = int(input("Introduceti numarul a: "))
b = int(input("Introduceti numarul b: "))
if a < b:
    c = int(input("Introduceti numarul divizibil c: "))
    for valoare in range(a,b):
        if valoare % c == 0:
            print(f"Numere divizile cu c intre [a,b] sunt: {valoare}")
else:
    print("Numarul b trebe sa fie mai mare ca a !!!")
# --------------------------------------------------------------------------------------------------------

# OPTIONAL EXERCISES Homework 4
"""
Exercitiu:
Scrieti un program prin care un user introduce de la tastatura o serie de numere integer, unul dupa altul folosind ENTER. Userul poate introduce cate numere vrea.
Cand userul introduce de la tastatura cuvantul "stop" in loc de un numar atunci programul ar trebui sa se opreasca si sa afiseze:
- toate numerele introduse sortate crescator
- cate numere pare au fost introduse si suma lor
Folositi continue si break
"""
numbers = []
suma = 0
nr_pare = 0

while True:
    x = input("[se opreste cu 'STOP']Introduceti numere intregi: ").lower()
    if x != "stop":                 # daca nu se introduce textul stop punem in lista numere intregi
        numbers.append(x)
    elif x == "stop":
        break                               # cand cuvantul stop este scris oprim ciclul repetitiv

numbers.sort(key=int)                               # sortam lista crescator dupa integer
print(f"Numerele sortate crescator: {numbers}")     # afisam lista de numbers

for i in range(len(numbers)):               # parcurgem lista
    if int(numbers[i]) % 2 == 1:            # daca numerele sunt impare facem skip cu continue
        continue
    suma += int(numbers[i])                 # cand nr sunt pare adunam suma lor
    nr_pare += 1                            # numaram de cate ori avem in lista nr pare
print(f"Au fost introduse: {nr_pare} numere pare")
print(f"Suma numerelor pare este: {suma}")
# --------------------------------------------------------------------------------------------------------
"""
Exercitiu:
Scrabble este un joc în care jucătorii obțin puncte scriind cuvinte. 
Cuvintele sunt punctate prin adunarea valorilor punctuale ale fiecărei litere individuale. 
Scrieti un program care ia ca intrare un cuvânt șir și returnează scorul scrabble echivalent pentru acel cuvânt.
"""
score = {
    "a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
    "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
    "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
    "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
    "x": 8, "z": 10 }

suma_scor = 0
text_introdus = input("Introduceti cuvantul: ").lower()
for litera in text_introdus:             # iteream toate elementele din textul introdus de la tastatura
    suma_scor += score[litera]           # adunam din dictionarul score cu valoarea corespunzatoare literei
print(f"Scorul Scrabble pentru cuvantul {text_introdus} este: {suma_scor}")
# --------------------------------------------------------------------------------------------------------
"""
Exercitiu:
Scrieți un program Python care repetă numerele întregi de la 1 la 50. 
Pentru multiplii de trei tipăriți „Fizz” în loc de număr, iar pentru multiplii de cinci tipăriți „Buzz”. 
Pentru numerele care sunt multipli de trei și cinci, se afișează „FizzBuzz”
"""
for i in range(1,51):                   # parcurgem intervalul 1 pana la 50
    if i % 3 == 0 and i % 5 == 0:       # daca 3 si 5 sunt divizibile cu numerele[1,50] printam FizzBuzz
        print("FizzBuzz")               # daca nu cu continue sarim(dam skip)
        continue
    elif i % 3 == 0:                    # aceaasi logica ca mai sus
        print("Fizz")
        continue
    elif i % 5 == 0:                    # aceaasi logica ca mai sus
        print("Buzz")
        continue
    print(i)
