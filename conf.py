#coding:utf-8
CSV_DELIMITER       = ';'
CSV_QUOTE_CHAR      = '"'
CSV_ESCAPE_CHAR     = '\\'

FIRSTNAME = ("Gabriel","Léo","Raphaël","Arthur","Louis","Lucas","Adam","Jules","Hugo","Maël","Liam","Noah","Paul","Ethan","Tiago","Sacha","Gabin","Nathan","Mohamed","Aaron","Tom","Éden","Théo","Noé","Léon","Martin","Mathis","Nolan","Victor","Timéo","Enzo","Marius","Axel","Antoine","Robin","Isaac","Naël","Amir","Valentin","Rayan","Augustin","Ayden","Clément","Eliott","Samuel","Marceau","Baptiste","Gaspard","Maxence","Yanis","Malo","Ibrahim","Sohan","Maxime","Évan","Nino","Mathéo","Simon","Lyam","Alexandre","Imran","Naïm","Kaïs","Camille","Thomas","Milo","Ismaël","Côme","Owen","Lenny","Soan","Ilyan","Kylian","Noa","Oscar","Ilyes","Léandre","Pablo","Diego","Mathys","Joseph","Ayoub","Youssef","Wassim","Noam","Adem","William","Ali","Basile","Charles","Thiago","Antonin","Logan","Adrien","Marin","Jean","Charly","Esteban","Noham","Elio","Emma","Jade","Louise","Alice","Lina","Chloé","Rose","Léa","Mila","Ambre","Mia","Anna","Julia","Inès","Léna","Juliette","Zoé","Manon","Agathe","Lou","Lola","Camille","Nina","Jeanne","Inaya","Romy","Éva","Romane","Léonie","Iris","Lucie","Luna","Adèle","Sarah","Louna","Charlotte","Margaux","Olivia","Sofia","Charlie","Victoria","Victoire","Nour","Margot","Mya","Giulia","Clémence","Alix","Aya","Clara","Éléna","Capucine","Lana","Lya","Lyna","Lyana","Théa","Léana","Anaïs","Gabrielle","Emy","Yasmine","Mathilde","Maëlys","Alicia","Lilou","Apolline","Roxane","Lise","Assia","Élise","Lily","Maria","Maya","Valentine","Héloïse","Marie","Noémie","Elsa","Lisa","Lila","Alya","Thaïs","Ilyana","Célia","Candice","Livia","Zélie","Salomé","Constance","Soline","Emmy","Maëlle","Éléna","Maryam","Amelia","Joy","Océane","Maïssa","Arya")
LASTNAME  = ("Martin","Bernard","Thomas","Petit","Robert","Richard","Durand","Dubois","Moreau","Laurent","Simon","Michel","Lefèvre","Leroy","Roux","David","Bertrand","Morel","Fournier","Girard","Bonnet","Dupont","Lambert","Fontaine","Rousseau","Vincent","Muller","Lefevre","Faure","Andre","Mercier","Blanc","Guerin","Boyer","Garnier","Chevalier","Francois","Legrand","Gauthier","Garcia","Perrin","Robin","Clement","Morin","Nicolas","Henry","Roussel","Mathieu","Gautier","Masson","Marchand","Duval","Denis","Dumont","Marie","Lemaire","Noel","Meyer","Dufour","Meunier","Brun","Blanchard","Giraud","Joly","Riviere","Lucas","Brunet","Gaillard","Barbier","Arnaud","Martinez","Gerard","Roche","Renard","Schmitt","Roy","Leroux","Colin","Vidal","Caron","Picard","Roger","Fabre","Aubert","Lemoine","Renaud","Dumas","Lacroix","Olivier","Philippe","Bourgeois","Pierre","Benoit","Rey","Leclerc","Payet","Rolland","Leclercq","Guillaume","Lecomte","Lopez","Jean","Dupuy","Guillot","Hubert","Berger","Carpentier","Sanchez","Dupuis","Moulin","Louis","Deschamps","Huet","Vasseur","Perez","Boucher","Fleury","Royer","Klein","Jacquet","Adam","Paris","Poirier","Marty","Aubry","Guyot","Carre","Charles","Renault","Charpentier","Menard","Maillard","Baron","Bertin","Bailly","Herve","Schneider","Fernandez","Le Gall","Collet","Leger","Bouvier","Julien","Prevost","Millet","Perrot","Daniel","Le Roux","Cousin","Germain","Breton","Besson","Langlois","Remy","Le Goff","Pelletier","Leveque","Perrier","Leblanc","Barre","Lebrun","Marchal","Weber","Mallet","Hamon","Boulanger","Jacob","Monnier","Michaud","Rodriguez","Guichard","Gillet","Etienne","Grondin","Poulain","Tessier","Chevallier","Collin","Chauvin","Da Silva","Bouchet","Gay","Lemaitre","Benard","Marechal","Humbert","Reynaud","Antoine","Hoarau","Perret","Barthelemy","Cordier","Pichon","Lejeune","Gilbert","Lamy","Delaunay","Pasquier","Carlier","Laporte")
COMMENT   = ("Une véritable \"machine\" de guerre.", "Un terminator.", "Sauve des vies chaque jour passant.", "A trouvé du pétrole mais continue de creuser.", "Dangereux à la mer, inutile à quai.", "S/O, il brille par ailleurs au Sudoku.", "Qui est cette personne ?", "Présent.")


'''
PARAMETRAGE DES COLONNES CSV A ANONYMISER

SYNTAXE:
"nom_de_la_colonne":TYPE de valeur randomizée à utiliser en remplacement des valeurs de cette colonne

Liste des TYPES de valeurs:
    - LASTNAME  -> nom de famille   (pris du dictionnaire LASTNAME)
    - FIRSTNAME -> prénom           (pris du dictionnaire FIRSTNAME)
    - COMMENT   -> commentaire      (pris du dictionnaire COMMENT)
    - "intXX"   -> nombre entier de longueur XX (attention: ne pas oublier les "")

Exemple:
    "NOM":          LASTNAME,
    "PRENOM":       FIRSTNAME,
    "IDENTIFIANT":  "int8",
    "COMMENTAIRE":  COMMENT

'''
COLUMN_TO_ANONYMIZE = {     # 0002
                            "NACHN":    LASTNAME,       # NOM       (0002)
                            "VORNA":    FIRSTNAME,      # PRENOM    (0002)
                            "YYID1":    "int10",        # NID       (0002)
                            "YYPN2":    FIRSTNAME,      # PRENOM2   (0002)
                            "YYPN3":    FIRSTNAME,      # PRENOM3   (0002)

                            # 0185
                            "ICNUM":    "int9",         # MLE MN

                            # 9533  (not off)
                            "GRNOQD":   LASTNAME,       # Grade/nom_notateur/fonction
                            "BILOBS":   COMMENT,
                            "COMDEN":   COMMENT,
                            "ADAEMP":   COMMENT,
                            "COGERE":   COMMENT,
                            "RESROB":   COMMENT,
                            "COMEVE":   COMMENT,
                            "COMTEC":   COMMENT,
                            "GRNOQU":   LASTNAME,
                            "GRNOQAS":  LASTNAME
}