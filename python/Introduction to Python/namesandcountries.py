name = input("What is the name of the user you'd like to know the country of origin? ")

names_dictionary = {
    'Alice': 'USA',
    'Francois': 'Canada',
    'Inti': 'Peru',
    'Monika': 'Germany',
    'Sanyu': 'Uganda',
    'Yoshitaka': 'Japan',
}

print(names_dictionary[name] if name in names_dictionary else "Not found.")
