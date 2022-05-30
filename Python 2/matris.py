import numpy as np

def get_element(mat_A, mat_B, i, j):
    '''
    Parametrar:
        mat_A och mat_B: matriser av typen ndarray
        i och j: rad- och kolonnindex, 1-baserat
    Returvärde:
        Givet att matriserna är multiplicerbara:
            talet på den önskade positionen
        Givet att matriserna inte är multiplicerbara:
            None
    '''
    result = np.array([])
    # Här processas matriserna mat_A och mat_B
    # samt att värdet på result uppdateras
    return result

# Ingångsvärden, kan förändras
A = np.array([[1, 2, 3], [4, 5, 6]])  # 2x3-matris
B = np.array([[2, 3], [4, 5], [6, 7]])  # 3x2-matris
i, j = 2, 1  # Sökt index, rad och kolonn

# Ändra inget under denna rad,
# men ta gärna inspiration till det som
# behöver skrivas i funktionen get_element.
number_of_rows_in_A = A.shape[0]
number_of_cols_in_B = B.shape[1]

if i <= number_of_rows_in_A and i > 0 and j <= number_of_cols_in_B and j > 0:
    c_ij = get_element(A, B, i, j)
    if c_ij != None:
        # Skriver ut talet 64 givet
        # ingångsvärdena som de var från början
        print(c_ij)
    else:
        print("De angivna matriserna är inte multiplicerbara med varandra")
else:
    print("Begärt index finns ej i resultatmatrisen")
print("Programmet avslutades normalt")