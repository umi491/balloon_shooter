def handle_enemy_movement(enemy, direction, speed_x, speed_y):
    if enemy.left <= 20 or enemy.right >= 550:
        direction *= -1
        speed_x = randint(0, 8) * direction
        speed_y = randint(0, 8) * direction

        if speed_x == 0 and speed_y == 0:
            speed_x = randint(2, 8) * direction
            speed_y = randint(2, 8) * direction
    
    if enemy.top <= 20 or enemy.bottom >= 550:
        direction *= -1
        speed_x = randint(0, 8) * direction
        speed_y = randint(0, 8) * direction

        if speed_x == 0 and speed_y == 0:
            speed_x = randint(2, 8) * direction
            speed_y = randint(2, 8) * direction
    
    enemy.left += speed_x
    enemy.top += speed_y