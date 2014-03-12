from gi.repository import Gtk
from SignKeysPages import KeyListPage, FingerprintCheckPage

FINGERPRINT_SAMPLE = '22A3 0C2C 21CA 3580 D478\n2E06 B2FA 08EC DC37 8D64'

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


class GetSignedSection(Gtk.Box):

    def __init__(self):
        super(GetSignedSection, self).__init__()

        # setup the fingerprint label
        self.fingerprintLabel = Gtk.Label()
        self.fingerprintLabel.set_markup('<span size="30720">' + FINGERPRINT_SAMPLE + '</span>') # FIXME hardcoded

        # pack it
        self.pack_start(self.fingerprintLabel, True, False, 0)

