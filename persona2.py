class Persona:
    def __init__(self):

        self.name=""

        self.lastname=""

        self.age=0

        #funzione che manda i output i dati

    def displaydata(self) -> None:
        print(f"nome:{self.name} cognome:{self.lastname} età:{self.age}")
        
        #funzione per importare i valori

    def setName(self,name:str):
        self.name=name 
    def setLastname(self,lastname:str):
        self.lastname=lastname
    def setAge(self,age:int):
        if age<0 or age>130:
            self.age=0
        else:
            self.age=age
       
        #funzione che mi ritorna i dati
    def getName(self) -> str:
        return self.name
    def getLastname(self) -> str:
        return self.lastname
    def getAge(self) -> int:
        return self.age
        