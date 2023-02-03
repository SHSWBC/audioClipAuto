import wx


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800, 600))
        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        menubar = wx.MenuBar()

        file_menu = wx.Menu()
        file_menu.Append(wx.ID_FILE, 'Import', 'Import audio file')
        file_menu.Append(wx.ID_EXIT, 'Exit', 'Exit the application')
        menubar.Append(file_menu, 'File')

        setting_menu = wx.Menu()
        setting_menu.Append(wx.ID_PREFERENCES, 'Preferences', 'Application preferences')
        menubar.Append(setting_menu, 'Settings')

        help_menu = wx.Menu()
        help_menu.Append(wx.ID_ABOUT, 'About', 'About the application')
        menubar.Append(help_menu, 'Help')

        self.SetMenuBar(menubar)

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        content_text = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        vbox.Add(content_text, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=5)

        export_btn = wx.Button(panel, label='Export')
        vbox.Add(export_btn, flag=wx.ALIGN_RIGHT | wx.RIGHT | wx.BOTTOM, border=5)

        panel.SetSizer(vbox)


if __name__ == '__main__':
    app = wx.App()
    MainWindow(None, title='Audio Clip Auto')
    app.MainLoop()
