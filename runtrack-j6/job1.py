def draw_rectangle(width, height):
    # Dessiner la première ligne du rectangle (composée de '-')
    print('-' * width)

    # Dessiner les lignes intermédiaires (composées de '|' aux extrémités)
    for _ in range(height - 2):
        print('|' + ' ' * (width - 2) + '|')
        print('|' + ' ' * (width - 2) + '|')
        print('|' + ' ' * (width - 2) + '|')

    # Dessiner la dernière ligne du rectangle (composée de '-')
    if height > 1:
        print('-' * width)

draw_rectangle(10, 3)
