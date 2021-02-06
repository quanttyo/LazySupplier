import os.path
import config
import wx


def get_static_bitmap(name, parent):
    static = wx.StaticBitmap(parent)
    static.SetBitmap(get_bitmap(name))
    return static


def get_bitmap(name):
    path = os.path.join(config.path, "icons1", name + ".png")
    return wx.Image(path).ConvertToBitmap()
