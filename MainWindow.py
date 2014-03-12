from gi.repository import Gtk, GdkPixbuf
from Sections import SignKeysSection, GetSignedSection

class MainWindow(Gtk.Window):
    
    def __init__(self):
        Gtk.Window.__init__(self, title="Geysign")
        self.set_border_width(5)

        # setup the global notebook
        notebook = Gtk.Notebook()
        notebook.append_page(SignKeysSection(), Gtk.Label('Sign keys'))
        notebook.append_page(GetSignedSection(), Gtk.Label('Get your key signed'))

        self.add(notebook)

        # setup signals
        self.connect("delete-event", Gtk.main_quit)

