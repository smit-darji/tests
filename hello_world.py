from threading import Event # Needed for the  wait() method
from time import sleep     

print("\n wait for 10 sec start")
sleep(100)               # Conventional sleep() Method.
print("\nafter 10 sec")   
Event().wait(3.0) # wait() Method, useable sans thread.
print("\n all Completed")
