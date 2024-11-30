def calculate_distance(num_steps, step_height_cm):
    
    # Calculer la distance pour un aller-retour aux toilettes
    distance_per_trip_cm = 2 * num_steps * step_height_cm

    # Nombre de fois que le gardien va aux toilettes par jour
    trips_per_day = 5

    # Nombre de jours dans une semaine
    days_per_week = 7

    # Calculer la distance totale parcourue en une semaine en centimètres
    total_distance_cm = distance_per_trip_cm * trips_per_day * days_per_week

    # Convertir la distance de centimètres en mètres
    total_distance_m = total_distance_cm / 100

    # Afficher le résultat
    print(f"Pour {num_steps} marches de {step_height_cm} cm, le gardien parcourt {total_distance_m:.2f} m par semaine.")

# Exemple d'utilisation
num_steps = 100  # Nombre de marches
step_height_cm = 20  # Hauteur de chaque marche en cm
calculate_distance(num_steps, step_height_cm)
