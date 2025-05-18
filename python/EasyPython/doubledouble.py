
def twice(ddnum):
    ddnum_s = str(ddnum)
    if len(ddnum_s) % 2 != 0:
        return(ddnum * 2)

    return ddnum if ddnum_s[:len(ddnum_s) // 2] == ddnum_s[len(ddnum_s) // 2:] else ddnum * 2




print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True