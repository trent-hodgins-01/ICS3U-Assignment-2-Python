# !/usr/bin/env python3

# Created by Trent Hodgins
# Created on 09/23/2021
# This program calculates the surface area of a sphere
# The user enters the radius

import math


def main():
    # This calculates the circumference

    # input
    print("We will be calculating the surface area of a sphere")
    radius = int(input("Enter in the radius (mm): "))
    print("")

    # process
    surface_area = 4 * math.pi * radius * radius

    # output
    print("Surface Area is {} mm.".format(surface_area))
    print("\nDone.")


if __name__ == "__main__":
    main()
