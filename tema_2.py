# 1. if, else = executa anumite comenzi cand o conditie este adevarata si alte comenzi cand aceasta este falsa

# --------------------------------------------------------------------------------------------------------
# 2. verificam si afisam daca un nr este natural sau nu

print("*" * 50)
x = float(input("Introduceti numarul 'x': "))
if x >= 0 and x == int(x):
    print("Numar este natural")
else:
    print("Nu este un nr natural")
# --------------------------------------------------------------------------------------------------------
# 3. verificam si afisam daca un nr este pozitiv,negativ sau neutru

print("*" * 50)
if x == 0 or x == 1:                      # neutru care nu schimba valoarea unei expresii am luat si inumultirea
    print("Numarl este neutru")
elif x > 1:
    print("Numar pozitiv")
else:
    print("Numar negativ")
# --------------------------------------------------------------------------------------------------------
# 4. Verificam si afisam daca un nr este intre -2 si 13

print("*" * 50)
if x >= -2 and x <= 13:
    print("Numarul este in intervalul[-2,13]")
else:
    print("Numarul nu este in interval")
# --------------------------------------------------------------------------------------------------------
# 5. Verificam si afisam daca diferenta dintre x si y este mai mica decat 5

print("*" * 50)
y = int(input("Introduceti numarul 'y': "))
if x-y < 5:
    print("Diferenta este mai mica decat 5")
else:
    print("Diferenta este mai mare decat 5")
# --------------------------------------------------------------------------------------------------------
# 6. Verificam daca x nu este intre 5 si 27 folosim 'not'

print("*" * 50)
if not(x < 5 or x > 27):
    print("Este in intervalul [5,27]")
else:
    print("NU este in intervalul [5,27]")
# --------------------------------------------------------------------------------------------------------
# 7. Verificam daca x si y sunt egale, daca nu afisam pe cel mai mare

print("*" * 50)
if x == y:
    print("Numerele x si y sunt egale")
elif x > y:
    print(f"X este mai mare Nr:{x}")
else:
    print(f"Y este mai mare Nr:{y}")
# --------------------------------------------------------------------------------------------------------
# 8. x,y,z laturile unui triunghi
#    afisam daca triunghiul este isoscel, echilateral sau oarecum

print("*" * 50)
z = int(input("Introduceti numarul 'z': "))
if x == y == z:
    print("Triunghiul este echilateral")
elif (x == y and x != z) or (x == z and x != y) or (y == z and y != x):
    print("Triunghiul este isoscel")
else:
    print("Triunghiul este oarecare")
# --------------------------------------------------------------------------------------------------------
# 9. Citim de la tastatura o litera ,verificam daca este vocala sau nu

print("*" * 50)
input_keyboard = input("Introduceti o litera: ").lower()
if input_keyboard == 'a' or input_keyboard == 'e' or input_keyboard == 'i' or input_keyboard == 'o' or input_keyboard == 'u' or input_keyboard == 'ă' or input_keyboard == 'î' or input_keyboard == 'â':
    print("Litera este o vocala")
else:
    print("Litera NU este vocala")
# --------------------------------------------------------------------------------------------------------
# 10. Transformă și printează notele din sistem românesc în A,B,C... etc

print("*" * 50)
nota = round(float(input("Nota acordata elevului este: ")))
print(nota)
if 0 < nota <= 10:
    if nota >= 9:
        nota = 'A'
        print(f"Nota in noul sistem este: {nota}")
    elif nota >= 8:
        nota = 'B'
        print(f"Nota in noul sistem este: {nota}")
    elif nota >= 7:
        nota = 'C'
        print(f"Nota in noul sistem este: {nota}")
    elif nota >= 6:
        nota = 'D'
        print(f"Nota in noul sistem este: {nota}")
    elif nota > 4:
        nota = 'E'
        print(f"Nota in noul sistem este: {nota}")
    elif nota <= 4:
        nota = 'F'
        print(f"Nota in noul sistem este: {nota}")
else:
    print(f"Introduceti o nota validă între [1-10]. Acesta {nota} nu este valida!")
# --------------------------------------------------------------------------------------------------------
# 11. verifica daca un numar x are minim 4 cifre

print("*" * 50)
nr = int(input("Introduceti un numar: "))
if nr > 999 or nr < -999:
    print("Are 4 cifre")
else:
    print("NU are 4 cifre")
# --------------------------------------------------------------------------------------------------------
# 12. verificăm dacă nr are exact 6 cifre

print("*" * 50)
if (nr > 99999 and nr <= 999999) or (nr < -99999 and nr >= -999999):
    print("Are 6 cifre")
else:
    print("Nu are 6 cifre")
# --------------------------------------------------------------------------------------------------------
# 13. verificăm nr par sau impar

print("*" * 50)
if nr % 2 == 0:
    print("Numarul este par")
else:
    print("Numarul este impar")
# --------------------------------------------------------------------------------------------------------
# 14. x,y,z afisam care este mai mare dintre ele

print("*" * 50)
print("14.Cel mai mare numar dintre x,y,z")
x = int(input("Introduceti numarul 'x': "))
y = int(input("Introduceti numarul 'y': "))
z = int(input("Introduceti numarul 'z': "))
if x > y  and x > z:
    print(f"Cel mai mare numar este: {x}")
elif y > z and y > x:
    print(f"Cel mai mare numar este: {y}")
elif z > x and z > y:
    print(f"Cel mai mare numar este: {z}")
else:
    print("Cel putin 2 numere sunt egale")
# --------------------------------------------------------------------------------------------------------
# 15. x, y, z - reprezintă unghiurile unui triunghi, verificam și afișam dacă triunghiul este valid sau nu.
# triunghi daca are suma unghiurilor egale cu 180 grade

print("*" * 50)
x = int(input("Introduceti unghiul 1: "))
y = int(input("Introduceti unghiul 2: "))
z = int(input("Introduceti unghiul 3: "))
if x > 0 and y > 0 and z > 0:
    if (x + y + z == 180):
        print("Triunghiul este valid")
else:
    print("Triunghiul nu este valid")
# --------------------------------------------------------------------------------------------------------
# 16. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
# ● Citiți de la tastatură un int x
# ● Afișează stringul fără ultimele x caractere
# Exemplu: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'

print("*" * 50)
sentence_1 = "Coral is either the stupidest animal or the smartest rock"
x = int(input("Introduceti un numar: "))
print(sentence_1[:-x])
# --------------------------------------------------------------------------------------------------------
# 17. Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5

print("*" * 50)
sentence_2 = sentence_1[:5] + sentence_1[-5:]
print(f"Noul string este: {sentence_2}")
# --------------------------------------------------------------------------------------------------------
# 18. Același string.
# ● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint: este o funcție care te ajuta sa faci asta)
# ● Folosind această variabilă + slicing, afișează tot stringul până la acest cuvant
# ● output: 'Coral is either the stupidest animal or the smartest '

print("*" * 50)
sentence_1 = "Coral is either the stupidest animal or the smartest rock"
cuvant_index = sentence_1.index("rock")      # hint: index pentru a gasi indexul de start al cuvantului rock
print(cuvant_index)                          # il gasim de la index 53
print(sentence_1[0:cuvant_index])
# --------------------------------------------------------------------------------------------------------
# 19. un string de la tastatura,verificăm dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
# Atentie: se dorește ca programul sa fie case insensitive - 'apA' e acceptat

print("*" * 50)
cuvant_1 = str(input("Introduceti un cuvant(primul si ultimul caracter sa fie la fel): "))
primul_caracter = cuvant_1[0]
ultimul_caracter = cuvant_1[-1]
assert primul_caracter.lower()  == ultimul_caracter.lower()        # lower = convertim caracterele in mici
print(f"Primul si ultimul caracter sunt identice {primul_caracter} = {ultimul_caracter}")
# --------------------------------------------------------------------------------------------------------
# 20.  Avand stringul '0123456789'
# ● Afișați doar numerele pare
# ● Afișați doar numerele impare
# (hint: folositi slicing, controlați din pas)

print("*" * 50)
cuvant_2 = '0123456789'
print(f"Numerele pare sunt: {cuvant_2[0:10:2]}")
print(f"Numerele impare sunt: {cuvant_2[1:10:2]}")
# --------------------------------------------------------------------------------------------------------
# 21.  Joc ghicit zarul
''' se generează un număr random.Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
Luați un numărul ghicit de la utilizator. Verificați și afișați dacă utilizatorul a ghicit
Veți avea 3 opțiuni
● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
● Ai ghicit. Felicitari! Ai ales x si zarul a fost y '''

print("*" * 50)
import random

dice_roll = random.randrange(1,7)           # random.range face numere aletorie intre 1 si 6;[1,10->intre 1 si 9]
number_user = int(input("Alegeti un numar intre 1 si 6: "))
if number_user >=1 and number_user <=6:
    if dice_roll == number_user:
        print(f"Ai ghicit.Felicitari! Ai ales {number_user} si zarul a fost {dice_roll}")
    elif number_user < dice_roll:
        print(f"Ai pierdut.Ai ales un numar mai mic. Ai ales {number_user} dar a fost {dice_roll}")
    elif number_user > dice_roll:
        print(f"Ai pierdut.Ai ales un numar mai mare. Ai ales {number_user} dar a fost {dice_roll}")
else:
    print("Te rugam sa alegi un numar intre 1 si 6!!!")