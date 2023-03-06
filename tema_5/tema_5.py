# from Functile.functi_5 import calculator_ziua_de_nastere,time_zone,reducere_pret,suma_nr,par_impar,nr_total_caractere,arieDr,arieCr,caracterul_x,caractere_mici_mari,lista_numere_pozitive,numar_mare,nr_primit,ziua_din_luna,calculator,lista_cifre,numer_maxim,sum_numere,liste_comune
from Functile.functi_5 import *

suma_nr()
print(par_impar())
nr_total_caractere()
arieDr()
arieCr()
print(caracterul_x())
caractere_mici_mari()
lista_numere_pozitive()
numar_mare()
print(nr_primit({1,2,3,4,5},2))

tastaura_luna = str(input("Introduceti luna[Ianuarie,Februarie...etc]: "))
ziua_din_luna(tastaura_luna)

a,b,c,d = calculator(12,2)

list_nr = [1, 3, 1, 5, 9, 7, 7, 5, 5]
lista_cifre(list_nr)

numer_maxim(4,2,2)

sum_numere(0)

liste_comune([1, 1, 2, 3],[2, 2, 3, 4])

reducere_pret(100,10)

time_zone()

calculator_ziua_de_nastere()