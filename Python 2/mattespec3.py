# Denna fil behöver inte ändras, enbart ligga i samma
# katalog som den filen som anropas den definierade funktionen.

import numpy as np
sus = float(input('Vad är din gissning?-->'))

def numeric_derivative(f, h):
    '''
    Utför numerisk derivering på en funktion med central differenskvot.
    Parametrar:
    arg1 : En funktion, x |-> f(x), där x och f(x) är tal.
           Det är vid x-värdet som deriveringen utförs.
    arg2 : Ett tal som anger hur nära x-värdet vi ska gå i beräkningen
           i den centrala differenskvoten (typiska h: 0.1, 0.01, 0.001).
    Returnerar: Derivatan av funktionen som ett tal, evaluerad vid x.
    '''

    # Funktionen som skickades med i parametern anropas
    # i uttrycket nedan.
    if h != 0:
        def derivative(x): return (f(x+h)-f(x-h)) / (2*h)
        return derivative

    print('h måste vara nollskild.')
    return None


# Nedanstående körs ej om denna fil inkluderas
# som modul från en annan fil.
if __name__ == '__main__':
    # En funktion f(x) definieras
    def f(x): return np.exp(x)
    h = 0.1

    # Användning av deriveringsfunktionen
    fprime = numeric_derivative(f, h)
    if fprime:
        print(fprime(1))
# Denna fil använder funktionen numeric_derivative, som
# finns defnierad  i filen derivata.py.
# Filen är fullt körbar, men behöver ändras / kompletteras
# för att lösa uppgifterna som hör till den.
import math as m

def formel(x):
    f(x) = x**2
    return (x-(f(x)(derivative(x))))
    print(x)

for i in range(10):
    formel(x)
    print




# Detta värde ska gå mot noll, pröva h = 0.1,
# h = 0.01 och # h= 0.001 och se vad det blir
# för skillnad
h = 0.1

# Deriveringspunkt (i det här fallet x = pi)
x = 10

# Derivatans funktion skapas med hjälp av
# funktionen numeric_derivative (som definieras
# i filen derivata.py).
# Filen derivata.py måste ligga i samma
# katalog som denna fil (newton-raphson.py).
fprime = numeric_derivative(f, h)
print(f"f'({x:.2f}) ≈ {fprime(x)}")
