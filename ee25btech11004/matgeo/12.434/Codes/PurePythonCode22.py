import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg

vec1 = np.array([2,-3,0])
vec2 = np.array([3,2,0])

cross = np.cross(vec1, vec2)
area = np.linalg.norm(cross)

print(area)

fig = plt.figure(figsize = (7,7))
ax = fig.add_subplot(111)

ax.quiver(0,0,2,-3, color = 'green', label = '$a$',  angles='xy', scale_units='xy', scale=1)
ax.quiver(0,0,3,2, color = 'orange', label = '$b$',  angles='xy', scale_units='xy', scale=1)
ax.quiver(3,2,2,-3, color = 'red', label = '$a$',  angles='xy', scale_units='xy', scale=1)
ax.quiver(2,-3,3,2, color = 'purple', label = '$b$',  angles='xy', scale_units='xy', scale=1)

ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')


ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)
ax.grid(True)
ax.legend()
plt.show()