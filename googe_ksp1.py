


"""def sum_distances(n: int, cans: list)-> int:
    house_cans = {} # store cans or no cans
    dist_sum = 0
    
    if sum(cans) == 0:
        return 0 
    
    for i in range(len(cans)):
        if cans[i] == 1:
            house_cans[i+1] = 1
    
    for i in range(n):
        dist_closest = len(cans)
        if i+1 not in house_cans.keys():
            for j in house_cans.keys():
                dist = abs(j-(i+1))
                
                if dist < dist_closest:
                    dist_closest = dist
        else:
            dist_closest = 0

        dist_sum += dist_closest
    return dist_sum

if __name__ == "__main__":
    
    # Collect input for number of test cases
    T = int(input())
    list_tests = []
    # Collect input until number of tests reached
    for i in range(T):
        test = input().strip().replace(" ", "")
        N = int(test[0])
        
        if len(test)-1 == N:
            trash_cans = [int(test[i]) for i in range(1, N+1)]
            total_dist = sum_distances(N, trash_cans)
            list_tests.append(total_dist)
    for i in range(len(list_tests)):
        print(f"Case #{i+1}: {list_tests[i]}")"""
def sum_distances(n: int, cans: list)-> int:
    house_cans = {} # store cans or no cans
    dist_sum = 0
    
    if sum(cans) == 0:
        return 0
    
    for i in range(len(cans)):
        if cans[i] == 1:
            house_cans[i+1] = 1
    
    for i in range(n):
        dist_closest = len(cans)
        if i+1 not in house_cans.keys():
            for j in house_cans.keys():
                dist = abs(j-(i+1))
                
                if dist < dist_closest:
                    dist_closest = dist
        else:
            dist_closest = 0

        dist_sum += dist_closest
    return dist_sum
                
            

    
# Collect input for number of test cases
T = int(input())
list_tests = []
# Collect input until number of tests reached
for i in range(T):
    test = input().strip().replace(" ", "")
    N = int(test[0])
    if len(test)-1 == N:
        trash_cans = [int(test[i]) for i in range(1, N+1)]
        total_dist = sum_distances(N, trash_cans)
        list_tests.append(total_dist)
for i in range(len(list_tests)):
    print(f"Case #{i+1}: {list_tests[i]}")

    
