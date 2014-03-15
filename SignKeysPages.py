from gi.repository import Gtk, GdkPixbuf

FINGERPRINT_SAMPLE = '22A3 0C2C 21CA 3580 D478\n2E06 B2FA 08EC DC37 8D64'
SAMPLE_DATA = [(
    "Andrei Duma",
    "andrei.duma.dorian@gmail.com",
    "4096R/DC378D64"
    ), (
    "John Cow",
    "john.cow@gmail.com",
    "4096R/A7DB3E09"
)]
SAMPLE_ID = SAMPLE_DATA[0]

class KeyListPage(Gtk.HBox):

    def __init__(self):
        super(KeyListPage, self).__init__()

        # setup the list store & fill with dummy values; FIXME hardcoded!
        self.store = Gtk.ListStore(str, str, str)

        for entry in SAMPLE_DATA:
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
        self.peerFingerprintLabel.set_markup('<span size="30720">' + FINGERPRINT_SAMPLE + '</span>') # FIXME hardcoded value

        # pack them into a container for alignment
        container = Gtk.VBox()
        container.pack_start(instructionsLabel, False, False, 0)
        container.pack_start(self.peerFingerprintLabel, False, False, 0)
        container.set_valign(Gtk.Align.CENTER)

        self.pack_start(container, True, False, 0)


class IdentityCheckPage(Gtk.HBox):

    def __init__(self):
        super(IdentityCheckPage, self).__init__()

        # setup the instructions label
        instructionsLabel = Gtk.Label()
        instructionsLabel.set_markup('Check the <b>identification papers</b> of the other person.\n' +
                                     '<b>Make sure</b> the name below and the ID name <b>match</b>!')
        instructionsLabel.set_justify(Gtk.Justification.LEFT)
        instructionsLabel.set_halign(Gtk.Align.START)
        instructionsLabel.set_margin_bottom(10)

        # setup the name label
        self.peerNameLabel = Gtk.Label()
        self.peerNameLabel.set_markup('<span size="30720">' + SAMPLE_ID[0] + '</span>') # FIXME hardcoded value

        # pack them into a container for alignment
        container = Gtk.VBox()
        container.pack_start(instructionsLabel, False, False, 0)
        container.pack_start(self.peerNameLabel, False, False, 0)
        container.set_valign(Gtk.Align.CENTER)

        self.pack_start(container, True, False, 0)


class PostSignPage(Gtk.HBox):

    def __init__(self):
        super(PostSignPage, self).__init__()

        # setup the label
        signedLabel = Gtk.Label()
        signedLabel.set_text('The key was signed! What next?')

        # setup the buttons
        sendBackButton = Gtk.Button('Send back to owner')
        sendBackButton.set_image(Gtk.Image.new_from_icon_name(Gtk.STOCK_GO_BACK, Gtk.IconSize.BUTTON))
        sendBackButton.set_always_show_image(True)
        sendBackButton.set_halign(Gtk.Align.CENTER)

        saveButton = Gtk.Button('Save the key locally')
        saveButton.set_image(Gtk.Image.new_from_icon_name(Gtk.STOCK_SAVE, Gtk.IconSize.BUTTON))
        saveButton.set_always_show_image(True)
        saveButton.set_halign(Gtk.Align.CENTER)

        emailButton = Gtk.Button('Email the key owner')
        emailButton.set_image(Gtk.Image.new_from_icon_name(Gtk.STOCK_GO_FORWARD, Gtk.IconSize.BUTTON))
        emailButton.set_always_show_image(True)
        emailButton.set_halign(Gtk.Align.CENTER)

        # pack them into a container for alignment
        container = Gtk.VBox(spacing=3)
        container.pack_start(signedLabel, False, False, 8)
        container.pack_start(sendBackButton, False, False, 0)
        container.pack_start(saveButton, False, False, 0)
        container.pack_start(emailButton, False, False, 0)
        container.set_valign(Gtk.Align.CENTER)

        self.pack_start(container, True, False, 0)
