
g = [[True, False, True], [False, True, False], [True, False, True]]
g2 = [[True, True, False, True, False, True, False, True, True, False], [True, True, False, False, False, False, True, True, True, False], [True, True, False, False, False, False, False, False, False, True], [False, True, False, False, False, False, True, True, False, False]]
g3 = [[True, False, True, False, False, True, True, True], [True, False, True, False, False, False, True, False], [True, True, True, False, False, False, True, False], [True, False, True, False, False, False, True, False], [True, False, True, False, False, True, True, True]]

def solution(g):
    def permute(n):
        if n == 1:
            return [[0], [1]]
        else:
            return [[0] + x for x in permute(n-1)] + [[1] + x for x in permute(n-1)]
    
    def count_neighbors(cell, grid):
        moves = [(0, 0), (0, 1), (1, 0), (1, 1)]
        count = 0
        for i, j in moves:
            count += grid[cell[0]+i][cell[1]+j]
        return count


    def check(perm1, perm2, col):
        temp = []
        for i in range(len(perm1)):
            temp.append([perm1[i], perm2[i]])
        for i in range(len(temp)-1):
            if  count_neighbors((i, 0), temp) == 1:
                if g[i][col] == False:
                    return False
            else:
                if g[i][col] == True:
                    return False
        return True

    def check_single(perm, col):
        for i in range(len(perm)-1):
            if g[i][col] == True and perm[i] == 1 and perm[i+1] == 1:
                return False
        return True
    

    permutations = permute(len(g)+1)
    current, past = [0 for _ in range(len(permutations))], [1 for _ in range(len(permutations))]
    
    for col in range(len(g[0])-1, -1, -1):
        for i in range(len(permutations)):
            for j in range(len(permutations)):
                if not check_single(permutations[i], col):
                    continue
                if check(permutations[i], permutations[j], col):
                    current[i] += past[j]
        past = current
        current = [0 for _ in range(len(permutations))]
    
    return sum(past)

solution(g), solution(g2), solution(g3) # (4, 11567, 254)