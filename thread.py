import threading
import time

num = 0

def plus():
  global num
  for i in range(100):
    print("+")
    number = num
    number = number + 1
    # f = open("test.txt", "w")
    # f.write("hello")
    num = number

def minus():
  global num
  for i in range(100):
    print("-")
    number = num
    number = number - 1
    num = number

thread1 = threading.Thread(target=plus)
thread2 = threading.Thread(target=minus)

thread1.start()
thread2.start()

for i in range(100):
  print("main")

time.sleep(2)

print("result num : ", num)