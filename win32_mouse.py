import win32api
import time

for i in range(10):
  win32api.SetCursorPos((i * 10, i * 10))
  time.sleep(0.5)

for i in range(10):
  curpos = win32api.GetCursorPos()
  print(curpos)
  time.sleep(0.5)
