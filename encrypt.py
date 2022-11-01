from fcheck import *

keys = {
    # Character spécial
    " ": "%_%",
    # Lettres minuscules
    "a": "%10",
    "b": "%20",
    "c": "%30",
    "d": "%40",
    "e": "%50",
    "f": "%60",
    "g": "%70",
    "h": "%80",
    "i": "%90",
    "j": "%11",
    "k": "%21",
    "l": "%22",
    "m": "%23",
    "n": "%24",
    "o": "%25",
    "p": "%26",
    "q": "%27",
    "r": "%28",
    "s": "%29",
    "t": "%31",
    "u": "%32",
    "v": "%33",
    "w": "%34",
    "x": "%35",
    "y": "%36",
    "z": "%37",
    # Lettres majuscules
    "A": "@10",
    "B": "@20",
    "C": "@30",
    "D": "@40",
    "E": "@50",
    "F": "@60",
    "G": "@70",
    "H": "@80",
    "I": "@90",
    "J": "@11",
    "K": "@21",
    "L": "@22",
    "M": "@23",
    "N": "@24",
    "O": "@25",
    "P": "@26",
    "Q": "@27",
    "R": "@28",
    "S": "@29",
    "T": "@31",
    "U": "@32",
    "V": "@33",
    "W": "@34",
    "X": "@35",
    "Y": "@36",
    "Z": "@37"
}

# Vérifie si le fichier exist
def encrypt(nom_fichier):
    if not verif_file(f'./files/{nom_fichier}'):
        return "Le fichier n'a pas été trouvé !"

# Crypt le fichier
    file = open(f'./files/{nom_fichier}', 'r')
    lines = file.readlines()
    file.close()
    ls = []
    for line in lines:
        lne = line.replace('\n', '')
        for k in keys:
            lne = lne.replace(k, keys[k])
        ls.append(lne)
    write_file(nom_fichier, ls)
    return "Le fichier a bien été crypté !"


def decrypt(nom_fichier):
    if not verif_file(f'./files/{nom_fichier}'):
        return "Le fichier n'a pas été trouvé !"

# Décrypt le fichier
    file = open(f'./files/{nom_fichier}', 'r')
    lines = file.readline().split(' ')
    file.close()
    ls = []
    for line in lines:
        lne = line
        for k in keys:
            lne = lne.replace(keys[k], k)
        ls.append(lne)
    write_file(nom_fichier, ls, "decrypt")
    return "Le fichier a bien été décrypté !"
