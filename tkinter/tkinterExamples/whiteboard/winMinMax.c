#include <windows.h>

HWND canvasWindow = FindWindowEx(0, 0, "tk", 0);

ShowWindow(canvasWindow, SW_MINIMIZE)
