# this program will calculate how many cans of paint needed to paint a wall, 1 can = 5 square meter
import math

def paint_calc(height,width,cover):
    cans = (height * width) / cover
    results = int(math.ceil(cans))
    return results

height_wall = int(input("Height of wall: "))
width_wall = int(input("Width of wall: "))
coverage = 5
cans_need = paint_calc(height=height_wall, width=width_wall, cover=coverage)

print(f"You'll need {cans_need} cans of paint.")


