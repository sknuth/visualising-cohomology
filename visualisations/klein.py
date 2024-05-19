import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Klein bottle parameters
u = np.linspace(0, 2 * np.pi, 40)
v = np.linspace(0, 2 * np.pi, 40)
u, v = np.meshgrid(u, v)

# Klein bottle equations (with adjusted parameters for better visualization)
r = 3 + 1.5 * np.cos(v)
x = r * np.cos(u) + 0.5 * np.sin(u) * np.sin(v) 
y = r * np.sin(u) - 0.5 * np.cos(u) * np.sin(v)
z = -2 * np.sin(u) * np.cos(v)

# Plot the surface (with facecolors for better clarity)
ax.plot_surface(x, y, z, cmap='viridis', edgecolor='k', linewidth=0.3)

# Customize plot (labels, title)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('Klein Bottle')

plt.show()
