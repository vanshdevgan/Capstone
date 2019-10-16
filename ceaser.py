import time
def en():
    start_time=time.time()
    print(start_time)
    s=input("Enter the plain text!\n")
    e=""
    for i in range(0,len(s)):
        n=((ord(s[i])-97+3)%26)+97
        e=e+chr(n)
    tym=(time.time() - start_time)
    print(e)
    print()
    print("--- %s seconds ---" % tym)
def dec():
    start_time=time.time()
    s=input("Enter the cipher text!\n")
    p=""
    for i in range(0,len(s)):
        n=((ord(s[i])-97-3)%26)+97
        p=p+(chr(n))
    print(p)
    print("--- %s seconds ---" % (time.time() - start_time))

def Ceaser():
	n=input("Enter 1 for encryption and 2 for decryption!\n")
	if(n=='1'):
		en()
	elif(n=='2'):
		dec()
	
#ceaser()
