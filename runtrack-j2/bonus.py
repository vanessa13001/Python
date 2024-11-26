#afficher le carré des chiffres pair jusqu'à 20
x = 0 
y = 0
while x < 20:
    x += 2
    y = x**2
    print(y)

for x in range (2, 21, 2):
    x = x**2
    print(x)