import wx
import gui
from AppControls import myButtonSubclass, htmlContainer

class MainFrame(gui.wx2jsWindow):
	
	def __init__(self, parent):
		# Create window frame
		# All gui-stuff is in gui.py
		gui.wx2jsWindow.__init__(self, parent)

		# Set Value for Input field
		self.wxInputField.SetValue("Hallo")

		print wx.version()
		print 'App loaded'





	# Run this function when button is pressed
	def sendVarToJS(self, event):
		js_function = 'document.getElementById("variable").innerHTML = "%s";' % self.wxInputField.GetValue()
		self.htmlPanel.browser.RunScript(js_function)
		print 'Button clicked', self.wxInputField.GetValue()