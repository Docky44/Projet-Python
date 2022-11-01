import os


def is_file_present(path):
    return os.path.isfile(path)


def is_directory_present(path):
    return os.path.isdir(path)


def is_present(path):
    return os.path.exists(path)


def write_file(file_name, content, method="crypt"):
    if not is_directory_present("./result"):
        os.mkdir("./result")

    assert method == "crypt" or method == "decrypt"
    derniere_method = "crypt" if method == "decrypt" else "decrypt"
    # Créer un nouveau fichier vide
    file = open(f'./result/[{method}]{file_name.replace(f"[{derniere_method}]", "")}', 'x')
    file.close()
    # Remplacez le contenu de ce fichier par le contenu crypté 
    file = open(f'./result/[{method}]{file_name.replace(f"[{derniere_method}]", "")}', 'w')
    ls = []
    for line in content:
        n_line = " " if method == "crypt" else "\n"
        ls.append(f'{line}{n_line}')
    file.writelines(ls)
    file.close()

# Vérifie si le fichier exist
def verif_file(file_path):
    if not is_present(file_path):
        print("")
        print("[==========] ERREUR [==========]")
        print("Ce fichier n'existe pas !")
        print("[==========] ERREUR [==========]")
        print("")
        return False
    return True
