def en():
    s=input("Enter the plain text!")
    result = ""
    print("Enter the no for rot!")
    n=int(input())
    # Loop over characters.
    for v in s:
        # Convert to number with ord.
        c = ord(v)

        # Shift number back or forward.
        if c >= ord('a') and c <= ord('z'):
            c= ((c - 97)+n)%26+97
                
        elif c >= ord('A') and c <= ord('Z'):
             c= ((c - 65)+n)%26+65

        # Append to result.
        result += chr(c)

    # Return transformation.
    print(result)



def rotn():
    n=input("Enter 1 for encryption and 2 for decryption!\n")
    if(n=='1'):
    	en()
    elif(n=='2'):
        dec()

