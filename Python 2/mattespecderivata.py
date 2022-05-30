# Denna fil behöver inte ändras, enbart ligga i samma
# katalog som den filen som anropas den definierade funktionen.

import numpy as np


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