#!/usr/bin/python
from gi.repository import Gtk, GdkPixbuf

dummy_data = [(
    "Andrei Duma",
    "andrei.duma.dorian@gmail.com",
    "4096R/DC378D64"
    ), (
    "John Cow",
    "john.cow@gmail.com",
    "4096R/A7DB3E09"
)]

local_fingerprint = '22A3 0C2C 21CA 3580 D478\n2E06 B2FA 08EC DC37 8D64'

class MainWindow(Gtk.Window):
    
    def __init__(self):
        Gtk.Window.__init__(self, title="Geysign")
        self.set_border_width(5)

        notebook = Gtk.Notebook()
        notebook.append_page(SignKeysSection(), Gtk.Label('Sign keys'))
        notebook.append_page(GetSignedSection(), Gtk.Label('Get your key signed'))

        self.add(notebook)

class SignKeysSection(Gtk.VBox):
    def __init__(self):
        super(SignKeysSection, self).__init__()
        
        # setup the notebook
        self.notebook = Gtk.Notebook()
        self.notebook.append_page(KeyListPage(), None)
        self.notebook.append_page(FingerprintCheckPage(), None)
        # TODO add other pages

        self.notebook.set_show_tabs(False)

        # setup the progress bar
        self.progressBar = Gtk.ProgressBar()
        self.progressBar.set_text("Step 1: select a key and click 'Sign'")  # FIXME hardcoded
        self.progressBar.set_show_text(True)
        self.progressBar.set_fraction(0.25)  # FIXME hardcoded

        # setup the proceed button
        self.proceedButton = Gtk.Button('Sign')  # FIXME hardcoded
        self.proceedButton.set_image(Gtk.Image.new_from_icon_name(Gtk.STOCK_EDIT, Gtk.IconSize.BUTTON))
        self.proceedButton.set_always_show_image(True)
        
        # pack bar & button
        bottomBox = Gtk.HBox()
        bottomBox.pack_start(self.progressBar, True, True, 0)
        bottomBox.pack_start(self.proceedButton, False, False, 0)

        # pack them
        self.pack_start(self.notebook, True, True, 0)
        self.pack_start(bottomBox, False, False, 0)

class KeyListPage(Gtk.HBox):
    def __init__(self):
        super(KeyListPage, self).__init__()

        # setup the list store & fill with dummy values; FIXME hardcoded!
        self.store = Gtk.ListStore(str, str, str)

        for entry in dummy_data:
            self.store.append(entry)

        # setup the tree
        self.tree = Gtk.TreeView(model=self.store)

        nameRenderer = Gtk.CellRendererText()
        nameColumn = Gtk.TreeViewColumn("Name", nameRenderer, text=0)

        emailRenderer = Gtk.CellRendererText()
        emailColumn = Gtk.TreeViewColumn("Email", emailRenderer, text=1)

        keyRenderer = Gtk.CellRendererText()
        keyColumn = Gtk.TreeViewColumn("Key", keyRenderer, text=2)

        self.tree.append_column(nameColumn)
        self.tree.append_column(emailColumn)
        self.tree.append_column(keyColumn)

        # setup the image
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size('image.jpg', 200, -1)
        self.image = Gtk.Image()
        self.image.set_from_pixbuf(pixbuf)
        self.image.props.valign = Gtk.Align.START
        self.image.props.margin = 5

        # pack them
        self.pack_start(self.tree, True, True, 0)
        self.pack_start(self.image, False, False, 0)

class FingerprintCheckPage(Gtk.HBox):
    def __init__(self):
        super(FingerprintCheckPage, self).__init__()

        # setup the instructions label
        instructionsLabel = Gtk.Label()
        instructionsLabel.set_markup('The key owner should enter the <b>Get your key signed</b> section.\n' +
                '<b>Carefully</b> compare the two fingerprints to verify the authenticity of the key.')
        instructionsLabel.set_justify(Gtk.Justification.LEFT)
        instructionsLabel.set_halign(Gtk.Align.START)
        instructionsLabel.set_margin_bottom(10)

        # setup the fingerprint label
        self.peerFingerprintLabel = Gtk.Label()
        self.peerFingerprintLabel.set_markup('<span size="30720">' + local_fingerprint + '</span>') # FIXME hardcoded value

        # pack them into a container for alignment
        container = Gtk.VBox()
        container.pack_start(instructionsLabel, False, False, 0)
        container.pack_start(self.peerFingerprintLabel, False, False, 0)
        container.set_valign(Gtk.Align.CENTER)

        self.pack_start(container, True, False, 0)

class GetSignedSection(Gtk.Box):
    def __init__(self):
        super(GetSignedSection, self).__init__()

        # setup the fingerprint label
        self.fingerprintLabel = Gtk.Label()
        self.fingerprintLabel.set_markup('<span size="30720">' + local_fingerprint + '</span>') # FIXME hardcoded

        # pack it
        self.pack_start(self.fingerprintLabel, True, False, 0)

window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
