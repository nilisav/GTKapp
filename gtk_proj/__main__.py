import gi

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gdk

from gtk_proj.widgets import Window

class Application(Gtk.Application):
    def on_activate(self, _):
        win = Window(application=self)
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path("style.css")
        Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(), css_provider,
                                                  Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        win.set_css_classes(['window'])
        win.set_default_size(800, 800)
        win.set_title("Embedding in GTK4")
        win.set_visible(True)
        self.win = win
        self.connect('activate', self.on_activate)


app = Application(application_id='org.matplotlib.examples.EmbeddingInGTK4')
app.connect('activate', app.on_activate)

def monkeypatch():
    print('haha')

app.monkeypatch = monkeypatch

app.run(None)
