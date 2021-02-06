import wx
from gui import bitmap_loader
from gui.data_view import DataView
from gui.base.lctrl_base import ViewBase
from gui.base.prop_splitter import PSplitter
import gui.main_frame
#from gui.global_events import Message


class StatsPane(PSplitter):
    def __init__(self, parent):
        super().__init__(parent, proportion=0.5, minimum_pane_size=250)
        self.SplitHorizontally(Data(self), Pane(self))
        self.SetSashPosition(150)


class Data(ViewBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.set_cols({'a':' ', 'b':' '})


class Pane(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        size = wx.Size()
        size.SetWidth(3150)
        self.SetMinSize(size)

        self.SetBackgroundColour(wx.WHITE)
        self.mainFrame = gui.main_frame.MainFrame.get_instance()
        #wx.PostEvent(self.mainFrame, Message(obj=self))
        self.st = wx.StaticText(self, id=1, label='Info Pane!', size=wx.DefaultSize, style =0, name='statictext')

        #self.button.Bind(wx.EVT_BUTTON, self.onclick)

        #self.mainFrame = gui.main_frame.MainFrame.getInstance()


