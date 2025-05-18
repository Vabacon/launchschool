
def triangle(size):
    spaceRowMultiplier = size - 1
    starRowMultiplier = 1
    
    for row in range(size):
        spaces = spaceRowMultiplier * ' '
        stars = starRowMultiplier * '*'
        print(spaces + stars)
        spaceRowMultiplier -= 1
        starRowMultiplier += 1

triangle(5)
triangle(10)
triangle(15)