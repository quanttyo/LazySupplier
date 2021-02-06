from gui.main_frame import MainFrame
import wx
import os
import sys

if __name__ == "__main__":
    supp = wx.App(False)
    MainFrame()
    supp.MainLoop()
