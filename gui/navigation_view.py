import wx
from wx.lib.agw.customtreectrl import CustomTreeCtrl
from data.db.storage import queries
from gui.global_events import SendSelectedTree
import gui.main_frame


class NavView(CustomTreeCtrl):
    def __init__(self, parent):
        CustomTreeCtrl.__init__(self, parent, wx.ID_ANY, agwStyle=wx.TR_HIDE_ROOT | wx.TR_HAS_BUTTONS)
        self.AddRoot('root')
        self.AddItems()
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged, self)
        self.main_frame = gui.main_frame.MainFrame.getInstance()

    def AddItems(self):
        l = []
        for item in queries.roots_node():
            l.append(self.AppendItem(self.GetRootItem(), text=item[1], data=wx.TreeItemData(item[2])))
            for _ in l:
                for item in queries.roots_node(self.GetItemData(_)):
                    l.append(self.AppendItem(_, text=item[1], data=wx.TreeItemData(item[2])))

    def OnSelChanged(self, event):
        item = event.GetItem()

        if self.GetItemLevel(item) == 2:
            wx.PostEvent(self.main_frame, SendSelectedTree(object={'item': self.GetItemData(item), 'level': 2}))
        elif self.GetItemLevel(item) == 3:
            wx.PostEvent(self.main_frame, SendSelectedTree(object={'item': self.GetItemData(item), 'level': 3,
                                                               'parent': self.GetItemData(self.GetItemParent(item))}))

    def GetItemLevel(self, arg):
        if self.GetItemParent(arg) == self.GetRootItem():
            return 1
        elif self.GetItemParent(self.GetItemParent(arg)) == self.GetRootItem():
            return 2
        elif self.ItemHasChildren(arg) == False:
            return 3


