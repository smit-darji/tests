from threading import Event # Needed for the  wait() method
from time import sleep     

print("\n Live long and prosper!")
sleep(150)               # Conventional sleep() Method.
print("\n Just let that soak in..")   
Event().wait(3.0) # wait() Method, useable sans thread.
print("\n Make it So! = )\n")
