
class plan_cartesien:
    # cette classe nous permet d'effectuer les calculs geometriques
    def __init__(self, _p1, _p2,_p3,):
        self.p1=_p1
        self.p2=_p2
        self.p3=_p3
    def distance(self):
        return [(((self.p1[0]-self.p2[0])**2)+((self.p1[1]-self.p2[1])**2))**(0.5),
                (((self.p1[0]-self.p3[0])**2)+((self.p1[1]-self.p3[1])**2))**(0.5),
                (((self.p3[0]-self.p2[0])**2)+((self.p3[1]-self.p2[1])**2))**(0.5)]

    def is_aligne(self):
        if self.p1[0]==self.p2[0] and self.p2[0]==self.p3[0] or self.p1[1]==self.p2[1] and self.p2[1]==self.p3[1]:
            return True
        return False
# pc=plan_carterien([2,5],[5,5],[3,5])
# print pc.distance()[0]
# print pc.distance()[1]
# print pc.distance()[2]
# print pc.is_aligne()