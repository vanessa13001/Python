def calcul(num1, operator, num2):
    if operator == "+":
        return print (num1 + num2)
    elif operator == "-":
        return print(num1 - num2)
    elif operator == "*":
        return print(num1 * num2)
    elif operator == "/":
        if num2 != 0:
            return print(num1 / num2)
        else:
            return print("Erreur : Division par zéro")
    elif operator == "%":
        return print(num1 % num2)
    else:
        return print("Erreur : Opérateur invalide")
    
num1 = float(input("entrez le 1er numero "))
operator = input("entrez l'opérateur (+, -, *, /, %) ")
num2 = float(input("entrez le deuxieme numero "))