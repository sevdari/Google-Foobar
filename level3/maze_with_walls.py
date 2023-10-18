def solution(map):
    w = len(map[0])
    h = len(map)
    
    # map pos: steps, wall
    seen = {(0, 0): 0}
    seen_wall = {}
    # queue for BFS
    queue = [[0, 0, False]]
    # possible moves
    moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    
    steps = 1
    while True:
        steps += 1
        new_queue = []
        for pos in queue:
            for move in moves:
                x = pos[0] + move[0]
                y = pos[1] + move[1]

                # reached the end
                if x == h-1 and y == w-1:
                    return steps
                
                # invalid move
                if x < 0 or x >= h or y < 0 or y >= w:
                    continue
                
                # already used a wall
                if map[x][y] == 1 and pos[2]:
                    continue

                # been here before
                if (x, y) in seen:
                    if steps >= seen[(x, y)]:
                        continue
                
                if pos[2]:
                    if (x, y) in seen_wall:
                        if steps >= seen_wall[(x, y)]:
                            continue
                    seen_wall[(x, y)] = steps
                    new_queue.append([x, y, True])
                else:
                    if map[x][y] == 1:
                        if (x, y) not in seen_wall or steps < seen_wall[(x, y)]:
                            seen_wall[(x, y)] = steps
                            new_queue.append([x, y, True])
                    else:
                        seen[(x, y)] = steps
                        new_queue.append([x, y, False])
        queue = new_queue
            
if __name__ == "__main__":
    map = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
    for i in map:
        print(i)
    solution(map)