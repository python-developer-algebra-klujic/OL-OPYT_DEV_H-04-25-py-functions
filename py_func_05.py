


def generate_full_name(first_name:str, last_name:str = '') -> str:
    # full_name = f'{first_name} {last_name}'
    # return full_name
    if last_name == '':
        return f'{first_name}'
    else:
        return f'{first_name} {last_name}'



def podijeli(x:int, y:int) -> float:
    """Funkcija koja vraca rezutat dijeljnja. Ako je y = 0 onda ce vratiti -1
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    
    if y != 0:
        return x / y
    else:
        # return 'Nije dopusteno dijeliti s nulom'
        return -1.0


















first_name = 'Pero'
last_name = 'Peric'
full_name = generate_full_name(first_name, last_name)
print(full_name)

first_name = 'Ana'
# last_name = 'Anic'
full_name = generate_full_name(first_name)
print(full_name)


x = 5
y = 8
rezultat = podijeli(x, y)

if rezultat == -1:
    print(f'Nije moguce dijeliti s nulom (y ima vrijendost {y}).')
else:
    print(f'Rezutat dijeljnje je: {rezultat:.3f}')
