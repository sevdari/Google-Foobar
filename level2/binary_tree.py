def solution(h, q):
    answer = []
    
    for i in q:
        count = 0
        root = 2**h - 1
        if i == root:
            answer.append(-1)
            continue
        
        while True:
            if i == root//2 or i == root-1:
                answer.append(root + count)
                break
            if i > root//2:
                count += root//2
                i -= root//2
            root = root//2
    return answer

if __name__ == "__main__":
    solution(3, [7, 3, 5, 1])   