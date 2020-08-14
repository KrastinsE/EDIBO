class PartyAnimal:
   x = 0

#__init__ metode tiks izpildīta tikai vienu reizi veidojot katru instanci
   def __init__(self):
     print('I am constructed')
     x = 0
    
   def party(self) :
     self.x = self.x + 1
     print("So far x property of object is",self.x)

   def __del__(self):
     print('I am destructed', self.x)

print("Before an = PartyAnimal()")
#print(vars())
an = PartyAnimal()
print("After an = PartyAnimal()")
#print(vars())
#print("an data type: ", type(an))
#print("an methods and properties: ", dir(an))
#print("x property data type: ", type(an.x))
#print("an party method data type: ", type(an.party))
#print(vars(an)) #objekts tikai izveidots {}?

print("\nBefore first = an.party()")
an.party()
print("After first = an.party()")
#print(vars(an)) #objekts tikai izveidots {'x':1}

an.x = 100

print("\nBefore second = an.party()")
an.party()
print("After second = an.party()")

an.x = 200

print("\nBefore third = an.party()")
an.party()
print("After third = an.party()")

print("\nBefore one more = an.party()")
PartyAnimal.party(an)
print("After one more = an.party()")

# Code: http://www.py4e.com/code3/party2.py
