
# def contains(location, destinations):
#     for city in destinations:
#         if city == location:
#             return('True')
        
#     return('False')

def contains(location, destination):
    return(location in destination)

destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

print(contains('Barcelona', destinations))  # True
print(contains('Nashville', destinations))  # False