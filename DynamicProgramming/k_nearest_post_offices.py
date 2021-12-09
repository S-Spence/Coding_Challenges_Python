"""Find the k post offices located closest to you, given your location and a list of locations of all post offices available.
Locations are given in 2D coordinates in [X, Y], where X and Y are integers.
Euclidean distance is applied to find the distance between you and a post office.
Assume your location is [m, n] and the location of a post office is [p, q], the Euclidean distance between the office
and you is SquareRoot((m - p) * (m - p) + (n - q) * (n - q)).
K is a positive integer much smaller than the given number of post offices. from aonecode.com

e.g.
Input
you: [0, 0]
post_offices: [[-16, 5], [-1, 2], [4, 3], [10, -2], [0, 3], [-5, -9]]
k = 3

Output from aonecode.com
[[-1, 2], [0, 3], [4, 3]]"""
import math

def nearest_office(start: list, offices: list, k: int) -> int:
    m = start[0] # Starting x
    n = start[1] # Starting y
    dist_loc = {}     # Mapping of distances to locations
    k_locations = []  # K-closest locations

    # If no post offices, return
    if len(offices) == 0:
        return
    print(len(offices))
    # iterate through the offices and add distances to the dist:location dictionary
    for l in offices:
        p = l[0]
        q = l[1]
        distance = math.sqrt(((m-p) * (m-p)) + ((n-q) * (n-q)))
        if distance not in dist_loc.keys():
            dist_loc[distance] = l
        else:
            dist_loc[distance] = 

    # Sort dictionary keys to find k-closest
    sorted_dist = sorted(dist_loc.keys())
    print(sorted_dist)
    # Create the list of k closest locations
    if len(sorted_dist) > k:
        for i in range(k):
            k_locations.append(dist_loc[sorted_dist[i]])
    else:
        for val in sorted_dist:
                k_locations.append(dist_loc[val])

    return k_locations

you = [0, 0]
post_offices = [[-16, 5], [-1, 2], [4, 3], [10, -2], [0, 3], [-5, -9]]
#offices = [[3, 3], [-5, 1], [-2, 4]]
offices = [[0,1], [1, 0]]
print(nearest_office(you, offices, 2))


