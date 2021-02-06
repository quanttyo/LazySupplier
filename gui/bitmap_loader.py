import os.path
import config
import wx

def getStaticBitmap(name, parent):
    static = wx.StaticBitmap(parent)
    static.SetBitmap(getBitmap(name))
    return static

def getBitmap(name):
    path = os.path.join(config.path, "icons1", name + ".png")
    return wx.Image(path).ConvertToBitmap()