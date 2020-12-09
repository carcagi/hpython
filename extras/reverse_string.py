# Reverse any string using for
def reverse_with_for(string1):
    string2 = ''
    for character in string1:
        string2 = character + string2
    return string2


print(reverse_with_for("Zapato"))
