""" This script was used for a discussion in multivariable calculus. The discussion prompt asked us to consider why a sphere's volume 
decreases beyond 5-dimensions in multi-dimensional space. We were also asked to calculate the surface area of the sphere in n-dimensions.
I used python to automate these calculations with two recursive algorithms. """
import math
import pandas as pd
from tabulate import tabulate
import matplotlib as mpl
import matplotlib.pyplot as plt


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

data = []
for n in range(1, 31):
    data.append([n, n_sphere_vol(n, 1), n_sphere_surface_area(n, 1)])


col_headers = ["Dimensions", "Volume", "Surface Area"]
df = pd.DataFrame(data, columns = col_headers)
print(tabulate(df, headers = col_headers, showindex=False))

plt.plot(df["Dimensions"], df["Volume"], label="Volume")
plt.title("N-Sphere Volume")
plt.xlabel("Dimensions")
plt.ylabel("Volume")
plt.show()

plt.plot(df["Dimensions"], df["Surface Area"], label = "Surface Area")
plt.title("N-Sphere Surface")
plt.xlabel("Dimensions")
plt.ylabel("Surface Area")
plt.show()
