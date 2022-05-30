AntalSidor = int(input('Hur många sidor har boken?'))
all = ''
for i in range(AntalSidor):
    if (i+1)%2 != 0:
      all += (str(i+1))
noll = all.count('0')
ett = all.count('1')
två =  all.count('2')
tre = all.count('3')     
fyra = all.count('4')
fem = all.count('5')
sex = all.count('6')
sju = all.count('7')
åtta = all.count('8')
nio = all.count('9')
print(noll,ett,två,tre,fyra,fem,sex,sju,åtta,nio)         
        