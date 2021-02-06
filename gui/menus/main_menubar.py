import wx
from gui.minor_frames.fileselectwindow import FileSelection

class MainMenuBar(wx.MenuBar):
    def __init__(self):
        wx.MenuBar.__init__(self)

        # File menu
        file_menu = wx.Menu()
        self.Append(file_menu, "&File")
        file_menu.Append(wx.ID_EXIT)
        file_menu.Append(102, "&Test", "")
        self.Bind(wx.EVT_MENU, self.filemenu, id=102)

    def Menu102(self, event):
        print(event)

    def doLoadDataOrWhatever(self, data):
        FileSelection(data=data, parent=None, title='Test')

    def filemenu(self, event):
        with wx.FileDialog(self, 'Open', wildcard="XYZ files (*.xls|*.xls",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            pathname = fileDialog.GetPath()
            try:
                with open(pathname, 'r', encoding='utf-8') as file:
                    self.doLoadDataOrWhatever(file)
            except IOError:
                print('err')
