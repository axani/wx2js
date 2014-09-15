# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

from AppControls import myButtonSubclass
from AppControls import htmlContainer
import wx
import wx.xrc

###########################################################################
## Class wx2jsWindow
###########################################################################

class wx2jsWindow ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 571,435 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		boxSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.JSText = wx.StaticText( self, wx.ID_ANY, u"JavaScript says", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.JSText.Wrap( -1 )
		bSizer2.Add( self.JSText, 0, wx.ALL, 5 )
		
		self.wxInputField = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.wxInputField, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.myButton = myButtonSubclass( self, wx.ID_ANY, u"Send to JS", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.myButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		boxSizer.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.htmlPanel = htmlContainer( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3.Add( self.htmlPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		boxSizer.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( boxSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.myButton.Bind( wx.EVT_BUTTON, self.sendVarToJS )
	
	def __del__( self ):
		pass
	
	
	
	# Virtual event handlers, overide them in your derived class
	def sendVarToJS( self, event ):
		event.Skip()
	

