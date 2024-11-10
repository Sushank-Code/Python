class Train:

    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    
    def getStatus(self):
        print("Name : ",self.name)
        print("Seats : ", self.seats)
        print("Fare : ",self.fare)

abc=Train("EXpress",100,20)
abc.getStatus() 