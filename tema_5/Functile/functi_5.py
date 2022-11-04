# 1.Funcție care să calculeze și să returneze suma a două numere

print("*" * 50)
def suma_nr():
    a = int(input("Introduceti primul numar: "))
    b = int(input("Introduceti doilea numar: "))
    suma = a+b
    print(f"Suma numerelor este: {suma}")
# --------------------------------------------------------------------------------------------------------
# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar

def par_impar():
    numar = int(input("Verificare numar par/impar: "))
    if numar % 2 == 0:
        return True
    else:
        return False
# --------------------------------------------------------------------------------------------------------
# 3. Funcție care returnează numărul total de caractere din numele tău complet. (nume, prenume, nume_mijlociu)

def nr_total_caractere():
    numele_complet = input("Numele dvs complet este: ").split()
    total = 0
    for litera in numele_complet:
        total += len(litera)
    print(f"Numar total de caractere din numale tau: {total}")
# --------------------------------------------------------------------------------------------------------
# 4. Funcție care returnează aria dreptunghiului

def arieDr():
    lung = int(input("Introduceti Lungimea: "))
    lati = int(input("Introduceti Latimea: "))
    aria = lung * lati
    return print(f"Aria dreptunghiului este: {aria}")
# --------------------------------------------------------------------------------------------------------
# 5. Funcție care returnează aria cercului

def arieCr():
    PI = 3.14;
    raza = int(input("Introduceti Raza: "))
    aria = PI * (raza ** 2)
    return print(f"Aria cercului este: {aria}" )
# --------------------------------------------------------------------------------------------------------
# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
# și False dacă nu găsește.

def caracterul_x():
    text = input("Introduceti cuvantul: ").lower()
    for i in text:
        if 'x' in text:
            return True
        else:
            return False
# --------------------------------------------------------------------------------------------------------
# 7. Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y

count = {'lower_case': 0,
        'upper_case':0 }
def caractere_mici_mari():

    text = input("Introduceti cuvantul: ")
    for litera in text:
        if litera.islower():
            count["lower_case"] += 1
        elif litera.isupper():
            count["upper_case"] += 1
    print(f"Numarul de lower_case este: {count['lower_case']}")
    print(f"Numarul de upper_case este: {count['upper_case']}")
# --------------------------------------------------------------------------------------------------------
# 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
# numerele pozitive

def lista_numere_pozitive():
    numere = []
    numere_pozitive = []
    range = int(input("Care numere vreti sa adaugati in lista?: "))
    i=0
    while i < range:
        numere_tastatura = int(input("Introduceti numerele: "))
        i += 1
        numere.append(numere_tastatura)
    print(f"Lista generata este: {numere}")
    for i in numere:
        if i > 0:
            numere_pozitive.append(i)
    print(f"Lista cu numerele pozitive: {numere_pozitive}")
# --------------------------------------------------------------------------------------------------------
# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.

def numar_mare():
    x = int(input("Primul nr: "))
    y = int(input("Al doilea nr: "))
    if x > y:
        print(f"Primul numar {x} este mai mare decat al doilea nr {y}")
    elif x < y:
        print(f"Al doilea numar {y} este mai mare decat primul nr {x}")
    else:
        print(f"Numerele sunt egale {x} = {y}")
# --------------------------------------------------------------------------------------------------------
# 10. Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False

def nr_primit(lista_set,numar):
    a = set(lista_set)
    if numar not in a:
        a.add(numar)
        print(f"Am adaugat numarul nou in set. Lista de set actuala {a}")
        return True
    else:
        print(f"Nu am adaugat numarul in set.Acesta exista.")
        return False
# --------------------------------------------------------------------------------------------------------
# 11. Funcție care primește o lună din an și returnează câte zile are acea luna

def ziua_din_luna(luna):
    zile = {"Ianuarie": 31,
            "Februarie": 28,
            "Martie": 31,
            "Aprilie": 30,
            "Mai": 31,
            "Iunie": 30,
            "Iulie": 31,
            "August": 31,
            "Septembrie": 30,
            "Octombrie": 31,
            "Noiembrie": 30,
            "Decembrie": 31}
    for l, z in zile.items():
        if l == luna:
            print(f"Luna {l} are {z} de zile")
# --------------------------------------------------------------------------------------------------------
# 12.Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea, împărțirea a două numere.

def calculator(nr1,nr2):
    a = nr1 + nr2
    print(f"Suma: {a}")
    b = nr1 - nr2
    print(f"Diferenta: {b}")
    c = nr1 * nr2
    print(f"Inmultirea: {c}")
    d = nr1 / nr2
    print(f"Impartirea: {d}")
    return a,b,c,d
# --------------------------------------------------------------------------------------------------------
# 13.Funcție care primește o lista de cifre (adică doar 0-9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră

def lista_cifre(list_nr):
    cifra_dict = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
    for i in list_nr:
        a = str(i)
        cifra_dict[a] += 1
    print(cifra_dict)
# --------------------------------------------------------------------------------------------------------
# 14. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele

def numer_maxim(a,b,c):
    if a >= b and a >= c:
        print(f"Cel mai mare numar este: {a}")
    elif b >= a and b >= c:
        print(f"Cel mai mare numar este: {b}")
    else:
        print(f"Cel mai mare numar este: {c}")
# --------------------------------------------------------------------------------------------------------
# 15. Funcție care să primească un număr și să returneze suma tuturor numerelor de la 0 la acel număr
# Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)

def sum_numere(n):
    suma = 0
    if n >= 0:
        for i in range(0,n+1):
            suma += i
        print(f"Suma este: {suma}")
    else:
        print("Introduceti un numar pozitiv")
# --------------------------------------------------------------------------------------------------------
# 16. Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune
# Exemplu:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# Răspuns: {2, 3}

def liste_comune(lista1,lista2):
    print(set(lista1).intersection(lista2))
# --------------------------------------------------------------------------------------------------------
# 17. Funcție care să aplice o reducere de preț
# Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
# Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e invalidă.

def reducere_pret(pret,discount):
    if discount <= 100:
        reducere_pret = pret * discount/100
        pret_final = pret - reducere_pret
        print(f"Pretul produsului {pret} lei, iar dupa reducerea aplicata de {discount}% este de {pret_final} lei")
    else:
        print("Reducerea este invalida")
# --------------------------------------------------------------------------------------------------------
# 18. Funcție care să afișeze data și ora curentă din RO
# (bonus: afișați și data și ora curentă din China)

def time_zone():
    import datetime
    import pytz
    now_ro = datetime.datetime.now(pytz.timezone('Europe/Bucharest'))
    now_china = datetime.datetime.now(pytz.timezone('Asia/Shanghai'))
    print("Ora curenta RO:", now_ro.strftime("%Y-%m-%d %H:%M:%S"))
    print("Ora curenta China:", now_china.strftime("%Y-%m-%d %H:%M:%S"))
# --------------------------------------------------------------------------------------------------------
# 19. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la Crăciun

import datetime
today = datetime.date.today()
year = today.year
zi_nastere = datetime.date(1991, 5, 20)
def calculator_ziua_de_nastere():
        ziua_nastere = datetime.date(year+1, 5, 20)
        print("Urmatoare zi de nastere: " +  ziua_nastere.strftime('%d, %b %Y'))
        x = (ziua_nastere - today).days
        print(f"Zile ramase pana la ziua de nastere: {x}")


