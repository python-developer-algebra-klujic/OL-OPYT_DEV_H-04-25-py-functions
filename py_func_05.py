


def generate_full_name(first_name:str, last_name:str = '') -> str:
    # full_name = f'{first_name} {last_name}'
    # return full_name
    if last_name == '':
        return f'{first_name}'
    else:
        return f'{first_name} {last_name}'



def podijeli(x, y):
    rezultat = x / y
    return rezultat


















first_name = 'Pero'
last_name = 'Peric'
full_name = generate_full_name(first_name, last_name)
print(full_name)

first_name = 'Ana'
# last_name = 'Anic'
full_name = generate_full_name(first_name)
print(full_name)

print( podijeli(5, 0)  )