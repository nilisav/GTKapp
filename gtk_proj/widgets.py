import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

from matplotlib.backends.backend_gtk4agg import \
    FigureCanvasGTK4Agg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.animation as animation
import numpy as np
from sympy import *

from gtk_proj.model import PlotData

class Window(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        Gtk.ApplicationWindow.__init__(self, *args, **kwargs)
        app = kwargs['application']

        self.button_pressed = False
        self.fig = Figure(figsize=(16, 9), dpi=100, constrained_layout=False)
        self.ax = self.fig.add_subplot()
        self.line = None

        sw = Gtk.ScrolledWindow(margin_top=10, margin_bottom=10,
                            margin_start=10, margin_end=10)

        self.set_child(sw)
        self.ani = None

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, )
        sw.set_child(vbox)

        box = Gtk.Box(spacing=5)
        vbox.append(box)

        button_add_point = Gtk.Button()
        button_add_point.set_label("Добавить")

        button_add_point.connect('clicked', self.add_point)

        button_animation_show = Gtk.Button()
        button_animation_show.set_label("Показать")

        button_animation_show.connect('clicked', self.anime_on)

        button_animation_hide = Gtk.Button()
        button_animation_hide.set_label("Скрыть")

        button_animation_hide.connect('clicked', self.anime_off)

        self.data = PlotData()

        self.edit_x = Gtk.SpinButton(name="X", value=0)
        self.edit_y = Gtk.SpinButton(name="Y", value=0)

        for edit in {self.edit_x, self.edit_y}:
            edit.set_adjustment(Gtk.Adjustment(upper=100, step_increment=1, page_increment=10))

        button_quit = Gtk.Button()
        button_quit.set_label("Выйти")
        button_quit.connect('clicked', lambda x: app.quit())

        controls = (button_add_point, self.edit_x, self.edit_y, button_quit, button_animation_show, button_animation_hide)
        for c in controls:
            box.append(c)

        self.canvas = FigureCanvas(self.fig)
        self.canvas.set_size_request(800, 600)
        vbox.append(self.canvas)

    def add_point(self, *args, **kwargs):
        self.data.add_point(self.edit_x.get_value(), self.edit_y.get_value())
        if self.line is not None:
            self.line.remove()

        self.line, = self.ax.plot(*self.data)
        self.canvas.draw()

    def anime_off(self, *args, **kwargs):
            self.ani.event_source.stop()
            self.ax.cla()
            self.ax.plot(*self.data)
            self.canvas.draw()
            self.button_pressed = False

    def anime_on(self, *args, **kwargs):
            array = np.arange(0, 2*np.pi, 0.1)
            t = symbols('t')
            funcx = 16 * sin(t) ** 3
            funcy = 13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t)
            xarr, yarr = [], []


            for elem in array:
                xarr.append(funcx.subs(t, elem)*0.025 + 10)
                yarr.append(funcy.subs(t, elem)*0.025 + 10)

            line2 = self.ax.plot(xarr[0], yarr[0])[0]

            self.button_pressed = True

            def update_heart(frame):
                line2.set_xdata(xarr[:frame])
                line2.set_ydata(yarr[:frame])
                return [line2]

            self.ani = animation.FuncAnimation(
                fig=self.fig,
                func=update_heart,
                frames=100,
                interval=50,
                repeat=True
            )

            self.canvas.draw()