import numpy as np
import matplotlib.pyplot as plt

domain = np.arange(-10,10,0.05)
squared = np.power(domain,2)

fig, ax = plt.subplots()

ax.plot(domain, squared, color="blue")

points = np.array([7,5,3,-2,1,0])
labels = [1,2,3,4,5,6]
points_squared = np.power(points, 2)
ax.scatter(points, points_squared, color="red")

for ind, txt in enumerate(labels):
    ax.annotate(txt, (points[ind], points_squared[ind]), (points[ind]+0.1, points_squared[ind]+4.5))
plt.show()
