
def century(year):
    century = str(year / 100)
    if century[-1] == '0':
        print(century + 'th')
        return(century + 'th')
    elif century[-1] == '1' and century != '11':
        print(century + 'st')
        return(century + 'st')







print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
# print(century(1965) == "20th")          # True
# print(century(256) == "3rd")            # True
# print(century(5) == "1st")              # True
# print(century(10103) == "102nd")        # True
# print(century(1052) == "11th")          # True
# print(century(1127) == "12th")          # True
# print(century(11201) == "113th")        # True