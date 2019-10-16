import hashlib
import time
def md5():
    
    print("Enter the string!\n")
    s=input()
    start_time=time.time()
    s=str.encode(s)
    hash_object = hashlib.md5(s)
    c=hash_object.hexdigest()
    t=(time.time() - start_time)
    print(c)
    print("--- %s seconds ---" % t)
def sHa1():
    
    s=input("Enter the input!\n")
    start_time=time.time()
    def make_sha1(s, encoding='utf-8'):
        return hashlib.sha1(s.encode(encoding)).hexdigest()
    t=(time.time() - start_time)
    print(make_sha1(s, encoding='utf-8'))
    print("--- %s seconds ---" % t)    

    
def hashing():
    print("Enter 1 for md5 2 for sha1 3 for hash identification")
    n=input()
    if n=='1':
        md5()
        
    if n=='2':
        sHa1()
    
    
    



    
        
	
