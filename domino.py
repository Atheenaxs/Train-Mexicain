from tkinter import *
from random import randint
from classPile import *
from classDomino import *
from classJeuMexicain import *
from classJoueur import *

################################################################################
## l'initialisation des fonctions et creation du jeu
################################################################################

jMexicain = JeuMexicain()
albert = Joueur(jMexicain.pioche)
mauricette = Joueur(jMexicain.pioche)
ginette = Joueur(jMexicain.pioche)
maurice = Joueur(jMexicain.pioche)
jMexicain.ajouterjoueur(albert)
jMexicain.ajouterjoueur(mauricette )
jMexicain.ajouterjoueur(ginette)
jMexicain.ajouterjoueur(maurice)
jMexicain.choisirjoueur()
partiefinie=False
gagnant=0

################################################################################
# La fonction principal du jeu 
################################################################################

def jouer() :
    if partiefinie() :
        donothing()
    else :
        jMexicain.jouer()
        afficherreserve()
        afficherTrains()
        afficherdominodepart() 
        activationGo()


################################################################################
# D'autres fonctions
################################################################################
# La fonction actvation du bouton  
def activationGo():
    btn1['state']="active"
    btn1.config(bg='#674064',fg='white')
 
# la fonction qui affiche la reserve de maurice   
def afficherreserve():
    global photoR,maurice
    for i in range(1,4):
        for j in range(5):
            if (i-1)*5+j < len(jMexicain.joueuractuel.reserve):
                photoR[i-1][j]=PhotoImage(file='image\\petit-'+str(jMexicain.joueuractuel.reserve[(i-1)*5+j].A) +'-'+str(jMexicain.joueuractuel.reserve[(i-1)*5+j].B)+'.gif')
            else:
                photoR[i-1][j]=PhotoImage(file="image\\petit--1--1.gif")
    for i in range(3) :
        for j in range(5) :
            reserve.create_image(20+70*j,10+35*i, image=photoR[i][j],anchor=NW) 



# La fonction qui permet d'afficher les trains des joueurs et le train Mexicain  
def afficherTrains():
    global photo,jMexecain
    for i in range(1,6) :
        if i!=1   :
            l=min(5,jMexicain.joueurs[i-2].train.taille())
            for j in range(l):
                dom=jMexicain.joueurs[i-2].train.lesElts[jMexicain.joueurs[i-2].train.taille()-l+j]
                photo[i-1][j]=PhotoImage(file='image\\petit-'+str(dom.A) +'-'+str(dom.B)+'.gif')       
        else :
            l=min(5,jMexicain.trainM.taille()) 
            for j in range(l):
                dom=jMexicain.trainM.lesElts[jMexicain.trainM.nb-l+j]
                photo[i-1][j]=PhotoImage(file='image\\petit-'+str(dom.A) +'-'+str(dom.B)+'.gif')              
    for i in range(5) :
        for j in range(5) :
            trains.create_image(20+70*j,10+50*i, image=photo[i][j], anchor=NW)    


# La fonction qui permet l'affichage du domino de depart
def afficherdominodepart() :
    global photoD,jMexecain
    dom=jMexicain.dominoDepart
    photoD=PhotoImage(file='image\\petit-'+str(dom.A) +'-'+str(dom.B)+'.gif') 
    dominodepart.create_image(20,5, image=photoD,anchor=NW)     


# La fonction qui ouvre la fenetre de la fin du jeu
def donothing():
    filewin = Toplevel(fen)
    chaine='La partie est terminée, le gagnant est : \n\n'+nomdujoueur(gagnant)
    butt = Button(filewin, text=chaine)
    but=Button(filewin,text='quitter',command=fen.quit)
    butt.pack()
    but.pack()
    
 
 
 # La fonction indicatrice de la fin de la partie   
def partiefinie() :
    global gagnant
    for j in jMexicain.joueurs :
        if j.nombreDominosReserve == 0 :
            gagnant=j
    if jMexicain.piocheVide() :
        gagnant=jMexicain.joueurs[0]
        for j in jMexicain.joueurs :
            if j.valeurReserve() <gagnant.valeurReserve() :
                gagnant=j
    if gagnant!=0 :
        return True
    return False

# la fonction qui retourne le nom du joueur
def nomdujoueur(j) :
    if j==albert :
        return 'Albert'
    elif j==mauricette :
        return 'Mauricette'
    elif j==ginette :
        return 'Ginette'
    else  :
        return 'Maurice'

################################################################################
# La construction des frames et des canvas et...
################################################################################

# Fenetre principale
fen = Tk()
fen.title('Train Mexicain')
fen.geometry("600x520")
fen.config(bg='#d9d2e9')


# l'initialisation des images des domino ou domino vide
i=1
photo=[] # les images sur les trains
for i in range(5) :
    photos=[]
    for j in range(5) :
        photos.append(PhotoImage(file="image\\petit--1--1.gif"))
    photo.append(photos)
photoR=[] # les images de la reserve
for i in range(3) :
    photos=[]
    for j in range(5) :
        photos.append(PhotoImage(file="image\\petit--1--1.gif"))
    photoR.append(photos)
photoD=PhotoImage(file="image\\petit-1-1.gif") # l'image domino de depert

# actualise le nom des joueurs
def reservedequi():
    if btn1['state']== "active":
        lbl22.config(text='Reserve de '+nomdujoueur(jMexicain.joueuractuel))
        lbl44.config(text=nomdujoueur(jMexicain.joueuractuel))

# combine des fonctions
def two_funcs(*funcs):
    def two_funcs(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return two_funcs


# frame 3 : domino de départ
frm3=Frame(fen)
frm3.config(bg='#d9d2e9')
lbl11= Label(frm3, text='Domino de départ',bg='#674064',fg='white',font=17)
dominodepart=Canvas(frm3,width=95, height=50, bg='#d9d2e9',highlightthickness=0)
lbl11.grid(row=1, column=1)
dominodepart.grid(row=1,column=3,rowspan=1,padx=5,pady=5)
frm3.pack(side=TOP)

# frame 1 : Les trains des joueurs , les noms des joueurs
frm1=Frame(fen)
frm1.config(highlightthickness=0)
trains=Canvas(frm1,width=420, height=250,bg='#d9d2e9',highlightthickness=0)
trains.grid(row=1,column=3,rowspan=5,padx=5,pady=5)
frm1.pack(side=TOP)
lbl1 = Label(frm1, text='Train Mexicain',fg='#5b3959',font=("Arial",12))
lbl2 = Label(frm1, text='Albert',fg='#5b3959',font=("Arial",12))
lbl3 = Label(frm1, text='Mauricette',fg='#5b3959',font=("Arial",12))
lbl4 = Label(frm1, text='Ginette',fg='#5b3959',font=("Arial",12))
lbl5 = Label(frm1, text='Maurice',fg='#5b3959',font=("Arial",12))
lbl1.grid(row=1,column=1)
lbl2.grid(row=2,column=1)
lbl3.grid(row=3,column=1)
lbl4.grid(row=4,column=1)
lbl5.grid(row=5,column=1)

#frame 4 : Bouton GO!
frm4=Frame(fen)
frm4.config(bg='#d9d2e9')
btn1 = Button(frm4, width=10, height=1,text='GO!',command=two_funcs(jouer,reservedequi))
btn1.grid(row=4,column=2,padx=5,pady=5)
lbl44=Label(frm4, text=nomdujoueur(jMexicain.joueuractuel),font=("Arial",13),fg='#674064')
lbl44.grid(row=4,column=1,padx=5,pady=5)
frm4.pack(side=BOTTOM)


# frame 2 :reserve
frm2=Frame(fen)
lbl22=Label(frm2, text='Reserve de '+nomdujoueur(jMexicain.joueuractuel),fg='#5b3959',font=("Arial",10))
reserve=Canvas(frm2,width=420, height=120)
lbl22.grid(row=2,column=1,columnspan=2)
reserve.grid(row=1,column=3,rowspan=3,padx=5,pady=5)
frm2.pack(side=BOTTOM)



# initialisation
btn1['state']="disabled"
afficherreserve()
afficherTrains()
afficherdominodepart()
activationGo()

# lancer la fenetre

fen.mainloop()
fen.destroy()