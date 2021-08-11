#Write your code here
class Vaccine(object):
    def __init__(self, name, cost, duration):
        self.name = name
        self.cost = cost
        self.duration = duration

class Person(Vaccine):
    def __init__(self, name, age, status='Citizen'):
        self.name = name
        self.age = age
        self.status = status
    
    def pushVaccine(self, vaccine, dose=1):
        self.vaccine = vaccine
        self.dose = dose
        if self.dose == 1:
            print(f'1st dose done for {self.name}')
        else:
            print(f'2st dose done for {self.name}')

    def showDetail(self):
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("Type: " + self.status)
        print("Vaccine name: " + self.vaccine.name)
        print('1st dose: Given \n2nd dose: Please come after 60 days')


astra = Vaccine("AstraZeneca", "UK", 60)
modr = Vaccine("Moderna", "UK", 30)
sin = Vaccine("Sinopharm", "China", 30)
p1 = Person("Bob", 21, "Student")
print("=================================")
p1.pushVaccine(astra)
print("=================================")
p1.showDetail()
print("=================================")
p1.pushVaccine(sin, "2nd Dose")
print("=================================")
p1.pushVaccine(astra, "2nd Dose")
print("=================================")
p1.showDetail()
print("=================================")
p2 = Person("Carol", 23, "Actor")
print("=================================")
p2.pushVaccine(sin)
print("=================================")
p3 = Person("David", 34)
print("=================================")
p3.pushVaccine(modr)
print("=================================")
p3.showDetail()
print("=================================")
p3.pushVaccine(modr, "2nd Dose")

