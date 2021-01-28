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


def big_brand_value(lista):
    '''cea mai mare valoare de brand'''
    lista.sort(key=el_doi(1))
    lista = lista[-1]
    return lista

def car_brand_value(lista=cars):
    '''valoarea mașinilor per brand'''
    lista_brand = []
    for i in lista:
        lista_brand.append((i[1], i[2] * i[3]))
    return lista_brand

def total_cars(lista=cars):
    '''totalul mașinilor de pe stoc'''
    totalcars = 0
    for i in lista:
        totalcars += i[2]
    return totalcars


def total_car_value(lista=cars):
    '''valoarea totală a mașinilor de pe stoc'''
    value = 0
    for i in lista:
        value += i[3] * i[2]
    return value


masini_totale = total_cars()
valoare_totala = total_car_value()
valoare_brand = car_brand_value()
max_valoare_brand = big_brand_value(valoare_brand)


print(masini_totale)
print(valoare_totala)
print(valoare_brand)
print(max_valoare_brand)

# total_sum = sum(zip(cars[3]))
# help(zip)
# print(total_sum)