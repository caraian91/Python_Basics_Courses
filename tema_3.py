# 1. Declară o listă note_muzicale în care să pui do re mi etc pana la do.

note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si']
print(note_muzicale)                    # afisam lista

note_muzicale = note_muzicale[::-1]     # suprascrirem lista si inversam lista prin slicing
print(note_muzicale)                    # print varianta inversata

note_muzicale.reverse()                 # inversam ordinea din nou cu functia:'reverse' cu aceasta metoda nu mai avem nevoie de suprascriere !!!
print(note_muzicale)                    # printam lista
# --------------------------------------------------------------------------------------------------------
# 2. De câte ori apare ‘do’?
print("-" * 50)
print(note_muzicale.count("do"))        # count = vedem de cate ori se repeta cuvantul din ""
# --------------------------------------------------------------------------------------------------------
# 3. Având 2 liste, [3, 1, 0, 2] și [6, 5, 4].
print("-" * 50)
lista_1 = [3, 1, 0, 2]
lista_2 = [6, 5, 4]
lista_1.extend(lista_2)                 # extend = unim cele doua liste
print(lista_1)
# --------------------------------------------------------------------------------------------------------
# 4. Sortam si afisam lista generata anterior.
print("-" * 50)
lista_1.sort()
print(lista_1)

lista_1.remove(0)                       # stergem elementul 0 din lista
print(lista_1)
# --------------------------------------------------------------------------------------------------------
# 5. Folosind un if verifică lista generată la exercițiul 3 și afișază:
# ● Lista este goală si Lista nu este goală.
print("-" * 50)
if not lista_1:
    print("Lista este goala")
else:
    print("Lista nu este goala")
# --------------------------------------------------------------------------------------------------------
# 6. Folosește o funcție care să șteargă lista de la exercițiul 3.
print("-" * 50)
lista_1.clear()
print(lista_1)
# --------------------------------------------------------------------------------------------------------
# 7. Copy paste la exercițiul 5. Verifică încă o dată.
# Acum ar trebui să se afișeze că lista e goală.
print("-" * 50)
if not lista_1:
    print("Lista este goala")
else:
    print("Lista nu este goala")
# --------------------------------------------------------------------------------------------------------
# 8. Având dicționarul dict1. Folosește o funcție că să afișezi Elevii (cheile)
dict1 = {'Ana': 8,'Gigel': 10, 'Dorel': 5}
print(dict1.keys())
# --------------------------------------------------------------------------------------------------------
# 9. Printeaza cei 3 elevi si notele lor ex: "Ana a luat nota {x}".
# Doar nota o vei lua folosindu-te de cheie.
print("-" * 50)
print(f"Ana a luat nota", dict1["Ana"])
print(f"Gigel a luat nota", dict1["Gigel"])
print(f"Dorel a luat nota", dict1["Dorel"])
# --------------------------------------------------------------------------------------------------------
# 10.Dorel a făcut contestație și a primit 6
# ● Modifică nota lui Dorel în 6[
# ● Printează nota după modificare
print("-" * 50)
dict1["Dorel"] = 6
print(f"Dorel are nota", dict1["Dorel"], "dupa contestatie")
# --------------------------------------------------------------------------------------------------------
# 11.Gigel se transferă din clasa. Căuta o funcție care să îl șteargă .Vine un coleg nou. Adaugă Ionică, cu nota 9. Printează noii elevi
print("-" * 50)
dict1.pop("Gigel")                          # stergem din dictionar pe Gigel
dict1["Ionica"] = 9                         # adaugam un elev nou cu nota 9
print(dict1)                                # afisam
# --------------------------------------------------------------------------------------------------------
# 12. SET
print("-" * 50)
zile_sapt = {'luni' ,'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}       # declaram 2 Set-uri
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni')                       # adaugam ziua de Luni in set, aceesta nu se va scrie de 2x ori
print(zile_sapt)
# --------------------------------------------------------------------------------------------------------
# 13.Folosește un if și verifică dacă:
# ● Weekend este un subset al zilelor din săptămânii.
# ● Weekend nu este un subset al zilelor din săptămânii.
print("-" * 50)
if weekend.issubset(zile_sapt):
    print("Weekend este un subset al zilelor din saptamani")
else:
    print("NU este weekend un subset al zilelor din saptamani")
# --------------------------------------------------------------------------------------------------------
# 14. Afișează diferențele dintre aceste 2 seturi.
print("-" * 50)
print(f"Diferentele dintre cele 2 seturi sunt:",zile_sapt.difference(weekend))      # difference = pentru diferente intre seturi
# --------------------------------------------------------------------------------------------------------
# 15. Afișază intersecția elementelor din aceste 2 seturi.
print("-" * 50)
print(f"Intersectia elementelor:", zile_sapt.intersection(weekend))             # intersection = intersectia intre seturi
# --------------------------------------------------------------------------------------------------------
# 16. Problema: Ne imaginăm o echipă de fotbal pt teren sintetic.
SCHIMBARI_MAX = 3                                                       # constanta = nu isi schimba valoarea
lista_jucatori = ['Messi', 'Ronaldo', 'Neymar', 'Mbappe', 'Halaand']    # declaram lista de jucatori
schimbari_efectuate = int(input("Schimbari efectuate: "))               # introducem de la tastatura schimbari efectuate
schimbari_neefectuate = SCHIMBARI_MAX - schimbari_efectuate             # calculam schimbari ramase

if schimbari_efectuate < SCHIMBARI_MAX:
    nume_jucator_iesit = input("Numele jucatorului care va iesi: ").capitalize()
    nume_jucator_intrat = input("Nume jucatorului care va intra: ").capitalize()
    SCHIMBARI_MAX -= schimbari_efectuate
    if nume_jucator_iesit in lista_jucatori and nume_jucator_intrat not in lista_jucatori:
        lista_jucatori.remove(nume_jucator_iesit)
        lista_jucatori.append(nume_jucator_intrat)
        schimbari_neefectuate -= 1
        print("Schimbare a intrat",nume_jucator_intrat,"si a iesit",nume_jucator_iesit,"mai ai",schimbari_neefectuate,"schimbari")
        print(lista_jucatori)
    elif nume_jucator_iesit not in lista_jucatori:
        print("Nu se poate efectua schimbarea deoarece jucatorul",nume_jucator_iesit,"nu este in teren")
        print("Mai ai",schimbari_neefectuate,"schimbari")
    elif nume_jucator_intrat in lista_jucatori:
        print("Nu se poate face schimbarea deoarece jucatorul care trebuie sa intre",nume_jucator_intrat, "este deja in teren")
else:
    print("Ati atins limita maxima de",SCHIMBARI_MAX,"schimbari")
