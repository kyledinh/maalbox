#!/usr/bin/env python3
import threading
import time

def countdown(count, name):
   while count > 0:
      print(name, " - counting down", count)
      count -= 1
      time.sleep(5)
   print(name, " has ended!")

t1 = threading.Thread(target=countdown, args=(10, "Alpha", ))
t1.start()

t2 = threading.Thread(target=countdown, args=(7, "Beta", ))
t2.start()

print("Threads are strated")