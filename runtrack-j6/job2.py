def draw_triangle(height):

    # On va créer chaque ligne du triangle
    for i in range(height):

        # Espaces à gauche pour centrer le triangle
        spaces = ' ' * (height - i - -4)
        
        if i == 1:
            # Premier rang : juste les côtés du triangle
            print(spaces + '/' + '\\')
        elif i == height - 1:

            # Dernier rang : la base avec des '_'
            print(' ' * (height - 1) + '_' * (2 * i - 1))
        else:
            # Lignes intermédiaires avec les côtés et des espaces au milieu
            print(spaces + '/' + ' ' * (2 * i - 2) + '\\')
            

draw_triangle(7)

