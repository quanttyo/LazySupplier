import wx


class PSplitter(wx.SplitterWindow):
    def __init__(self, parent, id=-1, proportion=0.5, size=wx.DefaultSize,
                 minimum_pane_size=20, style=wx.SP_LIVE_UPDATE):
        """ wx.SplitterWindow with size propotion
            PSplitter(self, parent, window_id, proportion,
            size, minimum_pane_size)
        """
        wx.SplitterWindow.__init__(self, parent, id=id,
                                   pos=wx.DefaultPosition,
                                   size=size, style=style)

        self.SetMinimumPaneSize(minimum_pane_size)
        self.proportion = proportion
        self.reset_sash()
        self.Bind(wx.EVT_SIZE, self.on_resize)
        self.Bind(wx.EVT_SPLITTER_SASH_POS_CHANGED,
                  self.on_sash_changed, id=id)
        # Set size on first EVT_PAINT event
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.first_paint = True

    def SplitHorizontally(self, window1, window2):
        if self.GetParent() is None:
            return False
        return wx.SplitterWindow.SplitHorizontally(self, window1, window2,
                                                   int(round(
                                                       self.GetParent()
                                                       .GetSize()
                                                       .GetHeight() *
                                                       self.proportion)))

    def SplitVertically(self, window1, window2):
        if self.GetParent() is None:
            return False
        return wx.SplitterWindow.SplitVertically(self,
                                                 window1, window2,
                                                 int(round(
                                                     self.GetParent()
                                                     .GetSize()
                                                     .GetWidth() *
                                                     self.proportion)))

    def get_expected_sash_position(self):
        """ The splitter has been moved, so we need to adjust
        the sash by self.proportions """

        if self.GetSplitMode() == wx.SPLIT_VERTICAL:
            value = max(self.GetMinimumPaneSize(),
                        self.GetParent().GetClientSize().width)
        else:
            value = max(self.GetMinimumPaneSize(),
                        self.GetParent().GetClientSize().height)
        return int(round(value * self.proportion))

    def reset_sash(self):
        self.SetSashPosition(self.get_expected_sash_position())

    def on_resize(self, event):
        """The window size has been changed, so we need to adjust
        the sash by self.proportion"""

        self.reset_sash()
        event.Skip()

    def on_sash_changed(self, event):

        """We change self.proportion depending on where the sash is dragged."""

        pos = float(self.GetSashPosition())
        if self.GetSplitMode() == wx.SPLIT_VERTICAL:
            tot = max(self.GetMinimumPaneSize(),
                      self.GetParent().GetClientSize().width)
        else:
            tot = max(self.GetMinimumPaneSize(),
                      self.GetParent().GetClientSize().height)
        self.proportion = pos / tot
        event.Skip()

    def on_paint(self, event):
        if self.first_paint:
            if self.GetSashPosition() != self.get_expected_sash_position():
                self.reset_sash()
            self.first_paint = False
        event.Skip()
