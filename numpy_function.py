# On commence par toujour importer la librerie car elle externe a python et elle est ecrit en langage C
import numpy as np

# creons un tableau a partir de d'une liste
table = [1,2,3,4,5]
print(table)

# verifions le type de notre variable Table
print(type(table))

# definissons un tableau a 2 dimensions
table2 = np.array([[1,2,4,5], [3,4,5,6]])
print(table2)

# combien de dimention a table2
table2.ndim

# NB: un tableau a une dimention est appele vecteur, et celui de 2 dimension Matrice

# passons maintenant au tableau a 3 dimention
table3 = [
    [
        ['a','b','c'],
        ['d','e','f']
        ],
  [
      ['g','h','i'],
      ['j','k','k']
      ],
  [
      ['l','m','n'],
      ['o','p','q']
      ],
  [
      ['r','s','u'],
      ['v','w','x']
      ]
    ]
print(table3)

# nombre de dimension
table3.ndim

# maintenant accedons aux differnte valeur
# comme exercice nous allons acceder aux valeurs en pour ecrire le mot LIKE

# creation d'un table de zeros contenant 3 lignes et 3 colonnes, puis un autre contenant 3 ligne et 6 colonnes
tableau1 = np.zeros((3,3))
print("tableau 1 \n")
print(tableau1)
print("tableau 2 \n")
tableau2 = np.zeros((6,3))
print(tableau2)

#creation d'un tableau de 1 de 10 ligne et 3 connes
tableau3 = np.ones((10,3))
print(tableau3)

# la creation d'un tableau ayant 5 ligne et 5 colonne avec 1 en diagonal
tableau4 = np.eye(5)
print(tableau4)

# creation d'un tableau de donné automatique grace a la fonction ARANGE
tableau5 = np.arange(10)
print(tableau5)

# avec 2 parametre : debut et fin
tableau6 = np.arange(1,15)

# avec 3 parametre : debut,fin et pas d'incrementation
tableau6 = np.arange(1,17, 2)
print(tableau6)

# creation d'un tableau avec les valeurs aleatoire
tableau7 = np.random.randint(0,10,20)
print(tableau7)

# gener une sequence de nombre compris entre 2 nombre avec un ecart regulier
tableau8 = np.linspace(1,10,15)
print(tableau8)

# creation d'un tableau de valueurs aleatoires : les parametres sont lenombre de ligne et de colonnes
array_aleatoire = np.random.random(4,3)
print(array_aleatoire)

# Acceder aux element, selectionner, modifier et mettre a jour nunpy
array = np.arange(10)
print(array)

# selectionner le premier elemnent du tableau
print(array[0])

# modifier la troisieme valeur du tableau
array[2] = 15
print(array)

# selectionner les valeurs superieur ou egale a 5
valeurs = array[array > 5]
print(valeurs)

# au lieu de renvoyer les valeurs, renvoyer plutot leurs indices
indices = np.where(array > 5)
print(indices)

# remplacer toutes les valeurs inferieur  a 5 par la valeur zero
array[array < 5] = 0
print(array)

# les operation sur les tableau
tab1 = np.arange(5)
tab2 = np.random.randint(1,10,5)


# les fonctiond mathematique et statistique 

table_somme = np.sum(array)  # somme d'un tableau   
table_moyenne = np.mean(array) # la moyenne 
table_ecartType = np.sqrt(array) # racine carre de chaque valeur dans un tableau 
table_std = np.std(array) # 
table_max = np.max(array)
table_min = np.min(array)
table_abs = np.abs(array)
table_median = np.median(array)

# MANIPULATION DE TABLEAU 

# Produit de valeur a valeur 

a = np.array([[1, 2, 3],
                  [4, 5, 6]])
b = np.array([[2, 1, 3],
                  [3, 2, 1]])

Produit1 = a*b
print(Produit1)

# Produit de Matriciel Nb: l'operztion exige que les deux tableau ayent le meme nombre de ligne et colonnes

a2 = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [3, 2, 1]])
b2 = np.array([[2, 1, 3],
                  [3, 2, 1],[3, 2, 1]])

Produit_matriciel = np.dot(a2, b2)
print(Produit_matriciel)

# SLICING ET INDEXATION SELECTION 

# la premiere colonne de a2
sliced = a2[:, 0]
print(sliced)	

# une sous matrice 
sliced = a2[0:1,0:1]

# redimentionner un vecteur en tableau 
data = np.arange(20)
tableau = data.reshape(4,5)
print(tableau)

# ajouter un des element au tableau NB: Axis: determine la place d'ajout
ajout_tableau = np.append(tableau,[[0,0,0,0,0]],axis=0)
print(ajout_tableau)
