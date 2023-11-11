
def solution(g):
    """
    This solution does a left swipe through the columns of the grid by
    using dynamic programming and memoization.
    At each column we ask the question:
    Given a certain permutation and restricting the grid to the 
    previous columns and the current column, how many solutions are there 
    such that the current column is filled like the permutation?
    """

    def permute(n):
        # Returns all permutations of length n where each element is either 0 or 1.
        if n == 1:
            return [[0], [1]]
        else:
            return [[0] + x for x in permute(n-1)] + [[1] + x for x in permute(n-1)]
    
    def generate_column(perm1, perm2):
        # Generates a column given two permutations based on the rules of the game.
        column = []
        for i in range(len(perm1)-1):
            current_sum = perm1[i] + perm2[i] + perm1[i+1] + perm2[i+1]
            column.append(True if current_sum == 1 else False)
        return tuple(column)
    
    # auxillary data structures
    rows = len(g) + 1
    permutations = permute(rows)
    columns, column_generated_from = [], {}
    current, past = [0 for _ in range(len(permutations))], [1 for _ in range(len(permutations))]
    for col in range(len(g[0])):
        current_column = tuple([g[i][col] for i in range(len(g))])
        columns.append(current_column)
        column_generated_from[current_column] = []
    
    # from which permutations can a column be generated
    for i in range(len(permutations)):
        for j in range(len(permutations)):
            column = generate_column(permutations[i], permutations[j])
            if column not in column_generated_from:
                continue
            column_generated_from[column].append((i, j))
    
    # dynamic programming left swipe through the grid
    for col in range(len(columns)-1, -1, -1):
        current_column = columns[col]
        for i, j in column_generated_from[current_column]:
            current[i] += past[j]
        past = current
        current = [0 for _ in range(len(permutations))]
    
    return sum(past)

if __name__ == "__main__":
    solution(g), solution(g2), solution(g3) # (4, 11567, 254)