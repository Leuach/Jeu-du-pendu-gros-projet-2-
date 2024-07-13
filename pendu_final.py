# -*- coding: utf-8 -*-

from random import randint
from tkinter import *

mafenetre=Tk()
mafenetre.geometry("200x280")
mafenetre.title("Pendu !!")

dessin = Canvas(mafenetre, width=200, height=150)
dessin.pack()

essai=1
gagne=False
lettre_prop="" #liste des lettres proposées

information3=Label(master=mafenetre,text="")
information2=Label(master=mafenetre,text="Lettre(s) utilisée(s) : "+lettre_prop)
information=Label(master=mafenetre,text="Essai %d Entrez votre proposition"%(essai))

saisie=Entry(mafenetre,width=15)

##########################################################################
def valider():
    global essai,information,information2,lettre_prop,gagne
    print("valider essai=%d"%(essai))
    
    if(essai>=12):
        information.config(text="Le mot à trouver était : "+inconnu)
        information2.config(text="PERDU!!!! TOTO est mort !")
        gagne=True
    
    if(gagne==False):
        proposition=saisie.get()
        proposition=proposition.replace('é','e')
        proposition=proposition.replace('è','e')
        proposition=proposition.strip()
        leng=len(proposition)
        
        if(leng==1):  #une seule lettre a été saisie
            lettre_prop=lettre_prop+proposition
            indice=""
            information.config(text=show_lettre(lettre_prop,inconnu,indice))
            information2.config(text="Lettre(s) utilisée(s) : "+lettre_prop)
        else : #le joueur a entré un mot
            if (proposition==inconnu):
                information2.config(text="TOTO est sauvé !")
                information.config(text="Bravo vous avez trouvé en %d coups !"%(essai))
                gagne=True
            else:
                information.config(text="Essai %d Entrez votre proposition"%(essai))
        pendu(100,40,"blue",essai)
        essai+=1
    

##########################################################################"""
def pendu(x,y,couleur,etape):
    #print("etape=%d"%(etape))
    
    #potence
    if(etape==1):  #plancher
        dessin.create_line(10, y+80, 90, y+80, fill=couleur, width=4)
    
    if(etape==2):  #barre verticale
        dessin.create_line(30, y+80, 30, 20, fill=couleur, width=4)
        
    if(etape==3):  #barre horirontale haute
        dessin.create_line(20, 20, 120, 20, fill=couleur, width=4)
        
    if(etape==4):  #barre oblique
        dessin.create_line(30, 40, 50, 20, fill=couleur, width=4)
    
    if(etape==5):  #haut corde
        dessin.create_line(x, 20, x, y-10, fill=couleur, width=4)
        
    if(etape==6):#tete
        dessin.create_oval(x-10,y-10,x+10,y+10,fill=couleur,width=4,outline=couleur)
    
    #colonne vertébrale
    if(etape==7):
        dessin.create_line(x, y+10, x, y+40, fill=couleur, width=4)
    
    #jambe droite
    if(etape==8):
        dessin.create_line(x, y+40, x+20, y+60, fill=couleur, width=4)
    
    #jambe droite
    if(etape==9):
        dessin.create_line(x, y+40, x-20, y+60, fill=couleur, width=4)
    
    #bras droit
    if(etape==10):
        dessin.create_line(x, y+15, x+20, y+30, fill=couleur, width=4)
    
    #bras gauche
    if(etape==11):
        dessin.create_line(x, y+15, x-20, y+30, fill=couleur, width=4)

###############################################################################"
#let : string avec les lettres proposées depuis le début de la partie
#inc : mot à trouver
#indic : chaine de caractère donnant les lettres bien placées
def     show_lettre(let,inc,indic): 
    nombre=0
    indic=""
    #print("show lettre inc=|%s| len(inc)=%d let=|%s|"%(inc,len(inc),let))
    
    for i in range(len(inc)):
        rep="_"
        for j in range(len(let)):
            if(inc[i]==let[j]):
                if(j==(len(let)-1)):
                    nombre+=1  #ajoute la lettre à celles qui sont trouvées
                rep=inc[i]
                break
            else:
                rep="_"
        indic=indic+rep
        
    return("%d placement(s) correct(s) :|%s|"%(nombre,indic))    

def choisi_mot():
    global inconnu
    #ouvre et lit le fichier contenant tout les mots francais
    fichier=open('liste.de.mots.francais.frgut.txt')
    texte=fichier.readlines()  #lit toutes les lignes du fichier texte
    fichier.close()

    taille=len(texte)

    longueur=-1
    #tirage au sort d'un mot inconnu entre 6 et 3 lettres
    while (longueur>6) or (longueur<3):
        nombre = randint(0,taille-1)
        inconnu=texte[nombre]
        inconnu=inconnu.strip() #retire le \0 final
        inconnu=inconnu.replace('é','e')
        inconnu=inconnu.replace('î','i')
        inconnu=inconnu.replace('è','e')
        longueur=len(inconnu)
    information3.config(text="Mot de %d lettres, début : %c"%(len(inconnu),inconnu[0]))
    
###############################################################################"

bouton_valider=Button(mafenetre,text="valider",command=valider)

saisie.pack()
information3.pack()
information2.pack()
information.pack()
bouton_valider.pack()
    
choisi_mot()
mainloop()        
       
