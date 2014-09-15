import wx
from MainFrame import MainFrame

# Debug mode for development
debug = True
# redirect = True -> Print in External window, not console
redirect = False

def main():
	# Create app object by initiating class instance
	app = wx.App(redirect=redirect)

	# Create frame widget
	window = MainFrame(None)

	# Set the main top level window
	app.SetTopWindow(window)

	if debug:
		# Show pyCrust when in debug mode
		from wx import py
		crust = py.crust.CrustFrame(window)
		del py
		crust.Show(True)
		crust.shell.interp.locals['app'] = app

	# Show frame widget
	window.Show()

	# Execute the main GUI event loop
	app.MainLoop()

# Only execute when run as main script (not when imported module) 
if __name__ == '__main__':
	main()