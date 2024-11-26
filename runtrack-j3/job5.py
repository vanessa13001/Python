# Fonction pour vérifier si un nombre est premier
def est_premier(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
              return False
    return True
#afficher des nombres premiers jusqu'à 1000
for num in range(1, 1001):
     if est_premier(num):
          print(num)