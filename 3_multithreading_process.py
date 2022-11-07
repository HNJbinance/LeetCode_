import time
import threading


def process1():
    i = 0
    while i < 3:
        print("aaaaaaaaaa")
        time.sleep(0.3)
        i += 1


def process2():
    i = 0
    while i < 3:
        print("bbbbbbbbbb")
        time.sleep(0.3)
        i += 1


th1 = threading.Thread(target=process1())
th2 = threading.Thread(target=process2())
th3 = threading.Thread(target=process2())


th1.start()
th2.start()
th3.start()

th1.join()
th2.join()
th3.join()

print("Le programme est terminé")
