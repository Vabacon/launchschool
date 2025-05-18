
def get_grade(g1, g2, g3):
    average_grade = (g1 + g2 + g3) / 3

    if average_grade >= 90:
        return("A")
    elif average_grade >= 80:
        return("B")
    elif average_grade >= 70:
        return("C")
    elif average_grade >= 60:
        return("D")
    elif average_grade >= 50:
        return("F")


print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True