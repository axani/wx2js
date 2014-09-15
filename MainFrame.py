import wx
import gui
from AppControls import myButtonSubclass, htmlContainer

class MainFrame(gui.wx2jsWindow):
	
	def __init__(self, parent):
		# Create window frame
		# All gui-stuff is in gui.py
		gui.wx2jsWindow.__init__(self, parent)
		print wx.version()
		print 'App loaded'

	# Run this function when button is pressed
	def sendVarToJS(self, event):
		self.htmlPanel.browser.RunScript('document.body.style.background = "red";')
		print 'Button clicked', self.wxInputField.GetValue()