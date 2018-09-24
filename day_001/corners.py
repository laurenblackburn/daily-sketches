# 9/22/18

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.collections import PatchCollection
import numpy as np

def normalize_color(value, value_range):
    total_range = max(value_range) - min(value_range)
    value_dist = value - min(value_range)
    return value_dist / total_range

def center_rotated_square(a, theta, color):
    d = -a/2
    y = (d/np.cos(theta)) - (d*np.sin(theta)) + (d*np.cos(theta))
    x = (d*np.cos(theta)) - (d*np.sin(theta))
    square = patches.Rectangle(
        (x, y), a, a, theta*(180/np.pi),
        fill = False, edgecolor=color)
    return square

fig, ax = plt.subplots()
shapes = []

width = range(20, 300, 20)
for w in width:
    green_rect = center_rotated_square(
        w,
        np.pi/4,
        (0, normalize_color(w, width), 0))
    shapes.append(green_rect)

    red_rect = center_rotated_square(
        w,
        np.pi/3,
        (normalize_color(w, width), 0, 0))
    shapes.append(red_rect)

    blue_rect = center_rotated_square(
        w,
        np.pi/6,
        (0, 0, normalize_color(w, width)))
    shapes.append(blue_rect)

collection = PatchCollection(shapes, match_original=True)
ax.add_collection(collection)

ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)
plt.axis('off')
plt.show()


# day 1: ~2.5 hours. rotation around center is still off ...
