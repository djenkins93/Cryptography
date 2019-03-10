print "*** Beginning Vigenre Cipher ****"
def msgGen():
    #creation variables needed to compose 'message' to be encrypted
    global msg, msg_int, msg_length, txt
    
    msg = []#array to hold 'messages'
    txt = raw_input("Please enter a message for encryption...(only aplhabetical letters no special symbols)")
    msg.append(txt)
    msg = list(str(*msg))
    msg_length = len(msg)
    msg_int = [ ord(i) for i in msg ] #decimal values for letters in the message

    print msg,':(*message*)'
    print msg_int, ':(*ascii message*)'
      
msgGen()

def msgCheck():
    #purpose of this method is to ensure that the user has provided the proper user input
    #'for-loop' to traverse the array of ascii value
    for i in range(len(msg_int)):
        #cond. used to detect 'illegal' character input by user 
        if msg_int[i] in range(0, 64) or msg_int[i] in range (91, 96) or msg_int[i] in range(123, 127):
            print '\n'
            print "Illegal character has been found!:" "'",chr(msg_int[i]),"'"
            print "Try again."
            del msg[:] #clear 'illegal' msg allow for new entry
            msgGen()
            msgCheck()#recursive call until proper input is provided
            break
    
msgCheck()

def keyGen():
    #declaration variables needed to create encrypt/decrypt 'key' & 'keyword'
    global keyword,k_txt,key_int, key_length
    
    keyword = [] #array hold to 'keyword'
    k_txt = raw_input("Now please enter a 'keyword' you wish to use for the encryption/decryption processes...")
    keyword.append(k_txt)
    keyword = list(str(*keyword))
    key_length = len(keyword)
    key_int = [ ord(i) for i in keyword ] #decimal value for letters of keyword
    
    print keyword,':(keyword)'
    print key_int, ':(*ascii keyword*)'
    
keyGen()

def keyCheck():
    #purpose of this method is to ensure that the user has provided the proper user input
    #'for-loop' to traverse the array of ascii value
    for i in range(len(key_int)):
        #cond. used to detect 'illegal' character input by user 
        if key_int[i] in range(0, 64) or key_int[i] in range (91, 96) or key_int[i] in range(123, 127):
            print '\n'
            print "Illegal character has been found!:" "'",chr(key_int[i]),"'"
            print "Try again."
            del keyword[:] #clear 'illegal' keyword allow for new entry
            keyGen()
            keyCheck()#recursive call until proper input is provided
            break
    
keyCheck()

def encrypt_msg():
    # using the formula Ci=Ek(Mi)=(Mi + Ki) mod 26
    # where 'Mi' are the characters from the message and 'Ki' are the characters of the keyword
    
    global ciphertxt
    ciphertxt = ''
    
    #loop initiates the encryption process for the 'message'
    for i in range(len(msg_int)):
        value = (msg_int[i] + key_int[i % key_length]) % 26
        ciphertxt += chr(value + 65)
    
    print '\n'
    print '***Generating Ciphertext (ENCRYPTING)***'
    print ciphertxt,':(ciphertxt)'
    
encrypt_msg()

def decrypt_msg():
    
    plaintxt = ''
    ciphertxt_int = [ord(i) for i in ciphertxt]
    
    #loop initiates the decryption process based on the 'ciphertxt'
    for i in range(len(ciphertxt_int)):
        value = ((ciphertxt_int[i] - key_int[i % key_length] ) % 26)
        #conditional addresses the shift value issue presented by ascii python table
        x = (value + 59) #ascii shift value is off by 6 so we need to add by 59 instead of 65
        if x < 65:
            x += 26
            plaintxt += chr(x)
        elif x > 90:
            x -= 26
            plaintxt = chr(x)
        else:
            plaintxt += chr(value + 59) #create 'if...else' or 'while' cond. based on symbols or ascii values 'A-Z' & 'a-z'

    print '\n'
    print '*** Generating Plaintext (DECRYPTING) ***'
    print plaintxt, ':(plaintxt)' #remember yout tabs!

decrypt_msg()