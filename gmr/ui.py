import pygtk
pygtk.require('2.0')
import gtk

class MainWindow(gtk.Window):
	def on_delete_Event(self, widget, event):
		self.hide()
		return False

	def tray_activate(self, widget):
		self.present()

	def __init__(self):
		super(MainWindow, self).__init__()

		self.set_title("Giant Multiplayer Robot")
		self.set_border_width(0)
		self.set_size_request(720, 320)
		self.connect("delete-event", self.on_delete_Event)

		self.hbox = gtk.VBox()
		self.add(self.hbox)

		pixbuf = gtk.gdk.pixbuf_new_from_file("images/tray.png")
		statusicon = gtk.StatusIcon()
		statusicon = gtk.status_icon_new_from_pixbuf(pixbuf)
		statusicon.connect("activate", self.tray_activate)

		self.show_all()
		gtk.main()
