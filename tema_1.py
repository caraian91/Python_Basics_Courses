# Variabila = o memorie care stocheaza informatii
# Variabila = o cutiuta din memorie in care stocam valori, aceasta este creata in momentul in care ii atribuim o valoare
# --------------------------------------------------------------------------------------------------------
# declaram si initializam cate o variabila

marca_masina = "Audi"
an_fabricatie = 2010
pret_masina = 8000.50
stoc_masina = True
# --------------------------------------------------------------------------------------------------------
# verificam cu functia TYPE daca au tipul de date corecte

print(type(marca_masina))
print(type(an_fabricatie))
print(type(pret_masina))
print(type(stoc_masina))
# --------------------------------------------------------------------------------------------------------
# rotunjim variabila pret_masina(float) si suprascriem variabila respectiva

pret_masina = round(pret_masina)
print(pret_masina)
print(type(pret_masina))
# --------------------------------------------------------------------------------------------------------
# printam in consola 4 propozitii folosind cele 4 variabile de mai sus

print("Marca masini este:", marca_masina)
print("Anul de fabricatiei al masini:", an_fabricatie)
print("Pretul este:", pret_masina,"Euro")
print("Masina este in stoc:", stoc_masina)
# --------------------------------------------------------------------------------------------------------
# citim de la tastatura si afisam nr de caractere din nume+prenume

nume = input("Numele dvs este: ")
prenume = input("Prenumele dvs este: ")
nr_caractere = len(nume+prenume)
print(f"Numele complet este: {nume} {prenume} si are {nr_caractere} de caractere")
# --------------------------------------------------------------------------------------------------------
# aria unui dreptunghi

lung = int(input('Introduceti Lungimea '))
lati = int(input('Introduceti latimea '))
aria = lung * lati
print(f'Aria dreptunghiului este: {aria}')
# --------------------------------------------------------------------------------------------------------
# afisam de cate ori apare cuvantul "the" in propozitie

sentence = "Coral is either the stupidest animal or the smartest rock"
print("Cuvantul 'the' apare de:", sentence.count("the"))
# --------------------------------------------------------------------------------------------------------
# inlocuim cuvantul 'the' cu 'THE' peste tot

sentence_4 = "Coral is either the stupidest animal or the smartest rock"
print('Noua propozitie este:', sentence_4.replace("the", "THE"))
# --------------------------------------------------------------------------------------------------------
# assert verificam daca sentence contine numere   --- METODA 1

contine_nr = False
sentence_1 = "Coral is either the stupidest animal or the smartest rock"
for numere in sentence_1 :
    if numere.isdigit():
        contine_nr = True
assert contine_nr == False
print("Propozitia nu contine numere metoda 1")

# assert verificam daca sentence contine numere   --- METODA 2
# folosim isdigit
sentence_1 = "Coral is either the stupidest animal or the smartest rock"
assert sentence_1.isdigit() == False
print("Propozitia nu contine numere metoda 2")

# --------------------------------------------------------------------------------------------------------
# citim de la tastatura un string de dimensiune impara

cuvant = input("Introduceti un text de dimensiune impar:")
mijloc = int(len(cuvant)/2)          # impartim lungimea cuvantului
print(cuvant[mijloc])                # afisam caracterul din mijloc
# --------------------------------------------------------------------------------------------------------
# Folosind assert, verifică dacă un string este palindrom.
# palindrom = cuvant citit de la stanga la dreapta si de la dreapta la stanga are acelasi inteles

sentence_2 = input("Scrieti un cuvant palindrom:")
assert sentence_2 == sentence_2[::-1]
print("Acest cuvant este un palindrom")
# --------------------------------------------------------------------------------------------------------
# salvare a doua variabile citite de la tastatura si afisarea lor

telefon,model  = input("Scrieti marca de telefon modelul: ").split();print(telefon, model)
# --------------------------------------------------------------------------------------------------------
# Se citeste de la tastatura un cuvant, se salveaza primul caracter
# si capitalizam cu caractere doar litera 'A' excepand primul si ultimul caracter

sentence_3 = input("Introduceti un cuvant pentru capitalizare sa contina litera 'a':")
primul_caracter = sentence_3[0]
print("Primul caracter din cuvant este:",primul_caracter)
capitalizare = sentence_3[0] + sentence_3[1:-1].replace('a','A') + sentence_3[-1]
print("Transformarea cuvantului:", capitalizare)
# --------------------------------------------------------------------------------------------------------
# citim un user de la tastatura si o parola
# afisam datele utilizatorului iar in locul parolei vom afisa ***(in fct de cat de lunga este parola)

user = input("Utilizator: ")
parola = input("Parola: ")
stelute = "*" * len(parola)
print(f"Parola pentru {user} este {stelute} si are {len(parola)} caractere")