def solution(dimensions, your_position, trainer_position, distance):

    if your_position == trainer_position:
        return 0

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    
    def calc_direction(your_position, trainer_position):
        x = trainer_position[0] - your_position[0]
        y = trainer_position[1] - your_position[1]
        a, b = max(abs(x), abs(y)), min(abs(x), abs(y))
        norm = gcd(a, b)
        x = x / norm
        y = y / norm
        return (x, y)
    
    def calc_distance(your_position, trainer_position):
        x = trainer_position[0] - your_position[0]
        y = trainer_position[1] - your_position[1]
        return (x**2 + y**2)**0.5
    
    def get_reflection(i, j, a, b, target):
        if i % 2 == 1:
            x = i * a + (a - target[0])
        else:
            x = i * a + target[0]
        
        if j % 2 == 1:
            y = j * b + (b - target[1])
        else:
            y = j * b + target[1]
        return (x, y)
        
    
    a, b = dimensions
    hor_len = distance // a + 1
    ver_len = distance // b + 1
    
    def generate_directions(target, distance):
        directions = {}
        for i in range(-hor_len, hor_len+1):
            for j in range(-ver_len, ver_len+1):

                x, y = get_reflection(i, j, a, b, target)
                
                dist = calc_distance(your_position, (x, y))
                if dist == 0:
                    continue
                if dist <= distance:
                    direction = calc_direction(your_position, (x, y))
                    
                    if direction not in directions:
                        directions[direction] = dist
                    else:
                        if dist < directions[direction]:
                            directions[direction] = dist

        return directions
    
    enemy_directions = generate_directions(trainer_position, distance)
    your_directions = generate_directions(your_position, distance)

    count = 0
    for dir in your_directions:
        if dir in enemy_directions:
            if your_directions[dir] <= enemy_directions[dir]:
                count += 1
    
    return len(enemy_directions) - count
    

if __name__ == "__main__":
    print(solution([2,3], [1,1], [1,2], 4)) # 7
    print(solution([2,3], [1,1], [1,2], 100)) # 3995
    print(solution([300,275], [150,150], [185,100], 500)) # 9