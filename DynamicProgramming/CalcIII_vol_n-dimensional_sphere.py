import math

# SSpence: Recursive algorithm to calculate the volume of an n-dimensional sphere
def n_sphere_vol(n: int, r: int)-> int:

    # The volume of a sphere in zero dimensions is one
    if n == 0:
        return 1
    # The volume of a sphere in two dimensions in 2*r
    elif n == 1:
        return 2*r
    # The volume of a sphere in 2 - n dimensions is (2*pi*r^2)/n * recursive call until n-2 reaches 1
    else:
        return 2 * math.pi * math.pow(r, 2)/n * n_sphere_vol(n-2, r)  

def n_sphere_surface_area(n: int, r: int)-> int:

    # In zero dimensions the surface area is 0
    if n == 0:
        return 0
    elif n == 1:
        return 2
    elif n == 2:
        return 2*math.pi
    else:
        return (2 * math.pi)/(n-2) * n_sphere_surface_area(n-2, 1)


for n in range(1, 11):
    print(f"{n}-dimensional sphere:")
    print(f"    volume: {n_sphere_vol(n, 1)}, surface area: {n_sphere_surface_area(n, 1)}")

