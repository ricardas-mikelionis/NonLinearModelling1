from __future__ import division
import QuatMath
import matplotlib.pyplot as plt
import numpy as np

# pradinis kvaternijonas
z = [0.5, 0, 0, 0]

# Paveikslelio rezoliucija (r2,r4 kintamosions reiksmes)
resolutionX = 400
resolutionY = 200

# Apibreziama "begalybe"
infinity = 1000000

# Stabiliosios r kvaternijono reiksmes
r1 = 0.0
r3 = 0.0

# X reziai
xmin = -100.0
xmax = 100.0

# Y reziai
ymin = -100.0
ymax = 100.0

# intervalo ilgiai
hx = (xmax - xmin) / (resolutionX - 1)
hy = (ymax - ymin) / (resolutionY - 1)

matrix = [[128]*resolutionX]*resolutionY
matrix1 = matrix
for j in range(0, resolutionY):
    for k in range(0, resolutionX):
        r = [r1, (xmin + (hx * k)), r3, (ymin + (hy * j))]
        one = [1, 0, 0, 0]
        count = 0
        z = [0.5, 0, 0, 0]

        while count < 256 and QuatMath.absquat(z) < infinity:

            sub = QuatMath.subtraction(one, z)
            mul = QuatMath.multiplication(r, z)
            z = QuatMath.multiplication(mul, sub)
            count += 1
        matrix[j][k] = count


plt.imshow(matrix1, cmap="gray")
plt.show()

