# Write the Advising class so that the given code provides the expected 
# output. You can not change the given code.

#Write your code here

class Advising:
    def __init__(self, name, id, advisor = None):
        self.name = name
        self.id = id
        self.advisor = advisor
        self.cos = []

    def add_course(self, course, time):
        self.course = course
        self.time = time
        
        self.cos.append(self.course)


    def showDetails(self):
        if self.advisor is None:
            print('Advisor not assigned. Assign advisor name first')
        else:
            print(f'Student Name: {self.name}')
            print(f'Advisor Name: {self.advisor}')
            print(f'Courses of 17100000 {self.cos}')

    def show_exams(self):
        print(f'Exams of 17100000 {self.cos}')



adv1 = Advising('Michael Scott',16100000)
print("=================================")
adv1.add_course('Office Management','Day1')
print("=================================")
adv1.advisor = 'David Wallace'
adv1.add_course('Office Management','Day1')
adv1.add_course('Employee Management','Day2')
adv1.add_course('Intro to Best Boss','Day1')
adv1.showDetails()
print("=================================")
adv1.show_exams()
print("####################################")
adv2 = Advising('Dwight Schrute',17100000,'Michael Scott')
adv2.showDetails()
print("=================================")
adv2.show_exams()
print("=================================")
adv2.add_course('How to be Regional Manager','Day1')
adv2.add_course('Farming','Day1')
adv2.showDetails()
print("=================================")
adv2.show_exams()
print("=================================")
