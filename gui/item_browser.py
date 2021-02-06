import wx
from gui.info_pane import StatsPane
from gui.navigation_view import NavView
from gui.base.prop_splitter import PSplitter


class ItemBrowser(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.splitter = PSplitter(parent=self, id=-1, proportion=0.5)
        vbox.Add(self.splitter, 1, wx.EXPAND)
        self.SetSizer(vbox)
        self.navView = NavView(self.splitter)
        self.itemView = StatsPane(self.splitter)
        self.splitter.SplitHorizontally(self.navView, self.itemView)
        self.splitter.SetSashInvisible(True)








