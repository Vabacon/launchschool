def is_empty_or_blank(str1):
    return(str1.isspace() or str1 == '')

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True