"""
Post-Scan GUI

This is the GUI module for selecting a function after the general area scan (e.g. Correcting a previous measurement,
performing a zoom scan, exiting the area scan module). This GUI is intended to be run in conjunction with the
'xy_positioner_gui.py' only.

This module contains a single class:
    - PostScanGUI(wx.Dialog): basic GUI dialog to select between correcting a prev. measurement, perform a zoom scan,
                              save data (NOTE: note yet implemented), or exiting the area scan module.

Authors:
Chang Hwan 'Oliver' Choi, Biomedical/Software Engineering Intern (Aug. 2018) - changhwan.choi@pctest.com
"""

import wx


class PostScanGUI(wx.Dialog):
    """
    GUI that provides user post-scan options (e.g. Exit, Zoom Scan, Correct Previous Value, Save Data).
    """
    def __init__(self, *args, **kw):
        super(PostScanGUI, self).__init__(*args, **kw)

        # UI Elements
        self.option_rbox = wx.RadioBox(self,
                                       label="Options",
                                       choices=['Exit', 'Zoom Scan', 'Correct Previous Value', 'Save Data'],
                                       style=wx.RA_SPECIFY_COLS,
                                       majorDimension=1)
        self.select_btn = wx.Button(self, wx.ID_OK, "Select")
        self.Bind(wx.EVT_CLOSE, self.OnQuit)

        # Sizers/Layout, Static Lines, & Static Boxes
        self.mainv_sizer = wx.BoxSizer(wx.VERTICAL)

        self.mainv_sizer.Add(self.option_rbox, proportion=1, border=5, flag=wx.EXPAND | wx.ALL)
        self.mainv_sizer.Add(self.select_btn, proportion=0, border=5, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM)
        self.SetSizer(self.mainv_sizer)
        self.SetAutoLayout(True)
        self.mainv_sizer.Fit(self)

    def OnQuit(self, e):
        """
        Function called on quit.
        :param e: Event handler.
        :return: Nothing.
        """
        self.Destroy()


if __name__ == '__main__':
    post_scan_gui = wx.App()
    panel = PostScanGUI(None)
    panel.ShowModal()
    post_scan_gui.MainLoop()