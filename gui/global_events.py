import wx.lib.newevent


SendDataViewInstance, EVT_DV_INS = wx.lib.newevent.NewEvent()
SendSelectedViewInstance, EVT_SV_INS = wx.lib.newevent.NewEvent()
SendSelectedTree, EVT_TREE_SEL = wx.lib.newevent.NewEvent()
DataViewItemSel, EVT_DV_SEL = wx.lib.newevent.NewEvent()
SelViewAction, EVT_SV_AC = wx.lib.newevent.NewEvent()
ChangeFocus, EVT_CHANGE_FOCUS = wx.lib.newevent.NewEvent()
