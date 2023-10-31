from itertools import permutations 

def solution(times, time_limit):

    # Auxiliary functions
    def bellman_ford(times, start):
        """
        Runs the Bellman-Ford algorithm.
        Returns False if there is a negative cycle.
        """
        dist = [i for i in times[start]]
        for k in range(len(times)+1):
            for i in range(len(times)):
                for j in range(len(times)):
                    if dist[j] > dist[i] + times[i][j]:
                        if k == len(times):
                            return False
                        dist[j] = dist[i] + times[i][j]
        return dist
    
    def check_path(shortest_paths, path):
        """
        Checks if the provided path is a valid path.
        """
        total = shortest_paths[0][path[0]]
        for i in range(0, len(path)-1):
            total += shortest_paths[path[i]][path[i+1]]
        total += shortest_paths[path[-1]][len(shortest_paths)-1]
        return total
    
    # Actual script starts here
    default_solution = [i for i in range(len(times)-2)]

    # generate all pairs shortest paths
    shortest_paths = []
    for i in range(len(times)):
        temp = bellman_ford(times, i)
        if temp == False:
            return default_solution
        shortest_paths.append(temp)
    
    default_solution = [i + 1 for i in range(len(times)-2)]

    # generate all possible paths
    for i in range(len(times)-2, 0, -1):
        for path in permutations(default_solution, i):
            if check_path(shortest_paths, path) <= time_limit:
                return sorted([i-1 for i in list(path)])
            
    return []

solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3)