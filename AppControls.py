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
		browser = wx.html2.WebView.New(self)
		browser.LoadURL(website)

		htmlSizer.Add(browser, 1, wx.EXPAND)
		self.SetSizer(htmlSizer)



class myButtonSubclass(wx.Button):

	# *args and **kwargs takes all the same argument as the standard window
	def __init__(self, *args, **kwargs):
		wx.Button.__init__(self, *args, **kwargs)
		print 'Button loaded'