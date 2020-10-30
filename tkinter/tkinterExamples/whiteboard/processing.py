import win32gui
import win32con
import winxpgui
import win32api
import subprocess
import time

hwnd = win32gui.FindWindow(None, "sketch_201030a")

win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(
    hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)

active = True
while True:
    if active:
        win32gui.ShowWindow(hwnd, win32con.SW_SHOWMAXIMIZED)
    else:
        win32gui.ShowWindow(hwnd, win32con.SW_SHOWMINIMIZED)

    for i in range(1, 256):
        if win32api.GetAsyncKeyState(i):
            if chr(i) == "q" or chr(i) == "Q":
                winxpgui.SetLayeredWindowAttributes(
                    hwnd, win32api.RGB(0, 0, 0), 255, win32con.LWA_ALPHA)
                active = True
            elif chr(i) == "a" or chr(i) == "A":
                winxpgui.SetLayeredWindowAttributes(
                    hwnd, win32api.RGB(0, 0, 0), 200, win32con.LWA_ALPHA)
                active = True
            elif chr(i) == "z" or chr(i) == "Z":
                winxpgui.SetLayeredWindowAttributes(
                    hwnd, win32api.RGB(0, 0, 0), 0, win32con.LWA_ALPHA)
                active = False

    time.sleep(0.01)
