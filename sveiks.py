def sveiks(vards):
    burts=vards[-1]
    if burts=='a' or burts=='e':
        return "Sveika, "+vards
    else:
        return "Sveiks, "+vards

print(sveiks("Anna"))
print(sveiks("Ivo"))
print
