import pygtk
pygtk.require('2.0')
import gtk
import os

def getFilePath(fileName):
	return os.path.join(os.path.dirname(__file__), fileName)

class MainWindow(gtk.Window):
	def on_delete_event(self, widget, event):
		self.hide()
		return True

	def tray_activate(self, widget):
		self.present()

	def __init__(self):
		super(MainWindow, self).__init__()

		# Create window
		self.set_title("Giant Multiplayer Robot")
		self.set_border_width(0)
		self.set_size_request(720, 320)
		self.connect("delete-event", self.on_delete_event)

		# Create the tray icon and bind an action to it
		iconPath = getFilePath("images/tray.png")
		pixbuf = gtk.gdk.pixbuf_new_from_file(iconPath)
		statusicon = gtk.status_icon_new_from_pixbuf(pixbuf)
		statusicon.connect("activate", self.tray_activate)

		# Create a vertical box in which we will display the header and games
		windowBox = gtk.VBox()
		self.add(windowBox)

		# Create a box for the header and make it a nice light gray
		headerBox = gtk.EventBox()
		headerBox.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color("#808080"))

		# Add a header object to the box and pack it into the window
		self.header = WindowHeader()
		headerBox.add(self.header)
		windowBox.pack_start(headerBox, False, True, 0)

		# Create an eventBox which will contain both the active turns and all 
		# games box. Make this dark gray.
		gameBox = gtk.EventBox()
		gameBox.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color("#303030"))

		# The gameContainer will contain two boxes: One for current turns and
		# one for all games.
		gameContainer = gtk.VBox()
		gameBox.add(gameContainer)
		gameContainer.set_spacing(10)
		windowBox.pack_start(gameBox, True, True, 0)

		# Create a CurrentTurns box and pack it into the gameContainer
		turnsEB = gtk.EventBox()
		turnsEB.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color("#484848"))
		self.turns = CurrentTurns()
		turnsEB.add(self.turns)
		gameContainer.pack_start(turnsEB, True, True, 0)

		# Do the same thing for a box containing all games
		gamesEB = gtk.EventBox()
		gamesEB.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color("#484848"))
		self.games = AllGames()
		gamesEB.add(self.games)
		gameContainer.pack_start(gamesEB, False, True, 0)

		# Enter the gtk loop
		self.show_all()
		gtk.main()

class WindowHeader(gtk.HBox):
	def __init__(self):
		super(WindowHeader, self).__init__()

		# Create an Image object, load the logo and pack it
		logo = gtk.Image()
		logo.set_from_file(getFilePath("images/logo.png"))
		self.pack_start(logo)

		# Create a box for the player data
		player = gtk.VBox()
		
		# Get the player avatar
		avatar = gtk.Image()
		avatar.set_from_file(getFilePath("images/avatar.jpg"))
		player.pack_start(avatar)

		# The second part of the player box will be a box representing the
		# number of points the player has on GMR
		score = gtk.HBox()
		pointIcon = gtk.Image()
		pointIcon.set_from_file(getFilePath("images/points.png"))
		score.pack_start(pointIcon)

		# Get a number of points
		self.label = gtk.Label()
		self.label.set_text("3,708")
		score.pack_start(self.label)

		# Pack any remaining components
		player.pack_start(score)
		self.pack_start(player, False, False, 0)

class CurrentTurns(gtk.VBox):
	def __init__(self):
		super(CurrentTurns, self).__init__()
		
		# Create a box for the heading of the current turns, which will contain
		# the preferences button and some text
		header = gtk.HBox()
		self.pack_start(header, False, False, 0)

		# Add some text and add it to the header
		self.turnLabel = gtk.Label()
		self.turnLabel.set_text("Your Turns (1)")
		self.turnLabel.set_alignment(0.0, self.turnLabel.get_alignment()[1])
		header.pack_start(self.turnLabel, True, True, 0)

		# Add a configuration button, which has an image
		self.prefButton = gtk.Button()
		prefImage = gtk.Image()
		prefImage.set_from_stock(gtk.STOCK_PREFERENCES, 24)
		self.prefButton.add(prefImage)
		header.pack_start(self.prefButton, False, False, 5)

		# Add everything together
		self.games = gtk.HBox()
		self.pack_start(self.games, True, True, 5)

class AllGames(gtk.HBox):
	showAll = True

	def toggleExpand(self, widget):
		if self.showAll:
			self.showAll = False
			self.games.hide()
			self.prefImage.set_from_stock(gtk.STOCK_GO_DOWN, 24)
		else:
			self.showAll = True
			self.games.show()
			self.prefImage.set_from_stock(gtk.STOCK_GO_UP, 24)

	def __init__(self):
		super(AllGames, self).__init__()

		# Create a box for the heading of all games, this contains a button to
		# expand the list
		header = gtk.HBox()
		self.pack_start(header, False, False, 0)

		# Add an expansion button, which has an image
		self.prefButton = gtk.Button()
		self.prefImage = gtk.Image()
		self.prefImage.set_from_stock(gtk.STOCK_GO_UP, 24)
		self.prefButton.add(self.prefImage)
		self.prefButton.connect("clicked", self.toggleExpand)
		header.pack_start(self.prefButton, False, False, 5)

		# Add some text and add it to the header
		self.turnLabel = gtk.Label()
		self.turnLabel.set_text("All Games (2)")
		self.turnLabel.set_alignment(0.0, self.turnLabel.get_alignment()[1])
		header.pack_start(self.turnLabel)

		self.games = gtk.HBox()
		self.pack_start(self.games, True, True, 5)

if __name__ == "__main__":
	a = MainWindow()