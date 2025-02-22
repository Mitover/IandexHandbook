def can_eat(hourse_position, target_position):
    dx = abs(hourse_position[0] - target_position[0])
    dy = abs(hourse_position[1] - target_position[1])
    return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)