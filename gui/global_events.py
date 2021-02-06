import wx.lib.newevent


SendDataViewInstance, EVT_DV_INS = wx.lib.newevent.NewEvent()
SendSelectedViewInstance, EVT_SV_INS = wx.lib.newevent.NewEvent()
SendSelectedTree, EVT_TREE_SEL = wx.lib.newevent.NewEvent()
DataViewItemSel, EVT_DV_SEL = wx.lib.newevent.NewEvent()
SelViewCheckAll, EVT_SV_CA = wx.lib.newevent.NewEvent()


LineSelected, EVT_LINE_SEL = wx.lib.newevent.NewEvent()
ItemSelected, EVT_ITEM_SEL = wx.lib.newevent.NewEvent()
ListItemSelected, EVT_LIST_ITEM_SEL = wx.lib.newevent.NewEvent()
Message, EVT_MSG = wx.lib.newevent.NewEvent()
SelMessage, INSTANCE_SEL = wx.lib.newevent.NewEvent()
DataViewInstance, INS_DATA_VIEW = wx.lib.newevent.NewEvent()
CheckAll, EVT_LIST_CHECKALL = wx.lib.newevent.NewEvent()
