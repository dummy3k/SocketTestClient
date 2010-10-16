import logging

if __name__ == '__main__':
    import logging.config
    logging.config.fileConfig("logging.conf")

import wx

log = logging.getLogger(__name__)

class MainWindow(wx.Frame):
    def __init__(self, parent=None, id=wx.ID_ANY,
                 pos=wx.DefaultPosition):

        wx.Frame.__init__(self, parent, id,
                          title="Socket Test Client", pos=pos,
                          size=(640,480), style=wx.DEFAULT_FRAME_STYLE)
        log.debug("MainWindow Init")
    
if __name__ == '__main__':
    log.debug("Hello");

    app = wx.App()
    main_window = MainWindow()
    main_window.Show(True)

    log.info("entering main loop")
    app.MainLoop()
    
