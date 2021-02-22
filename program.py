from operator import itemgetter as el_doi
import csv
import os
import sqlite3
import time


fisier_csv = 'cars_stoc.csv'
fisier_db = 'cars_stoc.db'
sql_cars_table = """ CREATE TABLE IF NOT EXISTS cars (
                                                                id INTEGER,
                                                                brand VARCHAR(30),
                                                                items integer,
                                                                price integer); """
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

def one_function(lista=cars):
    valuetotal = 0
    totalcars = 0
    lista_brand = []
    for i in lista:
        valuetotal += i[3] * i[2]
        totalcars += i[2]
        lista_brand.append((i[1], i[2] * i[3]))
    lista_brand.sort(key=el_doi(1))
    max_brand_value = lista_brand[-1]

    return valuetotal, totalcars, lista_brand, max_brand_value


def to_db(lista, sql_table, cars_db=fisier_db):
    # if not os.path.isfile(cars_db):
    my_connection = sqlite3.connect(cars_db)
    my_cursor = my_connection.cursor()
    if my_connection:
        my_connection.execute(sql_table)
        time.sleep(0.5)
        print('Se scrie în baza de date:')
        for i in lista:
            print(i)
            my_cursor.execute('INSERT INTO cars VALUES (?,?,?,?)', i)
            time.sleep(0.5)
        my_connection.commit()
        my_connection.close()



def to_csv(lista=cars, cars_csv=fisier_csv):
    '''se scrie un fișier csv cu header și lista'''
    with open(cars_csv, 'w') as csv_file:
        line = csv.writer(csv_file)
        line.writerow(['id','brand','items','price'])
        time.sleep(0.5)
        print('Se scrie în csv:')
        for i in lista:
            print(i)
            line.writerow(i)
            time.sleep(0.5)


def from_csv(lista=cars, cars_csv=fisier_csv, cars_db=fisier_db):
    '''se verifică existența cars_csv, se crează o bază de date dacă nu există și se scrie în ea conținutul csv'''
    result = []
    if os.path.exists(cars_csv):
        print('Există fișierul csv {}'.format(cars_csv))
        with open(cars_csv, 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader, None) # nu se citește header
            for i in reader:
                result.append(i)
    else:
        print(f'Fișierul {fisier_csv} nu există!')

    return result



car_result = one_function(cars)

print(f'Valoarea totală a mașinilor de pe stoc este: {car_result[0]}\u20ac.')
print(f'Numărul total al mașinilor aflate pe stoc este: {car_result[1]}')

for i in car_result[2]:
    print(f'Valoarea totală a mașinilor marca {i[0]} este: {i[1]}\u20ac')

# se scrie cars în csv cars_stoc.csv
to_csv()

file = from_csv(cars, fisier_csv, fisier_db)
# print(file)
# se scrie în baza de date
to_db(file, sql_cars_table, fisier_db)