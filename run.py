import wx

from gui.main_frame import MainFrame
from config import LOG_LEVEL



if __name__ == "__main__":
    supp = wx.App(False)
    MainFrame()
    supp.MainLoop()

