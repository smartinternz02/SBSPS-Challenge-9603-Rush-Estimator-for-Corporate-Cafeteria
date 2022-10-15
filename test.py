import threading

def printit():
  threading.Timer(5.0, printit).start()
  print ("Hello, World!")

printit()
print("Hell")

for i in range(10):
    print(i)