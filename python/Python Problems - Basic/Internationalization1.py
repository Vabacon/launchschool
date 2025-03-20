def greet(lang):
    match lang:
        case 'en':
            return('Hi!')
        case 'fr':
            return('Salut!')
        case 'pt':
            return('Olá!')



print(greet('en'))         # Hi!
print(greet('fr'))         # Salut!
print(greet('pt'))         # Olá!
