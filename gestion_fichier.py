import xml.etree.ElementTree as ET
import os



def format_mat(mat):
    res = ""
    for i in mat:
        for n in i:
            res += (str(n)+";")
        res += ("\n")
    return(res)


#%% - XML - ###

def format_mat_XML(mat):
    res = ""
    for i in mat:
        for n in i:
            res += str(n)
        res += ("\n")
    return(res)

def xml_lecture(fichier):  
    liste_mat = []
    sub_mat = []
    root = ET.parse(fichier)
    for tour in root.iter("tour"):
        text = tour.find("./mat").text
        mat = []
        for i in range(48):
            if text[i] == '\n': 
                i +=1
                mat.append(sub_mat)
                sub_mat = []
            else :
                sub_mat.append(int(text[i]))
        liste_mat.append(mat)

    return liste_mat # return la liste des matrices

def xml_ecriture(fichier,liste_mat):
    tours = ET.Element("tours") #initialise
    for t in range(len(liste_mat)):
        tour = ET.SubElement(tours, "tour",tour=str(t))
        ET.SubElement(tour, "mat").text = format_mat_XML(liste_mat[t]) 

    tree = ET.ElementTree(tours)
    tree.write(fichier)

#%%############
def test_existence(nom): #return True si le fichier existe, false sinon
    try:
        fr = open(nom,"r")
        fr.close()
        return True
    except FileNotFoundError:
        return False
    

def sauvegarde(fichier,mat,tour): #créé un fichier de sauv
    fr = open(fichier,"w")
    fr.write(format_mat(mat))
    fr.write(str(tour)+"\n")
    fr.close()
    fr.close()


def chargement(nom):
    fr = open(nom,"r")

    sub_mat = []
    mat =[]

    for n in range (6):
        ligne = fr.readline()  
        sub_mat = []
        for i in range(14):
            if i %2 ==0:
                sub_mat.append(int(ligne[i]))
        mat.append(sub_mat)
    tour = fr.readline()
    fr.close()
    return(list(mat),int(tour))


def liste_fichiers(dossier): #renvoi la liste des fichier d'un dossier
    liste = []
    dirs = os.listdir( dossier )
    for file in dirs:   
        liste.append(file[:len(file)-4]) #ajoute le nom du fichier sans l'extension (.csv,.xml ...)
    return(liste)        