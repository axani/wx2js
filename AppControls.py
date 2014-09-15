import wx
import wx.html2
import os

class htmlContainer(wx.Panel):
	def __init__(self, *args, **kwargs):
		wx.Panel.__init__(self, *args, **kwargs)
		#html.HtmlWindow.__init__(self, *args, **kwargs)
		#self.LoadPage('html/index.html')
		htmlSizer = wx.BoxSizer(wx.VERTICAL)
		
		website = os.path.realpath('html/index.html')
		self.browser = wx.html2.WebView.New(self)
		self.browser.LoadURL(website)

		htmlSizer.Add(self.browser, 1, wx.EXPAND)
		self.SetSizer(htmlSizer)
		self.Bind(wx.html2.EVT_WEBVIEW_NAVIGATING, self.getFunctionFromURL, self.browser)

	def getFunctionFromURL(self, event):
		url = str(event.GetURL())
		if url.startswith('python://'):
			function_name = url[len('python://'):]
			event.Veto()

			# Run Python function
			self.runFunction(function_name)
			MainFrame.testFunction()

	def runFunction(self, function_name):
		print 'JavaScript to Python:', function_name

		# Change static text
		## Does not work!
		#self.parent.JSText.SetLabel(function_name)





class myButtonSubclass(wx.Button):

	# *args and **kwargs takes all the same argument as the standard window
	def __init__(self, *args, **kwargs):
		wx.Button.__init__(self, *args, **kwargs)
		print 'Button loaded'