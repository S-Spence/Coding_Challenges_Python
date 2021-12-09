def max_happiness(days: int, rides: dict, k: int) -> int:
    
    max_happiness = 0
    for day in range(days):
        k_rides = []
        for key, val in rides.items():
            if day >= val[0] and day <= val[1]:
            
                if len(k_rides) < k:
                    k_rides.append(key)
                else:
                    for rating in k_rides:
                        if rating < key:
                            k_rides.remove(rating)
                            k_rides.append(key)
    
                happiness = sum(k_rides)
                if max_happiness < happiness:
                    max_happiness = happiness
    return max_happiness
                

# num test cases
T = int(input())
rides = {}
for i in range(1, T+1):
    info = input().strip().split()
    for j in range(int(info[1])):
        ride_info = input().strip().split()
        rating = int(ride_info[0])
        start = int(ride_info[1])
        end = int(ride_info[2])

        rides[rating] = [start, end]
        
    day = int(info[0])
    num_to_ride = int(info[2])
    happiness = max_happiness(day, rides, num_to_ride)
    print(f"Case #{i}: {happiness}")
