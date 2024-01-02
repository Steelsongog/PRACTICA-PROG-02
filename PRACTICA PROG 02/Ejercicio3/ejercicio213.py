# Para conocer los pasos en la instalación de un paquete almacenado en pypi elegiremos el paquete 'wxPython' (tengamos en cuenta que es uno solo entre más de 191000 disponibles) que tiene por objetivo facilitar la implementación de interfaces visuales en Python.

# Desde la línea de comandos debemos ejecutar:

# pip install wxPython

import wx

aplicacion = wx.App()
ventana = wx.Frame(parent=None,title="Hola Mundo")
ventana.Show()
aplicacion.MainLoop()