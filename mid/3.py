class Division:
    def __init__(self, name = None):
        self.name = name
        
    
    def printDetail(self):
        if self.name is None:
            print('Name of division is not set')
        else:
            print('Name of division:', self.name)

    def add_district(self, d1 = None, d2 = None, d3 = None):
        pass
        

dhaka = Division()
print('----------------------------------')
dhaka.printDetail()
print('----------------------------------')
dhaka.add_district("Narayanganj", "Gazipur")
print('----------------------------------')
dhaka.setName("Rangpur")
print('----------------------------------')
dhaka.setName("Dhaka")
dhaka.add_district("Narayanganj")
dhaka.printDetail()
print('----------------------------------')
dhaka.add_district("Gazipur", "Munshiganj")
dhaka.printDetail()
print("===================================")
chittagong = Division("Chittagong")
chittagong.add_district("Feni", "Comilla", "Cox's Bazar")
chittagong.printDetail()
print("===================================")
sylhet = Division("Sylhet")
sylhet.add_district("Habiganj")
sylhet.printDetail()