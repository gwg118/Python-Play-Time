#Threading Program that does multiple things at a time.

import threading

# Multiple objects from this class running at the same time called threading
class GideonsMessenger(threading.Thread):
    def run(self):
        for _ in range(10): # the _ is whatever. So this statement says loop whatever 10 time.
            print(threading.currentThread().getName())

x = GideonsMessenger(name="Send out messages")
y = GideonsMessenger(name="Receive messages")
x.start()# With thread call the start function. Goes to the class and looks for "run"
y.start()


'''
Send out messages
Send out messages
Send out messages
Send out messages
Send out messages
Send out messages
Send out messages
Send out messages
Send out messages
Send out messages
Receive messages
Receive messages
Receive messages
Receive messages
Receive messages
Receive messages
Receive messages
Receive messages
Receive messages
Receive messages
'''
