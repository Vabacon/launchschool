# def local_greet(str1):
#     lang = str1[0:2]
#     match lang:
#         case 'en':
#             if str1[3:5] == 'US':
#                 return('Hey')
#             elif str1[3:5] == 'GB':
#                 return('Hello')
#             elif str1[3:5] == 'AU':
#                 return('Howdy')
#         case 'fr':
#             return('Salut!')

def local_greet(str1):
    lang = str1.split('_')[0]
    match lang:
        case 'en':
            if str1.split('_')[1].split('.')[0] == 'US':
                return('Hey')
            elif str1.split('_')[1].split('.')[0] == 'GB':
                return('Hello')
            elif str1.split('_')[1].split('.')[0] == 'AU':
                return('Howdy')
        case 'fr':
            return('Salut!')

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!
print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!