#!/usr/bin/env python3

note1 = input("Donner une note : ")
note2 = input("Donner une note : ")
note3 = input("Donner une note : ")

# Penser a convertir les arguments en entiers avant de calculer la moyenne
moyenne = (float(note1)+float(note3)+float(note2))/3

print(f"La moyenne est {moyenne}")

# Trois façon de faire l'affichage de la mention

# Méthode 1 : on est malins, comme les conditions sont évaluées dans l'ordre,
# on part de la plus petite car seul le bloc de la première condition vraie
# sera exécuté
if moyenne < 10:
	print("ajournée")
elif moyenne < 12:
	print("passable")
elif moyenne < 14:
	print("AB")
elif moyenne < 16:
	print("B")
else:
	print("TB")

# Méthode 2 : On utilise le 'and' logique pour vérifier qu'on est assez haut et
# pas trop haut
if moyenne < 10 :
	print("ajournée")
elif moyenne >= 10 and moyenne < 12 :
	print("passable")
elif moyenne >= 12 and moyenne < 14:
	print("AB")
elif moyenne >=14 and moyenne < 16:
	print("B")
else:
	print("TB")

# Méthode 3 : forme contractée, on teste les deux conditions en même temps
if moyenne < 10 :
	print("ajournée")
elif 10 <= moyenne < 12 :
	print("passable")
elif 12 <= moyenne < 14:
	print("AB")
elif 14 <= moyenne < 16:
	print("B")
else :
	print("TB")


# Méthode 4 : ifs imbriqués
if moyenne < 10:
    print("Ajourné")
else:
    if not moyenne >= 12:
        print("Passable")
    else:
        if not moyenne >= 14:
            print("AB")
        else:
            if not moyenne >= 16:
                print("B")
            else:
                print("TB")
