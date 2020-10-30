import win32gui
import win32con
import winxpgui
import win32api
import subprocess
import time


hwnd = win32gui.FindWindow(None, "Anaconda Prompt (anaconda3)")

win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(
    hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
winxpgui.SetLayeredWindowAttributes(
    hwnd, win32api.RGB(0, 0, 0), 180, win32con.LWA_ALPHA)

win32gui.ShowWindow(hwnd, win32con.SW_SHOWMINIMIZED)
win32gui.ShowWindow(hwnd, win32con.SW_SHOWMAXIMIZED)
