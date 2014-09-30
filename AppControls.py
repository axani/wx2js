import wx
import wx.html2
import os
import json

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
		self.Bind(wx.html2.EVT_WEBVIEW_TITLE_CHANGED, self.pageLoaded, self.browser)

	def pageLoaded(self, event):
		print 'Seite geladen'

	def getFunctionFromURL(self, event):
		url = str(event.GetURL())
		if url.startswith('python://'):
			function_name = url[len('python://'):]
			event.Veto()

			# Run Python function
			self.runFunction(function_name)
			#MainFrame.testFunction()

		if url.startswith('python-data://'):
			data = url[len('python-data://'):]
			data_clean = self.cleanString(data)
			data_json = json.loads(data_clean)
			self.runFunction_withAttr(data_json["functionName"], data_json["attr"])
	
	def cleanString(self, str):
		return str.replace('%7B', '{').replace('%22', '\"').replace('%7D', '}')
	
	def runFunction_withAttr(self, function_name, attr):
		if function_name == 'printXTimes':


			for i in xrange(int(attr) *100):
				if i == 0: 
					wx.GetApp().TopWindow.htmlPanel.browser.RunScript('showLoading()')

				if i == int(attr) * 99:
					wx.GetApp().TopWindow.htmlPanel.browser.RunScript('endLoading()')
				print i

			


	def runFunction(self, function_name):
		print 'JavaScript to Python:', function_name

		# Change static text
		## Does not work!
		#self.parent.JSText.SetLabel(function_name)
		wx.GetApp().TopWindow.JSText.Label = function_name
		#.SetLabel(function_name)

		if function_name == 'showMenu':
			wx.GetApp().TopWindow.myMenu.Show()
			wx.GetApp().TopWindow.Layout()

		if function_name == 'closeMenu':
			wx.GetApp().TopWindow.myMenu.Hide()
			wx.GetApp().TopWindow.Layout()





class myButtonSubclass(wx.Button):

	# *args and **kwargs takes all the same argument as the standard window
	def __init__(self, *args, **kwargs):
		wx.Button.__init__(self, *args, **kwargs)
		print 'Button loaded'