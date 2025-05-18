# NOT COMPLETED, will need to study this.
def clean_up(string):
    symbole_list = []
    for char in string:
        if not char.isalpha():
            symbole_list += [char]
    symbole_list = (list(set(symbole_list)))
    for elem in symbole_list:
        string = string.replace(elem, ' ')

    string = (' ').join(string.split())
    return(' ' + string + ' ')




print(clean_up("---what's my +*& line?") == " what s my line ") # True