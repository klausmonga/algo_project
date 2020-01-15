from triangle import triangle
def main():
    print("\t\t\tTP ALGO\n\n a. Lire triangle\n b. Afficher triangle\n c. Type triangle\n d. Tri tableau triangle")
    choix=input()
    p1=[0,0]
    p2=[0,0]
    p3=[0,0]
    if choix=="a":
        nbTriangle=int(input("Combien de triangles :"))
        t={}
        for i in range(0,nbTriangle):
            print("TAPER LES COORDONNEES DU TRIANGLE %d (x,y)"%(i+1))
            p1[0]=int(input("x1:"))
            p1[1]=int(input("y1:"))
            p2[0]=int(input("x2:"))
            p2[1]=int(input("y2:"))
            p3[0]=int(input("x3:"))
            p3[1]=int(input("y3:"))
            t[i]=triangle(p1,p2,p3)
        choix=input("\t\t\t OPTIONS \n\n b. Afficher triangle\n c. Type triangle\n d. Tri tableau triangle \n : ")
        if choix=="b":
            print("|-------------< Afficher triangle >-----------------|")
            for key in t:
                t[key].afficher_triangle()
            choix=input("\t\t\t OPTIONS \n\n c. Type triangle\n d. Tri tableau triangle \n : ")   
        if choix=="c":
            print("|-------------< Type triangle >-----------------|")
            for key in t:
                print("|%d------>Le Triangle %d est %s"%(key+1,key+1,t[key].type_triangle()))
            choix=input("\t\t\t OPTION \n\n d. Tri tableau triangle \n : ")
        if choix=="d":
            print("|-------------< Surfaces TriEes >-----------------|")
            tabAire={}
            for key in t:
                tabAire[key]=t[key].getAire()
            tabTr=t[0].tris_selection(tabAire)
            for key in tabTr:
                print("|----->surface %d : %d UNITE DE SURFACE"%(key,tabTr[key]))
main()