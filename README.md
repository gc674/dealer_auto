# dealer_auto
Exercitiul I
Un dealer auto are pe stoc o serie de masini care se gasesc in variabila cars.
from operator import itemgetter as el_doi
cars = (
        (1, 'Audi', 8, 52642),
        (2, 'Mercedes', 6, 57127),
        (3, 'Skoda', 10, 19000),
        (4, 'Volvo', 4, 29000),
        (5, 'Bentley', 1, 350000),
        (6, 'Hummer', 2, 41400),
        (7, 'Volkswagen', 7, 21600),
        (8, 'Reanult', 10, 14000),
        (9, 'Dacia', 15, 8000),
        (10, 'Ford', 5, 15000),
        )
Fiecare element al tuplului cars reprezinta un brand, iar elementele individuale ale
unui brad au urmatoarea semnificatie: id unic, nume brad, nr. masini, valoarea unei
masini in Euro.
Ex: (4, 'Volvo', 4, 29000) 4 reprezinta id-ul unic → al brandului, 'Volvo' numele
producatorului sau al brandului, 4 este nr. de masini de pe stoc, iar valoarea unei
masini este de 29000 Euro.

Realizati o aplicatie Python astfel:
1. Creati o functie care primeste ca argument variabila cars si returneaza un tuplu
cu urmatoarele elemente:
- valoarea totala a masinilor de pe stoc
- valoarea totala a masinilor pentru fiecare brand
- nr. total de masini din stoc
- brandul de pe stoc cu valoarea totala a masinilor cea mai mare (ex: Skoda (10 x
19000))
2. Creati o functie care primeste ca argument variabila cars si genereaza un fisier
csv astfel:
id,brand,items,price
1,'Audi',8,52642
2,'Mercedes',6,57127
...

3. Creati o functie care primeste ca argument un fisier csv cu structura celui de mai
sus si realizeaza urmatoarele operatii:
a) verifica existenta fisierului primit ca argument (os module)
b) creaza o baza de date sqlite numita auto_dealer si un tabel numit cars (daca nu
exista deja).
Tabelul cars va avea urmatoarele campuri:
id integer
brand varchar(30)
items integer
price integer

Statement-ul sql pentru crearea tabelului este:
CREATE TABLE IF NOT EXISTS cars (id INTEGER, brand VARCHAR(30), items
integer, price integer)
