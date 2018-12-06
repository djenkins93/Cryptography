print ('***Generating RSA values***')
def valueGen(): #initialize random prime num. generation
        global p,q,n
        p = random_prime(50) #generate random prime1
        q = random_prime(50) #generate random prime2
        n = (p*q) #multiply the two primes together
        global phi_n
        phi_n = (p-1)*(q-1)


        print p,'>> p :1st prime'
        print q,'>> q :2nd prime'
        print n,'>> n :p * q'
        print phi_n,'>> phi_n :Euler\'s Totient'
        print ''
        return phi_n
#END of valueGen()


import random

def encryptionKey():
    limit = valueGen()-1
    global e
    e = random.randint(2,(limit-1))
    while gcd(e,phi_n) != 1:
          e = random.randint(2,(limit-1))
    print ('***Generating RSA Encryption-Key***')
    #print limit,':This is the limit for "e" value'
    print e, ':encryption-key"e"'

#END of encryptionKey
encryptionKey()

def decryptionKey():
    global d
    d = inverse_mod(e,phi_n)

    print ''
    print ('***Generating RSA Decrypting-Key***')
    print d, ': decryption-key, "d"'
    

#END of decryptionKey
decryptionKey()

def publicValues():
    print ''
    print '***Displaying RSA public values***'
    print n, ':n =(p * q)'
    print e, ':encryption-key, "e"'

publicValues()

def privateValues():
    print ''
    print '***Displaying RSA private values***'
    print p,':p '
    print q,':q'
    print phi_n,':phi_n, Euler\'s Totient'
    print d, ': decryption-key, "d"'

privateValues()

def message():
    msg = []
    txt = raw_input("Enter a message for encryption:")
    msg.append(txt)
    
    #print '\n'
    print str(*msg),' :(*message*)'
    l = list(str(*msg))
    print ''
    print l, ":(*list of characters*)"
    
    print ''
    print '***Translating to ASCII***'
    
    global transl
    transl = [ord(i) for i in l ]
    print transl, 
    print ':(*ascii*)'
    
message()

import string
def msgEncrypt():
    print ''
    print  '***Encrypting ASCII translation***'
    #print transl
    global cipher_txt
    cipher_txt = [i**e % n for i in transl]
    print cipher_txt, ':(cipher-txt)'
    #print ('.'.join(cipher_txt)), ':(cipher-txt)'
    print ''
    print '***Scrambled Text***'
    #scramble = [ chr(i) for i in cipher_txt]
    scramble = [random.choice(string.ascii_letters + string.punctuation) for i in cipher_txt]
    print scramble, ':test'
    print ''
    print (''.join(scramble)), ':(*secret scramble text*)'

msgEncrypt()

def msgDecrypt():
    print ''
    print '***Decrypting Message***'
    decipher_txt = [i**d % n for i in cipher_txt]
    print decipher_txt, ':(*decrypted-txt*)'
    clear_txt = [chr(i) for i in decipher_txt]
    print ''
    print (''.join(clear_txt)), ':(*clear-txt*)'
    #print clear_txt, ':clear-txt'
    

msgDecrypt()