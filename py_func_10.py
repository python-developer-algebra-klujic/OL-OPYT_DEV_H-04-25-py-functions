
broj = 50
print(broj)
print(id(broj))


def uvecaj_za_10():
    global broj
    print(id(broj))
    broj = broj + 10
    print(broj)


uvecaj_za_10()
print(broj)


print()
numbers = [1, 2, 3]
print(id(numbers))
print(numbers)

def add_number():
    # global numbers
    print(id(numbers))
    numbers.append(5)

add_number()
print(numbers)


print()
person ={
    'first_name': 'Pero',
    'last_name': 'Peric'
}
print(person)


def change_last_name():
    person['last_name'] = 'Anic'


change_last_name()
print(person)
