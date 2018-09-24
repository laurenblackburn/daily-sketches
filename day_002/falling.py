# 9/23/18

import matplotlib.pyplot as plt
import numpy as np

def projectile_motion(x, v, a, t):
    return x + v*t + 0.5*a*(t**2)

fig, ax = plt.subplots()

time = np.arange(60)
time2 = np.arange(60*2)

x1 = projectile_motion(0, 300*np.cos(np.pi / 2.5), 0, time2)
y1 = projectile_motion(0, 300*np.sin(np.pi / 2.5), -9.8, time2)
ax.plot(x1, y1, color="xkcd:deep sky blue")

#x2 = projectile_motion(4000, 0, 0, time)
#y2 = projectile_motion(4000, 0, -9.8, time)
#ax.plot(x2, y2, color = 'xkcd:fire engine red')

x3 = projectile_motion(0, 150, 0, time)
y3 = projectile_motion(0, 0, -9.8, time)
ax.plot(x3, y3, color = 'xkcd:avocado green')

x4 = projectile_motion(0, 30, 0, time)
y4 = projectile_motion(0, 0, -9.8, time)
ax.plot(x4, y4, color = 'xkcd:rust orange')

x5 = projectile_motion(0, 0, 0, time)
y5 = projectile_motion(0, 0, -9.8, time)
ax.plot(x5, y5, color = 'xkcd:reddy brown')

x6 = projectile_motion(0, 300*np.cos(np.pi / 3), 0, time)
y6 = projectile_motion(0, 300*np.sin(np.pi / 3), -9.8, time)
ax.plot(x6, y6, color = 'xkcd:bright sky blue')

x7 = projectile_motion(0, 400*np.cos(np.pi / 2.8), 0, time2)
y7 = projectile_motion(0, 400*np.sin(np.pi / 2.8), -9.8, time2)
ax.plot(x7, y7, color="xkcd:carolina blue")

x8 = projectile_motion(0, 200*np.cos(np.pi / 3.4), 0, time)
y8 = projectile_motion(0, 200*np.sin(np.pi / 3.4), -9.8, time)
ax.plot(x8, y8, color="xkcd:water blue")

x9 = projectile_motion(0, 30, 20, time2)
y9 = projectile_motion(0, 0, 0, time2)
ax.plot(x9, y9, color='xkcd:camouflage green')

x10 = projectile_motion(0, 75, 0, time)
y10 = projectile_motion(0, 0, -9.8, time)
ax.plot(x10, y10, color='xkcd:muddy yellow')

x11 = projectile_motion(0, 400, 0, time)
y11 = projectile_motion(0, 0, -9.8, time)
ax.plot(x11, y11, color='xkcd:fern green')

x12 = projectile_motion(0, 350 * np.cos(np.pi / 2.4), 0, time2)
y12 = projectile_motion(0, 350 * np.sin(np.pi / 2.4), 0, time2)
ax.plot(x12, y12, color='xkcd:sunshine yellow')

ax.set_ylim(-10000, 8000)
ax.set_xlim(-100, 10000)
plt.axis("off")
plt.show()

# inspired by today's recurring theme of projectile motion, flying, and falling
