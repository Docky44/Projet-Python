utilisateur = "Théo"
mot_de_passe = "Python3*"


class User:
    def __init__(self, pseudo, mdp):
        self.pseudo = pseudo
        self.mdp = mdp


def auth(pseudo, mdp):
    return pseudo == utilisateur and mdp == mot_de_passe


