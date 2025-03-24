'''
#dal file persona.py importo la classe Persona
from persona import Persona

#creare l'oggetto di tipo Persona
ff:Persona=Persona("filippo","fronzi",20)

print(ff.name, ff.lastname, ff.age, sep=", ")'
'''
#importo da persona2 la classe Persona
from persona2 import Persona
ff:Persona=Persona()
 
 #voglio richiamare la funzione displaydata per l'output
ff.displaydata()

#impostare i dati

ff.setName("filippo")
ff.setLastname("fronzi")
ff.setAge(20)

ff.displaydata()

print(ff.getName(),ff.getLastname(), ff.getAge())