import wx.aui
from gui.data_view import DataView
from gui.selectedItems import SelectedItems
from gui.menus.main_toolbar import CustomToolBar


class FitMultiSwitch(wx.aui.AuiNotebook):
    def __init__(self, parent):
        wx.aui.AuiNotebook.__init__(self, parent, wx.ID_ANY)

        self.splitter = wx.SplitterWindow(self, style=wx.SP_LIVE_UPDATE)
        self.close_button_active_flag = self.GetWindowStyleFlag()
        self.close_button_inactive_flag = self.close_button_active_flag & ~(
                wx.aui.AUI_NB_CLOSE_BUTTON
                | wx.aui.AUI_NB_CLOSE_ON_ACTIVE_TAB
                | wx.aui.AUI_NB_CLOSE_ON_ALL_TABS)
        self.SetWindowStyle(self.close_button_inactive_flag)
        self.SetArtProvider(wx.aui.AuiSimpleTabArt())
        self.SetBackgroundColour(parent.GetBackgroundColour())

    def add_tab(self):
        p = wx.Panel(self)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(DataView(p), 1, wx.EXPAND)
        p.SetSizer(sizer)
        pos = self.GetPageCount() - 1
        self.InsertPage(pos, p, "Номенклатура")
        self.SetSelection(pos)

    def add_tab2(self):
        self.splitter.SplitHorizontally(CustomToolBar(self.splitter),
                                        SelectedItems(self.splitter), 25)
        self.splitter.SetMinimumPaneSize(25)
        self.splitter.SetSashInvisible(True)
        pos = self.GetPageCount()
        self.InsertPage(pos, self.splitter, 'Очередь на печать')

