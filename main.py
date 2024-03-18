import random

class PuissanceQuatre:

    def __init__(self, nb_colonne:int=7, nb_ligne:int=6):
        """
        PuissanceQuatre, int -> NoneType
        Construit un puissance quatre de dimension self.nb_colonne x self.nb_ligne
        """
        assert nb_colonne > 0, "Le nombre de colonnes doit être plus grand que 0"
        assert nb_ligne > 0, "Le nombre de lignes doit être plus grand que 0"
        self.nb_colonne:int = nb_colonne
        self.nb_ligne:int = nb_ligne
        self.__plateau:list = [[-1 for _ in range(self.nb_colonne)] for _ in range(self.nb_ligne)]
        self.carac:list = ['O', 'X']
        self.__dernier_coup:tuple = (-1, -1)
        return

    def carac_(self, joueur_:int):
        """
        PuissanceQuatre, int -> str
        Renvoie la marque sur le pion du joueur.
        """
        assert -1 <= joueur_ <= len(self.carac)-1, "Le numéro du joueur doit être égal à 0 ou 1, s'il est à -1, retournera vide"
        if joueur_ == -1:
            return ' '
        return self.carac[joueur_]
    
    def ligne_trait(self):
        """
        PuissanceQuatre -> NoneType
        Affiche le trait d'une ligne de PuissanceQuatre
        """
        print(''.join(['+'] + ["-+" for _ in range(self.nb_colonne)]))
        return
    
    def affiche_ligne(self, ligne:int):
        """
        PuissanceQuatre, int -> NoneType
        Affiche une ligne choisie de PuissanceQuatre
        """
        print(''.join(['|'] + [self.carac_(self.__plateau[ligne][i]) + '|' for i in range(self.nb_colonne)]))
        return
    
    def __str__(self):
        """
        PuissanceQuatre -> NoneType
        Affiche le plateau de PuissanceQuatre
        """
        print(''.join([' '] + [str(i) + ' ' for i in range(self.nb_colonne)]))
        self.ligne_trait()
        for i in range(self.nb_ligne):
            self.affiche_ligne(i)
            self.ligne_trait()
        return ''
    
    def colonne_valide(self, indice_colonne:int):
        """
        PuissanceQuatre, int -> bool
        Vérifie que indice_colonne est bien un indice de colonne et que il y a au moins une case libre dans cette colonne.
        """
        if type(indice_colonne) != int or not 0 <= indice_colonne <= self.nb_colonne-1 or self.__plateau[0][indice_colonne] != -1:
            return False
        return True
    
    def pose_colonne(self, choix_:int, joueur_:int):
        """
        PuissanceQuatre, int, int -> bool
        Fais tomber un pion dans la colonne choix_ du joueur_
        """
        if not self.colonne_valide(choix_):
            print("Veuillez saisir une colonne qui n'est pas remplie")
            return False
        
        for i in range(len(self.__plateau)-1, -1, -1):
            if self.__plateau[i][choix_] == -1:
                self.__plateau[i][choix_] = joueur_
                self.__dernier_coup = (i, choix_)
                break
        return True

    def coords_valide(self, num_ligne:int, num_colonne:int):
        """
        PuissanceQuatre, int, int -> bool
        Vérifie que les coordonnées passées en paramètre soient bien valides
        """
        return 0 <= num_ligne <= self.nb_ligne-1 and 0 <= num_colonne <= self.nb_colonne-1
    
    def compte_valeur(self, lig:int, col:int, val:int, inc_lig:int, inc_col) :
        """
        PuissanceQuatre, int, int, int, int, int -> int
        Retourne le nombre de cases de valeur val à partir de (lig,col) dans la direction (inc_lig, inc_col)
        """
        distance:int = 0
        while self.coords_valide(lig+inc_lig, col+inc_col):
            lig += inc_lig
            col += inc_col
            if self.__plateau[lig][col] == val:
                distance += 1
            else:
                break
        return distance
    
    def partie_finie(self):
        """
        PuissanceQuatre -> bool
        Vérifie si la partie est finie
        """
        joueur_:int = self.__plateau[self.__dernier_coup[0]][self.__dernier_coup[1]]
        if self.__dernier_coup[0] != -1 and self.__dernier_coup[1] != -1:
            if self.compte_valeur(self.__dernier_coup[0], self.__dernier_coup[1], joueur_, -1, -1) + self.compte_valeur(self.__dernier_coup[0], self.__dernier_coup[1], joueur_, 1, 1) + 1>= 4 or self.compte_valeur(self.__dernier_coup[0], self.__dernier_coup[1], joueur_, 1, -1) + self.compte_valeur(self.__dernier_coup[0], self.__dernier_coup[1], joueur_, -1, 1) + 1>= 4 or self.compte_valeur(self.__dernier_coup[0], self.__dernier_coup[1], joueur_, 1, 0) + self.compte_valeur(self.__dernier_coup[0], self.__dernier_coup[1], joueur_, -1, 0) + 1>= 4 or self.compte_valeur(self.__dernier_coup[0], self.__dernier_coup[1], joueur_, 0, 1) + self.compte_valeur(self.__dernier_coup[0], self.__dernier_coup[1], joueur_, 0, -1) + 1>= 4:
                print(f"La partie est terminée, {self.carac_(joueur_)} a gagné !")
                return True
        
        for i in range(self.nb_colonne):
            if self.colonne_valide(i):
                break
        else:
            return True
        return False
    
### script principal
if __name__ == '__main__' :
    p4:PuissanceQuatre = PuissanceQuatre()
    joueur:int = random.randint(0,1)
    while not p4.partie_finie():
        print(p4)
        print("Aux",p4.carac_(joueur),"de jouer")
        choix = int(input("Dans quelle colonne voulez-vous jouer ? "))
        res = p4.pose_colonne(choix,joueur)
        if not res:
            print("Non, ce n’est pas possible.")
        else:
            joueur = (joueur + 1) % 2
    print(p4)
    print("Partie finie. Bravo")
