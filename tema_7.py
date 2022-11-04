'''ABSTRACTION
Clasa abstracta FormaGeometrica
Contine un field PI=3.14
Contine o metoda abstracta aria
Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’
INHERITANCE
Clasa Patrat - mosteneste FormaGeometrica
constructor pt latura
ENCAPSULATION
latura este proprietate privata
Implementati getter, setter, deleter pt latura
Implementati metoda ceruta de interfata
Clasa Cerc - mosteneste FormaGeometrica
constructor pt raza
raza este proprietate privata
Implementati getter, setter, deleter pt raza
Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte
POLYMORPHISM
Definiti o noua metoda descrie - printati ‘Eu nu am colturi’
Creati un obiect de tip Patrat si jucati-va cu metodele lui
Creati un obiect de tip Cerc si jucati-va cu metodele lui
'''

# ABSTRACTION
from abc import ABC,abstractmethod
class FormaGeometrica(ABC):
    PI = 3.14
    # Method
    @abstractmethod
    def aria(self):
        pass
    @classmethod
    def descriere(self):
        print("Cel mai probabil am 4 colturi")
# --------------------------------------------------------------------------------------------------------
# INHERITANCE
class Patrat(FormaGeometrica):
    __latura = None

    # ENCAPSULATION
        # getter pentru latura -> folosit pentru afisarea latura
    def get_latura(self):
        return self.__latura

        # setter pentru latura -> folosit pentru setarea unei alte laturi
    def set_latura(self,valoare_noua_latura):
        self.__latura = valoare_noua_latura

        # deleter pentru latura -> folosim sa stergem latura
    def delete_latura(self):
        self.__latura = None

    def aria(self):
        total_arie_patrat = self.__latura * self.__latura
        print(f"Aria patratului este {total_arie_patrat}")
# --------------------------------------------------------------------------------------------------------
class Cerc(FormaGeometrica):
    __raza = None

    def get_raza(self):
        return self.__raza
    def set_raza(self,valoarea_noua_raza):
        self.__raza = valoarea_noua_raza
    def delete_raza(self):
        self.__raza = None
    def aria(self):
        total_arie_cerc = (self.__raza * self.__raza) * self.PI
        print(f"Aria cercului este {total_arie_cerc}")

    # POLYMORPHISM
    def descriere(self):
        print("Eu nu am colturi")

p1 = Patrat()
print(p1.get_latura())
p1.set_latura(10)
print(p1.get_latura())
p1.delete_latura()
print(p1.get_latura())
p1.descriere()
p1.set_latura(20)
print(p1.get_latura())
p1.aria()
print('-' * 100)
# --------------------------------------------------------------------------------------------------------
c1 = Cerc()
c1.set_raza(10)
print(c1.get_raza())
c1.aria()
c1.descriere()








