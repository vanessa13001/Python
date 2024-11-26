# Boucle allant de 1 à 100 inclus
for i in range(1,101):
 # Vérification si le nombre est un multiple de 3 et de 5
    if i % 3== 0 and i % 5 == 0:
     print("FizzBuzz")
 # Vérification si le nombre est un multiple de 3
    elif i % 3 ==0:
       print("Fizz")
    # Vérification si le nombre est un multiple de 5
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
