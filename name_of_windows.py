import pygetwindow as gw

def list_windows():
    windows = gw.getAllTitles()
    
    for window in windows:
        print(window)

if __name__ == "__main__":
    list_windows()

