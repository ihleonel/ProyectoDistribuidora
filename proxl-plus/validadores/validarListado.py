# -*- coding:utf-8 -*-
import wx
class ValidarList(wx.PyValidator):
	def __init__(self):
		wx.PyValidator.__init__(self)
		
	def Clone(self):
		return ValidarList()
		
	def Validate(self, win):
		tctrl = self.GetWindow()
		texto = tctrl.GetValue()
		if len(texto) == 0:
			tctrl.SetBackgroundColour("pink")
			tctrl.SetFocus()
			tctrl.Refresh()
			return False
		else: 
			return True
			
	def TransferToWindow(self):
		return True
		
	def TransferFromWindow(self):
		return True