# Calculates the surface area of a cylinder

import math as m

def cylinder_surface_area():
    r = float(input("Enter the radius of cylinder: "))
    h = float(input("Enter the height of cylinder: "))
    surface_area = (2 * m.pi * r) * h + 2 * m.pi * r * r
    s = round(surface_area, 2)

    print(f"The surface area of your cylinder of radius {r} and height {h} is {s} units squared.")


cylinder_surface_area()