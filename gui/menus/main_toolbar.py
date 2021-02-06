import wx
from gui import bitmap_loader
import gui.selectedItems
from gui.global_events import SelViewCheckAll
TBFLAGS = ( wx.TB_HORIZONTAL
            | wx.NO_BORDER
            | wx.TB_FLAT)

class MainToolBar(wx.ToolBar):
    def __init__(self, parent):
        wx.ToolBar.__init__(self, parent, wx.ID_ANY, style=wx.TB_HORIZONTAL | wx.NO_BORDER | wx.TB_FLAT)
        # self.AddCheckTool(wx.ID_ANY, "Ship Browser", bitmap_loader.getBitmap("ship_big"))
        # self.AddLabelTool(wx.ID_ANY, "Character Editor", bitmap_loader.getBitmap("character_big"))
        #tb = parent.CreateToolBar(wx.TB_HORIZONTAL |
        #                          wx.NO_BORDER | wx.TB_FLAT)
        new_bmp =  wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_TOOLBAR)
        open_bmp = wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR)
        copy_bmp = wx.ArtProvider.GetBitmap(wx.ART_COPY, wx.ART_TOOLBAR)
        paste_bmp= wx.ArtProvider.GetBitmap(wx.ART_PASTE, wx.ART_TOOLBAR)
        self.AddTool(10, 'New', new_bmp, wx.NullBitmap, wx.ITEM_NORMAL, "New", 'Long New')
        self.AddTool(20, 'Open', open_bmp, wx.NullBitmap, wx.ITEM_NORMAL, "Open", 'Long New')

        self.Realize()




class CustomToolBar(wx.Panel):
    def __init__(self, parent):
        import gui.main_frame
        self.main_frame = gui.main_frame.MainFrame.get_instance()
        self.parent = parent
        wx.ToolBar.__init__(self, parent, wx.ID_ANY)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.CheckAll = wx.CheckBox(parent, id=777)
        sizer.AddSpacer(5)
        sizer.Add(self.CheckAll)
        sizer.AddSpacer(20)
        Summary = wx.Button(self, id=wx.ID_ANY, label='Количество', size=(100, 25))
        sizer.Add(Summary)
        sizer.AddSpacer(50)
        Print = wx.Button(self, id=wx.ID_ANY, label='Печать', size=(50, 25))
        sizer.Add(Print)
        sizer.AddSpacer(50)
        self.Order = wx.Button(self, id=wx.ID_ANY, label='Сформировать заказ', size=(150, 25))
        sizer.Add(self.Order)
        self.SetSizer(sizer)

        self.Bind(wx.EVT_BUTTON, self.fuck, Summary)
        self.CheckAll.Bind(wx.EVT_CHECKBOX, self.checkall)

    def fuck(self, event):
        pass

    def checkall(self, event):
        pass
        wx.PostEvent(self.main_frame, SelViewCheckAll(state=wx.FindWindowById(event.GetId()).Value))
