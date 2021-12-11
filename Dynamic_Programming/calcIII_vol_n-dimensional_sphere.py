"""This script was used for a discussion in multivariable calculus. The discussion prompt asked us to consider why a sphere's volume 
decreases beyond 5-dimensions in multi-dimensional space. We were also asked to calculate the surface area of the sphere in n-dimensions.
I used python to automate these calculations with two recurisive algorithms."""

import math

def n_sphere_vol(n: int, r: int)-> int:
    """Recursive algorithm to calculate the volume of an n-dimensional sphere"""

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
    """Recursive algorithm to calculate the surface area of an n-dimensional sphere"""

    # In zero dimensions the surface area is 0
    if n == 0:
        return 0
    # In one dimension, the surface area is 2
    elif n == 1:
        return 2
    # In two dimensions, the surface area is 2pi
    elif n == 2:
        return 2*math.pi
    # In higher dimensions, the surface area is 2pi/n-2 * a recursive call to this function until n-2 reaches 2
    else:
        return (2 * math.pi)/(n-2) * n_sphere_surface_area(n-2, 1)

for n in range(1, 11):
    print(f"{n}-Dimensional Sphere:")
    print(f"    Volume: {n_sphere_vol(n, 1)} | Surface Area: {n_sphere_surface_area(n, 1)}")

