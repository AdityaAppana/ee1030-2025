import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg
import ctypes

c_lib = ctypes.CDLL('./22c.so')

vecA = np.array([2,-3,0])
vecB = np.array([3,2,0])

c_lib.crossx.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
c_lib.crossx.restype = ctypes.c_int

answerx = c_lib.crossx(
    ctypes.c_int(vecA[1]),
    ctypes.c_int(vecB[2]), 
    ctypes.c_int(vecA[2]),
    ctypes.c_int(vecB[1])
)

c_lib.crossy.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
c_lib.crossy.restype = ctypes.c_int

answery = c_lib.crossy(
    ctypes.c_int(vecA[0]),
    ctypes.c_int(vecB[2]), 
    ctypes.c_int(vecA[2]),
    ctypes.c_int(vecB[0])
)



c_lib.crossz.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
c_lib.crossz.restype = ctypes.c_int

answerz = c_lib.crossz(
    ctypes.c_int(vecA[0]),
    ctypes.c_int(vecB[1]), 
    ctypes.c_int(vecA[1]),
    ctypes.c_int(vecB[0])
)

crossvec = np.array([answerx, answery, answerz])
print(crossvec)


c_lib.norm.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_float]
c_lib.norm.restype = ctypes.c_float


answer = c_lib.norm(
    ctypes.c_float(crossvec[0]),
    ctypes.c_float(crossvec[1]), 
    ctypes.c_float(crossvec[2]),
)

print(answer)


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