def time_to_text(minutes):

    # Vérifier que le nombre de minutes est un entier positif

    if isinstance(minutes, int) and minutes >= 0:
        heures = minutes // 60  #heures
        minutes_restantes = minutes % 60  # minutes
        print(f"{heures} heures et {minutes_restantes} minutes")
    else:
        print("Veuillez entrer un nombre entier de minutes positif.")


#execution

time_to_text(125)
time_to_text(45) 
time_to_text(90) 
time_to_text(-10)
time_to_text(-30)
time_to_text(800)