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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 600,435 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		boxSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.myMenu = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.myMenu.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		self.myMenu.Hide()
		self.myMenu.SetMaxSize( wx.Size( 300,-1 ) )
		
		menuSizer = wx.BoxSizer( wx.VERTICAL )
		
		menuSizer.SetMinSize( wx.Size( 10,-1 ) ) 
		self.JSText = wx.StaticText( self.myMenu, wx.ID_ANY, u"JavaScript says", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.JSText.Wrap( -1 )
		menuSizer.Add( self.JSText, 0, wx.ALL, 5 )
		
		self.wxInputField = wx.TextCtrl( self.myMenu, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		menuSizer.Add( self.wxInputField, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.myButton = myButtonSubclass( self.myMenu, wx.ID_ANY, u"Send to JS", wx.DefaultPosition, wx.DefaultSize, 0 )
		menuSizer.Add( self.myButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.myMenu.SetSizer( menuSizer )
		self.myMenu.Layout()
		menuSizer.Fit( self.myMenu )
		boxSizer.Add( self.myMenu, 1, wx.EXPAND |wx.ALL, 0 )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.htmlPanel = htmlContainer( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3.Add( self.htmlPanel, 1, wx.EXPAND |wx.ALL, 0 )
		
		
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
	

