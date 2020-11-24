"""
Eric Meehan
2020-11-24

Solar Doomsday
"""

import math

def main():
    # Save the total area of the solar material
    TotalArea = 15324
    # An empty array to store the size of each panel
    Results = []
    # Generate new panels until there is no more material left
    while TotalArea > 0:
        # The surface area of the largest possible panel is the square root of the remaining area, rounded down to the nearest integer, squared.
        Panel = int(math.sqrt(TotalArea)) ** 2
        # Add this panel to the list
        Results.append(Panel)
        # Decrement the remaining area
        TotalArea -= Panel
    # Output the results
    print(Results)

main()
