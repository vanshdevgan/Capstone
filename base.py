import base64
import time

def en():
    start_time=time.time()
    s=input("Enter the plain text!\n")
    en=base64.b64encode(s.encode())
    print(en.decode())
    print("--- %s seconds ---" % (time.time() - start_time))
def dec():
    start_time=time.time()
    c=input("Enter the cipher text!\n")
    de=base64.b64decode(c.encode())
    print(de.decode())
    print("--- %s seconds ---" % (time.time() - start_time))
def Base():
	n=input("Enter 1 for encryption and 2 for decryption!\n")
	if(n=='1'):
		en()
	elif(n=='2'):
		dec()


