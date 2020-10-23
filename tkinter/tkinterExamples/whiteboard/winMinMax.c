#include <windows.h>
#include <unistd.h>
int main(){
    HWND canvasWindow = FindWindowA(0, "OpenCV/Numpy normal");
    sleep(15);
    ShowWindow(canvasWindow, SW_MINIMIZE);
    sleep(5);
    ShowWindow(canvasWindow, SW_SHOWMAXIMIZED);
}

