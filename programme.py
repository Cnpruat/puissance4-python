import tkinter as tk
from tkinter import ttk
import time,copy
import gestion_fichier as sv

C = ['red', 'black', 'white', '#3481F8',"#183c74", '#818181', 'blue'] #Couleurs utilisé dans le code
Cjoueurs = ['Blue', 'Green', 'Red', 'Cyan', 'Magenta', 'Yellow', 'Black', 'Purple'] #Couleurs utilisable par les joueurs
pro = False
etat_jeu = False
tour = 0
L1 = []
L2 = []
CJ1 = int()
CJ2 = int()
nom = './user/'
flag= 0
depart = 0
v_ini = 0
d = 0
liste_mat = []

#%% Chronomètre
def lancer_chrono():
    global depart, flag #flag fonction dans python
    flag=1
    depart = time.time()
    top_horloge()
def arreter_chrono():
    global flag
    flag=0 
def top_horloge():
    global depart,flag
    y=time.time()-depart    
    minutes = time.localtime(y)[4]
    secondes = time.localtime(y)[5]
    if flag :
        l_chrono.configure(text = "%i min %i sec " %(minutes,secondes))
    fen.after(1000,top_horloge)
def decompte():
    global d
    d = 16
    dec()
def dec():
    global d, tour, etat_jeu
    if etat_jeu: 
        d-=1
        l_decompte.configure(text = 'Temps restant : '+str(d)+'s')
        if d==0 :
            tour +=1
            d = 16
            for w in fr2.winfo_children():
                w.destroy()
            if tour%2==0 :
                Label1 = tk.Label(fr2,text = "Tour de "+str(L2[0]), fg = C[2],font=('Arial',20),bg=C[4])
                Label1.pack()
            if tour%2==1:
                Label1 = tk.Label(fr2,text = "Tour de "+str(L1[0]), fg = C[2],font=('Arial',20),bg=C[4])
                Label1.pack()
        fen.after(1000, dec)
    elif etat_jeu is False:
        return
    
    

#%% 
def affichage_mat(JEU): #Affiche les pions à partir de la matrice JEU
    for ligne in range(6):
        for colonne in range(7):
            x = (colonne+1)*100+10
            y = ligne*100+110
            if JEU[ligne][colonne] == 1:
                Zone.create_oval(x, y, x+80, y+80, fill=Cjoueurs[CJ1])
            elif JEU[ligne][colonne] == 2:
                Zone.create_oval(x, y, x+80, y+80, fill=Cjoueurs[CJ2])

def matrice(): #création matrice 6x7 avec des 0
    A=[]
    for i in range (6):
        B=[]
        for j in range (7):
            B.append(0)
        A.append(B)
    return A

def VerificationVictoire (i,j):
    VV = False  
    VerifVertic = False
    a = 0
    while a<4 and i+a<6 and JEU[i][j]==JEU[i+a][j]:
        a += 1
    if a>=4:
        VerifVertic = True
     
    VerifHorizontal = False
    b = 0
    while b<4 and j-b>=0 and JEU[i][j]==JEU[i][j-b]:
        b += 1
    c = 0
    while c<4 and j+c<7 and JEU[i][j]==JEU[i][j+c]:
        c += 1
    if b + c - 1 >= 4:
        VerifHorizontal = True
       
    VerifDiago1 = False
    d = 0
    while d<4 and i-d>=0 and j-d>=0 and JEU[i][j]==JEU[i-d][j-d]:
        d += 1
    e = 0
    while e<4 and i+e<6 and j+e<7 and JEU[i][j]==JEU[i+e][j+e]:  
        e += 1
    if d + e - 1 >= 4:
        VerifDiago1 = True
       
    VerifDiago2 = False
    f = 0
    while f<4 and i+f<6 and j-f>=0 and JEU[i][j]==JEU[i+f][j-f]:
        f += 1
    g = 0
    while g<4 and i-g>=0  and j+g<7 and JEU[i][j]==JEU[i-g][j+g]:  
        g += 1
    if f + g - 1 >= 4:
        VerifDiago2 = True
   
    if VerifDiago1 or VerifDiago2 or VerifHorizontal or VerifVertic:
        VV = True
    return VV

def Verifplein():
    VerifPlein = True
    for k in range (7):
        for m in range(6):
          Verif = JEU[m][k]
          if Verif == 0:
              VerifPlein = False
    return VerifPlein

def statistiques():
    global L1, L2
    frame_sta = tk.Frame(FF, bg= C[4])
    frame_sta.place(width=1020, height=600)
    Stat1=Stat(L1, frame_sta, 0, 0)
    Stat1.calculs()
    Stat2=Stat(L2, frame_sta, 2, 3)
    Stat2.calculs()
    Stat1.Comparaison(Stat2)
  
   
class Stat:
    def __init__(self, L, frame_sta, x, n):
        self.nom = str(L[0])
        self.NPar=int(L[1])
        self.NVic=int(L[2])
        self.NDef=int(L[3])
        self.NEga=int(L[4])
        self.v = int(n)
        self.frame_sta = frame_sta
        nJ1 = tk.Label(self.frame_sta,text=self.nom, bg= C[4],font=("Arial", 35),fg ="white")
        nJ1.grid(row = 0, column = x, pady =5, columnspan = 2)
       
       
    def calculs(self):
        if self.NPar == 0:
            self.TauxV= 0
            self.TauxD=0
            self.TauxE=0
        else :  
            self.TauxV=round((self.NVic/self.NPar)*100,2)
            self.TauxD=round((self.NDef/self.NPar)*100,2)
            self.TauxE=round((self.NEga/self.NPar)*100,2)
       
        if self.NDef == 0 :
            self.KDR = 0
        else :    
            self.KDR=round(self.NVic/self.NDef,2)
       
        self.Par1 = tk.Label(self.frame_sta, text='Nombre de parties :', bg=C[4],font=("Arial", 15),fg ="white")
        self.Par1.grid(row = 1, column = self.v, pady =5, ipadx = 5)
        self.Par2 = tk.Label(self.frame_sta, text=str(self.NPar), bg= C[4],font=("Arial", 20),fg ="white")
        self.Par2.grid(row = 2, column = self.v, pady =5, ipadx = 5)
        self.Vic1 = tk.Label(self.frame_sta, text='Taux de victoire :', bg= C[4],font=("Arial", 15),fg ="white")
        self.Vic1.grid(row = 3, column = self.v, pady =5, ipadx = 5)
        self.Vic2 = tk.Label(self.frame_sta, text=str(self.TauxV)+'%', bg= C[4],font=("Arial", 20),fg ="white")
        self.Vic2.grid(row = 4, column = self.v, pady =5, ipadx = 5)
        self.Def1 = tk.Label(self.frame_sta, text='Taux de défaite :', bg= C[4],font=("Arial", 15),fg ="white")
        self.Def1.grid(row = 5, column = self.v, pady =5, ipadx = 5)
        self.Def2 = tk.Label(self.frame_sta, text=str(self.TauxD)+'%', bg= C[4],font=("Arial", 20),fg ="white")
        self.Def2.grid(row = 6, column = self.v, pady =5, ipadx = 5)
        self.Ega1 = tk.Label(self.frame_sta, text="Taux d'égalité :", bg= C[4],font=("Arial", 15),fg ="white")
        self.Ega1.grid(row = 7, column = self.v, pady =5, ipadx = 5)
        self.Ega2 = tk.Label(self.frame_sta, text=str(self.TauxE)+'%', bg= C[4],font=("Arial", 20),fg ="white")
        self.Ega2.grid(row = 8, column = self.v, pady =5, ipadx = 5)
   
    def Comparaison(self, other):
        if self.NPar>other.NPar:
            t = str(self.nom)+" a plus souvent joué que "+str(other.nom)
            self.Pvic = tk.Label(self.frame_sta, text=t, bg= C[4],font=("Arial", 20),fg ="white")
            self.Pvic.grid(row = 3, column = 1, columnspan = 2, pady =5)
        elif self.NPar<other.NPar:
            t = str(self.nom)+" a moins souvent joué que "+ str(other.nom)
            self.Pdef = tk.Label(self.frame_sta, text=t, bg= C[4],font=("Arial", 20),fg ="white")
            self.Pdef.grid(row = 3, column = 1, columnspan = 2, pady =5)
        elif self.NPar==other.NPar:
            t = str(self.nom)+" a aussi souvent joué que "+ str(other.nom)
            self.Pega = tk.Label(self.frame_sta, text=t, bg= C[4],font=("Arial", 20),fg ="white")
            self.Pega.grid(row = 3, column = 1, columnspan = 2, pady =5)
       
        if self.NVic>other.NVic:
            t = str(self.nom)+" a plus souvent gagné que "+ str(other.nom)
            self.Nvic = tk.Label(self.frame_sta, text=t, bg= C[4],font=("Arial", 20),fg ="white")
            self.Nvic.grid(row = 5, column = 1, columnspan = 2, pady =5)
        elif self.NVic<other.NVic:
            t = str(self.nom)+" a moins souvent gagné que "+ str(other.nom)
            self.Ndef = tk.Label(self.frame_sta, text=t, bg= C[4],font=("Arial", 20),fg ="white")
            self.Ndef.grid(row = 5, column = 1, columnspan = 2, pady =5)
        elif self.NVic==other.NVic:
            t = str(self.nom)+" a aussi souvent gagné que "+ str(other.nom)
            self.Nega = tk.Label(self.frame_sta, text=t, bg= C[4],font=("Arial", 20),fg ="white")
            self.Nega.grid(row = 5, column = 1, columnspan = 2, pady =5)
       
        if self.KDR>other.KDR:
            t = str(self.nom)+" est plus régulier.e que "+ str(other.nom)
            self.KDvic = tk.Label(self.frame_sta, text=t, bg= C[4],font=("Arial", 20),fg ="white")
            self.KDvic.grid(row = 7, column = 1, columnspan = 2, pady =5)
        elif self.KDR<other.KDR:
            t = str(self.nom)+" est moins régulier.e que "+ str(other.nom)
            self.KDdef = tk.Label(self.frame_sta, text=t, bg= C[4],font=("Arial", 20),fg ="white")
            self.KDdef.grid(row = 7, column = 1, columnspan = 2, pady =5)
        elif self.KDR==other.KDR:
            t = str(self.nom)+" est aussi régulier.e que "+ str(other.nom)  
            self.KDega = tk.Label(self.frame_sta, text=t, bg= C[4],font=("Arial", 20),fg ="white")
            self.KDega.grid(row = 7, column = 1, columnspan = 2, pady =5)


def Recherche_colonne(xClic):
    colonne = ((xClic)//100)-1
    return colonne

def Recherche_ligne(colonne):
    ligne = 5
    for i in range (6):      
        if JEU[ligne][colonne]!=0:
            ligne -= 1
    return ligne
def Tour(event):
    global JEU, tour, C, CJ1, CJ2, etat_jeu, L1, L2, nom, v_ini, d,liste_mat, Label1, Label2
    xClic,yClic = event.x,event.y
    if etat_jeu:  
        if 100<xClic<800 and 100<yClic<700 :
            
            if v_ini == 0 :
                lancer_chrono()
                decompte()
                v_ini +=1
            
            colonne = Recherche_colonne(xClic)
            ligne=Recherche_ligne(colonne)
            l_tour.configure(text= "Tour n°"+str(tour+2))
            if ligne<0 :
                return
       
            if tour%2==0:
                tour += 1
                d = 16
                JEU[ligne][colonne]=1
                for w in fr2.winfo_children():
                    w.destroy()
                Label1 = tk.Label(fr2,text = "Tour de "+str(L2[0])+' ', fg=C[2],font=('Arial',20),bg=C[4])
                Label1.pack()
                
                for w in fr3.winfo_children():
                    w.destroy()
                
                Label2 = tk.Label(fr3, text='Dernier coup joué : '+str(colonne+1), font=('Arial', 20), bg=C[4], fg=C[2])
                Label2.pack()
                if VerificationVictoire(ligne, colonne):
                    Label1.pack_forget()
                    Label2.pack_forget()
                    for w in fr1.winfo_children():
                        w.destroy()
                    L1[1] = str(int(L1[1]) + 1)
                    L2[1] = str(int(L2[1]) + 1)
                    L1[2] = str(int(L1[2]) + 1)
                    L2[3] = str(int(L2[3]) + 1)
                   
                    nom1 =nom+L1[0]+'.txt'
                    f = open(nom1, 'w')
                    f.write(L1[0] +';' + L1[1] + ';'+ L1[2] + ';' + L1[3] + ';' + L1[4])
                    f.close()

                    nom2 =nom+L2[0]+'.txt'
                    f = open(nom2, 'w')
                    f.write(L2[0] +';' + L2[1] + ';'+ L2[2] + ';' + L2[3] + ';' + L2[4])
                    f.close()                    
                   
                    ga = tk.Label(fr1, text='Victoire de '+str(L1[0]), fg=C[2],font=('Arial',20),bg=C[4])
                    ga.pack()
                    statistiques()
                    arreter_chrono()
                    etat_jeu = False
                   
               
            elif tour%2==1:
                tour += 1
                d = 16
                JEU[ligne][colonne]=2
                for w in fr2.winfo_children():
                    w.destroy()
                Label1 = tk.Label(fr2,text = "Tour de "+str(L1[0])+' ', fg=C[2],font=('Arial',20),bg=C[4])
                Label1.pack()
                
                for w in fr3.winfo_children():
                    w.destroy()
                Label2 = tk.Label(fr3, text='Dernier coup joué : '+str(colonne+1), fg=C[2], font=('Arial', 20), bg=C[4])
                Label2.pack()
                if VerificationVictoire(ligne, colonne):
                    Label1.pack_forget()
                    Label2.pack_forget()
                    for w in fr1.winfo_children():
                        w.destroy()
                    L1[1] = str(int(L1[1]) + 1)
                    L2[1] = str(int(L2[1]) + 1)
                    L1[3] = str(int(L1[3]) + 1)
                    L2[2] = str(int(L2[2]) + 1)
                   
                    nom1 =nom+L1[0]+'.txt'
                    f = open(nom1, 'w')
                    f.write(L1[0] +';' + L1[1] + ';'+ L1[2] + ';' + L1[3] + ';' + L1[4])
                    f.close()

                    nom2 =nom+L2[0]+'.txt'
                    f = open(nom2, 'w')
                    f.write(L2[0] +';' + L2[1] + ';'+ L2[2] + ';' + L2[3] + ';' + L2[4])
                    f.close()
                   
                    ga = tk.Label(fr1, text='Victoire de '+str(L2[0]), fg=C[2],font=('Arial',20),bg=C[4])
                    ga.pack()
                    statistiques()
                    arreter_chrono()
                    etat_jeu = False
                   
            if Verifplein():
                L1[1] = str(int(L1[1]) + 1)
                L2[1] = str(int(L2[1]) + 1)
                L1[4] = str(int(L1[4]) + 1)
                L2[4] = str(int(L2[4]) + 1)
                
                nom1 =nom+L1[0]+'.txt'
                f = open(nom1, 'w')
                f.write(L1[0] +';' + L1[1] + ';'+ L1[2] + ';' + L1[3] + ';' + L1[4])
                f.close()

                nom2 =nom+L2[0]+'.txt'
                f = open(nom2, 'w')
                f.write(L2[0] +';' + L2[1] + ';'+ L2[2] + ';' + L2[3] + ';' + L2[4])
                f.close()
               
                Label4 = tk.Label(fr1,text = "Égalité, le plateau est plein !", fg = 'black',bg=C[4])
                Label4.pack()
                statistiques()
                arreter_chrono()
                etat_jeu = False
            liste_mat.append(copy.deepcopy(JEU))
            affichage_mat(JEU)
             
   
def trace_ligne_ver(x):
    x1=x
    y1=100
    x2=x
    y2=700
    Zone.create_line(x1,y1,x2,y2,width=3,fill="black")
def trace_ligne_hor(x):
    x1=100
    y1=x
    x2=800
    y2=x
    Zone.create_line(x1,y1,x2,y2,width=3,fill="black")
def grille():
    x=100
    while x!=900:
        trace_ligne_ver(x)
        x=x+100

    x=100
    while x!=800:
        trace_ligne_hor(x)
        x=x+100
    y1 = 110
    for i in range (0,6):
        x1 = 110

        for i in range (0,7):
            Zone.create_oval(x1, y1, x1+80, y1+80, fill=C[2])
            x1 += 100
        y1 += 100

def etat_boutons(): #permet de changer la couleur des boutons et de changer "peut_ouvrir"
    global peut_ouvrir
    peut_ouvrir = not peut_ouvrir
    couleur = (lambda : C[3] if peut_ouvrir else "#414141")() #permet de changer couleur en fct de peut_ouvrir(T->bleu ;F->gris )
    Bouton_sauvegarde.config(bg=couleur) #change la couleur des boutons
    Bouton_charger.config(bg=couleur)
    Bouton_replay.config(bg=couleur)
    Bouton_sauv_replay.config(bg=couleur)
    
#%% Chargement /Sauvegarde
def chargement(): #chargement de partie
   
    def fermer():
        frame_ch.destroy()
        fen.bind("<Button-1>", Tour)   
        etat_boutons()
    def boite_chargement(liste_fichier): #affichage et gestion la boite de selection
 
        def selection():
            fichier = liste_sel.get(tk.ANCHOR)
            mat,t = sv.chargement("./sauv/"+fichier+".csv")
            reset(mat,t)
            fermer()

        liste_sel = tk.Listbox(frame_ch) #créé la boite de selection
        liste_sel.pack()
        for i in range(len(liste_fichier)): #ajoute les nom de fichier à la boite
            liste_sel.insert(i, liste_fichier[i])
        b_charger = tk.Button(frame_ch, text='Charger', fg='Black', font='Arial', bg=C[3],command = selection)
        b_charger.pack(pady=5)
    etat_boutons()
    fen.unbind("<Button-1>")
    frame_ch = tk.Frame(FF2, width=400, height=400, bg= C[4],highlightbackground=C[3],highlightthickness=2)  
    frame_ch.grid(padx = 15, pady = 5)
    b_annuler_sauv = tk.Button(frame_ch, text='Annuler', fg='Black', font='Arial', bg=C[3],command = fermer)
    b_annuler_sauv.pack(pady=5,side = tk.BOTTOM)
   
    liste_fichier = sv.liste_fichiers("./sauv")          #liste_fichier est la liste des noms de fichier de "./sauv"
   
    if len(liste_fichier)>0: # vérifie si la liste est vide ou pas (si il y as des fichiers dans ./sauv )
       boite_chargement(liste_fichier)
    else:
        l_pasfichier = tk.Label(frame_ch,text="Aucune sauvegarde trouvé",font=("Arial", 20),bg=C[4],fg ="red")
        l_pasfichier.pack(pady = 5)


def sauvegarde():#sauvegarde : demande nom -> si vérif fichier:( demander si suprimmer -oui-> sauv -non-> reprendre au début )sinon : sauv
    def fermer():
        frame_sv.destroy()
        fen.bind("<Button-1>", Tour)
        etat_boutons()
    def click():
        nom = e.get()
        if sv.test_existence("./sauv/{}.csv".format(nom)):
            def oui():
                sv.sauvegarde("./sauv/{}.csv".format(nom), JEU, tour)
                fermer()
            def non():
                fermer()
                sauvegarde()
            e.destroy()         # enleve les anciens widgets
            b_sauv.destroy()    # (Peut etre faire avec les frames?)
            text1.destroy()
            text2 = tk.Label(frame_sv,text="La sauvegarde '{}'\n existe déjà, la remplacer ?".format(nom),font=("Arial", 20),bg=C[4],fg ="red",)
            text2.pack()
            b_oui = tk.Button(frame_sv, text='Oui', fg='Black', font='Arial', bg=C[3], command = oui)
            b_oui.pack(side = tk.LEFT,padx = 50)
            b_non = tk.Button(frame_sv, text='Non', fg='Black', font='Arial', bg=C[3], command = non)
            b_non.pack(side = tk.RIGHT,padx = 50)
        else:
            sv.sauvegarde("./sauv/{}.csv".format(nom), JEU, tour)
            fermer()
    etat_boutons()
    fen.unbind("<Button-1>")
    frame_sv = tk.Frame(FF2, width=400, height=200, bg= C[4],highlightbackground=C[3],highlightthickness=2)
    frame_sv.grid(padx = 15, pady = 15)
    text1 = tk.Label(frame_sv,text="Nom de la sauvegarde :", bg= C[4],font=("Arial", 20),fg ="white")
    text1.pack(pady=5)
    e = tk.Entry(frame_sv)
    e.pack()
    b_sauv = tk.Button(frame_sv, text='Sauvegarder', fg='black', font='Arial', bg=C[3], command = click)
    b_sauv.pack(pady=5)
    b_annuler_sauv = tk.Button(frame_sv, text='Annuler', fg='Black', font='Arial', bg=C[3],command = fermer)
    b_annuler_sauv.pack(pady=5,side = tk.BOTTOM)

#%%    

def reset(mat,t): #permet de reset le jeu avec une matrice de jeu et un nbr de tour (pour le chargement de parties)
    global JEU,tour, etat_jeu, v_ini, liste_mat
    JEU,tour = mat,t  
    grille()
    affichage_mat(JEU)
    l_tour.configure(text= "Tour n°"+str(tour+1))
    v_ini = 0
    etat_jeu = True
    liste_mat = []
    for w in fr1.winfo_children():
        w.destroy()
    for w in fr2.winfo_children():
        w.destroy()
    for w in fr3.winfo_children():
        w.destroy()

#%%  replay
def replay():
 
    def fermer(r): #ferme la fenetre, r: bool(True : reset le jeu, False : ne reset pas)
        frame_ch.destroy()
        if r:
            reset(matrice(), 0)
        fen.bind("<Button-1>", Tour)
        etat_boutons()
    def boite_chargement(liste_fichier): #affichage et gestion la boite de selection

        def selection():

            def suivant(liste_mat):
                global tour
                if tour < len(liste_mat)-1:
               
                    tour+=1
                    reset(liste_mat[tour], tour)
            def precedent(liste_mat):
                global tour
                if tour > 0:
               
                    tour-=1
                    reset(liste_mat[tour], tour)    
            b_fermer.config(command = lambda: fermer(True))
            tour = 0
            fichier = boite_sel.get(tk.ANCHOR)
            liste_mat = sv.xml_lecture("./replay/"+fichier+".xml")
            boite_sel.destroy()
            b_charger.destroy()
            b_suivant = tk.Button(frame_ch, text='Suivant', fg='Black', font='Arial', bg=C[3],command = lambda : suivant(liste_mat))
            b_suivant.pack(side = tk.RIGHT,padx = 50)
            b_precedent = tk.Button(frame_ch, text='Précédent', fg='Black', font='Arial', bg=C[3],command = lambda : precedent(liste_mat))
            b_precedent.pack(side = tk.LEFT,padx = 50)
            reset(liste_mat[tour],tour)
         
     
        boite_sel = tk.Listbox(frame_ch) #créé la boite de selection
        boite_sel.pack()
       
        for i in range(len(liste_fichier)): #ajoute les nom de fichier à la boite
            boite_sel.insert(i, liste_fichier[i])
        b_charger = tk.Button(frame_ch, text='Charger', fg='Black', font='Arial', bg=C[3],command = selection)
        b_charger.pack(pady=5)
   
    etat_boutons()
    fen.unbind("<Button-1>")
    frame_ch = tk.Frame(FF2, width=400, height=400, bg= C[4],highlightbackground=C[3],highlightthickness=2)  
    frame_ch.grid(padx = 15, pady = 5)
    b_fermer = tk.Button(frame_ch, text='Fermer', fg='Black', font='Arial', bg=C[3],command = lambda: fermer(False))
    b_fermer.pack(pady=5,side = tk.BOTTOM)
   
    liste_fichier = sv.liste_fichiers("./replay/")          #liste_fichier est la liste des noms de fichier de "./sauv"
   
    if len(liste_fichier)>0: # vérifie si la liste est vide ou pas (si il y as des fichiers dans ./sauv )
        boite_chargement(liste_fichier)
    else:
        l_pasfichier = tk.Label(frame_ch,text="Aucun replay trouvé",font=("Arial", 20),bg=C[4],fg ="red")
        l_pasfichier.pack(pady = 5)

def sauvegarde_replay(): #Similaire à la fct sauvegarder, mais sauvegarde la liste de mat dans un fichier XML
    def fermer():
        frame_sv.destroy()
        fen.bind("<Button-1>", Tour)
        etat_boutons()
    def click():
        nom = e.get()
        if sv.test_existence("./replay/{}.xml".format(nom)):
            def oui():
                sv.xml_ecriture("./replay/{}.xml".format(nom), liste_mat)
                fermer()
            def non():
                fermer()
                sauvegarde_replay()
            e.destroy()         # enleve les anciens widgets
            b_sauv.destroy()  
            text1.destroy()
            text2 = tk.Label(frame_sv,text="Le replay '{}'\n existe déjà, le remplacer ?".format(nom),font=("Arial", 20),bg=C[4],fg ="red",)
            text2.pack()
            b_oui = tk.Button(frame_sv, text='Oui', fg='Black', font='Arial', bg=C[3], command = oui)
            b_oui.pack(side = tk.LEFT,padx = 50)
            b_non = tk.Button(frame_sv, text='Non', fg='Black', font='Arial', bg=C[3], command = non)   
            b_non.pack(side = tk.RIGHT,padx = 50)
        else:
            sv.xml_ecriture("./replay/{}.xml".format(nom), liste_mat)
            fermer()
    etat_boutons()
    fen.unbind("<Button-1>")
    frame_sv = tk.Frame(FF2, width=400, height=200, bg= C[4],highlightbackground=C[3],highlightthickness=2)
    frame_sv.grid(padx = 15, pady = 15)
    text1 = tk.Label(frame_sv,text="Nom du replay :", bg= C[4],font=("Arial", 20),fg ="white")
    text1.pack(pady=5)
    e = tk.Entry(frame_sv)
    e.pack()
    b_sauv = tk.Button(frame_sv, text='Sauvegarder', fg='black', font='Arial', bg=C[3], command = click)
    b_sauv.pack(pady=5)
    b_annuler_sauv = tk.Button(frame_sv, text='Annuler', fg='Black', font='Arial', bg=C[3],command = fermer)
    b_annuler_sauv.pack(pady=5,side = tk.BOTTOM)

    


#%% 

fen = tk.Tk()
fen.title('Puissance 4')    
fen.geometry("1920x1080")
fen.configure(bg='#3481F8')

Zone=tk.Canvas(fen,width=900,height=1080,bg=C[4], bd=0, highlightthickness=0)
Zone.place(x=0, y=0)
Zone.create_rectangle(100, 100, 800, 700, fill=C[6])

FF0 = tk.Frame(fen, bg=C[4], highlightbackground=C[5], highlightthickness=4)
FF0.place(x=900, y=0, width=1020, height=160)

FF = tk.Frame(fen, bg=C[4], highlightbackground=C[5], highlightthickness=4)
FF.place(x=900, y=160, width=1020, height=540)

FF2 = tk.Frame(fen, bg=C[4], highlightbackground=C[5], highlightthickness=4)
FF2.place(x=900, y=700, width=1020, height=300)

FF3 = tk.Frame(fen, bg=C[2], highlightbackground=C[5], highlightthickness=4)
FF3.place(x=900, y=955, width=1020, height=135)


fr1 = tk.Frame(FF0, bg=C[4], width=300, height=42, highlightbackground=C[3],highlightthickness=2)
fr1.grid(row=2, column = 2, columnspan =2, pady =5) 
fr1.pack_propagate(False)
fr2 = tk.Frame(FF0, bg=C[4], width=300, height=42, highlightbackground=C[3],highlightthickness=2)
fr2.grid(row=1, column = 3, pady =5)
fr2.pack_propagate(False)
fr3 = tk.Frame(FF0, bg=C[4], width=300, height=42, highlightbackground=C[3],highlightthickness=2)
fr3.grid(row=1, column=2, pady =5)
fr3.pack_propagate(False)
fr4 = tk.Frame(FF0,bg=C[4],width=300, height=42, highlightbackground=C[3],highlightthickness=2)
fr4.grid(row=1, column=1, pady =5)
fr4.pack_propagate(False)



def crea_fich(J, nom):
    nom1 = nom+J+'.txt'
    if sv.test_existence(nom1) is False :
         f = open(nom1, 'w')
         f.write(J +';' + '0' + ';'+ '0' + ';' + '0' + ';' + '0')
         f.close()    
     
    f=open(nom1, 'r')
    x = f.readline()
    L = x.split(sep=';')
   
    return L

def click():
   global L1, L2, CJ1, CJ2, Stat1, Stat2, etat_jeu, peut_ouvrir
   J1 = e1.get()
   C1 = CB1.current()
   J2 = e2.get()
   C2 = CB2.current()
   
   if J1 == J2:
        for w in fr_st2.winfo_children():
            w.destroy()
        er = tk.Label(fr_st2,text="Veuillez choisir 2 joueurs differents", bg= C[4],font=("Arial", 11),fg ="red")
        er.grid(pady=5)
   elif (len(J1) == 0) or (len(J2) == 0) :
        for w in fr_st2.winfo_children():
            w.destroy()
        er = tk.Label(fr_st2,text="Veuillez remplir les 2 champs", bg= C[4],font=("Arial", 11),fg ="red")
        er.grid(pady=5)
   elif len(J1)>9 or len(J2)>9:
       for w in fr_st2.winfo_children():
           w.destroy()
       er = tk.Label(fr_st2,text="Veuillez choisir un nom de 9 caractères maxium", bg= C[4],font=("Arial", 11),fg ="red")
       er.grid(pady=5)
    
   elif C1 == C2:
       for w in fr_st2.winfo_children():
           w.destroy()
       er = tk.Label(fr_st2,text="Veuillez choisir 2 couleurs differentes", bg= C[4],font=("Arial", 11),fg ="red")
       er.grid(pady=5)
    
   else :    
       
       CJ1 = C1 
       CJ2 = C2
       L1 = crea_fich(J1, nom)
       L2 = crea_fich(J2, nom)
       statistiques()
       etat_jeu = True
       frame_ini.destroy()
       etat_boutons()
   Label2 = tk.Label(fr3, text='Dernier coup joué :   ', font=('Arial', 20), bg=C[4], fg=C[2])
   Label2.pack()
   Label1 = tk.Label(fr2,text = "Tour de "+str(L1[0])+' ', fg=C[2],font=('Arial',20),bg=C[4])
   Label1.pack()



frame_ini = tk.Frame(FF2, width=800, height=200, bg= C[4],highlightbackground=C[3],highlightthickness=2)
frame_ini.grid(padx = 15, pady = 15, row =0, column = 0)
t1 = tk.Label(frame_ini,text="Nom du joueur 1 : ", bg= C[4],font=("Arial", 20),fg ="white")
t1.grid(row =0, column = 0, pady=5)
t2 = tk.Label(frame_ini,text="Nom du joueur 2 : ", bg= C[4],font=("Arial", 20),fg ="white")
t2.grid(row =1, column = 0, pady=5)
e1 = tk.Entry(frame_ini)
e1.grid(row =0, column = 1)
e2 = tk.Entry(frame_ini)
e2.grid(row =1, column = 1)
b_stat = tk.Button(frame_ini, text='Valider', fg='black', font='Arial', bg=C[3], command = click)
b_stat.grid(pady=5)
fr_st2 = tk.Frame(frame_ini, bg=C[4])
fr_st2.grid(pady = 5)

TCB1 = tk.Label(frame_ini, text ='Couleur du joueur 1 : ', bg= C[4],font=("Arial", 20),fg ="white")
TCB1.grid(row = 0, column = 2, padx =10)
CB1 = ttk.Combobox(frame_ini, values = Cjoueurs)
CB1.grid(row = 0, column = 3, padx = 5)
CB1.current(2)

TCB2 = tk.Label(frame_ini, text ='Couleur du joueur 1 : ', bg= C[4],font=("Arial", 20),fg ="white")
TCB2.grid(row = 1, column = 2, padx =10)
CB2 = ttk.Combobox(frame_ini, values = Cjoueurs)
CB2.grid(row = 1, column = 3, padx = 5)
CB2.current(5)


grille()
peut_ouvrir = False


fen.bind("<Button-1>", Tour)  #permet d'appeler la fct tour avec un clic gauche
fen.iconbitmap('ico.ico')    #change l'icone de la fenètre

#Création des boutons
Bouton2 = tk.Button(FF3, text='Rejouer', fg = 'black', font=('Arial', 14), bg=C[3],command = lambda : reset(matrice(),0)  )
Bouton2.grid(column = 0, row=0, pady = 10, padx = 10)
Bouton1 = tk.Button(FF3, text = 'Quitter', fg = 'black',font=('Arial', 14),bg= C[0], command = fen.destroy )
Bouton1.grid(column = 5, row=0, pady = 10, padx = 295)
Bouton_sauvegarde = tk.Button(FF3, text='Sauvegarde', fg='Black', font=('Arial', 14), bg="#414141",command = lambda : sauvegarde() if peut_ouvrir else())
Bouton_sauvegarde.grid(column = 2, row=0, pady = 10, padx = 10)
Bouton_charger = tk.Button(FF3, text='Charger', fg='Black', font=('Arial', 14), bg="#414141", command = lambda : chargement() if peut_ouvrir else())
Bouton_charger.grid(column = 1, row=0, pady = 10, padx = 10)
Bouton_replay = tk.Button(FF3, text='Replay', fg='Black', font=('Arial', 14), bg="#414141", command = lambda : replay() if peut_ouvrir else())
Bouton_replay.grid(column = 3, row=0, pady = 10, padx = 10)
Bouton_sauv_replay = tk.Button(FF3, text='Enregistrer Replay', fg='Black', font=('Arial', 14), bg="#414141", command = lambda : sauvegarde_replay() if peut_ouvrir else())
Bouton_sauv_replay.grid(column = 4, row=0, pady = 10, padx = 10)

#Création des labels (texte)
l_tour = tk.Label(fr4,text="Tour n°1", font=('Arial', 20), bg=C[4], fg=C[2])
l_tour.grid(row=0,column=1)
l_chrono = tk.Label(FF0, text = "0 min 0 sec ", font=('Arial', 13), bg=C[4], fg=C[2])
l_chrono.grid(row=0, column=0, pady = 10, padx=10)
l_decompte =tk.Label(FF0, text ='Temps restant : 15s', font=('Arial', 13), bg=C[4], fg=C[2])
l_decompte.grid(row = 0, column = 4, ipadx = 5)


JEU = matrice() #JEU (Matrice représantant le plateau) est initialisé comme un matrice contenant des 0


fen.mainloop()

