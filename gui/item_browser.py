import wx
from gui.info_pane import InfoPane
from gui.navigation_view import NavView
from gui.base.prop_splitter import PSplitter
import gui.main_frame


class ItemBrowser(wx.Panel):
    def __init__(self, parent):
        self.main_frame = gui.main_frame.MainFrame.get_instance()
        wx.Panel.__init__(self, parent)
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.splitter = PSplitter(parent=self, proportion=0.38)
        vbox.Add(self.splitter, 1, wx.EXPAND)
        self.SetSizer(vbox)
        self.navView = NavView(self.splitter)
        self.itemView = InfoPane(self.splitter)
        self.splitter.SplitHorizontally(self.navView, self.itemView)
        self.splitter.SetSashInvisible(True)








