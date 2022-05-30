class Elev:
    def __init__(self,namn,ålder,godkänd):
        self.namn = namn
        self.ålder = ålder
        self.godkänd = godkänd
        if self.godkänd == True:
            print('Glad')
Elev1 = Elev('Kalle',80,True)
  

print(Elev1.namn,Elev1.ålder)



