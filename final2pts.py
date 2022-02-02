import numpy as np
from Bezier import Bezier
import matplotlib.pyplot as plt

t_points = np.arange(0, 1, 0.01)
points1 = np.array([[6, 3], [4, 3], [1, 2], [-1, 2]])
curve1 = Bezier.Curve(t_points, points1)

plt.figure()
plt.plot(
    curve1[:, 0],   # x-coordinates.
    curve1[:, 1]    # y-coordinates.
)
plt.plot(
    points1[:, 0],  # x-coordinates.
    points1[:, 1],  # y-coordinates.
    'ro:'
)
plt.grid()
plt.show()
