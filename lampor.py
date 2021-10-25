top = input('Vilka färger på lamporna i högsta raden? ->')
right = input('Vilka färger på lamporna i högra kollumnen? ->')
bottom = input('Vilka färger på lamporna i lägsta raden? ->')
left = input('Vilka färger på lamporna i vänstra kollumnen? ->')
if len(bottom) != len(top) or len(left) != len(right):
    print('de är inte lika långa')

kollumn = len(right)
rad = len(top)
white = 0
for i in range(kollumn):
    for j in range(rad):
        rgb = set()
        rgb.add(top[j])
        rgb.add(right[i])
        rgb.add(bottom[j])
        rgb.add(left[i])
        if len(rgb) >= 3:
            white = white +1

print(white)