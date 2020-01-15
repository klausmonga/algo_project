from plan_cartesien import plan_cartesien
class triangle:
    def __init__(self,_p1,_p2,_p3):
        # la base 
        self.p1 = _p1
        self.p2 = _p2
        self.p3 = _p3
        self.plan = plan_cartesien(self.p1,self.p2,self.p3)
        self.cotes = self.plan.distance()
        self.demiPerimetre = (self.cotes[0] + self.cotes[1] + self.cotes[2]) / 2
    def getAire(self):
        return int((self.demiPerimetre * (self.demiPerimetre-self.cotes[0]) * (self.demiPerimetre-self.cotes[1]) * (self.demiPerimetre-self.cotes[2]))**(0.5))
    def tris_selection(self,tab):
        i=0
        j=0
        for i in tab:
            tmp=tab[i]
            j=i
            while j>0 and tab[j-1]>=tab[j]:
                tab[j]=tab[j-1]
                j=j-1
            tab[j]=tmp
        return tab
    def type_triangle(self):
        if self.plan.is_aligne():
            return "Un triangle PLAT"
        elif (self.cotes[0]==self.cotes[1] and self.cotes[1] == self.cotes[2]) and self.plan.is_aligne()==False:
            return "Un triangle EQUILATERAL"
        elif (self.cotes[0]==self.cotes[1] or self.cotes[1] == self.cotes[2] or self.cotes[0] == self.cotes[2]) and self.plan.is_aligne()==False:
            return "Un triangle ISOCELE"
        return "un triangle SCALENE"
    def afficher_triangle(self):
        print("|---------------------------------------------------|")
        print("|-->COTE AB : %06.2f UNITE DE DISTANCE--------------|"%self.cotes[0])
        print("|-->COTE Ac : %06.2f UNITE DE DISTANCE--------------|"%self.cotes[1])
        print("|-->COTE Bc : %06.2f UNITE DE DISTANCE--------------|"%self.cotes[2])
        print("|---------------------------------------------------|")
