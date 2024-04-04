from math import *

def prediction(objets):
    motier_ideale=sum(objets)/2
    print(motier_ideale)
    sac1=[]
    index=-1
    while motier_ideale>sum(sac1):
        test=[sqrt((motier_ideale-objet-sum(sac1))**2) for objet in objets]
        print(test)
        test=objets[test.index(min(test))]
        sac1.append(test)
        objets.remove(test)
    return (sac1,objets)


print(prediction([8,5,7,2,1]))




def prediction_précise(objets):
    liste=prediction([objet[1] for objet in objets])
    sac1,sac2=[],[]
    for objet in objets:
        if x in liste:
            pass
            #suite à écrire
        

#print(prediction_précise([("canape",20),("abricot",1),("table":10)]))
