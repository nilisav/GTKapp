from matplotlib.animation import FuncAnimation
import time
import matplotlib.pyplot as plt
import numpy as np
from sympy import *


tata = np.arange(0, 2*np.pi, 0.1)
x = symbols('x')
y = symbols('y')

arr = []
arr2 = []

for elem in tata:
    arr.append(func2.subs(t, elem))
    arr2.append(func3.subs(t, elem))

line2 = ax.plot(arr[0], arr2[0])[0]

def update_heart(frame):
    xar = arr[:frame]
    yar = arr2[:frame]
    line2.set_xdata(arr[:frame])
    line2.set_ydata(arr2[:frame])
    return [line2]



plt.ioff()
plt.show()





"""    def anime(self, *args, **kwargs):
        if self.anim_pressed:
            self.ani.event_source.stop()
            self.ax.cla()
            self.ax.plot(*self.data)
            self.canvas.draw()
            self.anim_pressed = False

        else:
            t = np.arange(0, 2*np.pi, 0.1)

            xx = 16*np.sin(t)

            yy = 13*np.cos(t) - 5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)

            scat = self.ax.scatter(xx[0], yy[0], s=5)
            line2 = self.ax.plot(xx[0], yy[0])[0]

            self.anim_pressed = True

            def update(frame):
                x = xx[:frame]
                y = yy[:frame]
                data = np.stack([x, y]).T
                scat.set_offsets(data)
                line2.set_xdata(xx[:frame])
                line2.set_ydata(yy[:frame])
                return [scat, line2]

            self.anim = animation.FuncAnimation(fig=self.fig, func=update, frames=40, interval=30)

            self.canvas.draw()"""